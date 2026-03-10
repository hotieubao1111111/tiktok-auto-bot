import os
import subprocess
import time

folder = r"C:\Users\ASUS\Downloads\tiktok_videos"
cookies = "cookies.txt"

videos = sorted([f for f in os.listdir(folder) if f.endswith(".mp4")])

for video in videos:
    path = os.path.join(folder, video)

    print("Uploading:", video)

    subprocess.run([
        "python",
        "-m",
        "tiktok_uploader",
        "-v",
        path,
        "-d",
        "#fyp #viral",
        "-c",
        cookies
    ])

    print("Uploaded:", video)

    # xóa video đã đăng
    os.remove(path)

    print("Deleted:", video)

    # chờ 24h
    time.sleep(86400)