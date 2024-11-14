import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "hiroVideo Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "HiroHelper")
ALIVE_NAME = getenv("ALIVE_NAME", "hiroMV")
BOT_USERNAME = getenv("BOT_USERNAME", "hiroMusikBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "HiroHelper")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "@molemutualan")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Updates_of_ElizaBot")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://ibb.co.com/YNTJq0N")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/hiro-v1/HiroVideoStreamer")
IMG_1 = getenv("IMG_1", "https://ibb.co.com/8zMMS5V")
IMG_2 = getenv("IMG_2", "https://ibb.co.com/4JpGphD")
IMG_3 = getenv("IMG_3", "https://ibb.co.com/rdtkVDD")
IMG_4 = getenv("IMG_4", "https://ibb.co.com/YNTJq0N")
