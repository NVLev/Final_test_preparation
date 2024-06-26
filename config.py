from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv("API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# путь к базе данных
DB_PATH = "database.db"

# поддерживаемые команды
DEFAULT_COMMANDS = (
    ("newtask", "Создать задачу"),
    ("tasks", "Последние 10 задач"),
    ("today", "Задачи на сегодня"),
)
DATE_FORMAT = "%d.%m.%Y"