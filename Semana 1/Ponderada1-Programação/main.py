from typing import Union

from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def func():
    return render_template('index.html')

