import torch
from yacs.config import CfgNode as CN
from cbase.data.datasets import build_dataset
from cbase.data.sampler import build_sampler
from cbase.data.analysis import build_collate_fn

def build_data_loader(cfg: CN, is_train: bool):
    """
    Data loader component

    1. Dataset
    """
    dataset = build_dataset(cfg, is_train)
    sampler = build_sampler(cfg, is_train)

    build_batch_data_loader(
        dataset,
        sampler,
        cfg,
        is_train
    )

def build_batch_data_loader(dataset, sampler, cfg, is_train):
    batch_sampler = torch.utils.data.sampler.BatchSampler(
        sampler = sampler,
        batch_size = cfg.DATA.BATCH_SIZE,
        drop_last = is_train
    )

    return torch.utils.data.DataLoader(
        dataset = dataset,
        num_workers = cfg.DATA.NUM_WORKERS,
        batch_sampler = batch_sampler,
        collate_fn = build_collate_fn,
        worker_init_fn = worker_init_reset_seed
    )


def worker_init_reset_seed(worker_id):
    """
    Currently blank here
    """
    pass

