import torchvision.datasets as dset
import torchvision.transforms as transforms
import torch.nn as nn
import torch
import numpy
from torchvision import models

dataset = dset.ImageFolder(root="sample",
                        transform=transforms.Compose([
                            transforms.Resize([224, 224]),
                            transforms.ToTensor(),
                            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
                        ]))
dataloader = torch.utils.data.DataLoader(dataset,
                                        batch_size=1,
                                        shuffle=False,
                                        num_workers=0)


model = models.densenet121()
model.classifier = nn.Linear(1024, 28)

model.load_state_dict(torch.load('checkpoint/checkpoint_epoch20.pt', map_location='cpu'))
model.eval()


output = model(list(dataloader)[0][0])
sortedOutput, sortedIndex = torch.sort(output, descending=True)

sortedIndex = sortedIndex[0][:3].tolist()

genres = ['Action', 'Adult', 'Adventure', 'Animation', 'Biography',
        'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
        'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror',
        'Music', 'Musical', 'Mystery', 'News', 'Reality-TV',
        'Romance', 'Sci-Fi', 'Short', 'Sport', 'Talk-Show',
        'Thriller', 'War', 'Western']

for index in sortedIndex:
    print(genres[index], end="  ")
print()