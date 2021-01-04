from yacs.config import CfgNode as CN
import torchvision as tv
from cbase.data.augmentation import build_transform

def build_dataset(cfg: CN, is_train: bool):
    
    dataset_name = cfg.DATA.DATASET.TRAIN if is_train else cfg.DATA.DATASET.TEST

    if dataset_name == "CIFAR10":
        root=cfg.DATA.DATASET.CIFAR10.ROOT
        dataset = tv.datasets.CIFAR10(
            root=root, 
            train=is_train,
            transform=build_transform(cfg, dataset_name, is_train),
            download=True,
            
        )
    elif dataset_name == "CIFAR10":
        root=cfg.DATA.DATASET.CIFAR100.ROOT
        dataset = tv.datasets.CIFAR10(
            root=root, 
            train=is_train,
            transform=build_transform(cfg, dataset_name, is_train),
            download=True,
        )

    return dataset