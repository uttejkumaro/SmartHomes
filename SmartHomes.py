
Original file is located at
    https://colab.research.google.com/drive/1_ABozKws8d7sHRGllRt4Fxjomnou28e9
"""

def signup():
    print("Welcome to Sign Up!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    users[username] = password
    print("Sign up successful!")

def login():
    print("Welcome to Login!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

def admin_login():
    print("Welcome to Administrator Login!")
    username = input("Enter your administrator username: ")
    password = input("Enter your administrator password: ")
    if username == admin_username and password == admin_password:
        print("Administrator Login successful!")
        add_user()
    else:
        print("Invalid administrator username or password.")

def add_user():
    print("\nAdding User:")
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    users[username] = password
    print("User added successfully!")

# Administrator credentials
admin_username = "admin"
admin_password = "admin123"

users = {}

while True:
    print("\nMenu:")
    print("1. Sign Up")
    print("2. Login")
    print("3. Administrator Login")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        admin_login()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

pip install google-cloud-speech

pip install pyproject.toml

pip install pyaudio

from google.cloud import speech
import pyaudio

# Set up Google Cloud credentials (replace 'path/to/your/credentials.json' with your actual path)
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credentials.json"

# Configure audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Initialize Google Cloud Speech client
client = speech.SpeechClient()

# Function to transcribe audio in real-time
def transcribe_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("Listening...")

    stream.start_stream()

    while True:
        data = stream.read(CHUNK)
        try:
            response = client.recognize(config={"encoding": speech.RecognitionConfig.AudioEncoding.LINEAR16, "sample_rate_hertz": RATE, "language_code": "en-US"}, audio={"content": data})
            for result in response.results:
                print("Transcript: {}".format(result.alternatives[0].transcript))
        except Exception as e:
            print("Error:", e)
            continue

    stream.stop_stream()
    stream.close()
    audio.terminate()

if __name__ == "__main__":
    transcribe_audio()

pip install speechrecognition

import speech_recognition as sr

def transcribe_audio(audio_file):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_file) as source:
        # Record the audio from the file
        audio_data = recognizer.record(source)

        try:
            # Use Google Web Speech API to recognize the audio
            text = recognizer.recognize_google(audio_data)
            print("Transcription:")
            print(text)
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

# Replace 'audio_file.wav' with the path to your audio file
audio_file = "audio_file.wav"
transcribe_audio(audio_file)

import cv2
import dlib
import numpy as np


# Capture frames from the primary camera
cap = cv2.VideoCapture(0)

# Face detector model
face_detector = dlib.get_frontal_face_detector()

# Capture frames continuously
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Convert RGB to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_detector(gray)

    # Iterate through all the faces and draw rectangles around each face and also number it
    for i, face in enumerate(faces):
        # Find the coordinates of the face
        x, y = face.left(), face.top()
        xl, yl = face.right(), face.bottom()

        # Draw the rectangle
        cv2.rectangle(frame, (x, y), (xl, yl), (0, 255, 0), 2)

        # Add face number
        cv2.putText(frame, "Face num " + str(i+1), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow('frame', frame)

    # Code to come out of the infinite loop / interrupt the execution
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
