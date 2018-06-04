from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_multiple_email(name, receiver):
    subject = 'Welcome to Laughing Blog Tutorial'
    sender = 'mail@achiengcindy.com'

    #passing in the context vairables
    text_template = render_to_string('newsletter/email-subscribe.txt',{"name": name})
    html_template = render_to_string('newsletter/email-subscribe.html',{"name": name})

    message = EmailMultiAlternatives(subject,text_template,sender, [receiver])
    message.attach_alternative(html_template, "text/html")
    message.send()