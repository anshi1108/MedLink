import tkinter as tk
from tkinter import ttk

def patient_my_profile():
    def save_patient_info():
        # Function to save patient information
        patient_name = name_entry.get()
        patient_age = age_entry.get()
        patient_gender = gender_var.get()
        patient_diagnosis = diagnosis_entry.get("1.0", tk.END)

        # Save or process the patient information as needed
        # For now, let's print the information to the console
        print("Patient Information:")
        print(f"Name: {patient_name}")
        print(f"Age: {patient_age}")
        print(f"Gender: {patient_gender}")
        print(f"Diagnosis:\n{patient_diagnosis}")

    def clear_fields():
        # Function to clear input fields
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        gender_var.set("Male")  # Set default gender to Male
        diagnosis_entry.delete("1.0", tk.END)

    # Create a new window
    profile_window = tk.Toplevel()
    profile_window.title("Patient Information Profile")

    # Create and place widgets
    frame = ttk.Frame(profile_window, padding="10")
    frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Patient Name
    ttk.Label(frame, text="Patient Name:").grid(column=0, row=0, sticky=tk.W)
    name_entry = ttk.Entry(frame, width=30)
    name_entry.grid(column=1, row=0, sticky=tk.W, padx=10, pady=5)

    # Patient Age
    ttk.Label(frame, text="Patient Age:").grid(column=0, row=1, sticky=tk.W)
    age_entry = ttk.Entry(frame, width=10)
    age_entry.grid(column=1, row=1, sticky=tk.W, padx=10, pady=5)

    # Patient Gender
    ttk.Label(frame, text="Patient Gender:").grid(column=0, row=2, sticky=tk.W)
    gender_var = tk.StringVar()
    gender_combobox = ttk.Combobox(frame, textvariable=gender_var, values=["Male", "Female", "Other"])
    gender_combobox.grid(column=1, row=2, sticky=tk.W, padx=10, pady=5)
    gender_combobox.set("Male")  # Set default gender to Male

    # Patient Diagnosis
    ttk.Label(frame, text="Patient Diagnosis:").grid(column=0, row=3, sticky=tk.W)
    diagnosis_entry = tk.Text(frame, wrap=tk.WORD, width=30, height=5)
    diagnosis_entry.grid(column=1, row=3, sticky=tk.W, padx=10, pady=5)

    # Save Button
    save_button = ttk.Button(frame, text="Save", command=save_patient_info)
    save_button.grid(column=0, row=4, columnspan=2, pady=10)

    # Clear Button
    clear_button = ttk.Button(frame, text="Clear", command=clear_fields)
    clear_button.grid(column=0, row=5, columnspan=2, pady=5)