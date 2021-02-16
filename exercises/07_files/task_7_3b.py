# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vl = input('Enter vlan id please: ')
res = []
with open('CAM_table.txt') as f:
  for line in f:
    if line.startswith(' ') and line[1].isdigit():
      l1 = line.strip().split('   ')
      vlan, mac, interface = int(l1[0]), l1[1].strip(), l1[3].strip()
      line = [int(vlan), mac, interface]
      res.append(line)

for vlan, mac, interface in sorted(res):
    if vlan == int(vl):
      print (f'''{vlan:<9}{mac:<20}{interface}''')
