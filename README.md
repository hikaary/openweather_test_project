 **OpenWeather** - Проект предоставляющий возможность сбора статистики о погоде в различных городах.
___
### **Что внутри**:
* Добавление города
* Сбор информации о погоде каждый чат с https://openweathermap.org
___
### **Как запустить проект**:

* Клонировать репозиторий и перейти в него в командной строке:
```
https://github.com/hikary-dev/openweather_test_project
cd openweather_test_project
```

### **Шаблон наполнения env-файла:**:
1) Шаблон наполнения .env должен быть расположен по пути infra/.env :
    ```
    SECRET=test
    DATABASE_URL=postgresql+asyncpg://test_user:test_pass@database:5432/test_project
    APP_TITLE=OpenWeatheTestProject
    OPENWEATHERMAP_KEY=
   ```


### **Как запустит проект**:
* Поднимаем контейнеры :
   ```
   docker-compose up -d --build
   ```
* Загружаем 50 крупнейших городов мира:
   ```
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   ```
___
### **Документация**:
* Весь список запросов можно посмотреть http://127.0.0.1:8000/docs#/:
```
http://127.0.0.1:8000/docs#/
```

* [Тронин Егор](https://github.com/hikary-dev) 