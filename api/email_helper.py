import sendgrid
import os
from sendgrid.helpers.mail import *

def send_email(subject, content):
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(os.environ.get('FROM'))
    to_email = To(os.environ.get('USER1'))
    subject = subject
    content = Content("text/plain", content)
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())