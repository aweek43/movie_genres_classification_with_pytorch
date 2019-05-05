import torchvision.datasets as dset
import torchvision.transforms as transforms
import torch
import numpy as np

batch_size = 32

class TrainImageFolder(dset.ImageFolder):
    def __getitem__(self, index):
        filename = str(self.imgs[index])
        filename = list(filename.split('th')[1][0:28])
        for i in range(len(filename)):
            filename[i] = int(filename[i])
        filename = torch.FloatTensor(filename)
        return super(TrainImageFolder, self).__getitem__(index), filename

def trainDataset():
    dataset = TrainImageFolder(root="dataset/poster_dataset/train",
                            transform=transforms.Compose([
                                transforms.RandomRotation(30),
                                transforms.RandomHorizontalFlip(),
                                transforms.RandomResizedCrop(224, scale=(0.96, 1.0), ratio=(0.95, 1.05)),
                                transforms.ToTensor(),
                                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
                            ]))
    dataloader = torch.utils.data.DataLoader(dataset,
                                            batch_size=batch_size,
                                            shuffle=True,
                                            num_workers=4)
    return dataloader                               

def testDataset():
    dataset = TrainImageFolder(root="dataset/poster_dataset/test",
                            transform=transforms.Compose([
                                transforms.Resize([224, 224]),
                                transforms.ToTensor(),
                                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
                            ]))
    dataloader = torch.utils.data.DataLoader(dataset,
                                            batch_size=batch_size,
                                            shuffle=False,
                                            num_workers=4)
    return dataloader
