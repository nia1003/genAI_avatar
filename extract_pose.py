# 📂 extract_pose.py（MediaPipe 替代 OpenPose）
# 使用 Google MediaPipe 提取姿勢點（macOS 原生支援）
# ============================
import cv2
import mediapipe as mp
import os
import json

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

cap = cv2.VideoCapture("manchild.mp4")
os.makedirs("output_pose", exist_ok=True)
frame_id = 0

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if results.pose_landmarks:
        landmarks = [
            {
                "x": lm.x,
                "y": lm.y,
                "z": lm.z,
                "visibility": lm.visibility
            }
            for lm in results.pose_landmarks.landmark
        ]
        with open(f"output_pose/frame_{frame_id:05d}.json", "w") as f:
            json.dump({"landmarks": landmarks}, f)
    frame_id += 1

print("✅ MediaPipe pose 完成！")