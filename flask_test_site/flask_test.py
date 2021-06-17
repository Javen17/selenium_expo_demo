from models.mock_db import MockDb
from flask import Flask
from flask import render_template

app = Flask(__name__)
#app.debug = True

@app.route('/')
def index():
    db_games = MockDb().db
    return render_template('main.html', games = db_games)

@app.route('/detail/<game_id>')
def detail(game_id):
    return render_template('detail.html', context= MockDb().db["games"][int(game_id)])

app.run()