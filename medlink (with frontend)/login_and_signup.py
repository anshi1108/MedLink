import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
import re
import mysql.connector
from PIL import Image, ImageTk
from functools import partial
from make_appoinment import *
from tkcalendar import DateEntry
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


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

# Create the patient_info table
execute_query("""CREATE TABLE IF NOT EXISTS patient_info (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Email VARCHAR(255),
    Name VARCHAR(255),
    Contact_no VARCHAR(255),
    Password VARCHAR(255),
    Age VARCHAR(255),
    Gender VARCHAR(255),
    Diagnosis VARCHAR(255),
    INDEX (Name)  -- Add this line to create an index on the 'Name' column
)""")


# Create the doctor_info table
execute_query("""
CREATE TABLE IF NOT EXISTS doctor_info (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Email VARCHAR(255),
    Name VARCHAR(255),
    Contact_no VARCHAR(255),
    Password VARCHAR(255),
    Qualifications VARCHAR(255),
    Speciality VARCHAR(255),
    INDEX (Name)  -- Add this line to create an index on the 'Name' column
)
""")

# Create the appointments table with foreign key constraints
execute_query("""
CREATE TABLE IF NOT EXISTS appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT,
    PatientName VARCHAR(255),
    DoctorName VARCHAR(255),
    AppointmentDate DATE,
    AppointmentDay VARCHAR(255),
    AppointmentTime TIME,
    AppointmentStatus VARCHAR(255),
    FOREIGN KEY (PatientName) REFERENCES patient_info(Name),
    FOREIGN KEY (DoctorName) REFERENCES doctor_info(Name)
)
""")



def get_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")


def p_signup(p_mail, p_pass, p_name, p_contact):
    query = "INSERT INTO patient_info (Email, Name, Contact_no, Password) VALUES (%s, %s, %s, %s)"
    values = (p_mail, p_name, p_contact, p_pass)
    execute_query(query, values)
    messagebox.showinfo("Signup", "Signed up successfully!")


def p_login(p_mail, p_pass):
    query = "SELECT * FROM patient_info WHERE Email= %s AND Password = %s"
    values = (p_mail, p_pass)
    user = fetch_data(query, values)

    if user:
        messagebox.showinfo("Login", "Patient login successful!")
        open_main_p()
    else:
        messagebox.showinfo("Login", "Invalid Contact number or password. Please try again!")


def d_signup(d_mail, d_pass, d_name, d_contact, d_qual, d_speciality):
    query = "INSERT INTO doctor_info (Email, Name, Contact_no, Password, Qualifications, Speciality) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (d_mail, d_name, d_contact, d_pass, d_qual, d_speciality)
    execute_query(query, values)
    messagebox.showinfo("Signup", "Signed up successfully!")


def d_login(d_mail, d_pass):
    query = "SELECT * FROM doctor_info WHERE Email = %s AND Password = %s"
    values = (d_mail, d_pass)
    user = fetch_data(query, values)

    if user:
        messagebox.showinfo("Login", "Doctor login successful!")
        open_main_d()
    else:
        messagebox.showinfo("Login", "Invalid Contact number or password. Please try again!")


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

def open_doctor_window():
    root.withdraw()
    doctor_window = tk.Toplevel(root)
    doctor_window.geometry("1000x625")

    new_image_path = r"medlink (with frontend)\doctor_l.png"
    new_pil_image = Image.open(new_image_path)
    new_tk_image = ImageTk.PhotoImage(new_pil_image)
    new_background_label = tk.Label(doctor_window, image=new_tk_image)
    new_background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def doctor_login_clicked():
        doctor_window.destroy()
        open_login_window("Doctor")

    def doctor_signup_clicked():
        doctor_window.destroy()
        open_signup_window("Doctor")

    login_button = tk.Button(
        doctor_window,
        text="Login", font=("Helvetica", 14),
        command=doctor_login_clicked,
        bd=0,  # Border width
        highlightthickness=-1,  # Set to a negative value for transparency
        bg="#A9BABD",  # Background color (you can set this to an empty string or any transparent color)
    )
    login_button.place(relx=0.70, rely=0.4, anchor="center")

    signup_button = tk.Button(
        doctor_window,
        text="Signup", font=("Helvetica", 14),
        command=doctor_signup_clicked,
        bd=0,  # Border width
        highlightthickness=-1,  # Set to a negative value for transparency
        bg="#A9BABD", 
    )
    signup_button.place(relx=0.70, rely=0.6, anchor="center")

    button_width = int(doctor_window.winfo_screenwidth() / 70)
    button_height = int(doctor_window.winfo_screenheight() / 180)
    login_button.config(width=button_width, height=button_height)
    signup_button.config(width=button_width, height=button_height)

    doctor_window.mainloop()

def open_patient_window():
    root.withdraw()
    patient_window = tk.Toplevel(root)
    patient_window.geometry("1000x800")

    new_image_path = r"medlink (with frontend)\eg.png"
    new_pil_image = Image.open(new_image_path).resize((1000, 800), Image.LANCZOS)
    new_tk_image = ImageTk.PhotoImage(new_pil_image)

    new_background_label = tk.Label(patient_window, image=new_tk_image)
    new_background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    def patient_login_clicked():
        patient_window.destroy()
        open_login_window("Patient")

    def patient_signup_clicked():
        patient_window.destroy()
        open_signup_window("Patient")

    login_button = tk.Button(
        patient_window,
        text="Login", font=("Helvetica", 14),
        command=patient_login_clicked,
        bd=0,  # Border width
        highlightthickness=-1,  # Set to a negative value for transparency
        bg="#A9BABD",  # Background color (you can set this to an empty string or any transparent color)
    )
    login_button.place(relx=0.70, rely=0.4, anchor="center")

    signup_button = tk.Button(
        patient_window,
        text="Signup", font=("Helvetica", 14),
        command=patient_signup_clicked,
        bd=0,  # Border width
        highlightthickness=-1,  # Set to a negative value for transparency
        bg="#A9BABD",  # Background color (you can set this to an empty string or any transparent color)
    )
    signup_button.place(relx=0.70, rely=0.6, anchor="center")

    button_width = int(patient_window.winfo_screenwidth() / 70)
    button_height = int(patient_window.winfo_screenheight() / 180)
    login_button.config(width=button_width, height=button_height)
    signup_button.config(width=button_width, height=button_height)

    patient_window.mainloop()

def open_login_window(user_type):
    root.withdraw()
    login_window = tk.Toplevel(root)
    login_window.title(f"{user_type} Login")
    login_window.geometry("1000x800")

    new_image_path = r"medlink (with frontend)\login2.png"
    new_pil_image = Image.open(new_image_path).resize((1000, 800), Image.LANCZOS)
    new_tk_image = ImageTk.PhotoImage(new_pil_image)

    new_background_label = tk.Label(login_window, image=new_tk_image)
    new_background_label.place(x=0, y=0, relwidth=1, relheight=1)

    email_label = tk.Label(login_window, text="Email:", width=25, height=3, bg="#A9BABD")
    email_label.place(relx=0.6, rely=0.4, anchor="center")

    email_entry = tk.Entry(login_window, width=25)
    email_entry.place(relx=0.9, rely=0.4, anchor="center")

    password_label = tk.Label(login_window, text="Password:", width=25, height=3, bg="#A9BABD")
    password_label.place(relx=0.6, rely=0.5, anchor="center")

    password_entry = tk.Entry(login_window, width=25, show='*')
    password_entry.place(relx=0.9, rely=0.5, anchor="center")

            
    def login():
        email = email_entry.get()
        password = password_entry.get()
        if validate_email(email) and password:
            if user_type == "Doctor":
                d_login(email, password)
                login_window.withdraw()
                open_main_d()
            else:
                p_login(email, password)
                login_window.withdraw()
                open_main_p()
        else:
            messagebox.showwarning("Login Error", "Please enter a valid email and password.")
            login_window.lift()

    login_button = tk.Button(login_window, text="Login", font=("Helvetica", 14), command=login, width=30, height=1,
                            bd=0, highlightthickness=0, bg="#A9BABD")
    login_button.place(relx=0.70, rely=0.8, anchor="center")

    not_user_button = tk.Button(login_window, text="Not a user? Signup here", font=("Helvetica", 14),
                                command=lambda: open_signup_window(user_type), width=30, height=1,
                                bd=0, highlightthickness=0, bg="#A9BABD")
    not_user_button.place(relx=0.70, rely=0.9, anchor="center")
    
    
    button_width = int(login_window.winfo_screenwidth() / 60)
    button_height = int(login_window.winfo_screenheight() / 250)
    login_button.config(width=button_width, height=button_height)
    not_user_button.config(width=button_width, height=button_height)

    login_window.mainloop()

def open_signup_window(user_type):
    root.withdraw()
    signup_window = tk.Toplevel(root)
    signup_window.title(f"{user_type} Signup")
    signup_window.geometry("1000x800")

    new_image_path = r"medlink (with frontend)\login1.png"
    new_pil_image = Image.open(new_image_path).resize((1000, 800), Image.LANCZOS)
    new_tk_image = ImageTk.PhotoImage(new_pil_image)

    new_background_label = tk.Label(signup_window, image=new_tk_image)
    new_background_label.place(x=0, y=0, relwidth=1, relheight=1)

    new_background_label = tk.Label(signup_window, image=new_tk_image)
    new_background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    name_label = tk.Label(signup_window, text="Name:", width=25, height=3, bg="#A9BABD")
    name_label.place(relx=0.6, rely=0.1, anchor="center")

    name_entry = tk.Entry(signup_window)
    name_entry.place(relx=0.7, rely=0.1)

    email_label = tk.Label(signup_window, text="Email:", width=25, height=3, bg="#A9BABD")
    email_label.place(relx=0.6, rely=0.2, anchor="center")

    email_entry = tk.Entry(signup_window, width=30)
    email_entry.place(relx=0.7, rely=0.2)

    password_label = tk.Label(signup_window, text="Password:", width=25, height=3, bg="#A9BABD")
    password_label.place(relx=0.6, rely=0.3, anchor="center")

    password_entry = tk.Entry(signup_window, width=30, show='*')
    password_entry.place(relx=0.7, rely=0.3)

    contact_label = tk.Label(signup_window, text="Contact Number:", width=25, height=3, bg="#A9BABD")
    contact_label.place(relx=0.6, rely=0.4, anchor="center")

    contact_entry = tk.Entry(signup_window)
    contact_entry.place(relx=0.7, rely=0.4)

    if user_type == "Doctor":
        qual_label = tk.Label(signup_window, text="Qualifications:", width=25, height=3, bg="#A9BABD")
        qual_label.place(relx=0.6, rely=0.5, anchor="center")

        qual_entry = tk.Entry(signup_window)
        qual_entry.place(relx=0.7, rely=0.5)

        speciality_label = tk.Label(signup_window, text="Speciality:", width=25, height=3, bg="#A9BABD")
        speciality_label.place(relx=0.6, rely=0.6, anchor="center")

        speciality_entry = tk.Entry(signup_window)
        speciality_entry.place(relx=0.7, rely=0.6)

    def signup():
        email = email_entry.get()
        password = password_entry.get()
        name = name_entry.get()
        contact = contact_entry.get()
        if validate_email(email) and password and name and contact and len(contact) == 10:
            if user_type == "Doctor":
                qual = qual_entry.get()
                speciality = speciality_entry.get()
                d_signup(email, password, name, contact, qual, speciality)
            else:
                p_signup(email, password, name, contact)
            messagebox.showinfo("Signup", "Signed up successfully!")
            signup_window.destroy()
            open_login_window(user_type)
        else:
            messagebox.showwarning("Signup Error", "Please fill in all fields with a valid email and a 10-digit contact number.")
            signup_window.lift()

    signup_button = tk.Button(signup_window, text="Signup", command=signup, font=("Helvetica", 14),  width=40, height=2,
                            bd=0, highlightthickness=0, bg="#A9BABD")
    signup_button.place(relx=0.70, rely=0.8, anchor="center")

    already_user_button = tk.Button(signup_window, text="Already a user? Login here", font=("Helvetica", 14),
                                    command=lambda: open_login_window(user_type), width=40, height=2,
                                    bd=0, highlightthickness=0, bg="#A9BABD")
    already_user_button.place(relx=0.70, rely=0.9, anchor="center")

    button_width = int(signup_window.winfo_screenwidth() / 60)
    button_height = int(signup_window.winfo_screenheight() / 250)
    signup_button.config(width=button_width, height=button_height)
    already_user_button.config(width=button_width, height=button_height)
    signup_window.mainloop()

def open_main_d():
    main_d = tk.Toplevel(root)
    main_d.geometry("1000x800")
    main_d.title("MedLink - Doctor Homepage")

    # Left Panel
    left_panel = tk.Frame(main_d, width=300, bg='lightgray', padx=10, pady=10)
    left_panel.pack(side=tk.LEFT, fill=tk.Y, expand=False)
    left_panel.pack_propagate(False)

    # MedLink Label
    tk.Label(left_panel, text="MedLink", font=('Helvetica', 18, 'bold'), bg='lightgray').pack(pady=30)

    # Doctor Buttons
    tk.Button(left_panel, text="My Profile", command=show_doctor_profile).pack(pady=50)
    tk.Button(left_panel, text="View Appointments", command=open_doctor_profile).pack(pady=50)

    # Right Panel
    right_panel = tk.Frame(main_d, bg='white', padx=20, pady=20)
    right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    company_info_text = """
    Welcome to MedLink - Your Trusted Healthcare Partner!

    MedLink is committed to providing exceptional healthcare services. Our platform connects doctors and patients seamlessly, ensuring quality care and a smooth experience.

    Explore the features designed to make your healthcare journey efficient and comfortable. For any assistance, feel free to reach out to our support team.

    - The MedLink Team
    """

    # MedLink Company Information
    tk.Label(right_panel, text=company_info_text, font=('Helvetica', 12)).pack()
    main_d.mainloop()
    
def show_doctor_profile():
    profile_page = tk.Toplevel(root)
    profile_page.geometry("400x300")
    profile_page.title("Doctor Profile")

    # Email Entry
    email_label = tk.Label(profile_page, text="Email:")
    email_label.pack(pady=5)

    email_entry = tk.Entry(profile_page)
    email_entry.pack(pady=5)

    # Password Entry
    password_label = tk.Label(profile_page, text="Password:")
    password_label.pack(pady=5)

    password_entry = tk.Entry(profile_page, show='*')
    password_entry.pack(pady=5)

    # View Profile Button
    view_button = tk.Button(profile_page, text="View Profile", command=lambda: view_profile(email_entry, password_entry))
    view_button.pack(pady=10)

    # Text widget to display the doctor's profile
    profile_text = tk.Text(profile_page, height=10, width=30)
    profile_text.pack(pady=10)

    def view_profile(email_entry, password_entry):
        email = email_entry.get()
        password = password_entry.get()
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM doctor_info WHERE email=%s AND password=%s", (email, password))
            result = cursor.fetchone()

            if result:
                profile_text.delete(1.0, tk.END)
                profile_text.insert(tk.END,
                                    f"First Name: {result[1]}\nLast Name: {result[2]}\nEmail: {result[3]}\nPhone number: {result[4]}\nQualification: {result[6]}")
            else:
                messagebox.showerror("Error", "Invalid credentials")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()


def open_doctor_profile():
    profile_page = tk.Toplevel(root)
    profile_page.geometry("400x300")
    profile_page.title("Doctor Profile")

    # Email Entry
    email_label = tk.Label(profile_page, text="Email:")
    email_label.pack(pady=5)

    email_entry = tk.Entry(profile_page)
    email_entry.pack(pady=5)

    # Password Entry
    password_label = tk.Label(profile_page, text="Password:")
    password_label.pack(pady=5)

    password_entry = tk.Entry(profile_page, show='*')
    password_entry.pack(pady=5)

    # Show Appointments Button
    show_appointments_button = tk.Button(profile_page, text="Show Appointments", command=lambda: show_doctor_appointments(email_entry.get(), password_entry.get()))
    show_appointments_button.pack(pady=10)

def show_doctor_appointments(email, password):
    # Validate email and password
    if not validate_email(email) or not password:
        messagebox.showwarning("Validation Error", "Please enter a valid email and password.")
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Fetch appointments data for the given doctor's email
        cursor.execute("""
            SELECT * FROM appointments
            INNER JOIN doctor_info ON appointments.DoctorID = doctor_info.id
            WHERE doctor_info.Email = %s AND doctor_info.Password = %s
            ORDER BY appointments.Time
        """, (email, password))

        appointments_data = cursor.fetchall()

        if appointments_data:
            # Create a new window to display the appointments
            appointments_window = tk.Toplevel(root)
            appointments_window.title("Doctor Appointments")
            appointments_window.geometry("500x400")

            # Create a text widget to display the appointments
            appointments_text = tk.Text(appointments_window, height=20, width=50)
            appointments_text.pack(pady=10)

            # Display appointments in chronological order
            for appointment in appointments_data:
                appointments_text.insert(tk.END,
                                          f"AppointmentID: {appointment[0]}\n"
                                          f"PatientName: {appointment[4]}\n"
                                          f"AppointmentDate: {appointment[3]}\n"
                                          f"AppointmentTime: {appointment[5]}\n"
                                          f"AppointmentStatus: {appointment[6]}\n\n")
        else:
            messagebox.showinfo("Appointments", "No appointments found for the given email and password.")

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()




def open_main_p():
    if hasattr(open_main_p, 'info_displayed') and open_main_p.info_displayed:
        # If info has already been displayed, return without creating a new window
        return

    main_p = tk.Toplevel(root)
    main_p.geometry("1000x800")
    main_p.title("Information Page")
    main_p.protocol("WM_DELETE_WINDOW", root.quit)  # Handle closing of main_p window

    company_info_text = """
    Welcome to MedLink - Your Trusted Healthcare Partner!

    MedLink is committed to providing exceptional healthcare services. Our platform connects doctors and patients seamlessly, ensuring quality care and a smooth experience.

    Explore the features designed to make your healthcare journey efficient and comfortable. For any assistance, feel free to reach out to our support team.

    - The MedLink Team
    """
    tk.Label(main_p, text=company_info_text, font=('Helvetica', 12), anchor='center').pack()

    # Create a menu bar
    menu_bar = tk.Menu(main_p)
    main_p.config(menu=menu_bar)

    # Create an "Options" menu
    options_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="MY MENU", menu=options_menu, font=('Helvetica', 14))

    # Add menu items with commands
    options_menu.add_command(label="SHOW APPOINTMENTS", command= open_patient_profile)
    options_menu.add_command(label="MAKE APPOINTMENTS", command= make_appointments)
    options_menu.add_command(label="VIDEO CONFERENCING", command=video_call)
    options_menu.add_command(label="CHAT WITH ME", command=launch_chatbot)
    options_menu.add_command(label="MY PROFILE", command=show_patient_profile)

    main_p.info_displayed = True  # Set the flag to indicate that info has been displayed
    main_p.mainloop()
# def create():
#     creat_a_frame = tk.Toplevel(root)
#     creat_a_frame .geometry("1000x800")
#     creat_a_frame .title("MY PROFILE")
#     creat_a_frame .protocol("WM_DELETE_WINDOW", root.quit) 
    
def make_appointments():
    
    makea = tk.Toplevel(root)
    makea.geometry("1000x800")
    makea.title("Appoinment")
    makea.protocol("WM_DELETE_WINDOW", root.quit) 
    create_appointment_frame(makea)
    

def open_patient_profile():
    profile_page = tk.Toplevel(root)
    profile_page.geometry("400x300")
    profile_page.title("Patient Profile")

    # Email Entry
    email_label = tk.Label(profile_page, text="Email:")
    email_label.pack(pady=5)

    email_entry = tk.Entry(profile_page)
    email_entry.pack(pady=5)

    # Password Entry
    password_label = tk.Label(profile_page, text="Password:")
    password_label.pack(pady=5)

    password_entry = tk.Entry(profile_page, show='*')
    password_entry.pack(pady=5)

    # Show Appointments Button
    show_appointments_button = tk.Button(profile_page, text="Show Appointments", command=lambda: show_patient_appointments(email_entry.get(), password_entry.get()))
    show_appointments_button.pack(pady=10)

def show_patient_appointments(email, password):
    # Validate email and password
    if not validate_email(email) or not password:
        messagebox.showwarning("Validation Error", "Please enter a valid email and password.")
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Fetch appointments data for the given patient's email
        cursor.execute("""
            SELECT * FROM appointments
            INNER JOIN patient_info ON appointments.PatientID = patient_info.id
            WHERE patient_info.Email = %s AND patient_info.Password = %s
            ORDER BY appointments.Time
        """, (email, password))

        appointments_data = cursor.fetchall()

        if appointments_data:
            # Create a new window to display the appointments
            appointments_window = tk.Toplevel(root)
            appointments_window.title("Patient Appointments")
            appointments_window.geometry("500x400")

            # Create a text widget to display the appointments
            appointments_text = tk.Text(appointments_window, height=20, width=50)
            appointments_text.pack(pady=10)

            # Display appointments in chronological order
            for appointment in appointments_data:
                appointments_text.insert(tk.END,
                                          f"AppointmentID: {appointment[0]}\n"
                                          f"DoctorName: {appointment[2]}\n"
                                          f"AppointmentDate: {appointment[3]}\n"
                                          f"AppointmentTime: {appointment[5]}\n"
                                          f"AppointmentStatus: {appointment[6]}\n\n")
        else:
            messagebox.showinfo("Appointments", "No appointments found for the given email and password.")

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()




def video_call():
    pass
def launch_chatbot():
    pass

def show_patient_profile():
    profile_page = tk.Toplevel(root)
    profile_page.geometry("400x300")
    profile_page.title("Patient Profile")

    # Email Entry
    email_label = tk.Label(profile_page, text="Email:")
    email_label.pack(pady=5)

    email_entry = tk.Entry(profile_page)
    email_entry.pack(pady=5)

    # Password Entry
    password_label = tk.Label(profile_page, text="Password:")
    password_label.pack(pady=5)

    password_entry = tk.Entry(profile_page, show='*')
    password_entry.pack(pady=5)

    # View Profile Button
    view_button = tk.Button(profile_page, text="View Profile", command=lambda: view_patient_profile(email_entry,password_entry))
    view_button.pack(pady=10)

    # Text widget to display the patient's profile
    profile_text = tk.Text(profile_page, height=10, width=30)
    profile_text.pack(pady=10)

    def view_patient_profile(email_entry,password_entry):
        email = email_entry.get()
        password = password_entry.get()
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM patient_info WHERE email=%s AND password=%s", (email, password))
            result = cursor.fetchone()

            if result:
                profile_text.delete(1.0, tk.END)
                profile_text.insert(tk.END,
                                    f"Name: {result[1]}\nAge: {result[2]}\nGender: {result[3]}\nDiagnosis: {result[4]}")
            else:
                messagebox.showerror("Error", "Patient not found")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()


    
def validate_email(email):
    if re.match(r'^[\w\.-]+@[\w\.-]+$', email):
        return True
    return False

root = tk.Tk()
root.title("eHealthcare")
w = 1000
h = 800
root.geometry(f"{w}x{h}")

image_path = r"medlink (with frontend)\main.png"
pil_image = Image.open(image_path).resize((1000, 800), Image.LANCZOS)
tk_image = ImageTk.PhotoImage(pil_image)

background_label = tk.Label(root, image=tk_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

doctor_button = tk.Button(root, text="Doctor", font=("Helvetica", 14), command=open_doctor_window, width=35, height=2,
                          bd=0, highlightthickness=0, bg="#A9BABD")
doctor_button.place(relx=0.70, rely=0.4, anchor="center")

patient_button = tk.Button(root, text="Patient", font=("Helvetica", 14), command=open_patient_window, width=35, height=2,
                           bd=0, highlightthickness=0, bg="#A9BABD")
patient_button.place(relx=0.70, rely=0.5, anchor="center")

button_width = int(w / 120)
button_height = int(h / 120)
root.mainloop()