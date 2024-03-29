# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""
from ipaddress import ip_address
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
import netmiko
import yaml
import subprocess as sp

def ping_one_ip (address):
    result = sp.run(['ping', '-c', '2', address],
                           stdout=sp.PIPE,
                           stderr=sp.PIPE,
                           encoding='utf-8')
    return result

def ping_ip_addresses (ip_list, limit=3):
    success = []
    unsuccess = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
            result = executor.map(ping_one_ip, ip_list)
            for ip, output in zip(ip_list, result):
                if output.returncode == 0:
                    success.append(ip)
                else:
                    unsuccess.append(ip)

    return (success,unsuccess)
    


if __name__ == '__main__':
    ip_addresses = ['192.168.100.1', '192.168.100.2', '192.168.100.3', '192.168.100.4'] 
    pprint(ping_ip_addresses(ip_addresses))

