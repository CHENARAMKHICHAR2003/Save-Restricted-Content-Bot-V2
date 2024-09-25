# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23833905463"))
API_HASH = getenv("API_HASH", "4956e23833905463efb588eb806f9804")
BOT_TOKEN = getenv("BOT_TOKEN", "7227942593:AAEjEu4NKFlWrlnjHBsNtskNaQmvWQLmZRg")
OWNER_ID = list(map(int, getenv("OWNER_ID", "902551614").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://crchoudharyji1122:<Chenaram@2003>@cluster0.cuje2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-2202175238")
CHANNEL_ID = int(getenv("CHANNEL_ID", "2182291545"))
