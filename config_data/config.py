from environs import Env

# Distance threshold in meters
DISTANCE_THRESHOLD = 100

env = Env()
env.read_env()

# Telegram bot token from BotFather
API_TOKEN = env("BOT_TOKEN")

# Admins list
ADMIN_IDS = env.list("ADMIN_IDS", subcast=int)

COLLEGE_LAT = env("COLLEGE_LAT")
COLLEGE_LON = env("COLLEGE_LON")

# Database settings
DB_URL = env("DB_URL")
# DB_PASSWORD = env("DB_PASSWORD")
# DB_NAME = env("DB_NAME")
# DB_HOST = env("DB_HOST")


# Timezone for datetime objects
TIMEZONE = "Asia/Almaty"
