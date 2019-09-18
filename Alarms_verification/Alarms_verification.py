# the Purpose is to check which switches lost their uplink silently

lost_devs = set()
with open('Lost_switches.txt', 'r') as lost_devices:
    for line in lost_devices:
        print(line.strip()[2:])
        lost_devs.add(line.strip()[2:])

alarms_per_device = {x: [] for x in lost_devs}
with open('reported_alarms.txt', 'r') as alarms:
    for line in alarms:
        for dev in alarms_per_device.keys():
            if dev in line:
                alarms_per_device[dev].append(line.strip())


with open('output.txt', 'w+') as file:
    for x in alarms_per_device:
        file.write(f'{x} >>>>>\n')
        file.write(f'{alarms_per_device[x]}\n')
        file.write(f'_________________________________\n')
