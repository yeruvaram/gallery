import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,otp=False,subject=False,body=False):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('yeruvaramanjaneyulu@gmail.com','rnkb tcle izfm jdbz')
    msg=EmailMessage()
    msg['From']='yeruvaramanjaneyulu@gmail.com'
    msg['Subject']='Account Sign up OTP' if subject==False else subject
    msg['To']=to
    body=f'Your one time otp for registration is {otp}' if body==False and otp!=False else body
    msg.set_content(body)
    server.send_message(msg)
    server.quit()