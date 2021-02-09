# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
address_correct = False
while not address_correct:
  ip = input('Enter IP-address in x.x.x.x format: ')
  octs = ip.split('.')
  if len(octs) == 4:

    for i in octs:
        if i.isdigit():
            a = int(i)
            if 0 <= a < 256:
               pass
            else:
              print('Неправильный IP-адрес')
              break
        else:
          print('Неправильный IP-адрес')
          break
    else:
       address_correct = True
  else:
    print('Неправильный IP-адрес')

first_oct = octs[0]
if 0 < int(first_oct) < 224:
    print('unicast')
elif 223 < int(first_oct) < 240:
    print('multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')