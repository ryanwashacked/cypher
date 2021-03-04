from flask import request
from bert_functions import answer_query
from flask_cors import CORS
from flask import jsonify
from flask_jwt import JWT, jwt_required
from werkzeug.security import safe_str_cmp
from user import User
from main import app


def authenticate(username, password):
    user = User.query.filter(User.username == username).first()
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    return User.query.filter(User.id == payload['identity']).first()


app.debug = True
app.config['SECRET_KEY'] = 'super-secret'
jwt = JWT(app, authenticate, identity)
CORS(app)

if __name__ == "__main__":
    app.run()


@app.route('/')
@jwt_required()
def get_answer():
    question = request.args.get('question')
    results = answer_query(question)

    return jsonify(results)
