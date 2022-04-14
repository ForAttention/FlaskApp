# REST API
from flask_restful import Resource, reqparse
from FlasK import api

"""
Faza testowa co do wyświetlania, co będziemy sobie printować na stronie
Nazwa strony jaka figuruje w URL
Będziemy sprawdzać czy działa serwer (kody http)
Która to była godzina
Błąd - jeśli wystąpi jakikolwik (try - exception)
"""

first_data_as_dict = {'URN_NAME': "www.mojastrona.pl",
                      "STATUS_CODE": 200,
                      "DATA_TIME": "costamcostam",
                      "ERROR_CODE": "Probelmy techniczne nie występują"}

good_news = reqparse.RequestParser()
good_news.add_argument("url_name", type=str, help="Nazwa strony w formacie URL")
good_news.add_argument("status_code", type=int, help="Kody http zwracane przez serwer")
good_news.add_argument("data_time", type=str, help="Godzina i dzień")
good_news.add_argument("error_code", type=str, help="Jeżeli wystąpią jakieś problemy z odpytywaniem strony lub z samym "
                                                    "połączeniem, możeliwe że sam program wyrzuci jakiś błąd - to "
                                                    "jest właśnie to")


class ApiREST(Resource):

    def get(self, name, test):
        return {"data": name, "test": test}

    def delt(self):
        pass


api.add_resource(ApiREST, "/apirest/<string:name>/<int:test>")
