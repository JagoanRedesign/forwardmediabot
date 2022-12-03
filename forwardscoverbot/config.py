from dotenv import load_dotenv
from os import path, getenv


if path.exists("local.env"):
    load_dotenv("local.env")
else:
    load_dotenv()


class Config:
    BOT_TOKEN = getenv("BOT_TOKEN", "5660988324:AAHb_O3YGm8otZGuE2O9R4v7i5WS0cYczYc")
    ADMINS = int(getenv("ADMINS", "5166575484"))
    DB_PATH = getenv("DB_PATH", "database/database.db")
    GROUP = getenv("GROUP", "t.me/musikkugroup")
    CHANNEL = getenv("CHANNEL", "t.me/DutabotID")
    KODE = getenv("KODE", "https://github.com/kenkansaja/forwardmediabot")
config = Config()

