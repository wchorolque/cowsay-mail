# /usr/bin/env python
# -*- coding: utf-8 -*
#
# script basado en: http://www.sniferl4bs.com/2014/07/automatizacion-reconquistando-la-novia.html
#

import smtplib
import os

from email import MIMEMultipart
from email import MIMEBase

# export MAIL_FROM='mail_from@mail.com'
# export MAIL_PASS='password mail'
# export MAIL_TO='mail_to@mail.com'
mail_from = os.environ.get('MAIL_FROM')
mail_pass = os.environ.get('MAIL_PASS')
mail_to = os.environ.get('MAIL_TO')

if True == os.path.exists('/tmp/mail_log.txt'):
    os.remove('/tmp/mail_log.txt')

os.system('fortune computers | cowsay -f koala | tee /tmp/mail_log.txt')

attach_file = MIMEBase.MIMEBase('multipart', 'encrypted')

with open('/tmp/mail_log.txt', 'rb') as file:
    attach_file.set_payload(file.read())
    attach_file.add_header('Content-Disposition', 'attachment', filename='cowsay.txt')

msg =  MIMEMultipart.MIMEMultipart()
msg['From'] = (mail_from)
msg['To'] = (mail_to)
msg['Subject'] = "Frase del dia"
msg.attach(attach_file)

mailServer = smtplib.SMTP('smtp.gmail.com', 587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login(mail_from, mail_pass)
mailServer.sendmail(mail_from, mail_to, msg.as_string())
mailServer.close()


