import os, requests

def login(request):
    auth = request.authorization
    if not auth:
        return None, ('Missing credentials', 401)

    basicAuth = (auth.username, auth.password)
    response = requests.post('http://auth_svc:5000/login', basicAuth=basicAuth)    
    