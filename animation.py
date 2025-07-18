# 📂 animate_anyone_inference.py（Python API 版本）
# 合成動畫：參考人物圖片 + Pose JSON 資料（MediaPipe 格式轉換）
# ============================
import os
import subprocess

def run_animate_anyone(ref_image, pose_folder, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    cmd = [
        "python", "inference.py",
        "--ref_image", ref_image,
        "--pose_folder", pose_folder,
        "--output", output_dir
    ]
    subprocess.run(cmd)
    print(f"✅ 動畫已輸出到 {output_dir}")

if __name__ == "__main__":
    run_animate_anyone(
        ref_image="processed_elon/bg_removed_0001.png",
        pose_folder="output_pose",
        output_dir="out_elon_manchild"
    )