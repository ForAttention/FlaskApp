from FlasK import app
from flask import render_template
from FlasK.modeles import GoodBase, WrongBase


@app.route('/')
def index():
    good_list = GoodBase.query.all()
    wrong_list = WrongBase.query.all()
    return render_template('index.html', item=good_list, iten=wrong_list)
