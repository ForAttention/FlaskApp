# REST API
from flask_restful import Resource, reqparse, fields, marshal_with, abort
from FlasK import api
from FlasK.modeles import GoodBase, WrongBase
from FlasK import db

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

apiinfo = reqparse.RequestParser()
apiinfo.add_argument("url_name", help="Nazwa strony w formacie URL", required=True, location='json')
apiinfo.add_argument("status_code", help="Kody http zwracane przez serwer", location='json')
apiinfo.add_argument("data_time", help="Godzina i dzień", required=True, location='json')
apiinfo.add_argument("error_code", help="Jeżeli wystąpią jakieś problemy z odpytywaniem strony lub z samym "
                                        "połączeniem, możeliwe że sam program wyrzuci jakiś błąd - to "
                                        "jest właśnie to", location='json')

resource_fields = {
    'id': fields.Integer,
    'url_name': fields.String,
    'status_code': fields.String,
    'data_time': fields.String,
    'error_code': fields.String
}


class ApiREST(Resource):
    """Myślę, że na tą pokazową aplikację wystarczy tylko put i patch
        put będzie pierwszy ponieważ patch będzie sie odnosił do put za kazdym razem kiedy
        rekord jakiś nie będzie istniał, stąd co prawda wiele linijek kodu w put-ie nie ma sensu skoro ma to tak działać
        ale jak bedzie kiedyś potrzeba robudowy tego, to mam na szczęście to już zrobione"""

    @marshal_with(resource_fields)
    def put(self, num):
        data = apiinfo.parse_args()
        result = GoodBase.query.filter_by(id=num).first()
        if result:
            abort(409, message="Rekord już istnieje o takim ID")
        typing_data = GoodBase(id=num,
                               url_name=data['url_name'],
                               status_code=data['status_code'],
                               data_time=data['data_time'],
                               error_code=data['error_code'])
        db.session.add(typing_data)
        db.session.commit()
        return 201

    @marshal_with(resource_fields)
    def patch(self, num):
        data = apiinfo.parse_args()
        result = GoodBase.query.filter_by(id=num).first()
        another_results = WrongBase.query.filter_by(url_name=data['url_name']).first()

        if another_results:
            """Jeśli jest rekord w złej bazie to trzeba go wyrzucić"""
            db.session.delete(another_results)

        if not result:
            ApiREST.put(self, num)
            abort(418, message='Nie da się aktualizować rekordu, który nie istnieje, przeniesione do put-a')
        if data['url_name']:
            result.url_name = data['url_name']
        if data['status_code']:
            result.status_code = data['status_code']
        if data['data_time']:
            result.data_time = data['data_time']
        if data['error_code']:
            result.error_code = data['error_code']

        db.session.commit()
        return 201

    def get(self, name, test):
        return {"data": name, "test": test}

    def delete(self):

        pass


class ApiWREST(Resource):
    """Myślę, że na tą pokazową aplikację wystarczy tylko put i patch
        put będzie pierwszy ponieważ patch będzie sie odnosił do put za kazdym razem kiedy
        rekord jakiś nie będzie istniał, stąd co prawda wiele linijek kodu w put-ie nie ma sensu skoro ma to tak działać
        ale jak bedzie kiedyś potrzeba robudowy tego, to mam na szczęście to już zrobione"""

    @marshal_with(resource_fields)
    def put(self, num):
        data = apiinfo.parse_args()
        result = WrongBase.query.filter_by(id=num).first()
        if result:
            abort(409, message="Rekord już istnieje o takim ID")
        typing_data = WrongBase(id=num,
                                url_name=data['url_name'],
                                status_code=data['status_code'],
                                data_time=data['data_time'],
                                error_code=data['error_code'])
        db.session.add(typing_data)
        db.session.commit()
        return 201

    @marshal_with(resource_fields)
    def patch(self, num):
        data = apiinfo.parse_args()
        result = WrongBase.query.filter_by(id=num).first()
        another_results = GoodBase.query.filter_by(url_name=data['url_name']).first()

        if another_results:
            """Jeśli jest rekord w dobrej bazie to trzeba go wyrzucić"""
            db.session.delete(another_results)

        if not result:
            ApiWREST.put(self, num)
            abort(418, message='Nie da się aktualizować rekordu, który nie istnieje, przeniesione do put-a')

        if data['url_name']:
            result.url_name = data['url_name']
        if data['status_code']:
            result.status_code = data['status_code']
        if data['data_time']:
            result.data_time = data['data_time']
        if data['error_code']:
            result.error_code = data['error_code']

        db.session.commit()
        return 201

    def get(self, name, test):
        return {"data": name, "test": test}

    def delete(self):
        pass


api.add_resource(ApiREST, "/apirest/apiv1/<int:num>")
api.add_resource(ApiWREST, "/apirest/apiv2/<int:num>")
