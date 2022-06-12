# -*- coding: utf-8 -*-
"""
Задание 21.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами.
  Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - "templates"

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
"""
import textfsm
from textfsm import clitable
from netmiko import ConnectHandler

def parse_command_dynamic (command_output, attributes_dict, index_file='index', templ_path='templates'):
  cli_table = clitable.CliTable(index_file, templ_path)
  attributes = {'Command': attributes_dict['Command'], 'Vendor': attributes_dict['Vendor']}
  cli_table.ParseCmd(command_output, attributes)
  header = list(cli_table.header)
  output = [list(row) for row in cli_table]
  result = []
  for list1 in output:
     i=0
     dict_1 = {}
     for j in list1:
       dict_1[header[i]] = j
       i+=1
     result.append(dict_1)
  return  result

if __name__ == "__main__":
    r1_params = {
        "device_type": "cisco_ios",
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    attributes_dict = {'Command': 'show ip int br', 'Vendor': 'cisco_ios'}
    with ConnectHandler(**r1_params) as r1:
        r1.enable()
        output = r1.send_command(attributes_dict['Command'])
    result = parse_command_dynamic(output, attributes_dict)
    print(result)
