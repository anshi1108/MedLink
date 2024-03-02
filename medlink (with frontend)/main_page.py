import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import doctor_profilepage
import patient_homepage
import login_and_signup

def create_signup_window(user_type):
    # Close the main window
    root.iconify()

    signup_window = tk.Toplevel(root)
    signup_window.title(f"MedLink - {user_type} Signup")
    signup_window.geometry(f"{w}x{h}")
    signup_window.attributes('-fullscreen', True)

    # Labels
    tk.Label(signup_window, text="MedLink", font=('Helvetica', 23)).pack(pady=20)
    tk.Label(signup_window, text=f'{user_type} Signup', font=('Helvetica', 18)).pack()

    # Entry fields
    tk.Label(signup_window, text="Name: ").pack()
    name_entry = tk.Entry(signup_window, width=30)
    name_entry.pack()

    tk.Label(signup_window, text="Email: ").pack()
    email_entry = tk.Entry(signup_window, width=30)
    email_entry.pack()

    tk.Label(signup_window, text="Password: ").pack()
    password_entry = tk.Entry(signup_window, width=30, show='*')
    password_entry.pack()

    tk.Label(signup_window, text="Contact Number: ").pack()
    contact_entry = tk.Entry(signup_window, width=30)
    contact_entry.pack()

    if user_type == "Doctor":
        tk.Label(signup_window, text="Qualification: ").pack()
        qualification_entry = tk.Entry(signup_window, width=30)
        qualification_entry.pack()

        tk.Label(signup_window, text="Speciality: ").pack()
        speciality_entry = tk.Entry(signup_window, width=30)
        speciality_entry.pack()

    # Signup button function
    def signup():
        user_info = {
            'Name': name_entry.get(),
            'Email': email_entry.get(),
            'Password': password_entry.get(),
            'Contact Number': contact_entry.get(),
        }

        if user_type == "Doctor":
            user_info.update({
                'Qualification': qualification_entry.get(),
                'Speciality': speciality_entry.get()
            })

            # Call doctor signup function
            login_and_signup.d_signup(user_info['Email'], user_info['Password'], user_info['Name'],
                     user_info['Contact Number'], user_info['Qualification'], user_info['Speciality'])
        elif user_type == "Patient":
            # Call patient signup function
            login_and_signup.p_signup(user_info['Email'], user_info['Password'], user_info['Name'], user_info['Contact Number'])
        messagebox.showinfo("Signup", "Signed up successfully!")
        login()

    # Already a user? Login button function
    def login():
        signup_window.destroy()  # Close the signup window
        
        # Open login window
        login_window = tk.Toplevel(root)
        login_window.title(f"MedLink - {user_type} Login")
        login_window.geometry(f"{w}x{h}")
        login_window.attributes('-fullscreen', True)

        # Labels
        tk.Label(login_window, text="MedLink", font=('Helvetica', 23)).pack(pady=20)
        tk.Label(login_window, text=f'{user_type} Login', font=('Helvetica', 18)).pack()

        # Entry fields
        tk.Label(login_window, text="Email: ").pack()
        email_entry = tk.Entry(login_window, width=30)
        email_entry.pack()

        tk.Label(login_window, text="Password: ").pack()
        password_entry = tk.Entry(login_window, width=30, show='*')
        password_entry.pack()

        # Login button function
        def user_login():
            if user_type == "Doctor":
                # Call doctor login function
                login_and_signup.d_login(email_entry.get(), password_entry.get())

            elif user_type == "Patient":
                # Call patient login function
                login_and_signup.p_login(email_entry.get(), password_entry.get())

        # Login button
        btn_login = tk.Button(login_window, text='Login', command=user_login, width=18, height=2)
        btn_login.pack(pady=20)

    # Signup button
    btn_signup = tk.Button(signup_window, text='Signup', command=signup, width=18, height=2)
    btn_signup.pack(pady=20)

    # Already a user? Login button
    btn_login = tk.Button(signup_window, text=f'Already a user? Login', command=login)
    btn_login.pack()

# Main window
root = tk.Tk()
root.title("MedLink")
root.attributes('-fullscreen', True)  # Fullscreen mode
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

# Set the window dimensions
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

# Labels
tk.Label(root, text="MedLink", font=('Helvetica', 23)).pack(pady=20)
tk.Label(root, text='Welcome to "MedLink"!', font=('Helvetica', 18)).pack()

# Buttons
btn_doctor = tk.Button(root, text='Doctor Signup', command=lambda: create_signup_window("Doctor"), width=18, height=2)
btn_doctor.pack(pady=20)

btn_patient = tk.Button(root, text='Patient Signup', command=lambda: create_signup_window("Patient"), width=18, height=3)
btn_patient.pack()

root.mainloop()