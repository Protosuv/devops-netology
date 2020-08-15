#!/usr/bin/env python3

import os
import argparse
parser = argparse.ArgumentParser(description='Show status of files in Git directory')
parser.add_argument(
    '--indir',
    type=str,
    default='~/PycharmProjects/netology.devops/devops-netology',
    help='Input dir for files')
args = parser.parse_args()
print(f'Каталог git с проектом: {args.indir}')
bash_command = ["cd {}".format(args.indir), "git status"]
# print(bash_command[1])
# print(type(bash_command))
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