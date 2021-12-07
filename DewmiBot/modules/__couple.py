"""
MIT License
Copyright (c) 2021 TheHamkerCat
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import random
from datetime import datetime

from pyrogram import filters

from DewmiBot import pbot
from DewmiBot.modules.mongo.couples_mongo import get_couple, save_couple

# Date and time
def dt():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    dt_list = dt_string.split(" ")
    return dt_list


def dt_tom():
    a = (
        str(int(dt()[0].split("/")[0]) + 1)
        + "/"
        + dt()[0].split("/")[1]
        + "/"
        + dt()[0].split("/")[2]
    )
    return a


today = str(dt()[0])
tomorrow = str(dt_tom())


@pbot.on_message(filters.command("couple") & ~filters.edited)
async def couple(_, message):
    if message.chat.type == "private":
        return await message.reply_text("This command only works in groups.")
    try:
        chat_id = message.chat.id
        is_selected = await get_couple(chat_id, today)
        if not is_selected:
            list_of_users = []
            async for i in pbot.iter_chat_members(message.chat.id):
                if not i.user.is_bot:
                    list_of_users.append(i.user.id)
            if len(list_of_users) < 2:
                return await message.reply_text("Not enough users")
            c1_id = random.choice(list_of_users)
            c2_id = random.choice(list_of_users)
            while c1_id == c2_id:
                c1_id = random.choice(list_of_users)
            c1_mention = (await pbot.get_users(c1_id)).mention
            c2_mention = (await pbot.get_users(c2_id)).mention

            couple_selection_message = f"""**Couple of the day:**
{c1_mention} + {c2_mention} = ❤️
__New couple of the day may be chosen at 12AM {tomorrow}__"""
            await pbot.send_message(
                message.chat.id, text=couple_selection_message
            )
            couple = {"c1_id": c1_id, "c2_id": c2_id}
            await save_couple(chat_id, today, couple)

        elif is_selected:
            c1_id = int(is_selected["c1_id"])
            c2_id = int(is_selected["c2_id"])
            c1_name = (await pbot.get_users(c1_id)).first_name
            c2_name = (await pbot.get_users(c2_id)).first_name
            couple_selection_message = f"""Couple of the day:
[{c1_name}](tg://openmessage?user_id={c1_id}) + [{c2_name}](tg://openmessage?user_id={c2_id}) = 
┳┻┳┻╭━━━━╮╱▔▔▔╲
┻┳┻┳┃╯╯╭━┫▏╰╰╰▕
┳┻┳┻┃╯╯┃▔╰┓▔▂▔▕╮
┻┳┻┳╰╮╯┃┈╰┫╰━╯┏╯
┳┻┳┻┏╯╯┃╭━╯┳━┳╯
┻┳┻┳╰━┳╯▔╲╱▔╭╮▔╲
┳┻┳┻┳┻┃┈╲┈╲╱╭╯╮▕
┻┳┻┳┻┳┃┈▕╲▂╱┈╭╯╱
┳┻┳┻┳┻┃'''┈┃┈┃┈'''╰╯
┻┳┻┳┻┏╯▔'''╰┓┣━┳┫
┳┻┳┻┳╰┳┳┳'''╯┃┈┃┃
┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃
┳┻┳┻┳┻┃┃┃'''┊┃┈┃┃
┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃.
┳┻┳┻┳┻┣╋┫'''┊┣━╋┫
┻┳┻┳┻╭╯╰╰-╭╯━╯.''╰╮
I Love You 💕
__New couple of the day may be chosen at 12AM {tomorrow}__"""
            await pbot.send_message(
                message.chat.id, text=couple_selection_message
            )
    except Exception as e:
        print(e)
        await message.reply_text(e)
__help__ = """    
@szrosebot🇱🇰
It's just a fun module for having little fun. 
**Couples**
❍ /couple: Choose a random couple of the day     
"""
__mod_name__ = "couple"      
             
__funtools__ = __help__        
