import requests
import base64



def test():
    headers = {
        "Host": "192.168.0.1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding":"gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "36",
        "Origin": "http://192.168.0.1",
        "Connection": "keep-alive",
        "Referer": "http://192.168.0.1/login.asp?0",
        "Cookie": "ecos_pw=YWRtaW4=cvb:language=en",
        "Upgrade-Insecure-Requests": "1"
    }
    username = "admin"
    password = "YWRtaW4="
    # hashed_password = base64.b64encode(password.encode('utf-8'))
    payload = {"username":username, "password":password}
    response = requests.post("http://192.168.0.1/LoginCheck", data=payload, headers=headers)
    print(response.status_code)
                

test()