from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from fastapi.middleware.cors import CORSMiddleware
from database.db_scripts import schemes, models, crud

SQLALCHEMY_DATABASE_URL = "sqlite:///database/ponderada.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configure CORS to allow requests to the external URL
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://172.25.109.194:8501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def landing_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# login

@app.get("/user_login_page", response_class=HTMLResponse)
def user_login_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/user_signin", response_class=HTMLResponse)
def user_signin(request: Request, username: str = Form(...), password: str = Form(...)):
    db_password = crud.get_user_password(db, username=username)[0]
    if (not db_password) or (db_password != password):
        print('db_password: ', db_password, 'password: ', password)
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return templates.TemplateResponse("landing_page.html", {"request": request})   
    
# create user

@app.get("/user_create_page", response_class=HTMLResponse)
def user_create_page(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

@app.post("/user_signup")
def user_create(request: Request, username: str = Form(...), password: str = Form(...)):
    user = schemes.UserCreate(username=username, password=password)
    db_user = crud.get_user_by_username(db, username=username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    else:
        crud.create_user(db=db, user=user)
        return templates.TemplateResponse("index.html", {"request": request})