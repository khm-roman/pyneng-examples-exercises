# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

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