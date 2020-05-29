import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "mjjpipi@163.com"
receivers = ["maojj@tingyun.com"]

# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="@163.com"    #用户名
mail_pass="jseea!@#$2018"   #口令

message = MIMEText('您在听云华东项目管理系统提交了找回密码申请。如果您没有提交修改密码的申请请忽略本邮件', 'plain', 'utf-8')
message['From'] = "mjjpipi@163.com"
message['To'] = "maojj@tingyun.com"

subject = '这是一个邮件'
message['Subject'] = Header(subject, 'utf-8')

smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
smtpObj.login(mail_user,mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
print ("邮件发送成功")

