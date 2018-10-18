from flask import Flask, jsonify
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
        'title': 'Saving Private Ryan',
        'director': 'Steven Spielberg',
        'starring': 'Tom Hanks, Matt Damon',
        'watched': True
    },
    {
        'title': 'Goodfellas',
        'director': 'Martin Scorsese',
        'starring': 'Ray Liotta, Robert DeNiro, Joe Pesci',
        'watched': True
    },
    {
        'title': 'Avengers: Infinity War',
        'director': 'Anthony Russo',
        'starring': 'Robert Downey Jr, Chris Hemsworth',
        'watched': False
    }
]


# check route
@app.route('/movies', methods=['GET'])
def all_movies():
    return jsonify({
        'status': 'success',
        'movies': MOVIES
    })


if __name__ == '__main__':
    app.run()