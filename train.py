from preprocessing import *
import time

import torch
import torch.optim as optim
import torch.nn as nn
from torch.autograd import Variable
import torchvision
from torchvision import models

lr = 0.001

train_loader = trainDataset()
test_loader = testDataset()

model = models.densenet121(pretrained=True)
model.fc = nn.Linear(2048, 28)

########################
# model.load_state_dict(torch.load('checkpoint/checpoint_epoch.pt'))
# model.eval()
########################
criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=1e-5)

def train(epoch):
    model.train()
    for idx, (data, filename) in enumerate(train_loader):
        target = filename

        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()

        if idx % 10 == 0:
            print("epoch: ", epoch, "  process: ", int((idx / len(train_loader)) * 100),
                "%  Loss: ", loss.data.item())

        torch.save(model.state_dict(), 'checkpoint/checpoint_epoch'+str(epoch)+'.pt')

def test():
    model.eval()
    test_loss = 0
    with torch.no_grad():
        for data, filename in test_loader:
            target = filename
            data = data[0]

            output = model(data)
            test_loss += criterion(output, target).data.item()
    
    test_loss /= len(test_loader.dataset)
    print("Average Loss: ", test_loss)


if __name__ == "__main__":
    for epoch in range(100):
        start = time.time()
        train(epoch)
        end = time.time()
        print("It takes ", end - start, " seconds")
        
        if epoch % 3 == 0:
            test()
