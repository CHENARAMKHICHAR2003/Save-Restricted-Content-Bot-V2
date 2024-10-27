# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24894984"))
API_HASH = getenv("API_HASH", "4956e23833905463efb588eb806f9804")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "24894984"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "")
LOG_GROUP = int(getenv("LOG_GROUP", "-4573949804"))
FORCESUB = getenv("FORCESUB", "-1002374822952")
