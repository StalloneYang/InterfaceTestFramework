# coding:utf-8

import os, sys
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 如果报告取的不是HTML格式的，邮件报告没有内容，只显示BK。保证取对报告HMTL格式
reportPath = os.path.join(os.getcwd(), 'testReports')  # 测试报告的路径
# reportPath = os.path.join(os.path.dirname(os.getcwd()), 'testReports')  # 如果只运行当前脚本，用这个测试报告的路径
print("打印路径：")

class SendMail(object):

    def get_report(self):  # 该函数的作用是为了在测试报告的路径下找到最新的测试报告

        dirs = os.listdir(reportPath)
        dirs.sort()
        print(dirs)
        newreportname = dirs[-2:-1][0]  # 取倒数第二个字符串
        print('The new report name: {0}'.format(newreportname))  # 打印最新报告名称
        _reportPath = os.path.join(reportPath, newreportname)
        print(_reportPath)
        return _reportPath  # 返回的是测试报告的名字

    def send(self):
        """发送邮件"""
        # 配置发送邮件的信息
        sender = "2355707806@qq.com"  # 发送的账号
        psw = "ajkzintnanbsdjed"     # 密码（qq邮箱是授权码）
        smtp_server = "smtp.qq.com"
        port = 465
        recipients = ['2563807532@qq.com', '736656393@qq.com']  # 发送给多个人
        # print(self.get_report())   # 打印报告的路径
        '''发送最新的测试报告内容'''
        with open(self.get_report(), "rb") as f:
           mail_body = f.read()
        # 定义邮件内容
        msg = MIMEMultipart()
        body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg['Subject'] = u"智慧工程2.0自动化测试报告"
        msg["from"] = sender
        # msg["to"] = ",".join(receiver)  # 只能字符串
        toaddrs = recipients
        msg.attach(body)
        # 添加附件
        att = MIMEText(open(self.get_report(), "rb").read(), "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename= "report.html"'
        msg.attach(att)
        try:
           smtp = smtplib.SMTP()
           smtp.connect(smtp_server)  # 连服务器
           smtp.login(sender, psw)
        except:
           smtp = smtplib.SMTP_SSL(smtp_server, port)
           smtp.login(sender, psw)  # 登录
        # smtp.sendmail(sender, receiver, msg.as_string())
        smtp.sendmail(sender, toaddrs, msg.as_string())
        smtp.quit()
        print('test report email has send out !')

if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()
    # get_report1 = sendMail.get_report()
    # print(get_report1)
