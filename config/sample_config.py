# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 2688530
API_HASH = "c5e9eb9ec6abb11a586b390c246ebeb3"

# Get this from @Botfather
TOKEN = "1404594390:AAGfCH2RHfdPQa4J9LKGhXvAIh-PYAwwylY"

# Your MongoDB URI (using a database named "vcpb"), if you don't provide, you can't use the playlist feature and wont see now playing message
MONGO_DB_URI = ""

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    1104666780,
    1294577077,
    1133402971
]

# The ID of the group where your bot streams
GROUP = -1001169043935

# Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
USERS_MUST_JOIN = False

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for user downloads in minutes
DUR_LIMIT = 5

# No need to touch the following.
LOG_GROUP = GROUP if MONGO_DB_URI != "" else None
SUDO_FILTER = filters.user(SUDO_USERS)
