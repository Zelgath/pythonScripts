import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

cnx = mysql.connector.connect(
  host="localhost",
  user="someUser",
  passwd="somePassword",
  database= "task_reporting",
  auth_plugin='mysql_native_password'
)
cursor = cnx.cursor()

query = ("SELECT employee_first_name, employee_last_name FROM employees WHERE id_job = 1")

cursor.execute(query)
string = ''

for (employee_first_name, employee_last_name) in cursor:
  print(employee_first_name + ' ' + employee_last_name)
  string += employee_first_name + ' ' + employee_last_name + '\n'


sender_address = ''
sender_pass = ''
receiver_address = 'someadress@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(string, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')

