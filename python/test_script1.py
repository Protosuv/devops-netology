#!/usr/bin/env python3

import os

bash_command = ["cd ~/PycharmProjects/netology.devops/devops-netology", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
# print(result_os)
is_change = False
modified_count = 0
for result in result_os.splitlines():
    if result.find('изменено') != -1:
        prepare_result = result.replace('\tизменено:   ', '')
        modified_count += 1
        print(f'Измененён: {prepare_result}')
print(f'Всего изменено: {modified_count}')