#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   tests\test_core\test_coordinator.py
# @Time    :   2022-07-15 20:22:22
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0


from pyexpat import model
import fedhf
from fedhf import algor
from fedhf.core import SimulatedSyncCoordinator, SimulatedAsyncCoordinator


class TestCoordinator(object):
    def test_simulated_async_coordinator(self):
        args = fedhf.init(
            model="mlp",
            dataset="mnist",
            num_rounds=3,
            num_epochs=1,
            num_clients=3,
            gpus="-1",
            test=True,
            algor="fedasync",
        )

        coordinator = SimulatedAsyncCoordinator(args)
        coordinator.run()

    def test_simulated_sync_coordinator(self):
        args = fedhf.init(
            model="mlp",
            dataset="mnist",
            num_rounds=3,
            num_epochs=1,
            num_clients=3,
            gpus="-1",
            test=True,
            select_ratio=0.5,
            algor="fedavg",
        )

        coordinator = SimulatedSyncCoordinator(args)
        coordinator.run()
