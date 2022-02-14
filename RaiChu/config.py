## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "Shubhanshu")
ALIVE_NAME = getenv("ALIVE_NAME", "Null")
BOT_IMG = getenv("BOT_IMG")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "YurikoPlugin")
BOT_USERNAME = getenv("BOT_USERNAME", "YurikoRobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "null")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "PmPermit")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "BotDuniya")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/66d20566acacf826372d7.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://telegra.ph/file/66d20566acacf826372d7.jpg")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/66d20566acacf826372d7.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/66d20566acacf826372d7.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/66d20566acacf826372d7.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/66d20566acacf826372d7.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/66d20566acacf826372d7.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/66d20566acacf826372d7.jpg")
