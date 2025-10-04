import random
import asyncio
import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# -------------------
# Load environment variables
# -------------------
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

# -------------------
# Anime Sticker list (100 placeholders)
# -------------------
STICKER_IDS = [
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY0AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY1AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY2AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY3AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY0AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY1AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY2AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY3AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY4AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY5AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY6AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY7AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY8AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY9AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY0AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY1AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY2AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY3AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY4AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY5AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY6AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY7AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY8AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY9AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY10AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY11AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY12AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY13AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY14AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY15AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY16AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY17AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY18AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY19AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY20AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY21AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY22AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY23AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY24AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY25AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY26AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY27AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY28AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY29AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY30AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY31AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY32AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
    "CAACAgUAAxkBAAEBX1Jgkq9a8g2Jw1k0F1Oq6k7JtY33AAI8gAAp2X0U5x6Z3j4JpH5gIAQ",
# ... baki stickers yaha add kar do (total 200)
]
CUSTOM_MESSAGES = [
    "Kawaii! 😍",
    "Anime surprise for you 😏",
    "Look at this cute sticker! 🎉",
    "Enjoy this anime sticker 😘",
    "Nyaa~ 🐾"
]

bot = Client("anime_sticker_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# -------------------
# Inline buttons
# -------------------
def sticker_buttons(sticker):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📄 View Info", callback_data=f"info|{sticker}")],
        [InlineKeyboardButton("🔁 Send Again", callback_data=f"again|{sticker}")]
    ])

# -------------------
# Reply only to sender
# -------------------
@bot.on_message(filters.group & ~filters.bot)
async def auto_reply(client, message):
    await asyncio.sleep(random.randint(2, 5))  # natural delay
    sticker = random.choice(ANIME_STICKERS)
    custom_text = random.choice(CUSTOM_MESSAGES)
    
    await client.send_sticker(
        chat_id=message.chat.id,
        sticker=sticker,
        caption=custom_text,
        reply_to_message_id=message.message_id,
        reply_markup=sticker_buttons(sticker)
    )

# -------------------
# Callback query
# -------------------
@bot.on_callback_query()
async def callbacks(client, callback_query):
    data = callback_query.data
    if data.startswith("info|"):
        sticker = data.split("|")[1]
        await callback_query.message.reply_text(f"Sticker ID: {sticker}")
    elif data.startswith("again|"):
        sticker = data.split("|")[1]
        await callback_query.message.reply_sticker(sticker)

# -------------------
# Help command (Pyrogram v2 compatible)
# -------------------
@bot.on_message(filters.command("help") & filters.group)
async def help_cmd(client, message):
    help_text = (
        "📌 **Anime Sticker Bot Commands:**\n\n"
        "/help - Show this help message\n"
        "/broadcast <message> - Send message to all group members (Owner only)\n"
        "Automatic anime sticker reply to any message sender is active."
    )
    await message.reply_text(help_text, parse_mode="markdown")

# -------------------
# Broadcast command (Owner only)
# -------------------
@bot.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(client, message):
    if len(message.command) < 2:
        await message.reply_text("Usage: /broadcast <message>")
        return
    text = message.text.split(None, 1)[1]
    chat_members = await client.get_chat_members(message.chat.id)
    for member in chat_members:
        if member.user.is_bot:
            continue
        try:
            await client.send_message(member.user.id, text)
        except:
            continue
    await message.reply_text("Broadcast sent to all members.")

# -------------------
# Run bot
# -------------------
bot.run()