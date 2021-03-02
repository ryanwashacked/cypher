from bert_serving.client import BertClient
from questions import questions, answers
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

bc = BertClient(ip='34.107.68.82', check_length=False)

q_embs = bc.encode(questions)


def answer_query(query):
    emb = bc.encode([query, "asfg"])[0].reshape((1, -1))
    similarities = [cosine_similarity(emb, x.reshape((1, -1))) for x in q_embs]
    most_similar = np.argmax(similarities)

    return [questions[most_similar], answers[most_similar]]
