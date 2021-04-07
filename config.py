from os import environ
from dotenv import load_dotenv

load_dotenv()
TOKEN = environ.get("TOKEN")
WEATHER_TOKEN = environ.get("WEATHER_TOKEN")
