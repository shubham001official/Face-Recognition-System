
# Face Recognition System and Attendance Viewer Setup

This guide provides instructions on setting up and running the Face Recognition System and Attendance Viewer project. This project involves creating a face recognition system with a training GUI and an attendance viewer GUI.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python (3.6 or higher): Download and install Python from the official website: https://www.python.org/downloads/
- `opencv-python` library: Install OpenCV using the following command:

 
  pip install opencv-python
numpy library: Install numpy using the following command:


pip install numpy
pandas library: Install pandas using the following command:


pip install pandas
mysql-connector-python library: Install the MySQL connector using the following command:

bash
Copy code
pip install mysql-connector-python
Installation
Clone or download this repository to your local machine.


git clone https://github.com/shubham001official/face-recognition-attendance.git
Navigate to the project directory.


cd face-recognition-attendance
Running the Face Recognition System
Navigate to the face_recognition directory.


cd face_recognition
Run the following command to start the face training GUI:


python face_training_gui.py
Follow the on-screen instructions to perform face training using your webcam.

Running the Attendance Viewer
Navigate to the attendance_viewer directory.


cd ../attendance_viewer
Run the following command to start the Attendance Viewer GUI:


python attendance_viewer_gui.py
Click the "Open CSV" button to select and display attendance data from a CSV file.

Usage
Use the Face Recognition System to perform face training using the face training GUI.
Use the Attendance Viewer to open and view attendance data stored in CSV files.
Troubleshooting
If you encounter any issues, ensure that you have met the prerequisites and followed the installation steps correctly.
Make sure your webcam is functional and accessible by the face training GUI.


License
This project is licensed under the MIT License.