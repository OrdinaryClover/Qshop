# nuoddmxxcfcgcegf
# bbsjuyqhyfebdgcj
# 1、导包
import smtplib
from email.mime.text import MIMEText

content = "测试中"
subject = "路人甲"
sender = "Bert_Woo@163.com"
recver = "1975964827@qq.com,3237734526@qq.com,805122275@qq.com"

#2、构建发送的邮件内容
message = MIMEText(content,'plain','utf-8')

"""
_text,   邮件内容
_subtype='plain'  内容类型  文本
_charset= "utf-8"  编码格式
"""
message["Subject"] = subject   ##主题
message["From"] = sender   ##发件人
message["To"] = recver   ##收件人
#3、登录邮件服务器并发送

smtp = smtplib.SMTP_SSL("smtp.163.com",465)
##登录
smtp.login("Bert_Woo@163.com","qaz123")
smtp.sendmail(sender,recver.split(","),message.as_string())

##发送人 收件人  邮件内容。序列化功能用于发送邮件中带上内容

#4、退出登录
smtp.close()
