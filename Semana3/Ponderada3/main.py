# from fastapi import FastAPI, Request, Body, Form
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from pydantic import BaseModel, Field, EmailStr
# from fastapi_sqlalchemy import db
# from fastapi_sqlalchemy import DBSessionMiddleware 

# app = FastAPI()

# templates = Jinja2Templates(directory="templates")

# class User(BaseModel):
#     id : int = Field(default=None, gt=0)
#     name: str = Field(default=None)
#     email: EmailStr = Field(default=None)
#     password: str = Field(default=None)

# app.add_middleware(DBSessionMiddleware, db_url="postgresql://postgres:password@localhost:5432/postgres")
# db.init_app(app)

# users = []

# @app.get('/', response_class=HTMLResponse)
# async def login(request: Request):
#     return templates.TemplateResponse('login.html', {"request": request})

# @app.post('/user_signup', response_class=HTMLResponse)
# async def user_signup(name:str=Form(...),email:str=Form(...),password:str=Form(...)):
#     user = User(name = name, email = email, password = password)
#     db.session.add(user)
#     db.session.commit()
#     return

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)

with app.app_context():
    db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/create_user')
def login():
    return render_template('create.html')

@app.route("/users")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template("list.html", users=users)

@app.route('/user_signup', methods=['POST'])
async def user_signup():
    user = User(name = request.form['name'], 
                email = request.form['email'], 
                password = request.form['password'])
    db.session.add(user)
    db.session.commit()
    return

if __name__ == '__main__':
    app.run(debug=True)