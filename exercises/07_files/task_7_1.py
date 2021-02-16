# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open('ospf.txt') as f:
    l1 = f.readline().strip().split(' ')
    prefix, metric, nexthop, update, interface = l1[-6], l1[-5].strip('[]'), l1[-3].rstrip(','), l1[-2].rstrip(','), l1[-1]
    print(f'''
    {'Prefix':22} {prefix:20}
    {'AD/Metric':22} {metric:20}
    {'Next-Hop':22} {nexthop:20}
    {'Last update':22} {update:20}
    {'Outbound Interface':22} {interface:20}
    ''')