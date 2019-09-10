# #-----------------发送qq邮件加附件 (一个或多个)---------------------------
# coding:utf-8
import smtplib
from email.header import Header

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

mail_host = "smtp.qq.com"
# mail_host = "smtp.163.com"
mail_user = "1836906814@qq.com"
mail_pass = "nnssczhntbqvbacb"
sender = "1836906814@qq.com"
receivers = ["1467323146@qq.com","673007285@qq.com"]
content = "快乐飞速度快了凡事都靠"
title = "实打实的是否认同"

def sendEmail():
    file_path = r"C:\Users\Administrator\Desktop\sys.html"
    with open(file_path,"rb") as fp:
        mail_body = fp.read()
    msg = MIMEMultipart()
    msg["From"] = formataddr(["zhongwen",sender])
    # msg["To"] = ",".join(receivers)
    to = ",".join(receivers)
    for i in ["li<1467323146@qq.com>","le<673007285@qq.com>"]:
        msg["To"] = formataddr([i, to])
    msg["Subject"] = title
    # 正文
    body = MIMEText(content, 'plain', "utf-8")
    msg.attach(body)
    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    fn = Header("test_report.html", 'utf-8').encode()
    att["Content-Disposition"] = 'attachment; filename=%s' % fn
    msg.attach(att)
    try:
        # smtp = smtplib.SMTP_SSL(mail_host,465)
        smtp = smtplib.SMTP(mail_host)
        smtp.login(mail_user,mail_pass)
        smtp.sendmail(sender,receivers,msg.as_string())
        print("成功过")
        smtp.quit()
    except smtplib.SMTPException as e:
        print(e)
if __name__ == "__main__":
    sendEmail()



# #-----------------发送163或qq邮件(一个或多个)---------------------------
# # coding:utf-8
# import smtplib
# from email.mime.text import MIMEText
# from email.utils import formataddr
#
# mail_host = "smtp.qq.com"
# # mail_host = "smtp.163.com"
# mail_user = "1836906814@qq.com"
# mail_pass = "nnssczhntbqvbacb"
# sender = "1836906814@qq.com"
# receivers = ["1467323146@qq.com","673007285@qq.com"]
# content = "方式规范的非dd官方"
# title = "更丰富的覆盖dd广泛"
#
# def sendEmail():
#     msg = MIMEText(content,'plain',"utf-8")
#     msg["From"] = formataddr(["lisanyang",sender])
#     msg["To"] = ",".join(receivers)
#     msg["Subject"] = title
#     try:
#         # smtp = smtplib.SMTP_SSL(mail_host,465)
#         smtp = smtplib.SMTP(mail_host)
#         smtp.login(mail_user,mail_pass)
#         smtp.sendmail(sender,receivers,msg.as_string())
#         print("成功过")
#         smtp.quit()
#     except smtplib.SMTPException as e:
#         print(e)
# if __name__ == "__main__":
#     sendEmail()












# # coding:utf-8
# import smtplib
# from email.mime.text import MIMEText
# from email.utils import formataddr
#
# mail_host = "smtp.163.com"
# mail_user = "q673007283@163.com"
# mail_pass = "Store123"
# sender = "q673007283@163.com"
# receivers = ["q673007284@163.com","q673007285@163.com"]
# content = "这是内容邮件绿萝"
# title = "李师傅的客人问问"
#
# def sendEmail():
#     msg = MIMEText(content,'plain',"utf-8")
#     msg["From"] = formataddr(["slri",sender])
#     msg["To"] = ",".join(receivers)
#     msg["Subject"] = title
#     try:
#         # smtp = smtplib.SMTP_SSL(mail_host,465)
#         smtp = smtplib.SMTP(mail_host)
#         smtp.login(mail_user,mail_pass)
#         smtp.sendmail(sender,receivers,msg.as_string())
#         smtp.quit()
#     except smtplib.SMTPException as e:
#         print(e)
#
# if __name__ == "__main__":
#     sendEmail()