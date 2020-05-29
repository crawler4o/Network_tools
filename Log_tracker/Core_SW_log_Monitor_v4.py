"""
The purpose of this script is to query logs and alert if there are interesting messages.
"""
from netmiko import Netmiko
import time
import datetime
from playsound import playsound
import getpass

my_user = input('User:')
my_pass = getpass.getpass('Password:')

command = "display logbuffer size 140"
ignore_strings = ['SHELL_LOGIN', 'AAA_LAUNCH', 'AAA_SUCCESS', 'SSH_LOGIN', 'SSH_CONNECTION_CLOSE', 'CFGMAN_EXIT',
                  'SHELL_LOGOUT', 'v-gurinder.singh@hssbc', 'v-alireza.moharami@hssbc', 'jluo@hssbc',
                  'v-david.men@hssbc', 'v-tao.lin@hssbc;', my_user] # , 'iskobkarev@hssbc;'
                    # 'Member port Ten-GigabitEthernet9/0/28 of aggregation group BAGG33']


significant_line_dist = ['%', 'state is changed']

highlight_key_words = ['OSPF', 'BGP', 'state is changed']

hosts = ['10.251.0.71',
         '10.251.0.72',
         '10.251.0.73',
         '10.251.0.74',
         '10.251.0.75',
         '10.251.0.76']

test_hosts = ['172.21.13.16', '172.16.37.243']  # not in use currently

connections = []
net_connects = []


def printer(cli_output):
    interesting_lines_count = 0
    for line in cli_output.splitlines():
        if not any(x in line for x in ignore_strings) and any(y in line for y in significant_line_dist):
            if any(z in line for z in highlight_key_words):
                print('**********  ' + line + '  **********')
                interesting_lines_count += 1
            else:
                print(line)
    print('  _____________________ \n')

    return interesting_lines_count


for host in hosts:
    connections.append({
                        "host": host,
                        "username": my_user,
                        "password": my_pass,
                        "device_type": "hp_comware",
                        })


for connection in connections:
    net_connects.append(Netmiko(**connection))

interesting_lines_old = 0

while True:
    interesting_lines_new = 0
    interesting_diff = 0
    print('Checking, please wait... \n')
    for net_connect in net_connects:
        output = net_connect.send_command(command)
        interesting_lines_new += printer(output)

    interesting_diff = interesting_lines_new - interesting_lines_old
    interesting_lines_old = interesting_lines_new

    if interesting_diff > 0:
        playsound('conscript-reporting.mp3')

    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(f'Total number of interesting lines =             {interesting_diff}')
    print(f'Total number of interesting lines =             {interesting_lines_new}')
    print('Check completed. Waiting...                     ', datetime.datetime.now())
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    time.sleep(900)

    # Warning, there is a design problem with the tool.
    # The results will not be accurate in case some lines fall behind during the same check new lines appear.
    # Also no notification will be played if the number of disappearing new lines
    # exceeds the number of new interesting lines.
