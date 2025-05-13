# Как запустить проект
Скопировать репозиторий и перейти в диресторию с ним:
``` 
git clone https://github.com/Nunime/api_final_yatube
```
```
cd api_final_yatube
```
Создать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Перейти в директорию с django проектом и выполнить миграции:
```
cd yatube_api
```
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```
# Докуметация
Документация доступна после запуска проекта по url:
```
http://127.0.0.1:8000/redoc/
```
