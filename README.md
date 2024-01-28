
# CookBook Test

Инструкция по развертыванию и запуску Backend приложения

1) Склонируйте данный репозиторий с помощью команды:

```
$ git clone https://github.com/312NoMad/TestCookBook.git
```

2) Для того чтобы приступить к следующему шагу у вас обязательно должен быть скачан Docker и Docker Compose. Если нет то вот ссылка на [документацию](https://docs.docker.com/desktop/?_gl=1*1fv4xo0*_ga*NjkxNTI0OTQzLjE2ODg3MTgxMTY.*_ga_XJWPQMJYHQ*MTcwNjQ3MTIwNy4zLjEuMTcwNjQ3MTIyMi40NS4wLjA.)
    
3) Запускаем наши контейнеры
```
$ docker-compose up --build
```

4) Если docker-compose удачно запустился и можно открыть страницу по URL адресу http://localhost:8000 , то останавливаем всё комбинацией клавиш Ctrl+C. Запускаем снова но уже командой:
```
$ docker-compose up -d --build
```

5) После успешного запуска применяем создаем и применяем миграции командами:
```
$ docker-compose exec web python manage.py makemigrations
$ docker-comopse exec web python manage.py migrate
```

6) Создаем суперюзера
```
$ docker-compose exec web python manage.py createsuperuser
```

Приложение готово к работе! Теперь можно смотреть и тестировать проект.



Адрес админ панели: http://localhost:8000/admin/

Адрес документации: http://localhost:8000/swagger/
