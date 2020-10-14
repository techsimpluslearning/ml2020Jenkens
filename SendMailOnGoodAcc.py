
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = """Hello,
You are Getting Good Accuracy. Just Check your Github Account"""


sender_address = 'techsimplus@gmail.com'
sender_pass = 'Techsim2020'
receiver_address = 'prateek29mishra@gmail.com'

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Your Accuracy Status'   #The subject line

message.attach(MIMEText(mail_content, 'plain'))

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls() 
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
