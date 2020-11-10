# DSS_WebApp
Web-приложение для системы поддержки принятия решения по выбору материалов для ограждающих конструкций
Web application with use Python, Flask, SQLite
# Запуск и настройка первоначальных настроек Python и других утилит через командную строку Windows (cmd)

Переход к каталогу
```
cd /D I:\WebApp
```
Активация виртуальной среды
```
venv\Scripts\activate
```
### Установка Flask
```
pip install flask

(venv) $ set FLASK_APP=webapp.py
```
Проверка установки Flask
```
(venv) $ py
>>> import flask
```
        
Расширения для Flask	
```
(venv) $ pip install flask-wtf
(venv) $ pip install flask-sqlalchemy
(venv) $ pip install flask-migrate
```          
### Запуск сайта
```
(venv) $ flask run
```
