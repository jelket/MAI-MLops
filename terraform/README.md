# Terraform: Создание S3-бакета в Yandex Cloud

## 🚀 Быстрый старт

1. Создайте `terraform.tfvars` с параметрами:
```hcl
yc_token        = "ваш_oauth_токен"
yc_cloud_id     = "идентификатор_облака"
yc_folder_id    = "идентификатор_каталога"
bucket_name     = "уникальное_имя_бакета"
bucket_access_key = "ключ_доступа_s3" 
bucket_secret_key = "секретный_ключ_s3"

Выполните команды:

```bash
terraform init
terraform plan
terraform apply
```

Необходимые параметры

yc_token - Токен для аутентификации в API
yc_cloud_id - Идентификатор облака
yc_folder_id - Идентификатор каталога
bucket_name - Название бакета
bucket_access_key - Ключ доступа
bucket_secret_key - Секретный ключ

Выходные данные
После выполнения вы получите:

Имя созданного бакета
Доменное имя для доступа к хранилищу

Предварительные требования

Terraform 0.12+
Аккаунт Yandex Cloud
Установленный и настроенный Yandex Cloud CLI
