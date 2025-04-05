from telethon import TelegramClient

from app.config import settings

client = TelegramClient(settings.SESSION_NAME, settings.API_ID, settings.API_HASH)
