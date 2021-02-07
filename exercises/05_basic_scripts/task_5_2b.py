# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
net = argv[1]
#net = input ('Enter network in format x.x.x.x/xx: ')
mask = net.split('/')[1]
mask_b = "1" * int(mask) + "0" * (32-int(mask))
mask_dd = [int(mask_b[0:8], 2), int(mask_b[8:16], 2), int(mask_b[16:24],2), int(mask_b[24:32], 2)]
ip = net.split('/')[0].split('.')
ip_b = '{:08b}{:08b}{:08b}{:08b}'.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3]))
net_b = (ip_b[0:int(mask)]) + "0" * (32-int(mask))
net_dd = [int(net_b[0:8], 2), int(net_b[8:16], 2), int(net_b[16:24],2), int(net_b[24:32], 2)]

ip_template = '''
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''
print(ip_template.format(net_dd[0], net_dd[1], net_dd[2], net_dd[3]))

mask_template = '''
Mask:
/{4}
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''
print(mask_template.format(mask_dd[0], mask_dd[1], mask_dd[2], mask_dd[3], mask))