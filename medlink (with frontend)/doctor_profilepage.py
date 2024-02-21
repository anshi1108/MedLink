import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import login_and_signup
import patient_homepage

# Global variable for company information
company_info_text = """
Welcome to MedLink - Your Trusted Healthcare Partner!

MedLink is committed to providing exceptional healthcare services. Our platform connects doctors and patients seamlessly, ensuring quality care and a smooth experience.

Explore the features designed to make your healthcare journey efficient and comfortable. For any assistance, feel free to reach out to our support team.

- The MedLink Team
"""
root = tk.Tk()
root.title("MedLink")

# Set the window dimensions
w = 800
h = 500
root.geometry(f"{w}x{h}")


def create_doctor_homepage():
    homepage = tk.Toplevel(root)
    homepage.title("MedLink - Doctor Homepage")
    homepage.geometry(f"{w}x{h}")
    homepage.attributes('-fullscreen', True)

    # Left Panel
    left_panel = tk.Frame(homepage, width=300, bg='lightgray', padx=10, pady=10)
    left_panel.pack(side=tk.LEFT, fill=tk.Y, expand=False)
    left_panel.pack_propagate(False)

    # MedLink Label
    tk.Label(left_panel, text="MedLink", font=('Helvetica', 18, 'bold'), bg='lightgray').pack(pady=30)

    # Doctor Buttons
    tk.Button(left_panel, text="My Profile", command=show_doctor_profile).pack(pady=50)
    tk.Button(left_panel, text="View Appointments", command=show_appointments).pack(pady=50)

    # Right Panel
    right_panel = tk.Frame(homepage, bg='white', padx=20, pady=20)
    right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # MedLink Company Information
    tk.Label(right_panel, text=company_info_text, font=('Helvetica', 12)).pack()

    
    
def create_patient_homepage():
    homepage = tk.Toplevel(root)
    homepage.title("MedLink - Patient Homepage")
    homepage.geometry(f"{w}x{h}")
    homepage.attributes('-fullscreen', True)

    # Left Panel
    left_panel = tk.Frame(homepage, width=300,bg='lightgray', padx=10, pady=10)
    left_panel.pack(side=tk.LEFT, fill=tk.Y, expand=False)
    left_panel.pack_propagate(False)

    # MedLink Label
    tk.Label(left_panel, text="MedLink", font=('Helvetica', 18, 'bold'), bg='lightgray').pack(pady=30)

    # Patient Buttons
    tk.Button(left_panel, text="My Profile", command=patient_homepage.patient_my_profile).pack(pady=50)
    tk.Button(left_panel, text="View Appointments", command=show_appointments).pack(pady=50)
    tk.Button(left_panel, text="Search Doctors", command=search_doctors).pack(pady=50)
    tk.Button(left_panel, text="Talk to AI Chatbot", command=talk_to_chatbot).pack(pady=50)

    # Right Panel
    right_panel = tk.Frame(homepage, bg='white', padx=20, pady=20)
    right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # MedLink Company Information
    tk.Label(right_panel, text=company_info_text, font=('Helvetica', 12)).pack()

def show_doctor_profile():
    messagebox.showinfo("Doctor Profile", "This is the doctor's profile.")

def show_appointments():
    messagebox.showinfo("Appointments", "Viewing Appointments.")

def search_doctors():
    messagebox.showinfo("Search Doctors", "Searching for doctors.")

def talk_to_chatbot():
    messagebox.showinfo("AI Chatbot", "Talking to AI Chatbot.")