import csv
from database import db
from question_answer import QuestionAnswer


def importTSVtoDB():
	print('Importing TSV to DB')
	with open('csv/questions_answers.tsv', newline = '') as f:
		reader = csv.reader(f, delimiter = '\t')
		for row in reader:
			question_answer = QuestionAnswer(question = row[0], answer = row[1], product = row[2])
			db.session.add(question_answer)
		db.session.commit()


importTSVtoDB()
