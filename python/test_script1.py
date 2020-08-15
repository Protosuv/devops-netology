#!/usr/bin/env python3

import os

bash_command = ["cd ~/PycharmProjects/netology.devops/devops-netology", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
# print(result_os)
is_change = False
# for result in result_os.split('\n'):
for result in result_os.splitlines():
    # print(result)
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)
        break
    elif result.find('изменено') != -1:
        prepare_result = result.replace('\tизменено:   ', '')
        print(prepare_result)
        break