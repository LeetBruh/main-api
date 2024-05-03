# API авторизации для LeetBruh

## Развёртывание

### Переменные для .env

```text
JWT_SECRET=<Секретный ключ>
JWT_ALGORITHM=HS256
HASH_SALT=<Соль питерская>
POSTGRES_USER=<Пользователь Postgres>
POSTGRES_PASSWORD=<Пароль пользователь Postgres>
DB_HOST=<Хост Postgres>
DB_PORT=<Порт Postgres>
DB_NAME=<Имя БД Postgres>
```

### Команды

#### Запуск

```shell
docker compose up -d
```

#### Запуск с повторной сборкой образа

```shell
docker compose up -d --build
```

#### Остановка

```shell
docker compose down
```