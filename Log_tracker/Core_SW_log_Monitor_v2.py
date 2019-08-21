"""
The purpose of this script is to query logs and alert if there are interesting messages.
"""
from netmiko import Netmiko
import time
import datetime
# import getpass  # getpass freezes with some interpreters under windows

my_user = input('User:')  # getpass()
my_pass = input('Password:')  # getpass.win_getpass()

command = "display logbuffer size 140"
ignore_strings = ['SHELL_LOGIN', 'AAA_LAUNCH', 'AAA_SUCCESS', 'SSH_LOGIN', 'SSH_CONNECTION_CLOSE', my_user]

hosts = ['10.251.0.71',
         '10.251.0.72',
         '10.251.0.73',
         '10.251.0.74',
         '10.251.0.75',
         '10.251.0.76']

test_hosts = ['172.21.13.16', '172.16.37.243']

connections = []
net_connects = []


def printer(cli_output):
    for line in cli_output.splitlines():
        if not any(x in line for x in ignore_strings) and '%' in line:
            print(line)
    print('\n _____________________ \n')


for host in hosts:
    connections.append({
                        "host": host,
                        "username": my_user,
                        "password": my_pass,
                        "device_type": "hp_comware",
                        })


for connection in connections:
    net_connects.append(Netmiko(**connection))


while True:
    print('Checking, please wait... \n')
    for net_connect in net_connects:
        output = net_connect.send_command(command)
        printer(output)

    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Check completed. Waiting...  ', datetime.datetime.now())
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    time.sleep(900)