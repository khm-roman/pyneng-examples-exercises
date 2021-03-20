from tabulate import tabulate
from task_12_1 import ping_ip_addresses

columns = ['reachable', 'unreachable']
ip_list = ['192.168.10.15','1.1.1.1', '192.168.10.10', '1.1.1.2', '192.168.10.12']


def print_ip_table(reach_ip, unreach_ip):
    table = {"Reachable": reach_ip, "Unreachable": unreach_ip}
    print(tabulate(table, headers=columns))


print_ip_table(*ping_ip_addresses(ip_list))
