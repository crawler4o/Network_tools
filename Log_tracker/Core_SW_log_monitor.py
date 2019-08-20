"""
The purpose of this script is to query logs and alert if there are interesting messages.
"""
from netmiko import Netmiko
import time

my_user = 'v-asen.georgiev@hssbc'
my_pass = ''

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

command = "dis log num 5"
ignore_strings = ['SHELL', 'AAA']

for device in (h3c1, h3c2, h3c3, h3c4, h3c5, h3c6):
    net_connect = Netmiko(**device)
    output = net_connect.send_command(command)
    for line in output.splitline():
        if any('SHELL'
    print(output)
    time.sleep(900)
net_connect.disconnect()
