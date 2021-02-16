# -*- coding: utf-8 -*-
"""
Задание 7.3a

Сделать копию скрипта задания 7.3.

Переделать скрипт:  Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Обратите внимание на vlan 1000 - он должен выводиться последним.
Правильной сортировки можно добиться, если vlan будет числом, а не строкой.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
res = []
with open('CAM_table.txt') as f:
  for line in f:
    if line.startswith(' ') and line[1].isdigit():
      l1 = line.strip().split('   ')
      vlan, mac, interface = int(l1[0]), l1[1].strip(), l1[3]
      line = [int(vlan), mac, interface]
      res.append(line)

for vlan, mac, interface in sorted(res):
      print (f'''{vlan:<9}{mac:<20}{interface}''')
