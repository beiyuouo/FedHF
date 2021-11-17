#!/usr/bin/env python
# -*- encoding: utf-8 -*-
""" 
@File    :   tests\test_model\test_alexnet_cifar10.py 
@Time    :   2021-11-17 17:29:32 
@Author  :   Bingjie Yan 
@Email   :   bj.yan.pa@qq.com 
@License :   Apache License 2.0 
"""

import torch
from torch import optim
from torch.utils.data import DataLoader

from fedhf.api import opts
from fedhf.model import build_model, build_optimizer
from fedhf.dataset import build_dataset


class TestAlexNetCIFAR10(object):
    args = opts().parse([
        '--model', 'alexnet_cifar10', '--num_classes', '10',
        '--model_pretrained', 'True', '--dataset', 'cifar10', '--gpus', '-1',
        '--task', 'classification', '--resize', False
    ])

    def test_alexnet_cifar10(self):
        model = build_model(self.args.model)(self.args)
        print(model)

        assert model.__class__.__name__ == 'AlexNetCIFAR10'
        assert model.num_classes == 10

        dataset = build_dataset(self.args.dataset)(self.args)
        dataloader = DataLoader(dataset.trainset, batch_size=1, shuffle=False)

        model = model.to(self.args.device)
        model.train()
        for data, target in dataloader:
            output = model(data)
            assert output.shape == (1, 10)
            assert output.dtype == torch.float32
            assert output.device == torch.device('cpu')
            break