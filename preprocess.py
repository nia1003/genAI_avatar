import os
from rembg import remove
from PIL import Image

def preprocess_images(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for file in os.listdir(input_dir):
        if file.lower().endswith(('.jpg', '.png')):
            img_path = os.path.join(input_dir, file)
            img = Image.open(img_path)
            result = remove(img)
            result.save(os.path.join(output_dir, f"bg_removed_{file}"))
    print("✅ 背景去除完成")