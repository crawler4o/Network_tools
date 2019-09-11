#  show inventory?  What I need is a quantity of each line card type, chassis type, power supply type in production.

from netmiko import Netmiko


my_user = input('User:')  # getpass()
my_pass = input('Password:')  # getpass.win_getpass()


command = "show inventory"

hosts = [
        '10.8.254.9',
        '10.8.254.6',
        '10.8.254.8',
        '10.26.101.59',
        '10.26.101.60',
        '10.26.101.4',
        '10.26.101.3',
        # '10.26.101.93',
        # '10.26.101.92',
        # '10.26.101.66',
        # '10.26.101.67',
        '10.27.1.2',
        '10.26.101.57',
        '10.26.101.58',
        '10.27.1.1',
        '10.27.1.3',
        ]

connections = []
net_connects = []


def printer(dev, cli_output):
    with open('line_cards.txt', 'a+') as file:
        file.write('\n')
        for line in cli_output.splitlines():
            if 'WS-X' in line or 'WS-CAC' in line or 'WS-C65' in line:
                file.write(f'{dev} >>> {line} \n')
        file.write('______________________________________________________________________________')


for host in hosts:
    connections.append({
        "host": host,
        "username": my_user,
        "password": my_pass,
        "device_type": "cisco_ios",
    })


for connection in connections:
    net_connects.append(Netmiko(**connection))


for net_connect in net_connects:
    output = net_connect.send_command(command)
    dev_id = net_connect.find_prompt()
    printer(dev_id, output)
    net_connect.disconnect()
