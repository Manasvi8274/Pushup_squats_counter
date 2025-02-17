from fastapi import FastAPI, WebSocket
import cv2
import numpy as np
import mediapipe as mp
import base64
import asyncio
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
cap = cv2.VideoCapture(0)

pushup_count = 0
squat_count = 0
prev_pushup = False
prev_squat = False
pushup_active = False
squat_active = False

def calculate_angle(a, b, c):
    a, b, c = np.array([a.x, a.y]), np.array([b.x, b.y]), np.array([c.x, c.y])
    ba, bc = a - b, c - b
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    return np.degrees(np.arccos(cosine_angle))

def detect_pushups(landmarks):
    global pushup_count, prev_pushup, pushup_active
    if not pushup_active:
        return
    shoulder, elbow, wrist, nose = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER], landmarks[mp_pose.PoseLandmark.LEFT_ELBOW], landmarks[mp_pose.PoseLandmark.LEFT_WRIST], landmarks[mp_pose.PoseLandmark.NOSE]
    elbow_angle = calculate_angle(shoulder, elbow, wrist)
    if elbow_angle < 50 and nose.y > 0.5 and not prev_pushup:
        pushup_count += 1
        prev_pushup = True
    elif elbow_angle > 140 and nose.y < 0.4:
        prev_pushup = False

def detect_squats(landmarks):
    global squat_count, prev_squat, squat_active
    if not squat_active:
        return
    hip, knee, ankle = landmarks[mp_pose.PoseLandmark.LEFT_HIP], landmarks[mp_pose.PoseLandmark.LEFT_KNEE], landmarks[mp_pose.PoseLandmark.LEFT_ANKLE]
    knee_angle = calculate_angle(hip, knee, ankle)
    if knee_angle < 70 and not prev_squat:
        squat_count += 1
        prev_squat = True
    elif knee_angle > 160:
        prev_squat = False

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    global pushup_count, squat_count
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.pose_landmarks:
            detect_pushups(results.pose_landmarks.landmark)
            detect_squats(results.pose_landmarks.landmark)
        _, buffer = cv2.imencode('.jpg', frame)
        await websocket.send_json({"image": base64.b64encode(buffer).decode(), "pushups": pushup_count, "squats": squat_count})
        await asyncio.sleep(0.05)

@app.get("/start_pushups")  # Start push-up tracking
def start_pushups():
    global pushup_active
    pushup_active = True
    return {"status": "Push-ups started"}

@app.get("/stop_pushups")  # Stop push-up tracking
def stop_pushups():
    global pushup_active
    pushup_active = False
    return {"status": "Push-ups stopped"}

@app.get("/start_squats")  # Start squat tracking
def start_squats():
    global squat_active
    squat_active = True
    return {"status": "Squats started"}

@app.get("/stop_squats")  # Stop squat tracking
def stop_squats():
    global squat_active
    squat_active = False
    return {"status": "Squats stopped"}

@app.get("/reset")  # Reset count
def reset_counters():
    global pushup_count, squat_count
    pushup_count, squat_count = 0, 0
    return {"status": "Counters reset"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
