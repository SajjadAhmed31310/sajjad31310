import requests
import threading
from pathlib import Path
req = requests.Session()
own_id = int(input("[+] your id in telegram : "))
tele_bot = input("[+] your token bot in telegram : ")

def check():
    users = open('user.txt', 'r')
    tokens = open('token.txt', 'r')
    re = 0
    while True:
        p_u = Path('user.txt').stat().st_size
        p_t = Path('token.txt').stat().st_size
        check = users.readline().split('\n')[0]
        tokened = tokens.readline().split('\n')[0]
        if check == '':
        	users = open('user.txt', 'r')
        	check = users.readline().split('\n')[0]
        if tokened == '':
        	tokens = open('token.txt', 'r')
        	tokened = tokens.readline().split('\n')[0]
        if p_u == 0:
        	urll = f'https://api.telegram.org/bot{tele_bot}/sendmessage'
        	req.post(urll, data={'chat_id': own_id, 'text': f"حاج خلصن اليوزرات روح ضيف يوزرات"})
        	break
        if p_t == 0:
        	urll = f'https://api.telegram.org/bot{tele_bot}/sendmessage'
        	req.post(urll, data={'chat_id': own_id, 'text': f"حاج خلصن التوكنات روح ضيف يوزرات"})
        	break
        url = f'https://botapi.tamtam.chat/chats/{check}?access_token=-tQkbPA8O77qG2Pfy9T3SC0Mj2PM6ga46DROdVZrvSE'
        get = req.get(url).text
        if ("chat_id") in get:
            print(f"[+] trying to hunt >> @{check}")
            re += 1
        else:
            print(f"[+] hunted >> @{check}")
            urlll = f'https://botapi.tamtam.chat/me?access_token={tokened}'
            gettt = req.patch(urlll, json={'username': check, 'name': 'swapped by @izii !'})
            print(gettt.reason)
            urll = f'https://api.telegram.org/bot{tele_bot}/sendmessage'
            req.post(urll, data={'chat_id': own_id, 'text': f"[+] platform : TamTam ,\n[+] swapped @{check},\n[+] requests : {re}"})
            with open("user.txt", "r") as f, open("token.txt", "r") as ft:
            	lines = f.readlines()
            	liness = ft.readlines()
            	with open("user.txt", "w") as f, open("token.txt", "w") as ft:
            		for line in lines:
            			if line.strip("\n") != check:
            				f.write(line)
            		for linee in liness:
            			if linee.strip("\n") != tokened:
            				ft.write(linee)
            pass

def t():
    t2 = []
    t3 = int(input("[+] thread : "))
    for i in range(t3):
        t1 = threading.Thread(target=check)
        t1.start()
        t2.append(t1)
    for thread in t2:
        thread.join()
th = threading.Thread(target=t).start()