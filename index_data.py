from elasticsearch import Elasticsearch, helpers
import csv

es = Elasticsearch(host= 'localhost', port = 9200)

with open('datasets/candidates_locations.csv') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='el7_challenge')