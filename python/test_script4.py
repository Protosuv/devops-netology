#!/usr/bin/env python3

import os
import socket
import csv
import json
import yaml

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
with open(dns_list, newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        dns, ip = row[0], row[1]
        our_hosts_old[dns] = ip
        new_ip = our_hosts[dns]
        old_ip = our_hosts_old[dns]
        if new_ip != old_ip:
            print(f'[ERROR] <{dns}> IP mismatch: <{old_ip}> <{new_ip}>')
# print(our_hosts)
# print("----")
# print(our_hosts_old)
# save dict on CSV file
with open(dns_list, "w") as a_file:
    writer = csv.writer(a_file)
    for key, value in our_hosts.items():
        writer.writerow([key, value])
a_file.close()
# save dict on JSON file
with open('dns_list.json', 'w') as json_file:
    for key, value in our_hosts.items():
        json.dump({key: value}, json_file)
json_file.close()
with open('dns_list.yml', 'w') as yaml_file:
    for key, value in our_hosts.items():
        yaml.dump({key: value}, yaml_file)
yaml_file.close()
