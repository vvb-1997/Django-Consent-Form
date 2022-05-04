import smtplib
import os

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header

def send_email(recipients, subject, body, recipients_cc=[], recipients_bcc=[], sender="joe@example.com", attachments={}, mime_type="html", msg_id=""):

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    msg['Cc'] = ', '.join(recipients_cc)
    msg['Subject'] = subject
    if msg_id:
        msg['Message-id'] = msg_id
    msg.attach(MIMEText(body, mime_type))

    ## attach files ##
    for name, attachment in attachments.items():
        msg.attach(
            MIMEApplication(
                attachment,
                Name = os.path.basename(name)    # this will appear as the attachment name in the email
            )
        )

    s=smtplib.SMTP('localhost:1025')
    s.sendmail(sender, recipients + recipients_cc + recipients_bcc, msg.as_string())
    s.quit()