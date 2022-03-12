# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = "AAAA:BBBB:CCCC"
mac = mac.split(':')
print('{:b}{:b}{:b}'.format(int(mac[0],16), int(mac[1],16), int(mac[2],16)))

####### or
mac = "AAAA:BBBB:CCCC"
mac_l = mac.split(':')
for i in mac_l:
    mac_l[mac_l.index(i)] = ((bin(int(i, base=16))).lstrip('0b'))
mac_b =  ''.join(mac_l)
print(mac_b)
