from typing import Mapping
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
from mappings import configurations



es_client = Elasticsearch(
    "localhost:9200",
    http_auth=["elastic", "changeme"],
)

es_index_client = IndicesClient(es_client)


#es_index_client.create(index="laptops-demo", body=configurations)

#create alias
es_index_client.put_alias(index="laptops-demo", name="laptops")

#pull alias
es_index_client.get_alias(index="laptops-demo")


print(es_index_client.get_alias(index="laptops", allow_no_indices=True, ignore_unavailable=True))


##add documents to index

#doc = {
#    "id": 1,
#    "name": "HP EliteBook 820 G2",
#    "brand": "HP",
#    "price": 38842.00,
#    "attributes": [
#        {"attribute_name": "cpu", "attribute_value": "Intel Core i7-5500U"},
#        {"attribute_name": "memory", "attribute_value": "8GB"},
#        {"attribute_name": "storage", "attribute_value": "256GB"},
#    ],
#}


#es_client.index(index="laptops-demo", id=1, body=doc)

#search index

search_query = {
    "query": {
        "match": {
        "name.ngrams": "Appl"
        }
    }
}
print(es_client.search(index="laptops-demo", body=search_query))
