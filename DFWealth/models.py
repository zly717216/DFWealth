# -*- coding: utf-8 -*-
"""
Created on 2022-10-08 17:23:33
---------
@summary: 数据结构
---------
@author: zly717216@163.com
"""

from AioSpider import models


class Model(models.SQLiteModel):
    """基类模型，仅用于继承"""

    is_delete = models.BoolField(name='逻辑删除')
    create_time = models.DateTimeField(name='创建时间')
    update_time = models.DateTimeField(name='更新时间')


class ListModel(Model):
    """股票列表数据结构"""

    MARKET_CHOICE = (
        (0, '深圳A股'), (1, '上海A股')
    )

    name = models.CharField(
        name='证券名称', max_length=255, null=False, blank=False
    )
    code = models.CharField(
        name='证券代码', max_length=6, null=False, blank=False
    )
    market = models.CharField(
        name='证券市场', max_length=255, choices=MARKET_CHOICE
    )

    order = [
        'name', 'code', 'market', 'is_delete', 'create_time', 'update_time'
    ]


class KlineModel(ListModel):
    """可转债K线数据结构"""

    datetime = models.DateTimeField(name='日期时间')
    period = models.CharField(name='K线级别', max_length=255)
    open = models.FloatField(name='开盘价')
    close = models.FloatField(name='收盘价')
    high = models.FloatField(name='最高价')
    low = models.FloatField(name='最低价')
    volume = models.IntField(name='成交量')
    amount = models.FloatField(name='成交额')
    amplitude = models.FloatField(name='振幅')
    range = models.FloatField(name='涨跌幅')
    range_money = models.FloatField(name='涨跌额')
    turnover = models.FloatField(name='换手率')

    order = [
        'name', 'code', 'market', 'datetime', 'period', 'open', 'close', 'high',
        'low', 'volume', 'amount', 'amplitude', 'range', 'range_money', 'turnover',
        'is_delete', 'create_time', 'update_time'
    ]


class FundModel(ListModel):
    """资金流数据结构"""

    date = models.DateTimeField(name='日期')
    main_buy = models.FloatField(name='主力净买入净额')
    super_buy = models.FloatField(name='超大单净净流入净额')
    big_buy = models.FloatField(name='大单净净流入净额')
    middle_buy = models.FloatField(name='中单净净流入净额')
    small_buy = models.FloatField(name='小单净净流入净额')

    order = [
        'name', 'code', 'market', 'date', 'main_buy', 'small_buy', 'middle_buy',
        'big_buy', 'super_buy', 'is_delete', 'create_time', 'update_time'
    ]


class FundFlowModel(FundModel):
    """资金流数据结构"""

    close = models.FloatField(name='收盘价')
    range = models.FloatField(name='涨跌幅')
    main_buy_rate = models.FloatField(name='主力净买入净占比')
    super_buy_rate = models.FloatField(name='超大单净净流入净占比')
    big_buy_rate = models.FloatField(name='大单净净流入净占比')
    middle_buy_rate = models.FloatField(name='中单净净流入净占比')
    small_buy_rate = models.FloatField(name='小单净净流入净占比')

    order = [
        'name', 'code', 'market', 'close', 'range', 'date', 'main_buy', 'main_buy_rate',
        'small_buy', 'small_buy_rate',  'middle_buy',  'middle_buy_rate', 'big_buy',
        'big_buy_rate', 'super_buy', 'super_buy_rate', 'is_delete', 'create_time', 'update_time'
    ]


# ------------- 可转债数据结构 ----------------

class BondListModel(KlineModel):
    """可转债数据列表数据结构"""
    pass


class BondModel(KlineModel):
    """可转债K线数据结构"""
    pass


# ------------- 可转债数据结构 ----------------


# ------------- 股票数据结构 ----------------

class StockListModel(ListModel):
    """股票列表数据结构"""
    pass


class Stock1dModel(KlineModel):
    """股票K线数据结构"""
    pass


class Stock1mModel(KlineModel):
    """股票K线数据结构"""
    pass


class Stock5mModel(KlineModel):
    """股票K线数据结构"""
    pass


class Stock15mModel(KlineModel):
    """股票K线数据结构"""
    pass


class Stock30mModel(KlineModel):
    """股票K线数据结构"""
    pass


class Stock60mModel(KlineModel):
    """股票K线数据结构"""
    pass


class Stock120mModel(KlineModel):
    """股票K线数据结构"""
    pass

# ------------- 股票数据结构 ----------------


# ------------- ETF数据结构 ----------------

class ETFListModel(ListModel):
    """ETF列表数据结构"""
    pass


class ETFModel(KlineModel):
    """ETFK线数据结构"""
    pass


# ------------- ETF数据结构 ----------------


# ------------- 板块数据结构 ----------------

class BlockListModel(ListModel):
    """ETF列表数据结构"""

    market = models.CharField(
        name='证券市场', max_length=255
    )


class BlockModel(KlineModel):
    """ETFK线数据结构"""

    market = models.CharField(
        name='证券市场', max_length=255
    )


# ------------- 板块数据结构 ----------------


# ------------- 板块数据结构 ----------------

class IndexListModel(ListModel):
    """ETF列表数据结构"""

    market = models.CharField(
        name='证券市场', max_length=255
    )


class IndexModel(KlineModel):
    """ETFK线数据结构"""

    market = models.CharField(
        name='证券市场', max_length=255
    )


# ------------- 板块数据结构 ----------------


# ------------- 资金流数据结构 ----------------

class Rank1FlowModel(FundFlowModel):
    """今日主力排名数据结构"""
    pass


class Rank3FlowModel(FundFlowModel):
    """3日主力排名数据结构"""
    pass


class Rank5FlowModel(FundFlowModel):
    """5日主力排名数据结构"""
    pass


class Rank10FlowModel(FundFlowModel):
    """10日主力排名数据结构"""
    pass


class StockFlowModel(FundFlowModel):
    """个股资金流数据结构"""
    pass


class StockTickFlowModel(FundModel):
    """个股当日实时资金流数据结构"""
    pass

# ------------- 资金流数据结构 ----------------


# ------------- 涨跌停池数据结构 ----------------

class DtbPoolModel(ListModel):
    """跌停板池数据结构"""

    date = models.DateTimeField(name='日期')
    new_price = models.FloatField(name='最新价')
    range = models.FloatField(name='涨跌幅')
    amount = models.FloatField(name='成交额')
    cir_market_value = models.FloatField(name='流通市值')
    total_market_value = models.FloatField(name='总市值')
    pe = models.FloatField(name='动态市盈率')
    close_fund = models.FloatField(name='封板资金')
    close_time = models.IntField(name='最后封板时间')
    turnover = models.FloatField(name='换手率')
    continue_dt = models.FloatField(name='连续跌停(天)')
    board_amount = models.FloatField(name='板上成交额')
    open_times = models.IntField(name='开板次数')
    industry = models.CharField(name='行业板块', max_length=255)

    order = [
        'date', 'name', 'code', 'market', 'range', 'new_price', 'amount',
        'cir_market_value', 'total_market_value', 'pe', 'turnover', 'close_fund',
        'close_time', 'board_amount', 'continue_dt', 'open_times', 'industry',
        'is_delete', 'create_time', 'update_time'
    ]


class ZtbPoolModel(ListModel):
    """涨停板池数据结构"""

    date = models.DateTimeField(name='日期')
    new_price = models.FloatField(name='最新价')
    range = models.FloatField(name='涨跌幅')
    amount = models.FloatField(name='成交额')
    cir_market_value = models.FloatField(name='流通市值')
    total_market_value = models.FloatField(name='总市值')
    close_fund = models.FloatField(name='封板资金')
    first_close_time = models.IntField(name='首次封板时间')
    last_close_time = models.IntField(name='最后封板时间')
    continue_zt = models.FloatField(name='连板数')
    turnover = models.FloatField(name='换手率')
    open_times = models.IntField(name='炸板次数')
    industry = models.CharField(name='行业板块', max_length=255)

    order = [
        'date', 'name', 'code', 'market', 'range', 'new_price', 'amount',
        'cir_market_value', 'total_market_value', 'turnover', 'close_fund',
        'first_close_time', 'last_close_time', 'open_times', 'continue_zt',
        'industry', 'is_delete', 'create_time', 'update_time'
    ]


class QsgPoolModel(ListModel):
    """强势股池数据结构"""

    SELECT_CHOICE = (
        (1, '60日新高'), (2, '近期多次涨停'), (3, '60日新高且近期多次涨停')
    )

    date = models.DateTimeField(name='日期')
    new_price = models.FloatField(name='最新价')
    range = models.FloatField(name='涨跌幅')
    amount = models.FloatField(name='成交额')
    cir_market_value = models.FloatField(name='流通市值')
    total_market_value = models.FloatField(name='总市值')
    turnover = models.FloatField(name='换手率')
    rising_speed = models.FloatField(name='涨速')
    is_up = models.BoolField(name='是否新高')
    volume_rate = models.FloatField(name='量比')
    zt_statistics = models.CharField(name='涨停统计', max_length=25)
    select_reasons = models.CharField(name='入选理由', max_length=25, choices=SELECT_CHOICE)
    zt_price = models.FloatField(name='涨停价')
    industry = models.CharField(name='行业板块', max_length=255)

    order = [
        'date', 'name', 'code', 'market', 'range', 'new_price', 'amount',
        'cir_market_value', 'total_market_value', 'turnover', 'rising_speed',
        'is_up', 'volume_rate', 'zt_statistics', 'select_reasons', 'zt_price',
        'industry', 'is_delete', 'create_time', 'update_time'
    ]


class ZbgPoolModel(ListModel):
    """炸板股池数据结构"""

    date = models.DateTimeField(name='日期')
    new_price = models.FloatField(name='最新价')
    range = models.FloatField(name='涨跌幅')
    amount = models.FloatField(name='成交额')
    cir_market_value = models.FloatField(name='流通市值')
    total_market_value = models.FloatField(name='总市值')
    turnover = models.FloatField(name='换手率')
    rising_speed = models.FloatField(name='涨速')

    close_time = models.IntField(name='首次封板时间')
    open_times = models.IntField(name='炸板次数')
    zt_statistics = models.CharField(name='涨停统计', max_length=25)
    amplitude = models.FloatField(name='振幅')

    zt_price = models.FloatField(name='涨停价')
    industry = models.CharField(name='行业板块', max_length=255)

    order = [
        'date', 'name', 'code', 'market', 'range', 'new_price', 'amount',
        'cir_market_value', 'total_market_value', 'turnover', 'rising_speed',
        'close_time', 'open_times', 'zt_statistics', 'amplitude', 'zt_price',
        'industry', 'is_delete', 'create_time', 'update_time'
    ]

# ------------- 涨跌停池数据结构 ----------------
