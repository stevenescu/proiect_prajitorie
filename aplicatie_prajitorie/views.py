from django.shortcuts import render
from datetime import datetime, date
#import locale
from urllib.parse import urlparse
from django.http import HttpResponse

def index(request):
    ip_index = request.META.get('REMOTE_ADDR')                                    #preia adresa IP a vizitatorului paginii
    url_index = request.build_absolute_uri()                                      #preia adresa URL completa care e accesata
    accesare_index = Accesare(ip_client=ip_index, url=url_index, parametri=request.GET)
    
    test = Accesare(ip_client=ip_index, url=url_index, parametri=request.GET)
    print("test string url: ", test.string_url())
    print("test pagina: ", test.pagina())
    
    
    return HttpResponse("<html><h1>Artisan Roastery – Prăjitorie de cafea de specialitate</h1><html>"
                        "<html><p>Platforma web „Artisan Roastery” este un magazin online dedicat comercializării cafelei de specialitate proaspăt prăjite, precum și a echipamentelor de preparare. Aplicația va oferi utilizatorilor posibilitatea de a explora cafele de origine unică (Single Origin), filtrate după țara de origine, profilul de prăjire, metoda de procesare, notele aromatice și modul de măcinare.</p><html>")

def info(request):
    ip_info = request.META.get('REMOTE_ADDR')
    url_info = request.build_absolute_uri()
    accesare_info = Accesare(ip_client=ip_info, url=url_info, parametri=request.GET)
    
    data_ora = formateaza_data_ro(datetime.now())
    return HttpResponse(f'<!DOCTYPE html> <html lang="ro"> <head> <meta charset="UTF-8"> <title>Informații despre server</title> </head> <body> <h1>Informații despre server</h1> <section> <h2>Data și ora</h2> <p>{data_ora}</p> </section> </body> </html>')


zile_ro = ["Luni", "Marți", "Miercuri", "Joi", "Vineri", "Sâmbătă", "Duminică"]
luni_ro = ["", "Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie", "Iulie", "August", "Septembrie", "Octombrie", "Noiembrie", "Decembrie"]

def formateaza_data_ro(data_obiect):
    ziua_saptamanii = zile_ro[data_obiect.weekday()]
    ziua_lunii = data_obiect.day
    luna_anului = luni_ro[data_obiect.month]
    anul = data_obiect.year
    
    ora = f"{data_obiect.hour:02d}"
    minut = f"{data_obiect.minute:02d}"
    secunda = f"{data_obiect.second:02d}"
    
    return f"{ziua_saptamanii}, {ziua_lunii} {luna_anului} {anul}, ora {ora}:{minut}:{secunda}"

class Accesare:
    contor_id = 0                                                           #contorul care pune primul id 1 (Accesare.contor_id trebuie sa fie inainte lui self.id)
    def __init__(self, ip_client, url, parametri = None, data = None):      #am pus None la argumentele paramatri si data ca sa nu fiu nevoit sa le dau o valoare de fiecare data cand vreau sa creez un obiect nou de tip Accesare
        Accesare.contor_id += 1                                             #la fiecare apel incrementeaza cu 1
        
        #proprietatile constructorului        
        self.id = Accesare.contor_id
        self.ip_client = ip_client
        self.url = url
        self.parametri = parametri if parametri is not None else {}         #proprietatea parametri este setat ca sa completeze un dictionar gol daca nu ii trimit alta valorare
        self.data = data if data is not None else datetime.now()            #proprietatea data este setat la data curenta in cazul in care nu trimit alta valoare
    
    def lista_parametri(self):
        rezultat = []
        for nume_param, val_param in self.parametri.items():                #metoda items ia fiecare element din dictionarul cu parametri si pune numele in nume_param si valoarea in val_param
            valoare_noua = val_param if val_param else None                 #daca utilizatorul lasa goala valoarea in url, pune None in loc de sir gol ""
            rezultat.append((nume_param, valoare_noua))                     #aici este tuplul pe care nu il intelegeam; deci adauga pereche (nume_param, valoare_param) care reprezinta un tuplu
        return rezultat                                                     #rezultatul va fi lista de tupluri de forma [('nume1', 'valoare1), ('nume2', 'valoare2')]
    
    def string_url(self):
        return self.url                                                     #clasa Accesare retine deja url complet in self.url, doar il returnez aici

    def pagina(self):
        url_parsat = urlparse(self.url)
        cale = url_parsat.path
        prefix = "/aplicatie_prajitorie"
        if cale.startswith(prefix):
            cale = cale[len(prefix):]
        return cale if cale else "/"
    
        