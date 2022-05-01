import csv
import logging

from elasticsearch import Elasticsearch, helpers

import settings

es = Elasticsearch(hosts="http://localhost:9200")


def load_csv_file_to_es():
    # Create the elasticsearch client.
    if es.indices.exists(index=settings.index_name):
        logging.info("Index already exists...skipping the loading step...")
        return
    # Open csv file and bulk upload
    with open(settings.csv_file) as f:
        reader = csv.DictReader(f)
        helpers.bulk(es, reader, index=settings.index_name)
    print("Successfully loaded the data into elasticsearch index - assam_river_tender")
