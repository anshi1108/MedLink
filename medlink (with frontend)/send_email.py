import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'sadneyasam05@gmail.com'
receiver_email = 'sadney14@gmail.com'
password = 'ehpy ztem lfvl bdec'

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


'''
import smtplib
import sqlite3
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

# Database initialization
conn = sqlite3.connect('appointment.db')
cursor = conn.cursor()
cursor.execute('''
# CREATE TABLE IF NOT EXISTS appointments (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#         patient_name TEXT,
#         patient_email TEXT,
    #     phone_number TEXT,
    #     scheduled_datetime DATETIME
    # )
''')
conn.commit()

def get_upcoming_appointments():
    current_time = datetime.now()
    end_time = current_time + timedelta(days=1)  # Change this based on your criteria for daily checkup
    # cursor.execute('''
    #     SELECT * FROM appointments
    #     WHERE scheduled_datetime BETWEEN ? AND ?
    # , (current_time, end_time))
#     return cursor.fetchall()

# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# sender_email = 'sadneyasam05@gmail.com'
# password = 'ehpy ztem lfvl bdec'

# # Connect to the SMTP server
# with smtplib.SMTP(smtp_server, smtp_port) as server:
#     server.starttls()
#     server.login(sender_email, password)

#     # Retrieve upcoming appointments
#     appointments = get_upcoming_appointments()

#     for appointment in appointments:
#         patient_name, patient_email, phone_number, scheduled_datetime = appointment

#         # Create a MIME object
#         message = MIMEMultipart()
#         message['From'] = sender_email
#         message['To'] = patient_email
#         message['Subject'] = 'Scheduled Appointment'

#         # Format the date, time, and day
#         formatted_datetime = scheduled_datetime.strftime('%Y-%m-%d %H:%M:%S')
#         formatted_date = scheduled_datetime.strftime('%A, %B %d, %Y')
#         formatted_time = scheduled_datetime.strftime('%I:%M %p')
#         formatted_day = scheduled_datetime.strftime('%A')

#         # Attach the body of the email
#         body = f"Dear {patient_name},\n\nYour appointment is scheduled for:\nDate: {formatted_date}\nDay: {formatted_day}\nTime: {formatted_time}\n\nBest regards,\nYour Clinic"

#         # Ask for the next appointment for daily checkup
#         next_appointment = scheduled_datetime + timedelta(days=1)
#         body += f"\n\nDo you want to schedule your next appointment for a daily checkup on {next_appointment.strftime('%A, %B %d, %Y')} at {next_appointment.strftime('%I:%M %p')}?"

#         message.attach(MIMEText(body, 'plain'))

#         # Send the email
#         server.sendmail(sender_email, patient_email, message.as_string())

# print('Mail sent successfully!')
