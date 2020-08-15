#!/usr/bin/env python3

import os
import socket
import csv
my_dir=os.getcwd()
dns_list = os.path.join(my_dir, 'dns_list.csv' )
print(dns_list)

our_hosts_dns_list = ["drive.google.com", "mail.google.com", "google.com"]
our_hosts = {}
our_host_modified = {}
modified_count = 0
for result in our_hosts_dns_list:
    ip_host = socket.gethostbyname(result)
    our_hosts.setdefault(result, ip_host)
    # modified_count += 1
    print(f'IP : {ip_host}')
    print(f'DNS : {result}')
    print("----")
    # if
# print(our_hosts)
# print(dns_list)
a_file = open(dns_list, "w")
writer = csv.writer(a_file)
for key, value in our_hosts.items():
    writer.writerow([key, value])
a_file.close()

# print(f'Всего изменено: {modified_count}')