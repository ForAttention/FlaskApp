## Opis trzeciego repozytorium
* [O aplikacji webowej flask](#O-aplikacji-webowej-flask)
* [O Programie](#O-programie)
* [Setup](#setup)

## O aplikacji webowej flask
Aplikacja webowa flask, miała ułatwić testowanie stron, sprawdzając w pętli wszytskie możliwe warianty koszykowe / rejestracji / logowania oraz dodtakowe rzeczy.
Znacznie ułatwiało mi to pracę, szczególnie jak napisałem osobne rubryki i model bazy, które wyświetlały mi błędy. Niestety nie wzbudziło to zainteresowania (sam podjąłem się pisania aplikacji).
Nie napisałem więc tego jako produktu dla firmy, tylko jako pomoc dla siebie, wszystkie wyniki testów przekierowywałem na moją stronę co dawało mi szybki podgląd na sytuację na produkcji po każdym updata / upgrade (firma posiadała ponad 450 stron).

Znakomicie sprawdzał się sposób na sprawdzaniu statusów HTTP stron i podstron. Napisałem program, który sprawdzał wszystkie podadresy strony, nawe te kryjące się za logiem sponsora jakiegoś wydarzenia (często źle był przypisany adres strony głównego sponsora i reklamodawcy):

```python
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
list1 = [...] # jest to lista już wyciągniętych stron ze strony głównej
x = "adres strony głównej"
baza = [...] # jest to lista stron, które są zapisywane już 'na stałe' *patrz końcówka programu
list2 = [...] # lista ta dostaje wszystkie adresy znalezione na jednej podstronie 
a = 0 # licznik
for url in list1:
    try:
        raz = requests.get(url)
    except Exception as ads:
        pass # tutaj dam pass, normalnie była wywoływana funkcja do 'wrong_base' 
    dwa = BeautifulSoup(raz.text, 'lxml')
    trzy = dwa.html.find_all('a')

    for data_1 in trzy:
        absolute_link = urljoin(url, data_1.get('href'))

        if str("\\") in absolute_link:
            # tutaj wyłapywałem podstony które w href="" miały backslash i go usówałem
            print(absolute_link)
            aaaa = absolute_link.replace('\\', '')
            absolute_link = aaaa # kończyły się pomysły na zmienne :/
            print("Nowy aboslute_link to: " + absolute_link)
        if x in str(absolute_link): 
            # sprawdzam czy wyciągnięty link z href zgadza się głównym URL 
            if str(absolute_link) in baza or str(absolute_link) in list1:
                # sprawdzam czy nie ma już wyciągniętego href'a w bazie i w liście 2
                continue
            else:
                # jeśli nie ma to dodajemy go do dwóch list
                baza.append(absolute_link)
                list2.append(absolute_link)
                print("Dodane do listy " + absolute_link)
        else:
            print("wykluczono URL", absolute_link)
            print("Loop number ", str(a))
            a += 1
            
        if len(list2) < 1:
            break
            
        del list1[:]
        
        for x in list2:
            list1.append(x)
            
        del list2[:]
        
        """
        Tutaj wyjaśnię trochę
        mamy 3 listy, lista 1 / 2 i baza
        z głównej strony zbieramy do listy 1 i do bazy
        potem z listy 1 zbieramy do bazy i listy 2 (sprawdzamy czy nie występuję takie same)
        potem kasujemy zawartość listy 1
        całą listę 2 przenosimy do listy 1 i czyścimy listę 2
        W ten sposób w pętli jesteśmy w stanie wyciągnąć wszystkie hrefy należące do strony xyz.pl
        Ponieważ mamy if'a który sprawdza czy wartość listy 2 jest mniejsza niż jeden
        """

```

Tak wygląda kod do wyciągania wszystkich podstron, później wszystkie sprawdzałem w takim sam sposób jak przykłądowy program, który napisałem do aplikacji.
Tutaj zaprezentowałem tylko ułamek mojej pracy, w grę wchodziło również:
* wyniki z testów zakupowych
* wyniki z logowania / rejestracji
* na aplikacji posiadałem też kod do wysyłania maila w danymi o znalezionym problemie 
* badałem zawartość stron (przez sumy znaków z source_page) i porównywałem 
* ilość grafik oraz innych plików (pdf, excel, mp4, ...)
* możliwość na stronie usuwania konkretnyh rekordów jak i ich archiwizacja (komunikacja po przez jQuery)


## O programie
Aplikacja Webowa została napisana według sztuki dla większych projektów, każdy 'moduł' posaida osobny plik.
Aplikacja skupia się głównie w odbieraniu danych json wysyłanych po API, api w aplikacji napisałem sam.
Folder FlasK posaida cały szkielet aplikacji, baza na git'cie jest pusta, możliwe jest tylko przesyłanie danych i ich przetrącanie z good_news do wrong_news.
W folderze głównym repo znajduje się jeszcze jeden folder ,,LocalSpy" - tam jest przykładowy program do relacji po API z aplikacją.
Aplikacja jest też cały czas na http://212.32.248.106/ LUB NA http://forattention.pl (jak na razie DNS jeszcze się nie przypisał, ale mam nadzieję że jednak ruszy).
Nagranie poniżej pokazuje jak wgrałem moją apliacjęn na serwer VPS, zależało mi na tym aby dało się wejść w nią bez żadnych przekierowań na porcie. Na filmmie pokazuje też, jak działa moja aplikacja.

Kliknij kwadrat aby przejść do filmu (nagrałem w jakości FullHD żeby było widać terminal ;) ) 

[![Film z pierwszego testu](https://antyweb.pl/img/781/440/fit/wp-content/uploads/2020/05/26104900/youtube3.jpg)](https://www.youtube.com/watch?v=ctMgM1LSc2Y "Deploy Flask Application")


## Setup
Aby zacząć pobierz repo z github
```shell
git clone https://github.com/ForAttention/FlaskApp.git
```

Aby uruchomić aplikację, przejdź do głównego folderu i uruchom plik frun.py

```shell
cd FlaskApp
python frun.py
```

Aplikacja uruchomi się na lokalnym adresie i domyślnym porcie: http://127.0.0.1:5000/

Żeby przesłać dane do aplikacji posłuż się plikiem w folderze LocalSpy.
Wykonaj poniższe komendy aby przejść i uruchomić plik do komunikacji z aplikacją

```shell
cd LocalSpy
python local_spy.py
```

Przejdź do aplikacji i odświeżaj stronę
