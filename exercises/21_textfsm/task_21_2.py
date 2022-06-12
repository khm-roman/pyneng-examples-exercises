# -*- coding: utf-8 -*-
"""
Задание 21.2

Сделать шаблон TextFSM для обработки вывода sh ip dhcp snooping binding
и записать его в файл templates/sh_ip_dhcp_snooping.template

Вывод команды находится в файле output/sh_ip_dhcp_snooping.txt.

Шаблон должен обрабатывать и возвращать значения таких столбцов:
* mac - такого вида 00:04:A3:3E:5B:69
* ip - такого вида 10.1.10.6
* vlan - 10
* intf - FastEthernet0/10

Проверить работу шаблона с помощью функции parse_command_output из задания 21.1.
"""
import textfsm

def parse_command_output (template, command_output):
    with open (template) as t, open(command_output) as out:
        fsm = textfsm.TextFSM(t)
        output = fsm.ParseText(out.read())
        header = fsm.header
        result = [header]+output
    return  result

if __name__ == "__main__":
    output_file = "output/sh_ip_dhcp_snooping.txt"
    template = "templates/sh_ip_dhcp_snooping.template"
    result = parse_command_output(template, output_file)
    print(result)

