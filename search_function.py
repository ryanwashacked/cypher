from elasticsearch import Elasticsearch
from bert_serving.client import BertClient
import itertools

bc = BertClient(ip = '10.51.101.101', check_length = False)
es = Elasticsearch(['https://i-o-optimized-deployment-8791cf.es.eu-central-1.aws.cloud.es.io:9243'],
				   http_auth = ('elastic', 'EhF2kCmpiwPCYy3VDKBV0II0'))


def remove_duplicates_from_list(combined):
	ret = []
	checked = []
	for c in combined:
		if c[0] not in checked:
			ret.append(c)
			checked.append(c[0])
	return ret


def findRelevantHits(in_query):
	in_query_vector = bc.encode([in_query])[0].tolist()
	queries = {
		'bert': {
			"script_score": {
				"query": {
					"match_all": {}
				},
				"script": {
					"source": "cosineSimilarity(params.in_query_vector, doc['vector']) + 1.0",
					"params": {
						"in_query_vector": in_query_vector
					}
				}
			}
		},
		'search': {
			"match": {
				"question": in_query
			}
		},
		'mlt': {
			"more_like_this": {
				"fields": ["question"],
				"like": in_query,
				"min_term_freq": 1,
				"max_query_terms": 150,
				"min_doc_freq": 5
			}
		}
	}

	result = {'bert': [], 'mlt': [], 'search': []}

	for metric, query in queries.items():
		body = {"query": query, "size": 3, "_source": ["question", "answer", "supported", "category", "subcategory"]}
		response = es.search(index = 'questions_answers_vectors', body = body, request_timeout = 120)
		result[metric] = [[a['_source']['question'], a['_source']['answer'], a['_score'], a['_source']['supported'],
						   a['_source']['category'], a['_source']['subcategory']] for a in
						  response['hits']['hits']]

	combined_results = result['bert'] + result['search']
	combined_results = sorted(combined_results, key = lambda result_entry: result_entry[2], reverse = True)
	combined_results = list(combined_results for combined_results, _ in itertools.groupby(combined_results))
	combined_results = remove_duplicates_from_list(combined_results)

	return combined_results
