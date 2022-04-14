# modeles.py
from FlasK import db


"""
Przekopiowane z api file dla wglądu

Faza testowa co do wyświetlania, co będziemy sobie printować na stronie
Nazwa strony jaka figuruje w URL
Będziemy sprawdzać czy działa serwer (kody http)
Która to była godzina
Błąd - jeśli wystąpi jakikolwik (try - exception)


first_data_as_dict = {'URL_NAME': "www.mojastrona.pl",
                      "STATUS_CODE": 200,
                      "DATA_TIME": "costamcostam",
                      "ERROR_CODE": "Probelmy techniczne nie występują"}
                      """


class GoodBase(db.Model):
    """Jak dobrze znam programowanie w pythonie to warto dać nullable
        tylko dla url strony i dla daty, error code będzie pewnie w
        większości None a jak już pojawi się jakiś błąd to wtedy status code będzie None

        Podobnie jest zresztą w api file gdzie dane od url i data są required-True
        """

    id = db.Column(db.Integer, primary_key=True)
    url_name = db.Column(db.String, nullable=True)
    status_code = db.Column(db.Integer, nullable=False)
    data_time = db.Column(db.String, nullable=True)
    error_code = db.Column(db.String, nullable=False)


class WrongBase(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    url_name = db.Column(db.String, nullable=True)
    status_code = db.Column(db.Integer, nullable=False)
    data_time = db.Column(db.String, nullable=True)
    error_code = db.Column(db.String, nullable=False)


"""To tylko raz odpalamy jako konstruktor!"""
# db.create_all()

"""To jednak musi być na końcu, żeby utworzyc wszystkie tabele
    Często kasuje bazę i ją odtwarzam na nowo właśnie tą komendą
    Pracowałem jako tester, a to robiłem dla siebie w pracy (nikt nie podzielał mojego entuzjazmu)
    Najgorzej jest wywalić bazę jak już aplikacja znajduje się na serwerze
    Trzeba było wtedy widzieć minę kolegów devów z pokoju jak zacząlem się cieszyć że w końcu udało mi się
    wykasować bazę z serwera :D
    """
