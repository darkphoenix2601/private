import requests
from pyrogram import Client, filters
from DewmiBot import pbot 
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, Message
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
import re
from io import BytesIO
from requests import get
import os 
from PIL import Image, ImageDraw, ImageFont
import random
import shutil

JOIN_ASAP = f"⛔️** Access Denied **⛔️\n\n🙋‍♂️ Hey There , You Must Join @szteambots Telegram Channel To Use This BOT. So, Please Join it & Try Again🤗. Thank You 🤝"

FSUBB = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Sz Team Bots <sz/>", url=f"https://t.me/szteambots") 
        ]]
    )

def nospace(s):

    s = re.sub(r"\s+", '%20', s)

    return s
@pbot.on_message(filters.command(["logo", f"logo@szrosebot"]))
async def getssh(_, message):
    try:
        await message._client.get_chat_member(int("-1001325914694"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return    
    if len(message.command) < 2:
            return await message.reply_text("Give a name to make logo")
    accname = message.text.split(None, 1)[1].replace(" ", "")
    button = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("☘️ Pic Me", callback_data=f"pic"),
                    InlineKeyboardButton("🎁 Logo", callback_data=f"logo {accname} ")
                ],
                [
                    InlineKeyboardButton("🗑 close 🗑", callback_data=f"cls")
                ],    
            ]
        )
    msg = await message.reply_text("""
**Do you want to Take a Picture** ? 🙈. Click The Pick Me Button Below , I will **Capture** you 😁
☘️ Pic Me - Capture Your Profile Picture
🎁 Logo - Generate Logo With Your Name
""",
    reply_markup = button)
    
@pbot.on_callback_query(filters.regex("logo"))
async def makessh(_, query):     
    m = await query.edit_message_text("📸 Creating..")
    data = query.data
    accname = data.split()[2].strip()
    api = get(f"https://api.singledevelopers.net/logo?name={accname}")
    await m.edit("📤 Uploading ...")
    await sz.send_chat_action(message.chat.id, "upload_photo")
    img = Image.open(BytesIO(api.content))
    logoname = "szlogo.png"
    img.save(logoname, "png")
    await query.edit_message_photo(photo = logoname,
                              caption="@szrosebot")
    await m.delete()
    if os.path.exists(logoname):
            os.remove(logoname)   
        
        
        



@pbot.on_callback_query(filters.command("pic"))
async def sems(_, query: CallbackQuery):
    id = query.message.from_user.photo.big_file_id
    photo = await pbot.download_media(id)
    await query.message.reply_photo(photo)
    os.remove(photo)        
        

@pbot.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()                
                
                
                
                
__help__ = """
@szrosebot🇱🇰
 ❍ Use /logo [name for logo] to make logo.
"""


__mod_name__ = "logo maker"
__advtools__ = __help__   
