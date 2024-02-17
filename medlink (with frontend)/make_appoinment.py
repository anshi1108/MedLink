import login_and_signup
import doctor_profilepage
import patient_homepage
from tkinter import ttk
from tkinter import tk
from tkcalendar import DateEntry

def create_appointment_frame():
    def submit_appointment():
        patient_name = name_entry.get()
        selected_doctor = doctor_combobox.get()
        appointment_date = cal.get_date()
        appointment_day = day_combobox.get()
        appointment_time = time_entry.get()
        appointment_status = status_combobox.get()

        # You can add code here to save the appointment details to a database or perform other actions.

        result_label.config(text=f"Appointment made for {patient_name} with {selected_doctor} on {appointment_day}, {appointment_date} at {appointment_time}. \nStatus: {appointment_status}")

    # Create and configure the frame
    frame = ttk.Frame(padding="50")  # Adjust the padding value to make the frame bigger
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    # Create labels and entry widgets
    name_label = ttk.Label(frame, text="Patient Name:")
    name_label.grid(row=0, column=0, sticky=tk.W, pady=5)

    name_entry = ttk.Entry(frame, width=30)
    name_entry.grid(row=0, column=1, sticky=tk.W, pady=10)  # Increased pady value for spacing

    doctor_label = ttk.Label(frame, text="Select Doctor:")
    doctor_label.grid(row=1, column=0, sticky=tk.W, pady=5)

    # Sample list of doctors, replace it with your own list
    doctors = ["Dr. A", "Dr. B", "Dr. C"]
    doctor_combobox = ttk.Combobox(frame, values=doctors, state="readonly")
    doctor_combobox.grid(row=1, column=1, sticky=tk.W, pady=10)  # Increased pady value for spacing

    date_label = ttk.Label(frame, text="Appointment Date:")
    date_label.grid(row=2, column=0, sticky=tk.W, pady=5)

    cal = DateEntry(frame, width=30, background='darkblue', foreground='white', borderwidth=2)
    cal.grid(row=2, column=1, sticky=tk.W, pady=10)  # Increased pady value for spacing

    day_label = ttk.Label(frame, text="Select Day:")
    day_label.grid(row=3, column=0, sticky=tk.W, pady=5)

    # Sample list of days, replace it with your own list
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    day_combobox = ttk.Combobox(frame, values=days, state="readonly")
    day_combobox.grid(row=3, column=1, sticky=tk.W, pady=10)  # Increased pady value for spacing

    time_label = ttk.Label(frame, text="Appointment Time:")
    time_label.grid(row=4, column=0, sticky=tk.W, pady=5)

    time_entry = ttk.Entry(frame, width=30)
    time_entry.grid(row=4, column=1, sticky=tk.W, pady=10)  # Increased pady value for spacing

    status_label = ttk.Label(frame, text="Appointment Status:")
    status_label.grid(row=5, column=0, sticky=tk.W, pady=5)

    # Sample list of appointment statuses, replace it with your own list
    statuses = ["Confirm", "Cancel"]
    status_combobox = ttk.Combobox(frame, values=statuses, state="readonly")
    status_combobox.grid(row=5, column=1, sticky=tk.W, pady=10)  # Increased pady value for spacing

    # Create a button to submit the appointment
    submit_button = ttk.Button(frame, text="Submit Appointment", command=submit_appointment)
    submit_button.grid(row=6, column=0, columnspan=2, pady=20)  # Adjust the pady value to provide more space

    # Create a label to display the result
    result_label = ttk.Label(frame, text="")
    result_label.grid(row=7, column=0, columnspan=2, pady=20)  # Adjust the pady value to provide more space

    return frame