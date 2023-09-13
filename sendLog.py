import os
import yaml
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart

try:
    with open("config.yml", "r", encoding='utf8') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
except FileNotFoundError:...

smtpHost : str = config.get("gobal_config").get("SMTP").get("smtpHost")
smtp_is_SSL : bool = config.get("gobal_config").get("SMTP").get("smtp_is_SSL",False)
smtpPort : int = config.get("gobal_config").get("SMTP").get("smtpPort")
smtpUser : str = config.get("gobal_config").get("SMTP").get("smtpUser")
smtpKey : str = config.get("gobal_config").get("SMTP").get("smtpKey")
smtp_sender : str = config.get("gobal_config").get("SMTP").get("smtp_sender")
smtp_senderName : str = config.get("gobal_config").get("SMTP").get("smtp_senderName", "caoliu自动回帖")
smtp_sendto : str = config.get("gobal_config").get("SMTP").get("smtp_sendto")

def sendLog(projectName):
    '''向邮箱发送附件'''
    attachmentsFileName = os.path.join('/tmp', f'{projectName}.log') # 附件文件，即日志文件
    mail = MIMEMultipart()
    mail['Subject'] = Header("caoliu回帖日志", 'utf-8')
    mail['From'] = formataddr((smtp_senderName, smtp_sender), "utf-8")
    mail['To'] = formataddr((None, smtp_sendto), "utf-8")
    mail.attach(MIMEText("日志见附件", 'html', 'utf-8'))
    att = MIMEText(open(attachmentsFileName, 'r', encoding='utf-8').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = f"attachment; filename = {projectName + '.txt'}"
    mail.attach(att)
    if smtp_is_SSL:smtpObj = smtplib.SMTP_SSL(smtpHost, smtpPort)
    elif smtp_is_SSL == False:smtpObj = smtplib.SMTP(smtpHost, smtpPort)
    smtpObj.login(smtpUser, smtpKey)
    smtpObj.sendmail(smtp_sender, smtp_sendto, mail.as_string())