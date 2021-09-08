from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from bert_serving.client import BertClient
import time
import csv

bc = BertClient(ip = '10.51.101.101', check_length = False)
es = Elasticsearch(['https://cypher.es.eu-central-1.aws.cloud.es.io:9243'],
				   http_auth = ('elastic', 'UVrF6kyW58KrBzxoffp2YRKH'))

es.indices.delete(index = 'questions_answers_vectors', ignore = [400, 404])

if not es.indices.exists(index = "questions_answers_vectors"):
	es.indices.create(index = 'questions_answers_vectors')

es.indices.put_mapping(index = 'questions_answers_vectors', body = {
	"properties": {
		"question": {"type": "text"},
		"answer": {"type": "text"},
		"product": {"type": "text"},
		"vector": {"type": "dense_vector", "dims": 1024}
	}})


def getQuestionAnswerData():
	start_time = time.time()
	print('Getting embeddings at %s' % start_time)
	with open('csv/questions_answers.tsv', newline = '') as f:
		reader = csv.reader(f, delimiter = '\t')
		for row in reader:
			vector = bc.encode([row[0]])[0].tolist()
			print('Getting embeddings for: %s' % row[0])
			yield {
				"_index": 'questions_answers_vectors',
				"question": row[0],
				"answer": row[1],
				"product": row[2],
				"supported": row[3] if 4 <= len(row) else '',
				"category": row[4] if 5 <= len(row) else '',
				"subcategory": row[5] if 6 <= len(row) else '',
				"vector": vector
			}
		print('Got embeddings in %s' % (time.time() - start_time))


bulk(client = es, actions = getQuestionAnswerData(), chunk_size = 1000, request_timeout = 120)
