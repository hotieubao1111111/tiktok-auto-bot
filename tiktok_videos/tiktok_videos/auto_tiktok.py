import os
import subprocess
import time
import requests
from datetime import datetime

folder = "videos"
cookies = "cookies.txt"

TELEGRAM_TOKEN = "8779188076:AAGi2EZN-7ngcnm06fMEiIDdvzCEwP0wafw"
CHAT_ID = "5464983623"


def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data)


print("TikTok bot started")

while True:

    now = datetime.now()

    if now.hour == 19 and now.minute == 0:

        videos = sorted([f for f in os.listdir(folder) if f.endswith(".mp4")])

        if videos:

            video = videos[0]
            path = os.path.join(folder, video)

            print("Uploading:", video)

            subprocess.run([
                "python",
                "-m",
                "tiktok_uploader",
                "-v",
                path,
                "-d",
                "#fyp #xuhuong",
                "-c",
                cookies
            ])

            os.remove(path)

            send_telegram(f"✅ Upload thành công: {video}")

        else:

            send_telegram("⚠️ Không còn video để đăng")

        time.sleep(60)

    time.sleep(20)