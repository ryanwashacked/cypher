from flask import request
from flask import jsonify
from flask_jwt import JWT, jwt_required
from werkzeug.security import safe_str_cmp
from user import User
from main import app
from search_function import findRelevantHits
import datetime

def authenticate(username, password):
    user = User.query.filter(User.username == username).first()
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    return User.query.filter(User.id == payload['identity']).first()


app.debug = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(hours = 1)

jwt = JWT(app, authenticate, identity)

if __name__ == "__main__":
    app.run()


@app.route('/')
@jwt_required()
def get_answer():
    question = request.args.get('question')
    results = findRelevantHits(question)

    return jsonify(results)
