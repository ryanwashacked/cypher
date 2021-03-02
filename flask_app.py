from flask import Flask, escape, request
from main import answer_query
from flask_cors import CORS
from flask import jsonify


app = Flask(__name__)
CORS(app)


@app.route('/')
def get_answer():
    question = request.args.get('question')
    results = answer_query(question)

    return jsonify(results)
