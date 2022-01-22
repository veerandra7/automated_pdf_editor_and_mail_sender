import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


email = 'XXXXXXXXXX@gmail.com'
password = 'XXXXXX'


def sendmail(mail,subject,student_name):
    message = MIMEMultipart()
    message['Subject'] = subject
    body = 'Hey' + ' '+ student_name +','+'\n\n\nGood to see the progress, Please find the attachment of your previous session.\n\n\nThank you,\nJohn'
    message.attach(MIMEText(body, 'plain'))
    pdfname = 'outputfile.pdf'
    binary_pdf = open(pdfname, 'rb')
    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    payload.set_payload((binary_pdf).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    message.attach(payload)
    text = message.as_string()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(email, password)
    server.sendmail(email, mail, text)
    server.quit()
    binary_pdf.close()

