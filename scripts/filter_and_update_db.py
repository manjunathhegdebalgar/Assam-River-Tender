import elasticsearch
from elasticsearch import Elasticsearch, helpers

import river_name_extractor
import settings


def update_proper_records():
    es = Elasticsearch(hosts="http://localhost:9200")

    positive_words = "((Flood) OR (flood) OR (Embankment) OR (embkt) OR (Relief) OR (Erosion) OR (SDRF) OR (River) OR (" \
                     "Inundation) OR (Hydrology) OR (Silt) OR (Siltation) OR (Bund) OR " \
                     "(Trench) OR (Drain) OR (Culvert) OR (Sluice) OR (Bridge) OR (Dyke) OR (Storm water drain))"
    negative_words = "((Driver) OR (Floodlight) OR (Flood Light))"

    body = {
        "query": {
            "query_string": {
                "query": positive_words + "AND NOT" + negative_words,
                "default_field": "tender/title"
            }
        }
    }
    results = elasticsearch.helpers.scan(es, query=body, index=settings.index_name)
    updated_count = 0
    for result in results:
        response = dict(result['_source'])
        river_name = river_name_extractor.get_river_name(response.get('tender/title'))
        if (len(river_name) != 0):
            updated_count += 1
        body = {
            'doc': {
                'river/name': river_name}
        }
        es.update(index=settings.index_name, body=body, id=result['_id'])
    print("updated ", updated_count, " records")
