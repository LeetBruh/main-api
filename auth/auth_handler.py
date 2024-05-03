import time
from typing import Literal

import jwt

from data.config import JWT_SECRET, JWT_ALGORITHM


def sign_jwt(
        id_type: Literal["user_id", "editor_id", "admin_id"],
        id_: int,
        jwt_type: Literal["editor", "user", "admin"],
        expire_time: int,
        admin: bool = False
) -> str:
    payload = {
        id_type: id_,
        "type": jwt_type,
        "expires": time.time() + expire_time
    }
    if admin:
        payload["admin"] = admin
    token: str = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token


def decode_jwt(token: str) -> dict[str, any] | None:
    try:
        decoded_token: dict[str, any] = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except:
        return None
    return decoded_token if decoded_token["expires"] >= time.time() else None
