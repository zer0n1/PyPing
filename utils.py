# -*- coding:utf-8 -*-
#
# Created Time: 2017-09-25 20:56:47
#    File Name: utils.py
#       Author: Zer0n1
#         Mail: zer0n1@163.com
# # # # # # # # # # # # # # # # # # # # # # 

import re
import socket

regex_ip = r'(((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?))'
pattern_ip = re.compile(regex_ip)
def is_ip(expression):
    matcher = pattern_ip.match(expression)
    if matcher:
        return True
    else:
        return False
