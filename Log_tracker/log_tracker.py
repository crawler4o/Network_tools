"""
The purpose of this script is to query logs and alert if diff.
"""
from netmiko import Netmiko
import time
# from getpass import getpass

cisco1 = {
    "host": "route-views.routeviews.org",
    "username": "rviews",
    "password": "",  # getpass(),
    "device_type": "cisco_ios",
}

net_connect = Netmiko(**cisco1)
command = "show ip int brief"

print()
print(net_connect.find_prompt())

for x in range(5):
    output = net_connect.send_command(command)
    print(output)
    print(type(output))
    print()
    time.sleep(10)
net_connect.disconnect()
