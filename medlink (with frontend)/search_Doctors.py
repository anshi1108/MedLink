import tkinter as tk
from tkinter import ttk

# Sample database (replace this with your actual database connection)
doctors_database = {
    "Available Doctors and Specilizations \n\n"
    "A": "Cardiologist",
    "B": "Dermatologist",
    "C": "Orthopedic Surgeon",
    "D": "Pediatrician",
    # Add more doctors as needed
}

def search_doctors():
    query = entry_search.get().lower()
    search_result.delete(1.0, tk.END)  # Clear previous search results

    for name, specialty in doctors_database.items():
        if query in name.lower() or query in specialty.lower():
            result_text = f"{name}: {specialty}\n"
            search_result.insert(tk.END, result_text)

# Main application window with increased size
app = tk.Tk()
app.title("Meet Our Doctors")
app.geometry("600x500")  # Set your desired width and height

# Create and place widgets in the window

label_med_link = tk.Label(app, text="Doctors at Med Link", font=("Helvetica", 17, "bold"))
label_med_link.pack(pady=17)

label_med_link = tk.Label(app, text="Know our Doctors")
label_med_link.pack(pady=17)

label_title = tk.Label(app, text="Search Doctors", font=("Helvetica", 13))
label_title.pack(pady=10)

entry_search = tk.Entry(app, font=("Helvetica", 12), width=30)
entry_search.pack(pady=10)

button_search = tk.Button(app, text="Search", command=search_doctors, font=("Helvetica", 13))
button_search.pack(pady=10)

search_result = tk.Text(app, height=10, width=40, font=("Helvetica", 12))
search_result.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
import tkinter as tk
from tkinter import ttk

# Sample database (replace this with your actual database connection)
doctors_database = {
    "Available Doctors and Speciliality \n\n"
    "A": "Cardiologist",
    "B": "Dermatologist",
    "C": "Orthopedic Surgeon",
    "D": "ophthalmologist",
    # Add more doctors as needed
}

def search_doctors():
    query = entry_search.get().lower()
    search_result.delete(1.0, tk.END)  # Clear previous search results

    for name, specialty in doctors_database.items():
        if query in name.lower() or query in specialty.lower():
            result_text = f"{name}: {specialty}\n"
            search_result.insert(tk.END, result_text)

# Main application window with increased size
app = tk.Tk()
app.title("Meet Our Doctors")
app.geometry("600x500")  # Set your desired width and height

# Create and place widgets in the window

label_med_link = tk.Label(app, text="Doctors at Med Link", font=("Helvetica", 17, "bold"))
label_med_link.pack(pady=17)

label_med_link = tk.Label(app, text="Know about our Doctors")
label_med_link.pack(pady=17)

label_title = tk.Label(app, text="Search Doctors", font=("Helvetica", 13))
label_title.pack(pady=10)

entry_search = tk.Entry(app, font=("Helvetica", 12), width=30)
entry_search.pack(pady=10)

button_search = tk.Button(app, text="Search", command=search_doctors, font=("Helvetica", 13))
button_search.pack(pady=10)

search_result = tk.Text(app, height=10, width=40, font=("Helvetica", 12))
search_result.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()