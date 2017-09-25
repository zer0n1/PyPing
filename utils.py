# -*- coding:utf-8 -*-
#
# Created Time: 2017-09-25 20:56:47
#    File Name: utils.py
#       Author: Zer0n1
#         Mail: zer0n1@163.com
# # # # # # # # # # # # # # # # # # # # # # 

import re

# using regex to find if the string is ip
regex_ip = r'(((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?))'
pattern_ip = re.compile(regex_ip)
def is_ip(expression):
    matcher = pattern_ip.match(expression)
    if matcher:
        return True
    else:
        return False

# calculate checksum of a ICMP Packet
# (may be ok for other packet)
def checksum(packet):
    length = len(packet)
    cks    = 0
    mod    = length % 2

    for i in range(0,length - mod,2):
        cks += (packet[i+1] << 8) + packet[i]

    if mod:
        cks += packet[-1]

    while cks >> 16:
        cks = (cks & 0xFFFF) + (cks >> 16)
    cks = ~cks & 0xFFFF
    cks = cks >> 8 | (cks << 8 & 0xFF00)

    return cks
