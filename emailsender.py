import ssl
import smtplib
from email.message import EmailMessage


email_sender = 'wabmedia2023@gmail.com'
email_password = 'rvbduhniocimmuno'

email_recevier ='ajjayya2002@gmail.com'
subject= "Hello welcome to wabmedia"
body = """ 
Don't forget buy new lanched products in wabmedia
"""

em = EmailMessage()
em['from']= email_sender
em['To']=email_recevier
em['subject']=subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_recevier, em.as_string())

