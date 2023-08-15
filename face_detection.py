import tkinter as tk
from tkinter import filedialog
import cv2
import os

# Function to perform face detection
def detect_faces(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Create a cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the image with detected faces
    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function to open a file dialog and select an image
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if file_path:
        detect_faces(file_path)

# Create the main window
root = tk.Tk()
root.title("Face Detection")

# Create a button to open an image for face detection
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
