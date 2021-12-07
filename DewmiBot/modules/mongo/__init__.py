from motor.motor_asyncio import AsyncIOMotorClient as RoseMongoClient
from DewmiBot import MONGO_DB_URI

rosemongo = RoseMongoClient(MONGO_DB_URI)
rosedb = rosemongo.szrose

#Indexes for Plugins
coupledb = rosedb.couple
karmadb = rosedb.karma
nsfwdb = rosedb.nsfw
chatbotdb = rosedb.chatbot
torrentdb = rosedb.torrentdb
AIbotdb = rosedb.AIbotdb
