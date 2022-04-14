# stąd nadajemy POSTy do aplikacji
import requests
import time

BASE = "http://127.0.0.1:5000/"
good_news = 'apirest/apiv1/'
wrong_news = 'apirest/apiv2/'

id = 9

dane = {'url_name': str("https://github.com/ForAttention"), 'status_code': str(200), 'data_time': str(time.ctime()), 'error_code': "none"}
danne = {'url_name': "asd", 'status_code': "ddd", 'data_time': str(time.ctime()), 'error_code': "none"}

response = requests.patch(BASE + wrong_news + "3", json=danne)
print(response.request)
print(response.status_code)
print(response.text)


first_data_as_dict = {'URN_NAME': "www.mojastrona.pl",
                      "STATUS_CODE": 200,
                      "DATA_TIME": "costamcostam",
                      "ERROR_CODE": "Probelmy techniczne nie występują"}
