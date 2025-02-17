# Push-Up and Squat Counter

## 📌 Overview
This project is a real-time push-up and squat counter that utilizes a camera to detect and count the number of push-ups and squats performed. The counter updates in real time, providing users with instant feedback on their exercises. It features a user-friendly interface and a robust backend to process movements efficiently.


## 🚀 Features
### 🎥 Real-time Detection: Uses a camera to track push-ups and squats.
### 📊 Live Counter: Updates the number of reps in real-time.
### 🖥️ Modern UI: A visually appealing frontend.
### ⚡ Fast & Efficient: Optimized for smooth performance.
### 🏗️ Tech Stack


## Frontend
### React.js (Styled without Tailwind)
### CSS for custom styling
### Camera integration for movement detection
### Backend
### FastAPI (Python-based lightweight backend)
### OpenCV & MediaPipe for pose detection


## 🛠️ Installation
### Prerequisites
### Node.js & npm
### Python 3.x
### Virtual environment (recommended)


## Setup Instructions
### 1️⃣ Clone the Repository
git clone https://github.com/yourusername/pushup-squat-counter.git
cd pushup-squat-counter

### 2️⃣ Backend Setup
    cd backend
    python -m venv venv  # Create a virtual environment
    source venv/bin/activate  # (For Mac/Linux)
    venv\Scripts\activate  # (For Windows)
    pip install -r requirements.txt
    uvicorn main:app --reload

### 3️⃣ Frontend Setup
    cd frontend
    npm install
    npm start

## 🎯 Usage
### Start the backend server.
### Run the frontend application.
### Select either push-ups or squats on the home screen.
### Allow camera access for real-time tracking.
### Perform exercises while the counter updates automatically.


## 🏋️‍♂️ Future Enhancements
### Add rep-based workout goals
### Improve accuracy with AI-based models
### Dark mode UI option
### Voice feedback on rep completion
