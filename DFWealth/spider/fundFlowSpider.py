# -*- coding: utf-8 -*-
"""
Created on 2022-10-15 10:41:46
---------
@summary: 个股资金流   东方财富 -> 数据 -> 资金流向 -> 个股资金流
---------
@author: zly717216@163.com
"""

import time

from AioSpider import tools
from AioSpider.http import Request
from AioSpider.spider import Spider

from DFWealth.models import *


class FundFlowSpider(Spider):
    name = 'fundFlowSpider'

    def start_requests(self):

        # @target: https://data.eastmoney.com/zjlx/detail.html
        url = 'https://push2.eastmoney.com/api/qt/clist/get'
        # 今日排行 3日排行 5日排行 10日排行
        fid_list = ['f62', 'f267', 'f164', 'f174']
        name_list = ['今日排行', '3日排行', '5日排行', '10日排行']
        field_list = [
            'f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f124,f1,f13,f3',
            'f12,f14,f2,f127,f267,f268,f269,f270,f271,f272,f273,f274,f275,f276,f257,f258,f124,f1,f13',
            'f12,f14,f2,f109,f164,f165,f166,f167,f168,f169,f170,f171,f172,f173,f257,f258,f124,f1,f13',
            'f12,f14,f2,f160,f174,f175,f176,f177,f178,f179,f180,f181,f182,f183,f260,f261,f124,f1,f13'
        ]

        for f, n, field in zip(fid_list, name_list, field_list):
            params = {
                'cb': f'jQuery1123012642335324644138_{int(time.time() * 1000)}',
                'fid': f,
                'po': '1',
                'pz': '10000',
                'pn': '1',
                'np': '1',
                'fltt': '2',
                'invt': '2',
                'ut': 'b2884a393a59ad64002292a3e90d46a5',
                'fs': 'm:0+t:6+f:!2,m:0+t:13+f:!2,m:0+t:80+f:!2,m:1+t:2+f:!2,m:1+t:23+f:!2,m:0+t:7+f:!2,m:1+t:3+f:!2',
                'fields': field
            }
            yield Request(url, params=params, callback=self.parse, name=n)

    def parse(self, response):

        json_data = response.jsonp['data']
        for i in json_data['diff']:
            if response.name == '今日排行':
                item = {
                    'date': i['f124'], 'code': i['f12'], 'market': i['f13'], 'name': i['f14'], 'close': i['f2'],
                    'range': i['f3'], 'main_buy': i['f62'], 'main_buy_rate': i['f184'], 'super_buy': i['f66'],
                    'super_buy_rate': i['f69'], 'big_buy': i['f72'], 'big_buy_rate': i['f75'], 'middle_buy': i['f78'],
                    'middle_buy_rate': i['f81'], 'small_buy': i['f84'], 'small_buy_rate': i['f87']
                }
                yield Rank1FlowModel(item)
            elif response.name == '3日排行':
                item = {
                    'date': i['f124'], 'code': i['f12'], 'market': i['f13'], 'name': i['f14'], 'close': i['f2'],
                    'middle_buy': i['f273'], 'main_buy': i['f267'], 'main_buy_rate': i['f268'], 'super_buy': i['f269'],
                    'super_buy_rate': i['f270'], 'big_buy': i['f271'], 'big_buy_rate': i['f272'], 'range': i['f127'],
                    'middle_buy_rate': i['f274'], 'small_buy': i['f275'], 'small_buy_rate': i['f276']
                }
                yield Rank3FlowModel(item)
            elif response.name == '5日排行':
                item = {
                    'date': i['f124'], 'code': i['f12'], 'market': i['f13'], 'name': i['f14'], 'close': i['f2'],
                    'middle_buy': i['f170'], 'main_buy': i['f164'], 'main_buy_rate': i['f165'], 'super_buy': i['f166'],
                    'super_buy_rate': i['f167'], 'big_buy': i['f168'], 'big_buy_rate': i['f169'], 'range': i['f109'],
                    'middle_buy_rate': i['f171'], 'small_buy': i['f172'], 'small_buy_rate': i['f173']
                }
                yield Rank5FlowModel(item)
            elif response.name == '10日排行':
                item = {
                    'date': i['f124'], 'code': i['f12'], 'market': i['f13'], 'name': i['f14'], 'close': i['f2'],
                    'middle_buy': i['f180'], 'main_buy': i['f174'], 'main_buy_rate': i['f175'], 'super_buy': i['f176'],
                    'super_buy_rate': i['f177'], 'big_buy': i['f178'], 'big_buy_rate': i['f179'], 'range': i['f160'],
                    'middle_buy_rate': i['f181'], 'small_buy': i['f182'], 'small_buy_rate': i['f183']
                }
                yield Rank10FlowModel(item)
            else:
                continue

            url1 = 'https://push2his.eastmoney.com/api/qt/stock/fflow/daykline/get'
            url2 = 'https://push2.eastmoney.com/api/qt/stock/fflow/kline/get'

            params1 = {
                'cb': f'jQuery112308126243769230457_{int(time.time() * 1000)}',
                'lmt': '0',
                'klt': '101',
                'fields1': 'f1,f2,f3,f7',
                'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65',
                'ut': 'b2884a393a59ad64002292a3e90d46a5',
                'secid': f'{item["market"]}.{item["code"]}',
                '_': int(time.time() * 1000)
            }
            params2 = {
                'cb': f'jQuery112308126243769230457_{int(time.time() * 1000)}',
                'lmt': '0',
                'klt': '1',
                'fields1': 'f1,f2,f3,f7',
                'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65',
                'ut': 'b2884a393a59ad64002292a3e90d46a5',
                'secid': f'{item["market"]}.{item["code"]}',
                '_': int(time.time() * 1000)
            }
            yield Request(url1, params=params1, callback=self.parse_details)
            yield Request(url2, params=params2, callback=self.parse_tick_fund)

    def parse_details(self, response):
        """解析个股资金详情数据"""

        json_data = response.jsonp['data']
        if not json_data:
            return

        for i in json_data['klines']:
            item = i.split(',')
            item.pop(14)
            item.pop(13)
            columns = [
                'date', 'main_buy', 'small_buy', 'middle_buy', 'big_buy', 'super_buy',
                'main_buy_rate', 'small_buy_rate', 'middle_buy_rate', 'big_buy_rate', 'super_buy_rate',
                'close', 'range'
            ]
            item = dict(zip(columns, item))
            item['code'] = json_data['code']
            item['name'] = json_data['name']
            item['market'] = json_data['market']
            yield StockFlowModel(item)

    def parse_tick_fund(self, response):
        """解析当日实时资金流向数据数据"""

        json_data = response.jsonp['data']
        if not json_data:
            return

        for i in json_data['klines']:
            item = i.split(',')
            columns = [
                'date', 'main_buy', 'small_buy', 'middle_buy', 'big_buy', 'super_buy',
            ]
            item = dict(zip(columns, item))

            item['main_buy'] = tools.type_converter(item['main_buy'], force=True, to=float)
            item['small_buy'] = tools.type_converter(item['small_buy'], force=True, to=float)
            item['middle_buy'] = tools.type_converter(item['middle_buy'], force=True, to=float)
            item['big_buy'] = tools.type_converter(item['big_buy'], force=True, to=float)
            item['super_buy'] = tools.type_converter(item['super_buy'], force=True, to=float)

            item['code'] = json_data['code']
            item['name'] = json_data['name']
            item['market'] = json_data['market']
            yield StockTickFlowModel(item)


if __name__ == '__main__':
    spider = FundFlowSpider()
    spider.start()
