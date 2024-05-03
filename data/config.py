from os import getenv


JWT_SECRET: str = getenv("JWT_SECRET")
JWT_ALGORITHM: str = getenv("JWT_ALGORITHM")
HASH_SALT: str = getenv("HASH_SALT")
DB_HOST: str = getenv("DB_HOST")
DB_PORT: str = getenv("DB_PORT")
DB_NAME: str = getenv("DB_NAME")
DB_USER: str = getenv("POSTGRES_USER")
DB_USER_PASS: str = getenv("POSTGRES_PASSWORD")