# 📂 generate_3d.py
# 製作裸眼3D 左右視角圖：使用 MiDaS 預測 depth → 產生 shift
# ============================
import cv2
import numpy as np
# 假設你已有一個 MidasDepth.predict() function

def generate_stereo(input_img):
    depth = MidasDepth().predict(input_img)
    shift = (depth / np.max(depth)) * 10
    h, w = input_img.shape[:2]
    left = np.zeros_like(input_img)
    right = np.zeros_like(input_img)
    for y in range(h):
        for x in range(w):
            dx = int(shift[y, x])
            if x + dx < w: left[y, x] = input_img[y, x + dx]
            if x - dx >= 0: right[y, x] = input_img[y, x - dx]
    return left, right