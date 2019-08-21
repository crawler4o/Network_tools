"""
The purpose of this script is to query logs and alert if there are interesting messages.
"""
from netmiko import Netmiko
import time
# import getpass  # getpass freezes with some interpreters under windows

my_user = input('User:')  # getpass()
my_pass = input('Password:')  # getpass.win_getpass()

# eNG-INT-Kam-Core-1
h3c1 = {
    "host": "10.251.0.73",
    "username": my_user,
    "password": my_pass,
    "device_type": "hp_comware",
}

# eNG-INT-Kel-Core-2
h3c2 = {
    "host": "10.251.0.74",
    "username": my_user,
    "password": my_pass,
    "device_type": "hp_comware",
}

# eNG-LM-CC-Core-2
h3c3 = {
    "host": "10.251.0.72",
    "username": my_user,
    "password": my_pass,
    "device_type": "hp_comware",
}

# eNG-LM-CW-Core-1
h3c4 = {
    "host": "10.251.0.71",
    "username": my_user,
    "password": my_pass,
    "device_type": "hp_comware",
}
# KDC-R4.23-Core-2
h3c5 = {
    "host": "10.251.0.76",
    "username": my_user,
    "password": my_pass,
    "device_type": "hp_comware",
}

# KDC-R4.7-Core-1
h3c6 = {
    "host": "10.251.0.75",
    "username": my_user,
    "password": my_pass,
    "device_type": "hp_comware",
}

# test switch - LMHCoreSW01
h3c_tst = {
    "host": "172.21.13.16",
    "username": my_user,
    "password": my_pass,
    "device_type": "hp_comware",
}

command = "display logbuffer size 140"
ignore_strings = ['SHELL_LOGIN', 'AAA_LAUNCH', 'AAA_SUCCESS', 'SSH_LOGIN', 'SSH_CONNECTION_CLOSE']

while True:
    print('Checking, please wait... \n')
    for device in (h3c_tst,):  # (h3c1, h3c2, h3c3, h3c4, h3c5, h3c6):
        net_connect = Netmiko(**device)
        output = net_connect.send_command(command)
        for line in output.splitlines():
            if not any(x in line for x in ignore_strings) and '%' in line:
                print(line)
        print('\n _____________________ \n')
        net_connect.disconnect()
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Check completed. Waiting...')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    time.sleep(900)
