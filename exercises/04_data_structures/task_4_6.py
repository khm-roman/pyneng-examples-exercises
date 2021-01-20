# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
l1 = ospf_route.split()
prefix, metric, nexthop, update, interface = l1[0], l1[1].strip('[]'), l1[3].rstrip(','), l1[4].rstrip(','), l1[5]
print(f'''
{'Prefix':<20} {prefix:<20}
{'AD/Metric':<20} {metric:<20}
{'Next-Hop':<20} {nexthop:<20}
{'Last update':<20} {update:<20}
{'Outbound Interface':<20} {interface:<20}
''')