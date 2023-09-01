from flask import Flask, render_template, request
from table import create_table, db
from models import User, Song

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres_felipe:postgres_felipe@localhost:5432/postgres_felipe"

db.init_app(app)

create_table(app)

# Home

@app.route('/')
def home():
    return render_template('login.html')

# User routes

@app.route('/user_signin', methods=['POST'])
def sign_in():
    email = request.form["email"]
    password = request.form["password"]

    user = User.query.filter_by(email=email).first()

    if password == user.password:
        return render_template('landingPage.html')

@app.route('/create_user')
def login():
    return render_template('create.html')

@app.route('/user_signup', methods=['POST'])
def user_signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    user = User(name=name, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return render_template('login.html')

# Song routes

@app.route("/song")
def user_list():
    songs = db.session.execute(db.select(Song).order_by(Song.name)).scalars()
    return render_template("songs.html", songs=songs)

@app.route('/song_add', methods=['POST'])
def song_addition():
    name = request.form['name']
    composer = request.form['composer']
    album = request.form['album']

    user = Song(name=name, composer=composer, album=album)
    db.session.add(user)
    db.session.commit()
    return 'foi'

if __name__ == '__main__':
    app.run(debug=True)