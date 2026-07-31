import yt_dlp
import os

def download_video(url):
    folder = "downloads"
    os.makedirs(folder, exist_ok=True)

    ydl_opts = {
        "outtmpl": f"{folder}/%(title)s.%(ext)s",
        "format": "best",
        "noplaylist": True,
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)
