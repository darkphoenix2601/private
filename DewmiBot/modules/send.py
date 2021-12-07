from pyrogram import filters
from DewmiBot import pbot as rose
from DewmiBot.modules.helper_funcs.chat_status import adminsonly
from pyrogram.errors import RPCError

@rose.on_message(filters.command("send") & ~filters.channel)
@adminsonly
async def sendasrose(rose, message):
    chat_id = message.chat.id   
    if not message.reply_to_message and len(message.command) < 2:
        return await message.reply_text("Use /send with text or by replying to message.")
    if message.reply_to_message:
        if len(message.command) > 1:
            send = message.text.split(None, 1)[1]
            reply_id = message.reply_to_message.message_id
            return await rose.send_message(chat_id, 
                         text = send, 
                         reply_to_message_id=reply_id)
        else:
           return await message.reply_to_message.copy(chat_id) 
    else:
        await rose.send_message(chat_id, text=message.text.split(None, 1)[1])

@rose.on_message(filters.command("edit") & ~filters.edited & ~filters.bot)
@adminsonly
async def captionedit(_, message):
    if not message.reply_to_message or len(message.command) < 2:
        return await message.reply_text("Please reply to a media and send /edit with captions.")
    process = await message.reply("Processing....")
    cap = message.text.split(None, 1)[1]
    reply = message.reply_to_message
    try:
        await reply.copy(message.chat.id,caption=cap)
        await process.delete()
    except RPCError as i:
        await process.edit(i)
        return      
