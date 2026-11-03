from django.shortcuts import render
from datetime import datetime, date
#import locale
from urllib.parse import urlparse
from django.http import HttpResponse

def index(request):
    return HttpResponse("<html><h1>Artisan Roastery – Prăjitorie de cafea de specialitate</h1><html>"
                        "<html><p>Platforma web „Artisan Roastery” este un magazin online dedicat comercializării cafelei de specialitate proaspăt prăjite, precum și a echipamentelor de preparare. Aplicația va oferi utilizatorilor posibilitatea de a explora cafele de origine unică (Single Origin), filtrate după țara de origine, profilul de prăjire, metoda de procesare, notele aromatice și modul de măcinare.</p><html>")

def info(request):
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