import smtplib
from email.message import EmailMessage

# 配置邮箱账户及密码
sender = '470731804@qq.com'
password = ''
receiver = '470731804@qq.com'


class EmailSender:
    def __init__(self, sub, cont):
        self.sender_email = sender
        self.password = password
        self.receiver_email = receiver
        self.sub = sub
        self.cont = cont

    def send_email(self):
        msg = EmailMessage()
        msg['From'] = self.sender_email
        msg['To'] = self.receiver_email
        msg['Subject'] = self.sub
        msg.set_content(self.cont)
        with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)

if __name__ == '__main__':
    send = EmailSender('执行成功通知', '执行成功').send_email()