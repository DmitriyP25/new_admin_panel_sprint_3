import time
from datetime import datetime

from elasticsearch import helpers

from config import ELASTIC_PATH, FILE, INDEX, ITERSIZE, TIME_SLEEP
from extract import data_generator, postgres_client, sql_command
from load import elastic_client, es_loader
from state import JsonFileStorage

state_file = JsonFileStorage(file_path=FILE)


if __name__ == "__main__":

    while True:

        last_modified = state_file.get_state(INDEX, default=str(datetime.min))
        sql = sql_command(last_modified)

        psql_cursor = postgres_client().cursor()
        psql_cursor.itersize = ITERSIZE
        psql_cursor.execute(sql)
        extracted_data = data_generator(psql_cursor)

        docs = es_loader(extracted_data)
        client = elastic_client(ELASTIC_PATH)

        lines, _ = helpers.bulk(
            client=client,
            actions=docs,
            index=INDEX,
        )

        time.sleep(TIME_SLEEP)
