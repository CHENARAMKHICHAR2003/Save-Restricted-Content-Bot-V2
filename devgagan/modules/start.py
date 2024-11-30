from pyrogram import filters
from devgagan import app
from devgagan.core import script
from devgagan.core.func import subscribe
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ------------------- Start-Buttons ------------------- #

buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("ALL UPDATES YHI AAYEGI TO JOIN KRLO ", url="https://t.me/TARGETAALLCOURSE")],
        [InlineKeyboardButton("Buy Premium", url="https://t.me/Free_course2_bot")]
    ]
)

@app.on_message(filters.command("start"))
async def start(_, message):
    try:
        # Check subscription status before proceeding
        join = await subscribe(_, message)
        if join == 1:
            return

        # Send a welcome message with a photo and inline buttons
        await message.reply_photo(
            photo="https://graph.org/file/4e80dc2f4f6f2ddadb4d2.jpg",
            caption=script.START_TXT.format(message.from_user.mention), 
            reply_markup=buttons
        )
    except Exception as e:
        # Handle any errors that occur during the process
        await message.reply_text(f"An error occurred: {str(e)}")
