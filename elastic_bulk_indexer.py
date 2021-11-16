import csv
import json
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient

es_client = Elasticsearch(
    "localhost:9200",
    http_auth=["elastic", "changeme"],
)


colums = ["id", "name", "price", "brand", "cpu", "memory", "storage"]
index_name = "laptops-demo"

with open("laptops_demo.csv", "r") as fi:
    reader = csv.DictReader(
        fi, fieldnames=colums, delimiter=",", quotechar='"'
    )

    # This skips the first row which is the header of the CSV file.
    next(reader)

    actions = []
    for row in reader:
        action = {"index": {"_index": index_name, "_id": int(row["id"])}}
        doc = {
            "id": int(row["id"]),
            "name": row["name"],
            "price": float(row["price"]),
            "brand": row["brand"],
            "attributes": [
                {"attribute_name": "cpu", "attribute_value": row["cpu"]},
                {"attribute_name": "memory", "attribute_value": row["memory"]},
                {
                    "attribute_name": "storage",
                    "attribute_value": row["storage"],
                },
            ],
        }
        actions.append(json.dumps(action))
        actions.append(json.dumps(doc))

    with open("laptops_demo.json", "w") as fo:
        fo.write("\n".join(actions))

    es_client.bulk(body="\n".join(actions))