import tkinter as tk
from tkinter import messagebox
import re
import mysql.connector
from PIL import Image, ImageTk
from functools import partial
import patient_homepage
import doctor_profilepage


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
execute_query("""
CREATE TABLE IF NOT EXISTS patient_info (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Email VARCHAR(255),
    Name VARCHAR(255),
    Contact_no VARCHAR(255),
    Password VARCHAR(255),
    Age VARCHAR(255),
    Gender VARCHAR(255),
    Diagnosis VARCHAR(255)
)
""")

# Create the doctor_info table
execute_query("""
CREATE TABLE IF NOT EXISTS doctor_info (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Email VARCHAR(255),
    Name VARCHAR(255),
    Contact_no VARCHAR(255),
    Password VARCHAR(255),
    Qualifications VARCHAR(255),
    Speciality VARCHAR(255)
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
    query = "SELECT * FROM patient_info WHERE Contact_no = %s AND Password = %s"
    values = (p_mail, p_pass)
    user = fetch_data(query, values)

    if user:
        messagebox.showinfo("Login", "Patient login successful!")
        # Redirect to patient homepage
    else:
        messagebox.showinfo("Login", "Invalid Contact number or password. Please try again!")


def d_signup(d_mail, d_pass, d_name, d_contact, d_qual, d_speciality):
    query = "INSERT INTO doctor_info (Email, Name, Contact_no, Password, Qualifications, Speciality) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (d_mail, d_name, d_contact, d_pass, d_qual, d_speciality)
    execute_query(query, values)
    messagebox.showinfo("Signup", "Signed up successfully!")


def d_login(d_mail, d_pass):
    query = "SELECT * FROM doctor_info WHERE Contact_no = %s AND Password = %s"
    values = (d_mail, d_pass)
    user = fetch_data(query, values)

    if user:
        messagebox.showinfo("Login", "Doctor login successful!")
        # Redirect to doctor homepage
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


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def open_doctor_window():
    root.withdraw()
    doctor_window = tk.Toplevel(root)
    center_window(doctor_window)
    doctor_window.geometry("1000x800")

    new_image_path = r"MedLink\medlink (with frontend)\doctor_l.png"
    new_pil_image = Image.open(new_image_path).resize((1000, 800), Image.LANCZOS)
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
        bg="#A9BABD",  # Background color (you can set this to an empty string or any transparent color)
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
    center_window(patient_window)
    patient_window.geometry("1000x800")

    new_image_path = r"MedLink\medlink (with frontend)\doctor_l.png"
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
    center_window(login_window)
    login_window.geometry("1000x800")

    new_image_path = r"MedLink\medlink (with frontend)\login2.png"
    new_pil_image = Image.open(new_image_path).resize((1000, 800), Image.LANCZOS)
    new_tk_image = ImageTk.PhotoImage(new_pil_image)

    new_background_label = tk.Label(login_window, image=new_tk_image)
    new_background_label.place(x=0, y=0, relwidth=1, relheight=1)

    email_label = tk.Label(login_window, text="Email:", width=30, height=3, bg="#A9BABD")
    email_label.place(relx=0.6, rely=0.4, anchor="center")

    email_entry = tk.Entry(login_window, width=30)
    email_entry.place(relx=0.9, rely=0.4, anchor="center")

    password_label = tk.Label(login_window, text="Password:", width=30, height=3, bg="#A9BABD")
    password_label.place(relx=0.6, rely=0.5, anchor="center")

    password_entry = tk.Entry(login_window, width=30, show='*')
    password_entry.place(relx=0.9, rely=0.5, anchor="center")

    def login():
        email = email_entry.get()
        password = password_entry.get()
        if validate_email(email) and password:
            if user_type == "Doctor":
                d_login(email, password)
            else:
                p_login(email, password)
        else:
            messagebox.showwarning("Login Error", "Please enter a valid email and password.")
            login_window.lift()

    login_button = tk.Button(login_window, text="Login", font=("Helvetica", 14), command=login, width=40, height=2,
                            bd=0, highlightthickness=0, bg="#A9BABD")
    login_button.place(relx=0.70, rely=0.8, anchor="center")

    not_user_button = tk.Button(login_window, text="Not a user? Signup here", font=("Helvetica", 14),
                                command=lambda: open_signup_window(user_type), width=40, height=2,
                                bd=0, highlightthickness=0, bg="#A9BABD")
    not_user_button.place(relx=0.70, rely=0.9, anchor="center")

    button_width = int(login_window.winfo_screenwidth() / 70)
    button_height = int(login_window.winfo_screenheight() / 220)
    login_button.config(width=button_width, height=button_height)
    not_user_button.config(width=button_width, height=button_height)

    login_window.mainloop()

def open_signup_window(user_type):
    root.withdraw()
    signup_window = tk.Toplevel(root)
    signup_window.title(f"{user_type} Signup")
    center_window(signup_window)
    signup_window.geometry("1000x800")

    new_image_path = r"MedLink\medlink (with frontend)\login1.png"
    new_pil_image = Image.open(new_image_path).resize((1000, 800), Image.LANCZOS)
    new_tk_image = ImageTk.PhotoImage(new_pil_image)

    new_background_label = tk.Label(signup_window, image=new_tk_image)
    new_background_label.place(x=0, y=0, relwidth=1, relheight=1)

    new_background_label = tk.Label(signup_window, image=new_tk_image)
    new_background_label.place(x=0, y=0, relwidth=1, relheight=1)

    email_label = tk.Label(signup_window, text="Email:", width=30, height=3, bg="#A9BABD")
    email_label.place(relx=0.6, rely=0.1, anchor="center")

    email_entry = tk.Entry(signup_window, width=30)
    email_entry.place(relx=0.7, rely=0.1)

    password_label = tk.Label(signup_window, text="Password:", width=30, height=3, bg="#A9BABD")
    password_label.place(relx=0.6, rely=0.2, anchor="center")

    password_entry = tk.Entry(signup_window, width=30, show='*')
    password_entry.place(relx=0.7, rely=0.2)

    name_label = tk.Label(signup_window, text="Name:", width=30, height=3, bg="#A9BABD")
    name_label.place(relx=0.6, rely=0.3, anchor="center")

    name_entry = tk.Entry(signup_window)
    name_entry.place(relx=0.7, rely=0.3)

    contact_label = tk.Label(signup_window, text="Contact Number:", width=30, height=3, bg="#A9BABD")
    contact_label.place(relx=0.6, rely=0.4, anchor="center")

    contact_entry = tk.Entry(signup_window)
    contact_entry.place(relx=0.7, rely=0.4)

    if user_type == "Doctor":
        qual_label = tk.Label(signup_window, text="Qualifications:", width=30, height=3, bg="#A9BABD")
        qual_label.place(relx=0.6, rely=0.5, anchor="center")

        qual_entry = tk.Entry(signup_window)
        qual_entry.place(relx=0.7, rely=0.5)

        speciality_label = tk.Label(signup_window, text="Speciality:", width=30, height=3, bg="#A9BABD")
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

    signup_button = tk.Button(signup_window, text="Signup", command=signup(), font=("Helvetica", 14),  width=40, height=2,
                            bd=0, highlightthickness=0, bg="#A9BABD")
    signup_button.place(relx=0.70, rely=0.8, anchor="center")

    already_user_button = tk.Button(signup_window, text="Already a user? Login here", font=("Helvetica", 14),
                                    command=lambda: open_login_window(user_type), width=40, height=2,
                                    bd=0, highlightthickness=0, bg="#A9BABD")
    already_user_button.place(relx=0.70, rely=0.9, anchor="center")

    button_width = int(signup_window.winfo_screenwidth() / 60)
    button_height = int(signup_window.winfo_screenheight() / 220)
    signup_button.config(width=button_width, height=button_height)
    already_user_button.config(width=button_width, height=button_height)
    signup_window.mainloop()

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def validate_email(email):
    if re.match(r'^[\w\.-]+@[\w\.-]+$', email):
        return True
    return False

root = tk.Tk()
root.title("eHealthcare")
w = 1000
h = 800
root.geometry(f"{w}x{h}")

image_path = r"MedLink\medlink (with frontend)\main.png"
pil_image = Image.open(image_path).resize((w, h), Image.LANCZOS)
tk_image = ImageTk.PhotoImage(pil_image)

background_label = tk.Label(root, image=tk_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

doctor_button = tk.Button(root, text="Doctor", font=("Helvetica", 14), command=open_doctor_window, width=40, height=2,
                          bd=0, highlightthickness=0, bg="#A9BABD")
doctor_button.place(relx=0.70, rely=0.4, anchor="center")

patient_button = tk.Button(root, text="Patient", font=("Helvetica", 14), command=open_patient_window, width=40, height=2,
                           bd=0, highlightthickness=0, bg="#A9BABD")
patient_button.place(relx=0.70, rely=0.5, anchor="center")

button_width = int(w / 120)
button_height = int(h / 120)
root.mainloop()
