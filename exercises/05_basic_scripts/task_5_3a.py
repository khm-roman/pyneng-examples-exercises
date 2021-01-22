# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""




access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
dct = {
   "access": {
      "templ": access_template,
      "quest": "Введите номер VLAN: "
    },
   "trunk": {
      "templ": trunk_template,
      "quest": "Введите разрешенные VLANы: "
    }

}
mode = input('ведите режим работы интерфейса (access/trunk): ')
if_num = input ('Введите тип и номер интерфейса: ')
vlans = input('{}'.format(dct[mode]["quest"]))


print('interface {}'.format(if_num))
print('\n'.join(dct[mode]["templ"]).format(vlans))