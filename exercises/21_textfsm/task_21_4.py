# -*- coding: utf-8 -*-
"""
Задание 21.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show
с помощью netmiko, а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br
и устройствах из devices.yaml.
"""
import yaml
from operator import index
import textfsm
from textfsm import clitable
from netmiko import ConnectHandler

def send_and_parse_show_command (device_dict, command, templates_path, index='index'):
    with ConnectHandler(**device_dict) as dev:
        dev.enable()
        output = dev.send_command(command)
        cli_table = clitable.CliTable(index, templates_path)
        attributes = {'Command': command, 'Vendor': device_dict['device_type']}
        cli_table.ParseCmd(output, attributes)
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
    devices = 'devices.yaml'
    command = 'sh ip int br'
    templates_path = 'templates'
    with open(devices) as f:
        devices_dict = yaml.safe_load(f)
    for r1 in devices_dict:
       result = send_and_parse_show_command(r1, command, templates_path)
       print(result)
