#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   fedhf\component\aggregator\__init__.py
@Time    :   2021-10-26 20:31:35
@Author  :   Bingjie Yan
@Email   :   bj.yan.pa@qq.com
@License :   Apache License 2.0
"""

__all__ = ['build_aggregator']

from .fedasync_aggregator import FedAsyncAggregator
from .fedavg_aggregator import FedAvgAggregator


aggregator_factory = {
    'fedavg': FedAvgAggregator,
    'fedasync': FedAsyncAggregator,
}


def build_aggregator(agg_name: str):
    if agg_name not in aggregator_factory.keys():
        raise ValueError(f'Unknown aggregator name: {agg_name}')
    agg = aggregator_factory[agg_name]
    return agg
