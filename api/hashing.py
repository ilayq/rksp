from hashlib import sha256
from .config import f
from .models import ExistingUser
from time import time


async def encode(password: str):
    encoder = sha256()
    encoder.update(password.encode())
    return encoder.hexdigest()


async def make_token(user: ExistingUser) -> str:
    token = (user.model_dump_json() + '|' + str(time())).encode()
    return f.encrypt(token).decode()


async def decode_token(token: str) -> ExistingUser:
    json_dump, _ = f.decrypt(token.encode()).decode().split('|')
    return ExistingUser.parse_raw(json_dump)
