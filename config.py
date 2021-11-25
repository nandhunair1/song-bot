import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    START_MSG = os.environ.get("START_MSG", "<b>Hi {},\nIam A Simple Youtube to Mp3 Downloader Bot,</b>\n\nSend me Any Songs name without command")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/0254a014cb78c3cca2df0.jpg")
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "tvseriezzz_music")
    msg = {}
