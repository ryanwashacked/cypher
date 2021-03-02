import csv

questions = []
answers = []

with open('csv/questions_answers.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        questions.append(row[0])
        answers.append(row[1])

