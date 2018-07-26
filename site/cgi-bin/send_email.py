#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import smtplib

import sys
reload(sys)
sys.setdefaultencoding('utf8')


url = 'http://api.myip.com'
login = 'api.myip.com@gmail.com'
psw = '89043019528Rustam'
from_email = "api.myip.com@gmail.com"
to_email = "xakacb4@mail.ru"
# to_email = happypelmeni@yandex.ru


r = requests.get(url)
if r.status_code == 200:
    j = r.json()
    text = j.get('ip')
    print('ip =', text)

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login(login, psw)
    smtpObj.sendmail(from_email, to_email, text)
    # print('email sended =', text)
        
else:
    print('Error occured, server status_code =', r.status_code)
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login(login, psw)
    smtpObj.sendmail(from_email, to_email, r.status_code)