import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import login_and_signup
from tkinter import messagebox
import re
import mysql.connector
from PIL import Image, ImageTk
from functools import partial
# MySQL connection parameters
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'ehealthcare',
}

# Function to execute SQL queries
def execute_query(query, values=None):
    try:
        global conn
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)

        conn.commit()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
def get_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

def fetch_data(query, values=None):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)

        data = cursor.fetchall()
        return data
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def create_appointment_frame(root, patient_name):
    def submit_appointment():
        selected_doctor = doctor_combobox.get()
        appointment_date = cal.get_date()
        appointment_day = day_combobox.get()
        appointment_time = time_entry.get()
        appointment_status = status_combobox.get()
        schedule_appointment(patient_name, selected_doctor, appointment_date, appointment_day, appointment_time, appointment_status)

        # Fetch email from the result (assuming the first tuple and first element)
        receiver_email = fetch_data("SELECT Email FROM patient_info WHERE Name = %s", (patient_name,))
        if receiver_email:
            receiver_email = receiver_email[0][0]
        else:
            print("Error: Email not found for the given patient name.")
            return

        print(f"Receiver Email: {receiver_email}")
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        sender_email = 'sadneyasam05@gmail.com'
        password = 'ehpy ztem lfvl bdec'

        # Create a MIME object
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = 'Appointment Schedule '

        # Create the body of the email with clickable links
        body = f"Appointment made for {patient_name} with {selected_doctor} on {appointment_day}, {appointment_date} at {appointment_time}.\nStatus: {appointment_status}\n\n"
        body += "Click the following links for more details:\n"
        body += f"- [Doctor's Profile](http://link_to_doctor_profile)\n"
        body += f"- [Hospital Information](http://link_to_hospital_info)\n"
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)

            # Send the email
            server.sendmail(sender_email, receiver_email, message.as_string())

        print('Mail sent successfully!')

    def schedule_appointment(patient_name, doctor_name, appointment_date, appointment_day, appointment_time, appointment_status):
        # Fetch patient and doctor IDs based on names
        patient_id = fetch_data("SELECT id FROM patient_info WHERE Name = %s", (patient_name,))
        doctor_id = fetch_data("SELECT id FROM doctor_info WHERE Name = %s", (doctor_name,))

        # Check if patient and doctor IDs are retrieved
        if patient_id and doctor_id:
            # Unpack the fetched IDs from the result tuples
            patient_id = patient_id[0][0]
            doctor_id = doctor_id[0][0]

            # Insert the appointment into the appointments table
            query = """
            INSERT INTO appointments (PatientID, DoctorID, AppointmentDate, AppointmentDay, AppointmentTime, AppointmentStatus)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (patient_id, doctor_id, appointment_date, appointment_day, appointment_time, appointment_status)
            execute_query(query, values)
            messagebox.showinfo("Appointment", "Appointment scheduled successfully!")
        else:
            messagebox.showerror("Error", "Patient or doctor not found. Please check the names and try again.")

    # Create and configure the frame
    frame = ttk.Frame(root, padding="50")  # Adjust the padding value to make the frame bigger
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    # Create labels and entry widgets
    name_label = ttk.Label(frame, text="Patient Name:")
    name_label.grid(row=0, column=0, sticky=tk.W, pady=5)
    name_label.configure(background="#A9BABD", foreground="white", font=("Helvetica", 12))

    name_entry = ttk.Entry(frame, width=30, state="readonly")
    name_entry.insert(0, patient_name)
    name_entry.grid(row=0, column=1, sticky=tk.W, pady=10)  # Increased pady value for spacing

    # Sample list of doctors, replace it with your own list
    doctors = fetch_data("SELECT Name FROM doctor_info")
    doctors = [doctor[0] for doctor in doctors]
    doctor_label = ttk.Label(frame, text="Select Doctor:")
    doctor_label.grid(row=1, column=0, sticky=tk.W, pady=5)
    doctor_label.configure(background="#A9BABD", foreground="white", font=("Helvetica", 12))

    doctor_combobox = ttk.Combobox(frame, values=doctors, state="readonly")
    doctor_combobox.grid(row=1, column=1, sticky=tk.W, pady=10)  # Increased pady value for spacing

    date_label = ttk.Label(frame, text="Appointment Date:")
    date_label.grid(row=2, column=0, sticky=tk.W, pady=5)
    date_label.configure(background="#A9BABD", foreground="white", font=("Helvetica", 12))

    cal = DateEntry(frame, width=30, background='darkblue', foreground='white', borderwidth=2)
    cal.grid(row=2, column=1, sticky=tk.W, pady=10)  # Increased pady value for spacing

    # Sample list of days, replace it with your own list
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    day_label = ttk.Label(frame, text="Select Day:")
    day_label.grid(row=3, column=0, sticky=tk.W, pady=5)
    day_label.configure(background="#A9BABD", foreground="white", font=("Helvetica", 12))

    day_combobox = ttk.Combobox(frame, values=days, state="readonly")
    day_combobox.grid(row=3, column=1, sticky=tk.W, pady=10)  # Increased pady value for spacing

    time_label = ttk.Label(frame, text="Appointment Time:")
    time_label.grid(row=4, column=0, sticky=tk.W, pady=5)
    time_label.configure(background="#A9BABD", foreground="white", font=("Helvetica", 12))

    time_entry = ttk.Entry(frame, width=30)
    time_entry.grid(row=4, column=1, sticky=tk.W, pady=10)  # Increased pady value for spacing

    # Sample list of appointment statuses, replace it with your own list
    statuses = ["Confirm", "Cancel"]
    status_label = ttk.Label(frame, text="Appointment Status:")
    status_label.grid(row=5, column=0, sticky=tk.W, pady=5)
    status_label.configure(background="#A9BABD", foreground="white", font=("Helvetica", 12))

    status_combobox = ttk.Combobox(frame, values=statuses, state="readonly")
    status_combobox.grid(row=5, column=1, sticky=tk.W, pady=10)  # Increased pady value for spacing

    # Create a button to submit the appointment
    submit_button = ttk.Button(frame, text="Submit Appointment", command=submit_appointment)
    submit_button.grid(row=6, column=0, columnspan=2, pady=20)  # Adjust the pady value to provide more space

    # Create a label to display the result
    result_label = ttk.Label(frame, text="")
    result_label.grid(row=7, column=0, columnspan=2, pady=20)  # Adjust the pady value to provide more space

    return frame
