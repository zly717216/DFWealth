# -*- coding: utf-8 -*-
"""
Created on 2022-10-15 10:23:12
---------
@summary: ETF数据
---------
@author: zly717216@163.com
"""

import time
from datetime import datetime

from AioSpider import tools
from AioSpider.http import Request
from AioSpider.spider import Spider

from DFWealth.models import *


class ETFSpider(Spider):
    name = 'etfSpider'

    def start_requests(self):

        t = int(time.time() * 1000)

        # target: http://quote.eastmoney.com/center/gridlist.html#fund_etf
        url = 'http://18.push2.eastmoney.com/api/qt/clist/get'
        params = {
            'cb': f'jQuery112409602299270368062_{t}', 'pn': '1', 'pz': '10000', 'po': '1',
            'np': '1', 'ut': 'bd1d9ddb04089700cf9c27f6f7426281', 'fltt': '2', 'invt': '2',
            'fid': 'f3', 'fs': 'b:MK0021,b:MK0022,b:MK0023,b:MK0024', 'fields': 'f12,f13,f14', '_': t
        }
        yield Request(url, params=params, callback=self.parse)

    def parse(self, response):

        # target: https://quote.eastmoney.com/concept/sh510880.html#
        for i in response.jsonp['data']['diff']:
            yield ETFListModel({
                'code': i['f12'], 'market': i['f13'], 'name': i['f14']
            })

            # 构造 1d、1m、5m、15m、30m、60m、120m K线请求
            for klt in ['101', '1', '5', '15', '30', '60', '120']:
                params = {
                    'fields1': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13',
                    'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61',
                    'beg': '0',
                    'end': '20500101',
                    'ut': 'fa5fd1943c7b386f172d6893dbfba10b',
                    'rtntype': '6',
                    'secid': f"{i['f13']}.{i['f12']}",
                    'klt': klt,
                    'fqt': '1',
                    'cb': f'jsonp{int(time.time() * 1000)}'
                }
                yield Request(
                    url='http://push2his.eastmoney.com/api/qt/stock/kline/get',
                    params=params,
                    callback=self.parse_kline,
                    period='1d' if klt == '101' else klt + 'm'
                )

    def parse_kline(self, response):

        if response.jsonp['data'] is None or not response.jsonp['data']['klines']:
            return None

        json_data = response.jsonp['data']

        code = json_data['code']
        name = json_data['name']
        market = json_data['market']
        period = response.period

        for i in json_data['klines']:
            columns = [
                'datetime', 'open', 'close', 'high', 'low', 'volume',
                'amount', 'amplitude', 'range', 'range_money', 'turnover'
            ]
            item = dict(zip(columns, i.split(',')))

            item['code'] = code
            item['name'] = name
            item['market'] = market
            item['period'] = period

            item['open'] = tools.type_converter(item['open'], to=float, force=True)
            item['close'] = tools.type_converter(item['close'], to=float, force=True)
            item['high'] = tools.type_converter(item['high'], to=float, force=True)
            item['low'] = tools.type_converter(item['low'], to=float, force=True)
            item['volume'] = tools.type_converter(item['volume'], to=int, force=True)
            item['amount'] = tools.type_converter(item['amount'], to=float, force=True)
            item['amplitude'] = tools.type_converter(item['amplitude'], to=float, force=True)
            item['range'] = tools.type_converter(item['range'], to=float, force=True)
            item['range_money'] = tools.type_converter(item['range_money'], to=float, force=True)
            item['turnover'] = tools.type_converter(item['turnover'], to=float, force=True)

            yield ETFModel(item)


if __name__ == '__main__':
    spider = ETFSpider()
    spider.start()
