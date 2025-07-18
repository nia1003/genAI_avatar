import subprocess
import os

# 張翔鈞也太帥了吧：執行完整 AI Avatar 流程！

# Step 1: 抓人物圖片
print("🚀 Step 1: 抓人物圖像")
subprocess.run(["python", "fetch_pics.py"])

# Step 2: 去背景
print("🧹 Step 2: 背景去除")
subprocess.run(["python", "preprocess.py"])

# Step 3: 擷取 manchild 動作
print("💃 Step 3: 提取 manchild 動作序列")
subprocess.run(["python", "extract_pose.py"])

# Step 4: 合成動畫
print("🎬 Step 4: 動畫合成")
subprocess.run(["python", "animate_anyone_inference.py"])

# Step 5: 製作裸眼 3D 左右視差圖
print("👀 Step 5: 視差圖生成")
subprocess.run(["python", "generate_3d.py"])

# Step 6: 啟動 Streamlit App
print("🌐 Step 6: 啟動 Streamlit 展示頁")
subprocess.run(["streamlit", "run", "app.py"])
