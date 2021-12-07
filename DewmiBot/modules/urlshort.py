

import json

import aiohttp
from pyrogram import filters

from DewmiBot.function.pluginhelpers import admins_only, get_text
from DewmiBot.services.pyrogram import pbot



@pbot.on_message(
    filters.command("short") & ~filters.edited & ~filters.bot & ~filters.private
)
@admins_only
async def shortify(client, message):
    lel = await client.send_message(message.chat.id, "`Wait a sec....`")
    url = get_text(message)
    if "." not in url:
        await lel.edit("Defuq!. Is it a url?")
        return
    header = {
        "Authorization": "Bearer ad39983fa42d0b19e4534f33671629a4940298dc",
        "Content-Type": "application/json",
    }
    payload = {"long_url": f"{url}"}
    payload = json.dumps(payload)
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://api-ssl.bitly.com/v4/shorten", headers=header, data=payload
        ) as resp:
            data = await resp.json()
    msg = f"**Original Url:** {url}\n\n**Shortened Url:** {data['link']}\n\n**Powered by**:-@szrosebot🇱🇰 "
    await lel.edit(msg)

__help__ = """
@szrosebot🇱🇰
Send the Long URL and get a Short URL Easily via szrosebot use this format 
 ❍ /short <your url> :-  you can get short url useing szrosebot
"""

__mod_name__ = "Url Short"
__advtools__ = __help__    
    
    
