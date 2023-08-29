import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OPENAI_KEY = config('OPENAI_KEY')
MONGODB_KEY = config('MONGODB_KEY')
