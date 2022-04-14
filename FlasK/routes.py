from FlasK import app, api
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', items=api.first_data_as_dict)
