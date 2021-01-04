import argparse
import os

import torch
from yacs.config import CfgNode as CN

from cbase.utils import get_default_config
from cbase.data import build_dataloader
from cbase.model import build_model
from cbase.trainer import build_trainer
from cbase.evaluator import build_evaluator
from cbase.launcher import build_launcher

def load_config():
    # parse args

    parser = argparse.ArgumentParser(description="test parser")

    parser.add_argument("--config", required=True, help="path to configuration file")

    args = parser.parse_args()

    # load base configuration and merge with input configuration file

    cfg = get_default_config()
    cfg.merge_from_file(args.config)
    cfg.freeze()

    return cfg

def main(cfg):
    """
    cbase project learning component

    1. Model
    2. Data loader
    3. Trainer
    4. Evaluator
    """
    pass

if __name__ == '__main__':
    cfg = load_config()
    launcher = build_launcher(cfg)
    launcher.launch(main, cfg)
