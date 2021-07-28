import pandas as pd
from search_function import findRelevantHits

data = pd.read_excel('input_files/SAMPLE_RFP.xlsx')
df = pd.DataFrame(data, columns = ['Question'])

answers = []
scores = []
for row in df['Question']:
    answers.append(next(iter(findRelevantHits(row) or []), None)[1])
    scores.append(next(iter(findRelevantHits(row) or []), None)[2])

df['Answer'] = answers
df['Score'] = scores

df.to_excel('input_files/SAMPLE_RFP_OUTPUT.xlsx')

print(df)
