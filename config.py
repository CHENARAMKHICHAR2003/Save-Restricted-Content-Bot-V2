# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23833905463"))
API_HASH = getenv("API_HASH", "4956e23833905463efb588eb806f9804")
BOT_TOKEN = getenv("BOT_TOKEN", "7601293855:AAG0J1lG04wfEnK9J1GnImfOWN7X_2wyaS4")
OWNER_ID = list(map(int, getenv("OWNER_ID", "902551614").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
