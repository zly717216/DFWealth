# -*- coding: utf-8 -*-
"""
Created on 2022-10-15 10:55:42
---------
@summary: 强势股数据
---------
@author: zly717216@163.com
"""

import time
from datetime import datetime, timedelta

from AioSpider import tools
from AioSpider.http import Request
from AioSpider.spider import Spider

from DFWealth.models import *


class QSGSpider(Spider):
    name = 'qsgSpider'

    def start_requests(self):

        # taget: http://quote.eastmoney.com/ztb/detail#type=qsgc
        for i in self.get_date_range():
            url = "http://push2ex.eastmoney.com/getTopicQSPool"
            params = {
                "cb": "callbackdata5344370",
                "ut": "7eea3edcaed734bea9cbfc24409ed989",
                "dpt": "wz.ztzt",
                "Pageindex": "0",
                "pagesize": "1000",
                "sort": "zdp:desc",
                "date": i,
                "_": int(time.time() * 1000)
            }
            yield Request(url, params=params, callback=self.parse, date=i, encoding='utf-8')

    def get_date_range(self, n=7, exclude_weekend=True):
        """计算时间范围"""

        dt = datetime.now().date()
        date_list = [dt.strftime("%Y%m%d")]

        while len(date_list) < n:

            d = (dt - timedelta(1))

            if exclude_weekend:
                date_list.append(d.strftime("%Y%m%d")) if d.weekday() not in [5, 6] else ...
            else:
                date_list.append(d.strftime("%Y%m%d"))

            dt = d

        return date_list

    def parse(self, response):

        json_data = response.jsonp['data']
        if json_data is None:
            return

        for i in json_data['pool']:
            item = {
                'name': i['n'], 'code': i['c'], 'market': i['m'], 'new_price': i['p'] / 1000, 'range': i['zdp'],
                'zt_price': i['ztp'] / 1000, 'rising_speed': i['zs'], 'is_up': i['nh'], 'select_reasons': i['cc'],
                'zt_statistics': f"{i['zttj']['days']}天{i['zttj']['ct']}板", 'volume_rate': i['lb'],
                'amount': i['amount'], 'cir_market_value': i['ltsz'], 'total_market_value': i['tshare'],
                'turnover': i['hs'], 'date': response.date, 'industry': i['hybk']
            }
            yield QsgPoolModel(item)


if __name__ == '__main__':
    spider = QSGSpider()
    spider.start()
