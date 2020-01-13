import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'rkguptaaa@gmail.com'
email['to'] = 'ravigupta1902@gmail.com'
email['subject'] = 'Hey Bro!!!'

email.set_content =('Hi Ravi, how are you, long time no seen!')
try:    
    with smtplib.SMTP(host = 'smtp.gmail.com', port = '587') as smtp:
        smtp.ehlo()
        smtp.starttls() #connect server securly 
        smtp.login('rkguptaaa@gmail.com', 'Ravi@12345')
        smtp.send_message(email)
        print('email sent')
except Exception as ex:
    print('wrong password')
    print(ex)