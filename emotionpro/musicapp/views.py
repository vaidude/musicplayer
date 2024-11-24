from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

     
        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return redirect('register')


        if not name:
            messages.error(request, "Name is required.")
        elif len(name) < 3:
            messages.error(request, "Name must be at least 3 characters.")
        elif not email:
            messages.error(request, "Email is required.")
        elif not password:
            messages.error(request, "Password is required.")
        elif len(password) < 8:
            messages.error(request, "Password must be at least 8 characters.")
        elif not phone or len(phone) != 10:
            messages.error(request, "Phone number must be 10 digits.")
        elif not address:
            messages.error(request, "Address is required.")
        else:
            # If everything is valid, save the user
            user = User.objects.create(
                name=name,
                email=email,
                password=password,  # Be sure to hash the password before saving
                phone=phone,
                address=address
            )
            user.save()

            messages.success(request, "Registration successful!")
            return redirect('index')  # Redirect to the index or home page after successful registration

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
    
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Invalid email and password")
            return render(request, 'login.html')

        # Check if the password matches
        if password != user.password:
            messages.error(request, "Invalid password.")
            return render(request, 'login.html')

    
        request.session['email'] = user.email
        messages.success(request, "Login successful!")
        return redirect('home')  
    return render(request, 'login.html')
def logout(request):
    request.session.flush()
    return redirect('index')

def profile(request):
    email = request.session.get('email')
    if email:
        user = User.objects.get(email=email)
        return render(request, 'profile.html', {'user': user})
    else:
        return redirect('login')
def editprofile(request):
    email = request.session.get('email')
    if email:
        user = User.objects.get(email=email)
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            profilepic = request.FILES.get('profilepic') 
            
            user.name = name
            user.phone = phone
            user.address = address
            if profilepic:
                print("Profile picture uploaded:", profilepic)
                user.profilepic = profilepic
            user.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')  
        return render(request, 'profile.html', {'user': user})
    messages.error(request, "You need to log in to edit your profile.")
    return redirect('login')

import numpy as np
import pandas as pd
import cv2
from time import time, sleep
from django.shortcuts import render
from keras.models import load_model

# Load pre-trained emotion model and music data
emotion_model = load_model("musicapp/face_emotion.h5")  # Correct path to your model
mood_music = pd.read_csv("musicapp/musicData.csv")  # Correct path to your CSV with music data

# Emotion dictionary and mapping to moods
emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

# More refined mood mapping
mood_map = {
    "Angry": "energetic",  # Energetic music for anger
    "Disgusted": "energetic",  # Energetic music for disgust
    "Fearful": "Chill",  # Calm music for fear
    "Happy": "Chill",  
    "Neutral": "relaxed",  # Relaxing music for neutral mood
    "Sad": "romantic",  # Romantic/slow music for sadness
    "Surprised": "Chill",  # Chill music for surprise
}

# Function to recommend music based on mood
def music_results(mood):
    mood_filtered = mood_map.get(mood, "relaxed")  # Default to relaxed if mood not found
    recommended_songs = mood_music[mood_music['mood'] == mood_filtered]
    
    # If no songs found, return an empty DataFrame
    if recommended_songs.empty:
        return pd.DataFrame()
    
    # Randomly sample up to 5 songs from the filtered mood
    return recommended_songs.sample(n=5, random_state=42)

# Main view function for emotion detection and music recommendation
def detect_emotion(request):
    webcam = cv2.VideoCapture(0)  # Open the webcam
    sleep(2)  # Wait for the webcam to initialize
    
    # Set the start time to capture for 5 seconds
    start_time = time()
    captured_image = None
    emotion_result = None
    data = None

    # Path to the Haar cascade file for face detection
    faceCascade = cv2.CascadeClassifier("musicapp/haarcascade_frontalface_default.xml")

    # Check if the classifier is loaded correctly
    if faceCascade.empty():
        raise Exception("classifier could not be loaded. Please check the file path.")

    while True:
        # Check if 5 seconds have passed
        if time() - start_time > 5:
            break
        
        check, image = webcam.read()  # Read the frame from the webcam
        
        if check:
            cv2.imshow("Capturing", image)  # Show the webcam feed
        else:
            print("Failed to capture image.")
            break
    
    # After 5 seconds, capture the frame
    if captured_image is None:
        check, captured_image = webcam.read()
    
    # Release the webcam and close the OpenCV window
    webcam.release()
    cv2.destroyAllWindows()
    
    if captured_image is not None:
        # Convert the captured frame to grayscale
        gray = cv2.cvtColor(captured_image, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray, scaleFactor=1.3, minNeighbors=3, minSize=(30, 30)
        )
        
        if len(faces) > 0:
            # Process the first detected face (for simplicity)
            x, y, w, h = faces[0]
            roi_color = captured_image[y:y+h, x:x+w]
            gray = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)
            img_ = cv2.resize(gray, (48, 48))
            
            # Prepare the image for emotion prediction
            img = np.array(img_)
            img = img.reshape(1, 48, 48, 1)
            
            # Predict emotion
            predict_x = emotion_model.predict(img)
            result = np.argmax(predict_x, axis=1)
            emotion_result = emotion_dict[result[0]]
            print(f"Detected Emotion: {emotion_result}")
            
            # Get music recommendations based on detected emotion
            data = music_results(emotion_result)
        
        else:
            print("No face detected.")
    
    # Handle the case when data is None or empty
    if data is None or (hasattr(data, 'empty') and data.empty):
        data = []  # Set to empty list if no data is found

    # Prepare context with songs and mood (emotion)
    context = {
        "songs": data.to_dict(orient="records") if hasattr(data, 'to_dict') else [],  # Safely check if `data` has `to_dict`
        "mood": emotion_result if emotion_result else "No Emotion Detected",
        "emoji_path": f"emojis/{emotion_result.lower()}.png" if emotion_result else "emojis/neutral.png",  # Path to the corresponding emoji
    }

    return render(request, 'playlist.html', context)
