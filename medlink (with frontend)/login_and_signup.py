import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
import re
import mysql.connector
from PIL import Image, ImageTk
from functools import partial
import doctor_profilepage
import make_appoinment

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

    new_image_path = r"MedLink\medlink (with frontend)\doctor_l.png"
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
    login_window.geometry("1000x800")

    new_image_path = r"MedLink\medlink (with frontend)\login2.png"
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

    new_image_path = r"MedLink\medlink (with frontend)\login1.png"
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
    # main_d = tk.Toplevel(root)
    # main_d.geometry("1000x800")
    # main_d.mainloop()
    pass


def open_main_p():
    main_p = tk.Toplevel(root)
    main_p.geometry("1000x800")
    main_p.title("Information Page")
    main_p.protocol("WM_DELETE_WINDOW", root.quit)  # Handle closing of main_p window
    
     # Create a menu bar
    menu_bar = tk.Menu(main_p)
    main_p.config(menu=menu_bar)

    # Create a "Options" menu
    options_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="MY MENU", menu=options_menu,fon=('Helvictica',14))

    # Add menu items with commands
    options_menu.add_command(label="SHOW APPOINMENTS", command=show_appointments)
    options_menu.add_command(label="MAKE APPOINMENTS", command=make_appointments)
    options_menu.add_command(label="VIDEO CONFERNCING", command=video_call)
    options_menu.add_command(label="CHAT WITH ME", command=launch_chatbot)
    options_menu.add_command(label="MY PROFILE", command=lambda: create_patient_profile(main_p))
    main_p.mainloop()

def make_appointments():
    make_appoinments = tk.Toplevel(root)
    make_appoinments.geometry("1000x800")
    make_appoinments.title("Appoinment")
    make_appoinments.protocol("WM_DELETE_WINDOW", root.quit) 
    make_appoinment.create_appointment_frame(make_appoinments)

def show_appointments():
    pass

def video_call():
    pass
def launch_chatbot():
    pass

def create_patient_profile(main_p):
    
    # Patient Name
    name_label = tk.Label(main_p,text="Name:", width=25, height=3, bg="#A9BABD")
    name_label.place(relx=0.1,rely=0.1)

    name_entry = tk.Entry(main_p)
    name_entry.place(relx=0.4, rely=0.1)
    # Patient Age
    
    age_label = tk.Label(main_p,text="Age:", width=25, height=3, bg="#A9BABD")
    age_label.place(relx=0.1,rely=0.2)
    
    age_entry = tk.Entry(main_p, width=10)
    age_entry.place(relx=0.4,rely=0.2)

    # Patient Gender
    gender_label = tk.Label(main_p,text="Gender:", width=25, height=3, bg="#A9BABD")
    gender_label.place(relx=0.1,rely=0.3)
    

    var = tk.StringVar()
    tk.Radiobutton(main_p, text="Male", variable=var, value="Male", font=("Helvetica", 12)).place(relx=0.4,rely=0.3)
    tk.Radiobutton(main_p, text="Female", variable=var, value="Female", font=("Helvetica", 12)).place(relx=0.4,rely=0.35)
    tk.Radiobutton(main_p, text="Other", variable=var, value="Other", font=("Helvetica", 12)).place(relx=0.4,rely=0.4)

    # Patient Diagnosis
    diagnosis_label = tk.Label(main_p,text="Diagnosis:", width=25, height=3, bg="#A9BABD")
    diagnosis_label.place(relx=0.1,rely=0.5)
    
    diagnosis_entry = tk.Text(main_p, wrap=tk.WORD, width=30, height=5)
    diagnosis_entry.place(relx=0.4,rely=0.5)

    # Save Button
    save_button = tk.Button(main_p, text="Save", bg="#A9BABD", command=lambda: save_patient_info(name_entry, age_entry, var, diagnosis_entry), font=("Helvetica", 14))
    save_button.place(relx=0.1,rely=0.7)

    # Clear Button
    clear_button = tk.Button(main_p, text="Clear", bg="#A9BABD", command=lambda: clear_fields(name_entry, age_entry, var, diagnosis_entry), font=("Helvetica", 14))
    clear_button.place(relx=0.1,rely=0.8)


    
    
def save_patient_info(name_entry,age_entry,var,diagnosis_entry):
    patient_name = name_entry.get()
    patient_age = age_entry.get()
    patient_gender = var.get()
    patient_diagnosis = diagnosis_entry.get("1.0", tk.END)

    print("Patient Information:")
    print(f"Name: {patient_name}")
    print(f"Age: {patient_age}")
    print(f"Gender: {patient_gender}")
    print(f"Diagnosis:\n{patient_diagnosis}")

    # Function to clear input fields
def clear_fields(name_entry,age_entry,var,diagnosis_entry):
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    var.set("Male")  # Set default gender to Male
    diagnosis_entry.delete("1.0", tk.END)

    

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