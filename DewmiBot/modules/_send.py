from DewmiBot import telethn as tbot
from DewmiBot.events import register
import os
import asyncio
import os
import time
from datetime import datetime
from DewmiBot import OWNER_ID, DEV_USERS
from DewmiBot import TEMP_DOWNLOAD_DIRECTORY as path
from DewmiBot import TEMP_DOWNLOAD_DIRECTORY
from datetime import datetime


client = tbot

@register(pattern=r"^/supun ?(.*)")
async def Prof(event):
    if event.sender_id == OWNER_ID or event.sender_id == DEV_USERS:
        pass
    else:
        return
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./DewmiBot/modules/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
     message_id = event.message.id
     await event.client.send_file(
             event.chat_id,
             the_plugin_file,
             force_document=True,
             allow_cache=False,
             reply_to=message_id,
         )
    else:
        await event.reply("No File Found!")
    
__help__ = """   
**Owner Only **
@szrosebot🇱🇰
 ❍ /supun - send any plugin
"""

    
__mod_name__ = "plugin"            
__advtools__ = __help__ 
