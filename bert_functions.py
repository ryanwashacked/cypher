from bert_serving.client import BertClient
from read_questions_csv import questions, answers
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

bc = BertClient(ip='10.51.101.101', check_length=False)

q_embs = bc.encode(questions)
topk = 5

def answer_query(query):
    emb = bc.encode([query, "asfg"])[0].reshape((1, -1))
    similarities = [cosine_similarity(emb, x.reshape((1, -1))) for x in q_embs]
    most_similar = np.argmax(similarities)
    results = []
    score = np.sum(emb * q_embs, axis=1) / np.linalg.norm(q_embs, axis=1)
    topk_idx = np.argsort(score)[::-1][:topk]
    for idx in topk_idx:
        # print('> %s\t%s' % (score[idx], questions[idx]))
        results.append([questions[idx], answers[idx]])

    return results
