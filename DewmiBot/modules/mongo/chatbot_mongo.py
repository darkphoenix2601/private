from DewmiBot.modules.mongo import chatbotdb

async def is_chatbot_on(chat_id: int) -> bool:
    chat = chatbotdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def chatbot_on(chat_id: int):
    is_flood = await is_chatbot_on(chat_id)
    if is_flood:
        return
    return chatbotdb.insert_one({"chat_id": chat_id})


async def chatbot_off(chat_id: int):
    is_flood = await is_chatbot_on(chat_id)
    if not is_flood:
        return
    return chatbotdb.delete_one({"chat_id": chat_id})
