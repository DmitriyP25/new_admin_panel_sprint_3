import os
import backoff

from dotenv import load_dotenv

load_dotenv()

BACKOFF_CFG = {
    "wait_gen": backoff.expo,
    "exception": Exception,
    "max_tries": 30,
}

POSTGRES_DSN = {
    'dbname': os.environ.get('DB_NAME'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'host': os.environ.get('DB_HOST'),
    'port': os.environ.get('DB_PORT'),
    'options': os.environ.get('DB_OPTIONS'),
}

ELASTIC_PATH = f"http://{os.environ.get('ELASTIC_HOST')}:{os.environ.get('ELASTIC_PORT')}"

FILE = "./state.json"

INDEX = 'movies'

ITERSIZE = 200

TIME_SLEEP = 30
