# -*- coding: utf-8 -*-
"""
Задание 20.5a

Создать функцию configure_vpn, которая использует
шаблоны из задания 20.5 для настройки VPN на маршрутизаторах
на основе данных в словаре data.

Параметры функции:
* src_device_params - словарь с параметрами подключения к устройству 1
* dst_device_params - словарь с параметрами подключения к устройству 2
* src_template - имя файла с шаблоном, который создает конфигурацию для строны 1
* dst_template - имя файла с шаблоном, который создает конфигурацию для строны 2
* vpn_data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна настроить VPN на основе шаблонов
и данных на каждом устройстве с помощью netmiko.
Функция возвращает кортеж с выводом команд с двух
маршрутизаторов (вывод, которые возвращает метод netmiko send_config_set).
Первый элемент кортежа - вывод с первого устройства (строка),
второй элемент кортежа - вывод со второго устройства.

При этом, в словаре data не указан номер интерфейса Tunnel,
который надо использовать.
Номер надо определить самостоятельно на основе информации с оборудования.
Если на маршрутизаторе нет интерфейсов Tunnel,
взять номер 0, если есть взять ближайший свободный номер,
но одинаковый для двух маршрутизаторов.

Например, если на маршрутизаторе src такие интерфейсы: Tunnel1, Tunnel4.
А на маршрутизаторе dest такие: Tunnel2, Tunnel3, Tunnel8.
Первый свободный номер одинаковый для двух маршрутизаторов будет 5.
И надо будет настроить интерфейс Tunnel 5.

Для этого задания тест проверяет работу функции на первых двух устройствах
из файла devices.yaml. И проверяет, что в выводе есть команды настройки
интерфейсов, но при этом не проверяет настроенные номера тунелей и другие команды.
Они должны быть, но тест упрощен, чтобы было больше свободы выполнения.
"""

import yaml
from jinja2 import Environment, FileSystemLoader
from task_20_5 import create_vpn_config
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

def send_config_commands(device, commands):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            hostname = ssh.find_prompt()
            output = ssh.send_config_set(commands)
        result = (hostname+'\n'+output+'\n')
        return result

    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)

def find_tunnels(devices, command):
    tun_intfs = []
    try:
        for device in devices:
            with ConnectHandler(**device) as ssh:
               ssh.enable()
               output = ssh.send_command(command)
               out = output.split()[1::2]
               tun_intfs.extend(out)
        if tun_intfs:
            new_tun_num = int(sorted(tun_intfs)[-1][6:])+1
        else:
            new_tun_num = 0 
        return new_tun_num
        
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)



def configure_vpn (src_device_params, dst_device_params, src_template, dst_template, vpn_data_dict):
    raw_commands = create_vpn_config(src_template, dst_template, vpn_data_dict)
    commands_r1 = raw_commands[0].split('\n+')
    commands_r2 = raw_commands[1].split('\n+')
    output1 = send_config_commands(src_device_params, commands_r1)
    output2 = send_config_commands(dst_device_params, commands_r2)
    return (output1, output2)


if __name__ == "__main__":
   command = "sh run | i Tunnel"
   
   with open("devices.yaml") as f:
           devices = yaml.safe_load(f)
   src_device_params = devices[0]
   dst_device_params = devices[1]
   src_template = "templates/gre_ipsec_vpn_1.txt"
   dst_template = "templates/gre_ipsec_vpn_2.txt"
   new_tun_num = find_tunnels(devices, command)
   
   data = {
       "tun_num": new_tun_num,
       "wan_ip_1": "192.168.100.1",
       "wan_ip_2": "192.168.100.2",
       "tun_ip_1": "10.0.1.1 255.255.255.252",
       "tun_ip_2": "10.0.1.2 255.255.255.252",
   }
   
   print(configure_vpn(src_device_params, dst_device_params, src_template, dst_template, data))
