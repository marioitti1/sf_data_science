import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from email_info import EMAIL_CONFIG

def ping_website(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print("Ошибка при пинге сайта:", e)
        return False

def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        email = MIMEMultipart()
        email['From'] = sender_email
        email['To'] = recipient_email
        email['Subject'] = subject
        email.attach(MIMEText(message, 'plain'))

        server.sendmail(sender_email, recipient_email, email.as_string())
        print("Сообщение отправлено успешно")
        server.quit()
    except Exception as e:
        print("Ошибка при отправке сообщения:", e)

# URL для пинга
#website_url = "https://tm.alrusdi.ru/"
website_url = 'https://www.google.com/'

# Параметры для отправки почты
sender_email = EMAIL_CONFIG['sender_email']
# Используйте пароль приложения вместо вашего обычного пароля Google
sender_password = EMAIL_CONFIG['email_password']
recipient_email = EMAIL_CONFIG['recipient_email']
subject = 'Сайт доступен'
message = f'Сайт {website_url} доступен'

ping_interval = 300
while True:
    
    if ping_website(website_url):
        print("Сайт доступен")
        send_email(sender_email, sender_password, recipient_email, subject, message)
        break
    else:
        print("Сайт недоступен")
    time.sleep(ping_interval)