from flask import Flask, render_template, jsonify, request
from database.database import database

app = Flask(__name__)


@app.route('/')
def index():
    print(request.args)
    return render_template('index.html')
