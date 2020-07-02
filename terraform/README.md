# terraform
## Обучение в Нетологии
###Описание файла .gitignore:
1. Игнорируются внутренние папки Terraform
**/.terraform/*
2. Игнорируются .tfstate файлы
*.tfstate
*.tfstate.*
3. Игнорируются логи
Crash log files: crash.log
4. Игнорируются файлы переопределяющие некоторые параметры:
override.tf
override.tf.json
5. Игнорируются файлы CLI
 .terraformrc
terraform.rc
