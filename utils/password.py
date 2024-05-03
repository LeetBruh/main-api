import hashlib
from data.config import HASH_SALT


def hash_password(password: str, salt: str = HASH_SALT) -> str:
    sha256 = hashlib.sha256()
    sha256.update(salt.encode('utf-8'))
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()
