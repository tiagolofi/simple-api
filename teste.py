from sapi.security import Login, LoginRequest

l = Login()
tokens = l.token(LoginRequest(username = 'admin', password = '1234'))
print(l.access_control(tokens, ['admin']))