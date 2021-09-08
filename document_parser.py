import pandas as pd
from search_function import findRelevantHits

data = pd.read_excel('input_files/SAMPLE_RFP.xlsx')
df = pd.DataFrame(data, columns = ['Question'])

related_questions = []
supported = []
answers = []
scores = []

for row in df['Question']:
    related_questions.append(next(iter(findRelevantHits(row) or []), None)[0])
    answers.append(next(iter(findRelevantHits(row) or []), None)[1])
    scores.append(next(iter(findRelevantHits(row) or []), None)[2])
    supported.append(next(iter(findRelevantHits(row) or []), None)[3])

df['Related_Questions'] = related_questions
df['Supported'] = supported
df['Explanation'] = answers
df['Score'] = scores

df.to_excel('input_files/SAMPLE_RFP_OUTPUT.xlsx')

print(df)
