import uuid


from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

MOVIES = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Saving Private Ryan',
        'director': 'Steven Spielberg',
        'starring': 'Tom Hanks, Matt Damon',
        'watched': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Goodfellas',
        'director': 'Martin Scorsese',
        'starring': 'Ray Liotta, Robert DeNiro, Joe Pesci',
        'watched': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Avengers: Infinity War',
        'director': 'Anthony Russo',
        'starring': 'Robert Downey Jr, Chris Hemsworth',
        'watched': False
    }
]


@app.route('/movies', methods=['GET', 'POST'])
def all_movies():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        MOVIES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'director': post_data.get('director'),
            'starring': post_data.get('starring'),
            'watched': post_data.get('watched')
        })
        response_object['message'] = 'Movie Added!'
    else:
        response_object['movies'] = MOVIES
    return jsonify(response_object)


@app.route('/movies/<movie_id>', methods=['PUT', 'DELETE'])
def single_movie(movie_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_movie(movie_id)
        MOVIES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'director': post_data.get('director'),
            'starring': post_data.get('starring'),
            'watched': post_data.get('watched')
        })
        response_object['message'] = 'Movie updated!'
    if request.method == 'DELETE':
        remove_movie()
        response_object['message'] = 'Movie removed!'
    return jsonify(response_object)


def remove_movie(movie_id):
    for movie in MOVIES:
        if movie['id'] == movie_id:
            MOVIES.remove(movie)
            return True
    return False


if __name__ == '__main__':
    app.run()