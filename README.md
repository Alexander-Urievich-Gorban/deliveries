<h2 align="center">FullStatsNet by Django</h2>


### Инструменты разработки

**Стек:**
- Python >= 3.8
- Django Rest Framework
- Postgres

## Старт

#### 1) Создать образ

    docker-compose build

##### 2) Запустить контейнер

    docker-compose up

## Разработка с Docker

##### 1) Сделать форк репозитория

##### 2) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 3) В корне проекта создать .env.dev

    
    # Data Base
    POSTGRES_DB=orders
    POSTGRES_ENGINE=django.db.backends.postgresql
    POSTGRES_DATABASE=orders
    POSTGRES_USER=orders_user
    POSTGRES_PASSWORD=orders_pass
    POSTGRES_HOST=orders-db
    POSTGRES_PORT=5432
    DATABASE=postgres

    
##### 4) Создать образ

    docker-compose build

##### 5) Запустить контейнер

    docker-compose up
    
##### 6) Создать суперюзера

    docker exec web python manage.py createsuperuser
                                                        
##### 7) Если нужно очистить БД

    docker-compose down -v
 
## License

Copyright (c) 2022-present, Gorban Alexander




