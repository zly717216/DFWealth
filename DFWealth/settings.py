# -*- coding: utf-8 -*-
"""
Created on 2022-10-08 17:23:33
---------
@summary: 配置文件
---------
@author: zly717216@163.com
"""

import os
import sys
from pathlib import Path

from AioSpider.constants import LogLevel, Color, When, UserAgent, WriteMode


# ---------------------------------- 系统相关配置 ---------------------------------- #

# 切换工作路径为当前项目路径
AIOSPIDER_PATH = Path(__file__).parent
os.chdir(AIOSPIDER_PATH)
sys.path.insert(0, AIOSPIDER_PATH)

# url缓存方式，记录已爬取url的状态，默认 queue（队列引擎），redis（redis引擎）
BACKEND_CACHE_ENGINE = {
    'queue': {
        'enabled': True,                    # 指定为队列引擎
    },
    'redis': {
        'enabled': False,                   # 指定为redis引擎
        'host': '101.42.138.122',           # ip / 域名
        'port': 6379,                       # redis端口，默认一般都是6379
        'db': 0,                            # 数据库
        'user': '',                         # 用户名，一般没有；没有就指定为空或None
        'password': '717216'                # 认证密码，一般没有；没有就指定为空或None
    }
}


# 日志配置
LOGGING = {
    # 'LOG_NAME': 'aioSpider',                        # 日志名称
    'LOG_PATH': AIOSPIDER_PATH / "log",               # 日志存储路径
    'LOG_CMD_FORMAT': '%(asctime)s - %(filename)s - %(lineno)s - %(levelname)s: %(message)s',   # 控制台输出日志格式
    'LOG_FILE_FORMAT': '%(asctime)s - %(levelname)s: %(message)s',  # 文件输出日志格式
    'LOG_CMD_DATE_FORMAT': '%Y-%m-%d %H:%M:%S',     # 控制台输出日志时间格式
    'LOG_FILE_DATE_FORMAT': '%Y-%m-%d %H:%M:%S',    # 文件输出日志时间格式
    'LOG_CMD_LEVEL': LogLevel.DEBUG,                # 控制台输出日志等级
    'LOG_FILE_LEVEL': LogLevel.DEBUG,                # 文件输出日志等级
    'LOG_COLORFUL': True,                           # 是否带有颜色
    'LOG_IS_CONSOLE': True,                         # 是否打印到控制台
    'LOG_IS_FILE': False,                           # 是否写文件
    'LOG_MODE': "a",                                # 写文件的模式
    'LOG_LIMIT_BYTES': 10 * 1024 * 1024,            # 每个日志文件的默认最大字节数
    'LOG_BACKUP_COUNT': 10,                         # 日志文件保留数量
    'LOG_ENCODING': 'utf-8',                        # 日志文件编码
    'LOG_COLOR_DICT': {
        'debug': Color.GREEN, 'info': Color.WHITE, 'warning': Color.YELLOW,
        'error': Color.RED, 'critical': Color.PINK
    },                                              # 日志颜色
    'OTHERS_WHEN': When.DAYS,                       # 日志轮询间隔
    'OTHERS_LOG_LEVEL': LogLevel.ERROR,             # 第三方库的log等级
}

# -------------------------------------------------------------------------------- #

# ---------------------------------- 爬虫相关配置 ---------------------------------- #

REQUEST_CONCURRENCY_COUNT = 1000        # 请求并发数
MAX_CONNECT_COUNT = 300                 # 请求最大连接数
NO_REQUEST_SLEEP_TIME = 3               # 单位秒，请求队列无请求时休眠时间
REQUEST_CONCURRENCY_SLEEP = 0           # 单位秒，每 REQUEST_CONCURRENCY_COUNT 个请求休眠1秒
PER_REQUEST_SLEEP = 0                   # 单位秒，每并发1个请求时休眠1秒
REQUEST_TIMEOUT = 300                   # 请求最大超时时间

# 请求失败是否要重试
RETRY_ENABLE = True
# 每个请求最大重试次数，RETRY_ENABLE指定为True时生效
MAX_RETRY_TIMES = 3
# 重试状态码，MAX_RETRY_TIMES大于0和RETRY_ENABLE指定为True时生效
RETRY_STATUS = [400, 403, 404, 500, 501, 502, 503]
# 优先级

# 默认请求头，优先级：spider headers > 默认headers > random headers
HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
}
RANDOM_HEADERS = True                   # 随机UserAgent
RETRY_FAILED_REQUESTS = False           # 爬虫启动时，重新抓取失败的requests
# 字符串类型或可迭代对象，值为chrome, ie, opera, firefox, ff, safari，若指定RANDOM_HEADERS为True时则不生效
USER_AGENT_TYPE = UserAgent.CHROME

REQUEST_PROXY = None                    # 代理 支持http和https，默认为NNone，不设置代理，需要设置则可以按照以下格式设置
# REQUEST_PROXY = 'http://127.0.0.1:7890'
# REQUEST_PROXY = '127.0.0.1:7890'

# 数据管道
ITEM_PIPELINES = {
    "DFWealth.pipelines.BondListPipeline": 100,
    "DFWealth.pipelines.BondPipeline": 200,
    "DFWealth.pipelines.StockListPipeline": 300,
    "DFWealth.pipelines.Stock1dPipeline": 400,
    "DFWealth.pipelines.Stock1mPipeline": 401,
    "DFWealth.pipelines.Stock5mPipeline": 402,
    "DFWealth.pipelines.Stock15mPipeline": 403,
    "DFWealth.pipelines.Stock30mPipeline": 404,
    "DFWealth.pipelines.Stock60mPipeline": 405,
    "DFWealth.pipelines.Stock120mPipeline": 406,
    "DFWealth.pipelines.ETFListPipeline": 500,
    "DFWealth.pipelines.ETFPipeline": 600,
    "DFWealth.pipelines.BlockListPipeline": 700,
    "DFWealth.pipelines.BlockPipeline": 800,
    "DFWealth.pipelines.IndexListPipeline": 900,
    "DFWealth.pipelines.Rank1FlowPipeline": 1000,
    "DFWealth.pipelines.IndexPipeline": 1100,
    "DFWealth.pipelines.Rank3FlowPipeline": 1200,
    "DFWealth.pipelines.Rank5FlowPipeline": 1300,
    "DFWealth.pipelines.Rank10FlowPipeline": 1400,
    "DFWealth.pipelines.StockFlowPipeline": 1500,
    "DFWealth.pipelines.StockTickFlowPipeline": 1600,
    "DFWealth.pipelines.DtbPoolPipeline": 1700,
    "DFWealth.pipelines.ZtbPoolPipeline": 1800,
    "DFWealth.pipelines.QsgPoolPipeline": 1900,
    "DFWealth.pipelines.ZbgPoolPipeline": 2000,
}

# 下载中间件
DOWNLOAD_MIDDLEWARE = {
    "AioSpider.middleware.download.FirstMiddleware": 100,
    "AioSpider.middleware.download.HeadersMiddleware": 101,
    "AioSpider.middleware.download.LastMiddleware": 102,
    "AioSpider.middleware.download.RetryMiddleware": 103,
    "AioSpider.middleware.download.ProxyMiddleware": 104,
    "AioSpider.middleware.download.ExceptionMiddleware": 105,
}

# 数据去重
DATA_FILTER_ENABLE = False                  # 是否启用数据去重
CACHED_ORIGIN_DATA = False                  # 是否启用缓存原始数据 数据量大的时候建议设置为True，每次启动将会自动去重
CAPACITY = 5000 * 10000                     # 去重的数据容量 数据器中可以容纳100亿条数据
MODEL_NAME_TYPE = 'smart'                   # lower / upper / smart，处理表明的方式

# URL去重
CACHED_REQUEST = {
    'CACHED': True,                         # 是否缓存爬过的请求 将爬过的请求缓存到本地
    'LOAD_SUCCESS': False,                  # 将CACHED_REQUEST缓存中成功的请求加载到队列
    'LOAD_FAILURE': False,                  # 将CACHED_REQUEST缓存中失败的请求加载到队列
    'CACHED_EXPIRE_TIME': 60 * 60 * 24 * 30,    # 缓存时间 秒
    'CACHE_PATH': AIOSPIDER_PATH / "cache",     # 数据和资源缓存路径
    'FILTER_FOREVER': True                  # 是否永久去重，配置此项 CACHED_EXPIRE_TIME 无效
}

IGNORE_STAMP = True                         # 去重忽略时间戳
STAMP_NAMES = ['_']                         # 时间戳字段名，一般指请求中params、data中的参数

USE_DNS_CACHE = True                        # 使用内部DNS映射缓存，用来查询DNS，使建立连接速度更快

# -------------------------------------------------------------------------------- #

# --------------------------------- 数据库相关配置 --------------------------------- #
DATABASE_ENGINE = {
    'CSVFile': {
        'ENABLE': False,
        'CSV_PATH': Path(AIOSPIDER_PATH) / 'data',
        'ENCODING': 'utf-8',
        'WRITE_MODE': WriteMode.A
    },
    'SQLITE': {
        'ENABLE': True,
        'SQLITE_PATH': Path(AIOSPIDER_PATH) / 'data',
        # 'SQLITE_PATH': Path(r'D:\feapder\wenzz'),
        'SQLITE_DB': "stock.db3",
        'SQLITE_TIMEOUT': 10
    },
    'MYSQL': {
        'ENABLE': False,
        'MYSQL_HOST': "127.0.0.1",
        'MYSQL_PORT': 3306,
        'MYSQL_DB': "bond",
        'MYSQL_USER_NAME': "root",
        'MYSQL_USER_PWD': "717216",
        'MYSQL_CHARSET': "utf8mb4",
        'MYSQL_CONNECT_TIMEOUT': 5,
        'MYSQL_TIME_ZONE': '+0:00',
    },
    'MONGODB': {
        'ENABLE': False,
        'MONGO_HOST': "localhost",
        'MONGO_PORT': 27017,
        'MONGO_DB': "",
        'MONGO_USER_NAME': "",
        'MONGO_USER_PWD': ""
    },
}

# -------------------------------------------------------------------------------- #

# ---------------------------------- 消息通知配置 ---------------------------------- #

# 钉钉报警
DINGDING_WARNING_URL = ""           # 钉钉机器人api
DINGDING_WARNING_PHONE = ""         # 报警人 支持列表，可指定多个
DINGDING_WARNING_ALL = False        # 是否提示所有人， 默认为False
# 邮件报警
EMAIL_SENDER = ""                   # 发件人
EMAIL_PASSWORD = ""                 # 授权码
EMAIL_RECEIVER = ""                 # 收件人 支持列表，可指定多个
EMAIL_SMTPSERVER = "smtp.163.com"   # 邮件服务器 默认为163邮箱
# 企业微信报警
WECHAT_WARNING_URL = ""             # 企业微信机器人api
WECHAT_WARNING_PHONE = ""           # 报警人 将会在群内@此人, 支持列表，可指定多人
WECHAT_WARNING_ALL = False          # 是否提示所有人， 默认为False
# 时间间隔
WARNING_INTERVAL = 3600             # 相同报警的报警时间间隔，防止刷屏; 0表示不去重
WARNING_LEVEL = "DEBUG"             # 报警级别， DEBUG / ERROR
WARNING_FAILED_COUNT = 1000         # 任务失败数 超过WARNING_FAILED_COUNT则报警

# -------------------------------------------------------------------------------- #
