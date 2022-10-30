# -*- coding: utf-8 -*-
"""
Created on 2022-10-08 17:23:33
---------
@summary: 可转债数据
---------
@author: zly717216@163.com
"""

import time
from datetime import datetime

from AioSpider import tools
from AioSpider.http import Request
from AioSpider.spider import Spider

from DFWealth.models import *


class BondSpider(Spider):
    name = 'bondSpider'

    def start_requests(self):

        t = int(time.time() * 1000)

        # target: https://data.eastmoney.com/kzz/default.html
        url = 'https://datacenter-web.eastmoney.com/api/data/v1/get'
        params = {
            'callback': f'jQuery1123011094267134428404_{t}', 'sortColumns': 'PUBLIC_START_DATE', 'sortTypes': '-1',
            'pageSize': '1000',
            'pageNumber': '1',
            'reportName': 'RPT_BOND_CB_LIST',
            'columns': 'ALL',
            'quoteColumns': 'f2~01~CONVERT_STOCK_CODE~CONVERT_STOCK_PRICE,f235~10~SECURITY_CODE~TRANSFER_PRICE,f236~'
                            '10~SECURITY_CODE~TRANSFER_VALUE,f2~10~SECURITY_CODE~CURRENT_BOND_PRICE,f237~10~SECURITY'
                            '_CODE~TRANSFER_PREMIUM_RATIO,f239~10~SECURITY_CODE~RESALE_TRIG_PRICE,f240~10~SECURITY_C'
                            'ODE~REDEEM_TRIG_PRICE,f23~01~CONVERT_STOCK_CODE~PBV_RATIO',
            'source': 'WEB',
            'client': 'WEB'
        }

        yield Request(url, params=params, callback=self.parse)

    def parse(self, response):

        # target: https://quote.eastmoney.com/concept/sh113638.html
        for i in response.jsonp['result']['data']:
            code = i['SECURITY_CODE']
            market = i['TRADE_MARKET']
            item = {
                'name': i['SECURITY_NAME_ABBR'], 'code': code, 'market': market, 'apply_date': i['PUBLIC_START_DATE'],
                'apply_code': i['CORRECODE'], 'apply_up': i['PAR_VALUE'],
                'stock_price': tools.type_converter(i['CONVERT_STOCK_PRICE'], to=float, force=True),
                'conv_stock_price': tools.type_converter(i['INITIAL_TRANSFER_PRICE'], to=float, force=True),
                'conv_value': tools.type_converter(i['TRANSFER_VALUE'], to=float, force=True),
                'new_price': tools.type_converter(i['CURRENT_BOND_PRICENEW'], to=float, force=True),
                'conv_premium': tools.type_converter(i['TRANSFER_PREMIUM_RATIO'], to=float, force=True),
                'security_date': i['SECURITY_START_DATE'], 'per_amount': i['FIRST_PER_PREPLACING'],
                'publish_scale': i['ACTUAL_ISSUE_SCALE'], 'win_publish_date': i['BOND_START_DATE'],
                'win_rate': tools.type_converter(i['ONLINE_GENERAL_LWR'], to=float, force=True),
                'listing_date':  i['LISTING_DATE'], 'expire_date': i['EXPIRE_DATE'],
                'rating': i['RATING'], 'stock_code': i['CONVERT_STOCK_CODE'], 'stock_name': i['SECURITY_SHORT_NAME']
            }
            yield BondListModel(item)

            # 构造 1d、1m、5m、15m、30m、60m、120m K线请求
            for klt in ['101', '1', '5', '15', '30', '60', '120']:
                params = {
                    'fields1': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13',
                    'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61',
                    'beg': '0',
                    'end': '20500101',
                    'ut': 'fa5fd1943c7b386f172d6893dbfba10b',
                    'rtntype': '6',
                    'secid': f'{1 if market == "CNSESH" else 0}.{code}',
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

            yield BondModel(item)


if __name__ == '__main__':
    spider = BondSpider()
    spider.start()
