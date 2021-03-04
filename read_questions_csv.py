import csv

questions = []
answers = []

with open('csv/questions_answers.tsv', newline='') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        questions.append(row[0])
        answers.append(row[1])

