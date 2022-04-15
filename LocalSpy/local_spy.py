# stąd nadajemy POSTy do aplikacji
import requests
import time

tabela_urlsow = ['https://www.gov.pl',
                 "https://overthewire.org/wargames/",
                 "https://www.hackthebox.com",
                 "https://stackoverflow.com",
                 "https://github.com/ForAttention",
                 "https://www.biedronka.pl/pl",
                 "https://www.freecodecamp.org",
                 "https://www.sololearn.com/home",
                 "https://docs.python.org/3/",
                 "https://selenium-python.readthedocs.io/api.html"]

BASE = "http://212.32.248.106/"
good_news = 'apirest/apiv1/'
wrong_news = 'apirest/apiv2/'

# dane = {'url_name': str("https://github.com/ForAttention"), 'status_code': str(200), 'data_time': str(time.ctime()), 'error_code': "none"}
# danne = {'url_name': "asd", 'status_code': "ddd", 'data_time': str(time.ctime()), 'error_code': "none"}
# response = requests.patch(BASE + wrong_news + "3", json=danne)
# print(response.request)
# print(response.status_code)
# print(response.text)


first_data_as_dict = {'URN_NAME': "www.mojastrona.pl",
                      "STATUS_CODE": 200,
                      "DATA_TIME": "costamcostam",
                      "ERROR_CODE": "Probelmy techniczne nie występują"}

while True:
    a = 0
    for url in tabela_urlsow:
        status_c = "none"
        error = "none"

        try:
            req_tru = requests.get(url)
        except Exception as error:
            dane = {'url_name': str(url), 'status_code': status_c,
                    'data_time': str(time.ctime()), 'error_code': str(error)}

            req = requests.patch(BASE + wrong_news + str(a), json=dane)
            continue

        status_c = req_tru.status_code
        if status_c != 200:
            dane = {'url_name': str(url), 'status_code': status_c,
                   'data_time': str(time.ctime()), 'error_code': str(error)}

            req = requests.patch(BASE + wrong_news + str(a), json=dane)
            continue
        dane = {'url_name': str(url), 'status_code': req_tru.status_code,
                'data_time': str(time.ctime()), 'error_code': error}

        req = requests.patch(BASE + good_news + str(a), json=dane)
        print(req.request)
        print(req.status_code)
        print(req.text)
        print(f"Loop number {a}")
        a += 1
