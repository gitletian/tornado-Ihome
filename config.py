# coding:utf-8

import os
from utils.named_dict import d2s

conf = None


def init_conf():
    global conf
    conf = d2s(dev)


dev = dict(
    # Application配置参数
    sys=dict(
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        cookie_secret="p7dxBFZSSO2YRBqE1I4efjJn/51qVUtMpy61qqdd6Mg=",
        xsrf_cookies=True,
        debug=True
    ),
    # 数据库配置参数
    mysql=dict(
        host="172.16.1.100",
        database="tornado1",
        user="tornado1",
        password="123456"
    ),
    # Redis配置参数
    redis=dict(
        host="172.16.1.100",
        port=6379
    ),
    # 日志配置
    log=dict(
        log_path=os.path.join(os.path.dirname(__file__), "logs/log"),
        log_level="warning",
    ),
    # 密码加密密钥
    passwd_hash_key = "nlgCjaTXQX2jpupQFQLoQo5N4OkEmkeHsHD9+BBx2WQ="
)


aut = dict(
    # Application配置参数
    sys=dict(
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        cookie_secret="p7dxBFZSSO2YRBqE1I4efjJn/51qVUtMpy61qqdd6Mg=",
        xsrf_cookies=True,
        debug=True
    ),
    # 数据库配置参数
    mysql=dict(
        host="172.16.1.100",
        database="tornado1",
        user="tornado1",
        password="123456"
    ),
    # Redis配置参数
    redis=dict(
        host="172.16.1.100",
        port=6379
    ),
    # 日志配置
    log=dict(
        log_path=os.path.join(os.path.dirname(__file__), "logs/log"),
        log_level="warning",
    ),
    # 密码加密密钥
    passwd_hash_key = "nlgCjaTXQX2jpupQFQLoQo5N4OkEmkeHsHD9+BBx2WQ="
)


pro = dict(
    # Application配置参数
    sys=dict(
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        cookie_secret="p7dxBFZSSO2YRBqE1I4efjJn/51qVUtMpy61qqdd6Mg=",
        xsrf_cookies=True,
        debug=True
    ),
    # 数据库配置参数
    mysql=dict(
        host="172.16.1.100",
        database="tornado1",
        user="tornado1",
        password="123456"
    ),
    # Redis配置参数
    redis=dict(
        host="172.16.1.100",
        port=6379
    ),
    # 日志配置
    log=dict(
        log_path=os.path.join(os.path.dirname(__file__), "logs/log"),
        log_level="warning",
    ),
    # 密码加密密钥
    passwd_hash_key = "nlgCjaTXQX2jpupQFQLoQo5N4OkEmkeHsHD9+BBx2WQ="
)

# 初始化配置
init_conf()


