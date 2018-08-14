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
# to_email = "xakacb4@mail.ru"
to_email = "happypelmeni@yandex.ru"


form = cgi.FieldStorage()

email = form.getfirst("exampleInputEmail1", " Email empty")
phone = form.getfirst("phone", "Phone empty")
text = form.getfirst("exampleFormControlTextarea1", "Text empty")

email = html.escape(email)
# text = html.escape(text)
phone = html.escape(phone)

# text = str(text)
phone = ("  " + str(phone))
text = email + phone
encoded_text = text.encode('utf8')

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login(login, psw)
smtpObj.set_debuglevel(1)
smtpObj.sendmail(from_email, to_email, encoded_text)

print("Content-type: text/html\n")	
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Спасибо!</title>
        </head>
        <body>""")
print("""
	<!-- Yandex.Metrika counter -->
    <script type="text/javascript" >
        (function (d, w, c) {
            (w[c] = w[c] || []).push(function() {
                try {
                    w.yaCounter49865173 = new Ya.Metrika2({
                        id:49865173,
                        clickmap:true,
                        trackLinks:true,
                        accurateTrackBounce:true
                    });
                } catch(e) { }
            });

            var n = d.getElementsByTagName("script")[0],
                s = d.createElement("script"),
                f = function () { n.parentNode.insertBefore(s, n); };
            s.type = "text/javascript";
            s.async = true;
            s.src = "https://mc.yandex.ru/metrika/tag.js";

            if (w.opera == "[object Opera]") {
                d.addEventListener("DOMContentLoaded", f, false);
            } else { f(); }
        })(document, window, "yandex_metrika_callbacks2");
    </script>
    <noscript><div><img src="https://mc.yandex.ru/watch/49865173" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
    <!-- /Yandex.Metrika counter -->
	""")

print("<h1>Ваша заявка принята</h1>")
# print("<p>exampleInputEmail1: {}</p>".format(email))
# print("<p>phone: {}</p>".format(phone))
# print("<p>exampleFormControlTextarea1: {}</p>".format(encoded_text))
# print("<p>msg: {}</p>".format(encoded_text))
# print("<p>msg: {}</p>".format(t))


print("""</body>
        </html>""")

