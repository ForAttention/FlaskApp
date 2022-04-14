from flask import Flask
from flask_restful import Api
app = Flask(__name__)
api = Api(app)

from FlasK import routes
from FlasK.api import ApiREST
