# Самоконтроль выполнения задания

1. Файл с `some_fact`находится в подпапке group_vars этого плейбука.
2. Для запуска плейбука выполнялась команда:
   `$ ansible-playbook playbook/site.yml -i playbook/inventory/test.yml`
3. Для шифрования файла использовалась команда:
   `$ ansible-vault encrypt group_vars/el/examp.yml`
4. Для расшифровки файла нужно использовать команду:
   `$ ansible-vault decrypt group_vars/deb/examp.yml`
5. Можно посмотреть содержимое зашифрованного файла при помощи команды:
   `$ ansible-vault view group_vars/deb/examp.yml`
6. Для того, чтобы запустить плейбук в котором часть файлов зашифрована, нужно использовать команду:
   `$ ansible-playbook site.yml -i inventory/prod.yml --ask-vault-pass`
   В таком случае система запросит пароль, для файлов находящихся в шифрованном состоянии.
7. Для подключения к host на windows в документации указывается команда:
   `winrm                          Run tasks over Microsoft's WinRM`
8. Описание модуля для ssh выдаётся командой:
   `~$ ansible-doc -t connection ssh`
9. Для модуля `ssh` пользователь определяется параметром:
`- remote_user
        User name with which to login to the remote server, normally set by the remote_user keyword.
        If no user is supplied, Ansible will let the ssh client binary choose the user as it normally
        [Default: (null)]`