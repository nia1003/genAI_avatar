from icrawler.builtin import GoogleImageCrawler
import os

def normalize_name(name: str) -> str:
    # 將人名轉為資料夾格式（空格轉底線）
    return name.strip().lower().replace(" ", "_")

def fetch_images(person_name: str):
    keyword = f"{person_name} face"
    num = 20
    folder_name = normalize_name(person_name)
    save_dir = f"images/{folder_name}"
    os.makedirs(save_dir, exist_ok=True)

    crawler = GoogleImageCrawler(storage={"root_dir": save_dir})
    crawler.crawl(keyword=keyword, max_num=num)

    print(f"✅ 成功爬到【{person_name}】的角色圖片，存到 {save_dir}")

if __name__ == "__main__":
    person = input("請輸入你要抓圖的人名（例如：Elon Musk）：").strip()

    fetch_images(person)
