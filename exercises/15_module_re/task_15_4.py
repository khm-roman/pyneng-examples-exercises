# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""
import re

regex = (r' description.*')
regex1 = (r'^interface\s(?P<iface>\S+)')

def get_ints_without_description(filename):

    with open (filename) as f:
        result = []
        for line in f:
            match1 = re.search(regex1, line)
            match = re.search(regex, line)
            if match1:
                result1 = match1.group('iface')
                result.append(result1)
            elif match:
                result.remove(result1)

        return result

print(get_ints_without_description('config_r1.txt'))