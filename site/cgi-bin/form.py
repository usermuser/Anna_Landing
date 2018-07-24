#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import html
import smtplib

from_email = "api.myip.com@gmail.com"
to_email = "xakacb4@mail.ru"
# to_email = "happypelmeni@yandex.ru"

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login(login, psw)
smtpObj.sendmail(from_email, to_email, text)
print('email sended =', text)

form = cgi.FieldStorage()

email = form.getfirst("exampleInputEmail1", "Empty")
text = form.getfirst("exampleFormControlTextarea1", "Empty")

email = html.escape(email)
text = html.escape(text)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>exampleInputEmail1: {}</p>".format(email))
print("<p>exampleFormControlTextarea1: {}</p>".format(text))

print("""</body>
        </html>""")

