#!/usr/bin/env python3

import os
import socket
import json

my_dir = os.getcwd()
dns_list = os.path.join(my_dir, 'dns_list.csv')
# print(dns_list)

our_hosts_dns_list = ["drive.google.com", "mail.google.com", "google.com"]
our_hosts = {}
our_hosts_old = {}
for result in our_hosts_dns_list:
    ip_host = socket.gethostbyname(result)
    our_hosts.setdefault(result, ip_host)
    # print(f'DNS : {result}')
    # print(f'IP : {ip_host}')

with open('dns_list.json') as json_file:
    our_hosts_old = json.load(json_file)
    for dns in our_hosts_old:
        new_ip = our_hosts[dns]
        old_ip = our_hosts_old[dns]
        if new_ip != old_ip:
            print(f'[ERROR] <{dns}> IP mismatch: <{old_ip}> <{new_ip}>')
json_file.close()
# print(our_hosts)
# print("----")
# print(our_hosts_old)

# save dict on JSON file (variant 2)
with open('dns_list.json', 'w') as json_file:
    json.dump(our_hosts, json_file)
json_file.close()

