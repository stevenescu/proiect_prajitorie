from django.shortcuts import render
from datetime import datetime, date
#import locale
from urllib.parse import urlparse
from django.http import HttpResponse

def index(request):
    return HttpResponse("<html><h1>Artisan Roastery – Prăjitorie de cafea de specialitate</h1><html>"
                        "<html><p>Platforma web „Artisan Roastery” este un magazin online dedicat comercializării cafelei de specialitate proaspăt prăjite, precum și a echipamentelor de preparare. Aplicația va oferi utilizatorilor posibilitatea de a explora cafele de origine unică (Single Origin), filtrate după țara de origine, profilul de prăjire, metoda de procesare, notele aromatice și modul de măcinare.</p><html>")



def info(request):
    return HttpResponse('<!DOCTYPE html> <html lang="ro"> <head> <meta charset="UTF-8"> <title>Informații despre server</title> </head> <body> <h1>Informații despre server</h1> </body></html>')