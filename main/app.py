from flask import Flask, session, request, render_template, redirect
from datetime import datetime
from flask_wtf.csrf import CSRFProtect, generate_csrf, CSRFError

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = 'I wish I could fly'

@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return redirect('/')

@app.route('/')
def mainPage():
    csrf_token = generate_csrf()
    