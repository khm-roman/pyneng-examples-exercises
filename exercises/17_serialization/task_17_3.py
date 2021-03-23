# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
import re

def parse_sh_cdp_neighbors(command_output):
   regex = ('(?P<local_host>\w+)>show cdp neighbors')
   regex1 = ('(?P<host>\w+\d+)\s+(?P<l_i>\w+\s\S+)\s+\d+\s+[\w ]+\s+\S+\s+(?P<r_i>\w+\s\S+)')
   result = {}
   local_host = re.search(regex, command_output).group('local_host')
   result[local_host] = {}
   for m in re.finditer(regex1, command_output):
                result[local_host][m.group('l_i')] = {m.group('host') : m.group('r_i')}
   return result

if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_sh_cdp_neighbors(f.read()))