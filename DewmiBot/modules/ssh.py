import requests
from pyrogram import Client, filters
from DewmiBot import pbot 
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, Message
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied


JOIN_ASAP = f"βοΈ** Access Denied **βοΈ\n\nπββοΈ Hey There , You Must Join @szteambots Telegram Channel To Use This BOT. So, Please Join it & Try Againπ€. Thank You π€"

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
            return await message.reply_text("Give a name to make ssh account β οΈ")
    accname = message.text.split(None, 1)[1].replace(" ", "")
    button = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("US 1 πΊπΈ", callback_data=f"ssh 330 {accname}"),
                    InlineKeyboardButton("US 2 πΊπΈ", callback_data=f"ssh 332 {accname}"),
                    InlineKeyboardButton("US 3 πΊπΈ", callback_data=f"ssh 334 {accname}")
                ],
                [
                    InlineKeyboardButton("SG 1 πΈπ¬", callback_data=f"ssh 336 {accname}"),
                    InlineKeyboardButton("SG 2 πΈπ¬", callback_data=f"ssh 338 {accname}"),
                    InlineKeyboardButton("SG 3 πΈπ¬", callback_data=f"ssh 340 {accname}")
                ],
                [
                    InlineKeyboardButton("UK 1 π¬π§", callback_data=f"ssh 342 {accname}"),
                    InlineKeyboardButton("UK 2 π¬π§", callback_data=f"ssh 344 {accname}"),
                    InlineKeyboardButton("UK 3 π¬π§", callback_data=f"ssh 346 {accname}")
                ],
                [
                    InlineKeyboardButton("π close π", callback_data=f"cls")
                ],    
            ]
        )
    await message.reply_text("""
   
βοΈ **Select Server Location**

π 3  Locations
π¦ 11 Servers Available
π₯ Unlimited Bandwith
π Fastest Servers
π 100% Free 

π  **Create SSH Yourself** π """,
    reply_markup = button)

@pbot.on_callback_query(filters.regex("ssh"))
async def makessh(_, query):     
    m = await query.edit_message_text("Connecting to the serverπ©")
    data = query.data
    server = data.split()[1].strip()
    accname = data.split()[2].strip()
    passwd = "szbots"
    ssh = server +"$" + accname + "$" + passwd
    servers = requests.get(f"https://single-developers.herokuapp.com/servers?id={server}").json()
    hosttoip = requests.get(f"http://ip-api.com/json/{servers['ip']}").json()
    ssh_result = requests.get(f"https://single-developers.herokuapp.com/create?ssh={str(ssh)}").json()
    await m.edit("βοΈ Creating Your SSH Account....")   
    try:
     await m.edit(
     text=f"""
πββοΈHey Your SSH Account Created β
α *Username* - `{ssh_result['username']}`
α *Password* - `{ssh_result['password']}`
α *Host* - `{servers['ip']}`
α *IP* - `{hosttoip["query"]}`
α *Port* - `{ssh_result['port']}`
α *Expire* - `{ssh_result['ex_date']}`
α *Limit* - `{ssh_result['login']}`

======================
=βNO SPAM
=βNO DDOS
=βNO HACKING
=βNO CARDING
=βNO TORRENT
=βNO OVER DOWNLOAD
=βNO MULTILOGIN                                                                
=======================

βββββββββββββββββ
π PoΟα₯±ΙΎα₯±α― Bα§ : @SingleDevelopers
π« Made By : @szrosebot|@szteambots
βββββββββββββββββ
     """)
    except:
       error=ssh_result
       if error == "Username already exists !!!" :
         await m.edit("__Username already exists, Try another username or try this username with another server β οΈ \nAnd also you can get a help from @slbotzone.__")
       if error == "Server Error !!!" :
         await m.edit("There was a error with this server, Please try another server β οΈ \nAnd also you can get a help from @slbotzone")
       else:
           await m.edit("__Error occured β οΈ \nYou can get a help from @slbotzone.__")

@pbot.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()                
                
                
                
                
__help__ = """
@szrosebotπ±π°
 β Use /ssh [name for account] to make ssh.
"""


__mod_name__ = "ssh creator"
__advtools__ = __help__              
                
