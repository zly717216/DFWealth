# -*- coding: utf-8 -*-
"""
Created on 2022-10-08 17:23:33
---------
@summary: 数据管道，注册数据结构模型
---------
@author: zly717216@163.com
"""

from AioSpider.pipelines import SqlitePipeline


class Pipeline(SqlitePipeline):
    pass


class BondListPipeline(Pipeline):
    model = 'BondListModel'


class BondPipeline(Pipeline):
    model = 'BondModel'


class StockListPipeline(Pipeline):
    model = 'StockListModel'




class StockPipeline(Pipeline):
    model = 'StockModel'


class Stock1dPipeline(Pipeline):
    model = 'Stock1dModel'


class Stock1mPipeline(Pipeline):
    model = 'Stock1mModel'


class Stock5mPipeline(Pipeline):
    model = 'Stock5mModel'


class Stock15mPipeline(Pipeline):
    model = 'Stock15mModel'


class Stock30mPipeline(Pipeline):
    model = 'Stock30mModel'


class Stock60mPipeline(Pipeline):
    model = 'Stock60mModel'


class Stock120mPipeline(Pipeline):
    model = 'Stock120mModel'


class ETFListPipeline(Pipeline):
    model = 'ETFListModel'


class ETFPipeline(Pipeline):
    model = 'ETFModel'


class BlockListPipeline(Pipeline):
    model = 'BlockListModel'


class BlockPipeline(Pipeline):
    model = 'BlockModel'


class IndexListPipeline(Pipeline):
    model = 'IndexListModel'


class IndexPipeline(Pipeline):
    model = 'IndexModel'


class Rank1FlowPipeline(Pipeline):
    model = 'Rank1FlowModel'


class Rank3FlowPipeline(Pipeline):
    model = 'Rank3FlowModel'


class Rank5FlowPipeline(Pipeline):
    model = 'Rank5FlowModel'


class Rank10FlowPipeline(Pipeline):
    model = 'Rank10FlowModel'


class StockFlowPipeline(Pipeline):
    model = 'StockFlowModel'


class StockTickFlowPipeline(Pipeline):
    model = 'StockTickFlowModel'


class DtbPoolPipeline(Pipeline):
    model = 'DtbPoolModel'


class ZtbPoolPipeline(Pipeline):
    model = 'ZtbPoolModel'


class QsgPoolPipeline(Pipeline):
    model = 'QsgPoolModel'


class ZbgPoolPipeline(Pipeline):
    model = 'ZbgPoolModel'
