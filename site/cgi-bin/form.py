#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import html
import smtplib

import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


login = 'api.myip.com@gmail.com'
psw = '89043019528Rustam'
from_email = "api.myip.com@gmail.com"
to_email = "xakacb4@mail.ru"
# to_email = "happypelmeni@yandex.ru"


form = cgi.FieldStorage()
email = form.getfirst("exampleInputEmail1", " Email empty")
phone = form.getfirst("phone", "Phone empty")
text = form.getfirst("exampleFormControlTextarea1", "Text empty")
email = html.escape(email)
text = html.escape(text)
encoded_text = text.encode('utf8')


smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login(login, psw)
smtpObj.sendmail(from_email, to_email, "Telephone: " + phone + " Text:" + encoded_text)
# print('email sended =', text)


print("Content-type: text/html\n")	
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Спасибо!</title>
        </head>
        <body>""")

print("<h1>Ваша заявка принята</h1>")
# print("<p>exampleInputEmail1: {}</p>".format(email))
# print("<p><a href="счастьевкаждыйдом.рф"></a></p>")
# print("<p>exampleFormControlTextarea1: {}</p>".format(text))

print("""</body>
        </html>""")

