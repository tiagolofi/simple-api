
from os import getenv, listdir
from typing import List, Dict, Any
from dotenv import load_dotenv
from jose import jwt
from datetime import datetime, timedelta, timezone

class Jwt:
    def __init__(self) -> None:
        if '.env' in listdir():
            load_dotenv(override=True)

        self.PRIVATE_KEY = '-----BEGIN PRIVATE KEY-----\n' + getenv('private.key', '') + '\n-----END PRIVATE KEY-----'
        self.PUBLIC_KEY = '-----BEGIN PUBLIC KEY-----\n' + getenv('public.key', '') + '\n-----END PUBLIC KEY-----'
        self.ALGHORITHM = 'RS256'
        self.expiration_min = getenv('expiration.minutes', 10)

    def encode(self, subject: str, groups: List[str]) -> str:
        iat = datetime.now(timezone.utc)
        exp = iat + timedelta(minutes=self.expiration_min)
        return jwt.encode(
            claims = {'sub': subject, 'groups': groups, 'exp': exp, 'iat': iat}, 
            key=self.PRIVATE_KEY,
            algorithm=self.ALGHORITHM
        )
    
    def decode(self, token: str) -> Dict[str, Any]:
        return jwt.decode(token=token, key=self.PUBLIC_KEY, algorithms=[self.ALGHORITHM])
    