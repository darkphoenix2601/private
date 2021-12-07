import requests
from pyrogram import Client, filters
from DewmiBot import pbot 
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, Message
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied


JOIN_ASAP = f"⛔️** Access Denied **⛔️\n\n🙋‍♂️ Hey There , You Must Join @szteambots Telegram Channel To Use This BOT. So, Please Join it & Try Again🤗. Thank You 🤝"

FSUBB = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Sz Team Bots <sz/>", url=f"https://t.me/szteambots") 
        ]]
    )

@pbot.on_message(filters.command("ssh"))
async def getssh(_, message):
    try:
        await message._client.get_chat_member(int("-1001325914694"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return    
    if len(message.command) < 2:
            return await message.reply_text("Give a name to make ssh account ⚠️")
    accname = message.text.split(None, 1)[1].replace(" ", "")
    button = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("US 1 🇺🇸", callback_data=f"ssh 330 {accname}"),
                    InlineKeyboardButton("US 2 🇺🇸", callback_data=f"ssh 332 {accname}"),
                    InlineKeyboardButton("US 3 🇺🇸", callback_data=f"ssh 334 {accname}")
                ],
                [
                    InlineKeyboardButton("SG 1 🇸🇬", callback_data=f"ssh 336 {accname}"),
                    InlineKeyboardButton("SG 2 🇸🇬", callback_data=f"ssh 338 {accname}"),
                    InlineKeyboardButton("SG 3 🇸🇬", callback_data=f"ssh 340 {accname}")
                ],
                [
                    InlineKeyboardButton("UK 1 🇬🇧", callback_data=f"ssh 342 {accname}"),
                    InlineKeyboardButton("UK 2 🇬🇧", callback_data=f"ssh 344 {accname}"),
                    InlineKeyboardButton("UK 3 🇬🇧", callback_data=f"ssh 346 {accname}")
                ],
                [
                    InlineKeyboardButton("🗑 close 🗑", callback_data=f"cls")
                ],    
            ]
        )
    await message.reply_text("""
   
☘️ **Select Server Location**

🌏 3  Locations
📦 11 Servers Available
🔥 Unlimited Bandwith
🚀 Fastest Servers
🌟 100% Free 

🛠 **Create SSH Yourself** 🛠""",
    reply_markup = button)

@pbot.on_callback_query(filters.regex("ssh"))
async def makessh(_, query):     
    m = await query.edit_message_text("Connecting to the server🌩")
    data = query.data
    server = data.split()[1].strip()
    accname = data.split()[2].strip()
    passwd = "szbots"
    ssh = server +"$" + accname + "$" + passwd
    servers = requests.get(f"https://single-developers.herokuapp.com/servers?id={server}").json()
    hosttoip = requests.get(f"http://ip-api.com/json/{servers['ip']}").json()
    ssh_result = requests.get(f"https://single-developers.herokuapp.com/create?ssh={str(ssh)}").json()
    await m.edit("⚙️ Creating Your SSH Account....")   
    try:
     await m.edit(
     text=f"""
🙋‍♂️Hey Your SSH Account Created ✅
ᗚ *Username* - `{ssh_result['username']}`
ᗚ *Password* - `{ssh_result['password']}`
ᗚ *Host* - `{servers['ip']}`
ᗚ *IP* - `{hosttoip["query"]}`
ᗚ *Port* - `{ssh_result['port']}`
ᗚ *Expire* - `{ssh_result['ex_date']}`
ᗚ *Limit* - `{ssh_result['login']}`

======================
=❌NO SPAM
=❌NO DDOS
=❌NO HACKING
=❌NO CARDING
=❌NO TORRENT
=❌NO OVER DOWNLOAD
=❌NO MULTILOGIN                                                                
=======================

◈───────────────◈
🚀 Poωᥱɾᥱᑯ Bყ : @SingleDevelopers
💫 Made By : @szrosebot|@szteambots
◈───────────────◈
     """)
    except:
       error=ssh_result
       if error == "Username already exists !!!" :
         await m.edit("__Username already exists, Try another username or try this username with another server ⚠️ \nAnd also you can get a help from @slbotzone.__")
       if error == "Server Error !!!" :
         await m.edit("There was a error with this server, Please try another server ⚠️ \nAnd also you can get a help from @slbotzone")
       else:
           await m.edit("__Error occured ⚠️ \nYou can get a help from @slbotzone.__")

@pbot.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()                
                
                
                
                
__help__ = """
@szrosebot🇱🇰
 ❍ Use /ssh [name for account] to make ssh.
"""


__mod_name__ = "ssh creator"
__advtools__ = __help__              
                
