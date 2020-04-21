import ipaddress
import json

with open('JSONdata') as f:
    data = json.load(f)

    for device in data:
        ip = device['lanIp']
        sn = device['serial']

        try:
            ipaddress.IPv4Address(ip)
            print(ip + ' is valid for serial ' + sn)

        except ValueError:
            print(ip + ' is not valid for serial '+ sn)