import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Create a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="student_db"
)
cursor = db.cursor()

def insert_data():
    name = name_entry.get()
    roll = roll_entry.get()
    age = age_entry.get()

    if name == "" or roll == "" or age == "":
        messagebox.showwarning("Warning", "All fields are required!")
        return

    query = "INSERT INTO students (name, roll, age) VALUES (%s, %s, %s)"
    values = (name, roll, age)
    
    cursor.execute(query, values)
    db.commit()

    messagebox.showinfo("Success", "Student data inserted successfully!")
    clear_fields()

def clear_fields():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Student Data Entry")

# Create labels and entry fields
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

roll_label = tk.Label(root, text="Roll Number:")
roll_label.pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

# Create buttons
submit_button = tk.Button(root, text="Submit", command=insert_data)
submit_button.pack()

clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.pack()

# Start the Tkinter event loop
root.mainloop()
