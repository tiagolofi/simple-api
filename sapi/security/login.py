
from sapi.core.database import DatabaseFactory
from sapi.security.jwt import Jwt

from typing import Dict, Any, Tuple, List
from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    token: str
    type: str = 'Bearer'

class LoginException(Exception):
    def __init__(self, mensagem: str):
        super().__init__(mensagem)

class Login:
    def __init__(self):
        self.users = self.__set_users()
        self.jwt = Jwt()

    def __set_users(self) -> Dict[str, Any]:
        factory = DatabaseFactory()
        database = factory.create()
        return database.get('users')

    def __validate_user(self, request: LoginRequest) -> bool:
        return request.username in [i.get('username') for i in self.users] 

    def __validate_pwd(self, request: LoginRequest) -> Tuple[bool, Dict[str, Any]]:
        user = [{k: v for k, v in i.items()} for i in self.users][0]
        return request.password == user.get('password'), user

    def token(self, request: LoginRequest) -> LoginResponse:
        if not self.__validate_user(request):
            raise LoginException('Invalid credentials')
        
        ok_pwd, user = self.__validate_pwd(request)
        if not ok_pwd:
            raise LoginException('Invalid credentials')
        
        token_jwt = self.jwt.encode(user.get('username', ''), user.get('groups', []))
        
        return LoginResponse(token = token_jwt)

    def access_control(self, response: LoginResponse, roles: List[str]) -> bool:
        payload = self.jwt.decode(response.token)
        for i in payload.get('groups', []):
            return i in roles
