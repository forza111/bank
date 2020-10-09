BANK
Приложение BANK позволяет суперпользователю(admin) создавать клиентов банка, вносить деньги на счет. Открывать кредиты.
Авторизованные пользователи могут совершать обмен валюты( на рубли ) по курсу, заданному администратором. Также есть возможность выплачивать кредит со своего рублевого счета.
How to use


Инструкции по настройке проекта, работающем с БД PostgresQL

sudo apt-get update

В виртуальном окружении необходимо выполнить следующие вещи:
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib

pip install django    #установим django

pip install psycopg2    #устновим бэк для PostgresQL

sudo -u postgres psql    #открываем консоль postgres

\password postgres     #задаем пароль администратора БД

Создаем и настраиваем пользователя
create user USER_NAME with password PASSWORD;
alter role user_name set client_encoding to 'utf8';
alter role USER_NAME set default_transactions_isolation to 'read commited';
alter role USER_NAME set timezone to 'UTC';

create database django_db owner USER_NAME;    #Создаем БД для нашего проекта


В корне приложения необходимо создать фаил secret.py, в который поместить приватные настройки
(ВАЖНО! При использовании контроля версий исключить данный фаил от отслеживания)

SECRET_KEY = 'YOUR_CODE' #Ваш секретный ключ

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db', #name database
        'USER': 'USER_NAME', #name superuser
        'PASSWORD' : 'PASSWORD', #password superuser
        'HOST' : 'localhost',
        'PORT' : ''
    }
}

Запустите миграции python manage.py migrate

Запустите сервер python manage.py runserver

В браузере необходимо перейте на адрес 
http://127.0.0.1:8000

Для создания Пользователей необходимо войти в панель администратора
http://127.0.0.1:8000/admin
и создать пользователей, баланс и кредиты

Вновь посетить главную страницу сайта 
http://127.0.0.1:8000 и следуя логике совершать действия, дозволенные рядовому пользователю банка
