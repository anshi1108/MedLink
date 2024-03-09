import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import mysql.connector
from tkinter import messagebox


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin@123",
    database="apotmnt"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()



def submit_appointment():
    global name_entry, doctor_combobox, cal, day_combobox, time_entry, status_combobox, result_label

    patient_name = name_entry.get()
    selected_doctor = doctor_combobox.get()
    appointment_date = cal.get_date()
    appointment_day = day_combobox.get()
    appointment_time = time_entry.get()
    appointment_status = status_combobox.get()
    
    availability_query = "SELECT * FROM appointments WHERE doctor_name = %s AND appointment_day = %s AND appointment_time = %s"
    availability_data = (selected_doctor, appointment_day, appointment_time)

    cursor.execute(availability_query, availability_data)
    existing_appointments = cursor.fetchall()

    if existing_appointments:
        messagebox.showinfo("Appointment Not Available", f"Sorry, the selected doctor is not available at {appointment_time} on {appointment_day}. Please choose a different time.")
    else:
        # Insert appointment into the database
        insert_query = "INSERT INTO appointments (patient_name, doctor_name, appointment_day, appointment_date, appointment_time, appointment_status) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (patient_name, selected_doctor, appointment_day, appointment_date, appointment_time, appointment_status)

        try:
            cursor.execute(insert_query, data)
            db.commit()
            result_label.config(text=f"Appointment made for {patient_name} with {selected_doctor} on {appointment_day}, {appointment_date} at {appointment_time}. \nStatus: {appointment_status}. \nAppointment Booked Successfully")
        except Exception as e:
            db.rollback()
            result_label.config(text=f"Error: {str(e)}")

def create_appointment_frame():
    global name_entry, doctor_combobox, cal, day_combobox, time_entry, status_combobox

    frame = ttk.Frame(root, padding="50")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    # Create a big, bold label for the "Book Appointment" text
    book_appointment_label = ttk.Label(frame, text="Book Appointment", font=("Helvetica", 18, "bold"))
    book_appointment_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))  # Add padding to the bottom

    # Create labels and entry widgets
    name_label = ttk.Label(frame, text="Patient Name:")
    name_label.grid(row=1, column=0, sticky=tk.W, pady=5)

    name_entry = ttk.Entry(frame, width=30)
    name_entry.grid(row=1, column=1, sticky=tk.W, pady=10)

    doctor_label = ttk.Label(frame, text="Select Doctor:")
    doctor_label.grid(row=2, column=0, sticky=tk.W, pady=5)

    doctors = ["Dr. A", "Dr. B", "Dr. C"]
    doctor_combobox = ttk.Combobox(frame, values=doctors, state="readonly")
    doctor_combobox.grid(row=2, column=1, sticky=tk.W, pady=10)

    date_label = ttk.Label(frame, text="Appointment Date:")
    date_label.grid(row=3, column=0, sticky=tk.W, pady=5)

    cal = DateEntry(frame, width=30, background='darkblue', foreground='white', borderwidth=2)
    cal.grid(row=3, column=1, sticky=tk.W, pady=10)

    day_label = ttk.Label(frame, text="Select Day:")
    day_label.grid(row=4, column=0, sticky=tk.W, pady=5)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    day_combobox = ttk.Combobox(frame, values=days, state="readonly")
    day_combobox.grid(row=4, column=1, sticky=tk.W, pady=10)

    time_label = ttk.Label(frame, text="Appointment Time:")
    time_label.grid(row=5, column=0, sticky=tk.W, pady=5)

    time_entry = ttk.Entry(frame, width=30)
    time_entry.grid(row=5, column=1, sticky=tk.W, pady=10)

    status_label = ttk.Label(frame, text="Appointment Status:")
    status_label.grid(row=6, column=0, sticky=tk.W, pady=5)

    statuses = ["Confirm", "Cancel"]
    status_combobox = ttk.Combobox(frame, values=statuses, state="readonly")
    status_combobox.grid(row=6, column=1, sticky=tk.W, pady=10)

    # Create a button to submit the appointment
    submit_button = ttk.Button(frame, text="Submit Appointment", command=submit_appointment)
    submit_button.grid(row=7, column=0, columnspan=2, pady=20)

    return frame


# Create the main window
root = tk.Tk()
root.title("Schedule Appointment")
root.minsize(600, 500)

# Create and configure the main frame
frame = create_appointment_frame()

# Create a label to display the result
result_label = ttk.Label(root, text="")
result_label.grid(row=1, column=0, pady=20)

style = ttk.Style()
style.configure("TButton", foreground="green", background="white", font=("Helvetica", 12, "bold"), padding=(10, 5))

root.mainloop()