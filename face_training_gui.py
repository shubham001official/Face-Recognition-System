import tkinter as tk
from tkinter import messagebox
import cv2
import os

# Create the main window
root = tk.Tk()
root.title("Face Training")

# Create a label for instructions
instructions_label = tk.Label(root, text="Enter the name of the person:")
instructions_label.pack()

# Create an entry field for the person's name
name_entry = tk.Entry(root)
name_entry.pack()

# Create a button to start face training
def start_training():
    person_name = name_entry.get()

    if person_name == "":
        messagebox.showwarning("Warning", "Please enter a name!")
        return

    # Create a directory for storing training images
    directory = f"training_images/{person_name}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Start capturing video from the webcam
    cap = cv2.VideoCapture(0)

    # Create a cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Initialize a counter for image filenames
    image_counter = 0

    while True:
        ret, frame = cap.read()

        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            # Save the detected face to the training directory
            face_img = frame[y:y+h, x:x+w]
            image_filename = f"{directory}/{person_name}_{image_counter}.jpg"
            cv2.imwrite(image_filename, face_img)
            image_counter += 1
            
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        cv2.imshow("Face Training", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    messagebox.showinfo("Success", "Face training completed!")

train_button = tk.Button(root, text="Start Training", command=start_training)
train_button.pack()

# Start the Tkinter event loop
root.mainloop()
