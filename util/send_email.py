import smtplib
from email.message import EmailMessage
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 配置邮箱账户及密码
sender = 'xiao_automation_test@outlook.com'
password = 'Babyshadodo2023'
receiver = 'xiao_automation_test@outlook.com'


class EmailSender:
    def __init__(self, sub, cont):
        self.sender = sender
        self.password = password
        self.receiver = receiver
        self.sub = sub
        self.cont = cont
        self.mail_host = 'smtp-mail.outlook.com'
        self.mail_port = 587

    def send_email(self):
        # 构造邮件消息
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = self.receiver
        msg['Subject'] = Header(self.sub, 'utf-8')
        msg.attach(MIMEText(self.cont, 'plain', 'utf-8'))

        # 连接到邮件服务器
        server = smtplib.SMTP(self.mail_host, self.mail_port)
        server.starttls()
        server.login(sender, password)

        # 发送邮件
        server.sendmail(sender, receiver, msg.as_string())

        # 关闭连接
        server.quit()

if __name__ == '__main__':
    send = EmailSender('执行成功通知', '执行成功').send_email()