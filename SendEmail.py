from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def SendEmail(bugStr):
    msg=MIMEText('This Fucking Program meets some bugs!'+bugStr,'plain','utf-8')

    # 输入Email地址和口令:
    from_addr = '826695156@qq.com'
    password = '123456aB'
    # 输入收件人地址:
    to_addr = 'alan20062006@vip.qq.com'
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.qq.com'


    msg['From'] = _format_addr('Your Fucking Program died <%s>' % from_addr)
    msg['To'] = _format_addr('Master <%s>' % to_addr)
    msg['Subject'] = Header('你的程序又跑挂了，快来重启', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
