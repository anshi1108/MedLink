import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'sadneyasam05@gmail.com'
receiver_email = 'sadney14@gmail.com'
password = '#s@dney@1435'

# Create a MIME object
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Subject of the email'

# Attach the body of the email
body = 'This is the body of the email.'
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Mail sent successfully!')
