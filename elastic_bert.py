from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from bert_serving.client import BertClient
import csv

bc = BertClient(ip = '10.51.101.101', check_length = False)
es = Elasticsearch(['https://i-o-optimized-deployment-8791cf.es.eu-central-1.aws.cloud.es.io:9243'],
				   http_auth = ('elastic', 'EhF2kCmpiwPCYy3VDKBV0II0'))

es.indices.delete(index = 'questions_answers_vectors', ignore = [400, 404])

if not es.indices.exists(index = "questions_answers_vectors"):
	es.indices.create(index = 'questions_answers_vectors')

es.indices.put_mapping(index = 'questions_answers_vectors', body = {
	"properties": {
		"question": {"type": "text"},
		"answer": {"type": "text"},
		"vector": {"type": "dense_vector", "dims": 1024}
	}})


def getQuestionAnswerData():
	print('Getting embeddings')
	with open('csv/questions_answers.tsv', newline = '') as f:
		reader = csv.reader(f, delimiter = '\t')
		for row in reader:
			vector = bc.encode([row[0]])[0].tolist()
			yield {
				"_index": 'questions_answers_vectors',
				"question": row[0],
				"answer": row[1],
				"vector": vector
			}


bulk(client = es, actions = getQuestionAnswerData(), chunk_size = 1000, request_timeout = 120)
