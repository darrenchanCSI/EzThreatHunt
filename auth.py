# ========================
# Imports
# ========================
import requests, pickle, os
from bs4 import BeautifulSoup

# ========================
# URLs
# ========================
loginURL = '/login'
sid_url = '/fapi/auth/verify'
passwordStep = '/fapi/auth/v2/step/password'
logout_url = '/fapi/auth/logout'

# ========================
# Others
# ========================
session = requests.session()

def checkDirectory(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

def saveCookies(cookieJar, filename):
    checkDirectory(filename)
    with open(filename, 'wb') as f:
        pickle.dump(cookieJar, f)
        
def saveHeaders(headers, filename):
    checkDirectory(filename)
    with open(filename, 'wb') as f:
        pickle.dump(headers, f)
        
def getCookies(server):
    filePath = "./auth/" + server.name + ".cookiejar"
    with open(filePath, 'rb') as f:
        return pickle.load(f)

def getHeaders(server):
    filePath = "./auth/" + server.name + ".headerfile"
    with open(filePath, 'rb') as f:
        return pickle.load(f)

def loadAuth(server):
    server.header = getHeaders(server)
    server.cookie = getCookies(server)
    
def authenticate(server, username, password):
    authSession = requests.session()
    loginReply = authSession.get(server.url + loginURL)
    csrf_token = BeautifulSoup(loginReply.text, 'lxml').select_one('meta[name="csrf-token"]')['content']
    cookiePage = authSession.get(server.url + sid_url)
    cookies = authSession.cookies.get_dict()
    headers = {
        'csrf-token': csrf_token,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Accept': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    
    data = json.dumps({
        'username': username,
        'password': password,
    })
    
    #data = '{"username":' + "\"" + username + "\"" + ',"password":' + "\"" + password + "\"" + '}'
    authResult = session.post(server.url + passwordStep, headers=headers, cookies=cookies, data=data)
    if (authResult.text == "{\"use2fa\":false}" or authResult.text == "{\"use2fa\":false,\"trustedDevice\":false}"):
        server.header = headers
        server.cookie = cookies
        saveCookies(cookies, "./auth/" + server.name + ".cookiejar")
        saveHeaders(headers, "./auth/" + server.name + ".headerfile")
        return True
    else:
        return False
    
def logout(server):
    return session.get(server.url + logout_url, headers = server.header, cookies = server.cookie).text == "{\"message\":\"Session terminated\"}"
