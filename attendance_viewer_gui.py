import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Function to open a file dialog and select a CSV file
def open_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        load_csv(file_path)

# Function to load and display attendance data from a CSV file
def load_csv(file_path):
    df = pd.read_csv(file_path)
    data_text.config(state=tk.NORMAL)
    data_text.delete(1.0, tk.END)
    data_text.insert(tk.END, df.to_string(index=False))
    data_text.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Attendance Viewer")

# Create a button to open a CSV file
open_button = tk.Button(root, text="Open CSV", command=open_csv)
open_button.pack(pady=10)

# Create a text widget to display the attendance data
data_text = tk.Text(root, wrap=tk.NONE, state=tk.DISABLED)
data_text.pack(fill=tk.BOTH, expand=True)

# Start the Tkinter event loop
root.mainloop()
