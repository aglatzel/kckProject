from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats
import random

import csv
import pandas as pd

animals = [
["Alpaka","alpaka.jpg","https://pl.wikipedia.org/wiki/Alpaka_(zwierz%C4%99)"],
["Chomik","chomik.jpg","https://pl.wikipedia.org/wiki/Chomik"],
["Delfin","delfin.jpg","https://pl.wikipedia.org/wiki/Delfin"],
["Diabeł Tasmański","diabeł tasmański.jpg","https://pl.wikipedia.org/wiki/Diabe%C5%82_tasma%C5%84ski"],
["Flaming","flaming.jpg","https://pl.wikipedia.org/wiki/Flamingi"],
["Jeż","jeż.jpg","https://pl.wikipedia.org/wiki/Je%C5%BC"],
["Kameleon","kameleon.jpg","https://pl.wikipedia.org/wiki/Kameleonowate"],
["Kangur","kangur.jpg","https://pl.wikipedia.org/wiki/Kangur"],
["Kapibara","kapibara.jpg","https://pl.wikipedia.org/wiki/Kapibara"],
["Koala","koala.jpg","https://pl.wikipedia.org/wiki/Koala"],
["Kot","kotek.jpg","https://pl.wikipedia.org/wiki/Kot_domowy"],
["Koza","koza.jpg","https://pl.wikipedia.org/wiki/Koza_domowa"],
["Królik","królik.jpg","https://pl.wikipedia.org/wiki/Kr%C3%B3lik"],
["Lampart","lampart.jpg","https://pl.wikipedia.org/wiki/Lampart_(rodzaj_ssaka)"],
["Leniwiec","leniwiec.jpg","https://pl.wikipedia.org/wiki/Leniwce"],
["Lew","lew.jpg","https://pl.wikipedia.org/wiki/Lew_afryka%C5%84ski"],
["Lis","lis.jpg","https://pl.wikipedia.org/wiki/Lis"],
["Małpa","małpa.jpg","https://pl.wikipedia.org/wiki/Ma%C5%82pokszta%C5%82tne"],
["Niedźwiedź","niedzwiedz.jpg","https://pl.wikipedia.org/wiki/Nied%C5%BAwied%C5%BA"],
["Nietoperz","nietoperz.jpg","https://pl.wikipedia.org/wiki/Nietoperze"],
["Okapi","okapi.jpg","https://pl.wikipedia.org/wiki/Okapi_le%C5%9Bne"],
["Owca","owca.jpg","https://pl.wikipedia.org/wiki/Owca_domowa"],
["Panda","panda.jpg","https://pl.wikipedia.org/wiki/Panda_wielka"],
["Papuga","papuga.jpg","https://pl.wikipedia.org/wiki/Papugowe"],
["Pies","piesek.jpg","https://pl.wikipedia.org/wiki/Pies_domowy"],
["Pingwin","pingwin.jpg","https://pl.wikipedia.org/wiki/Pingwiny"],
["Rosomak","rosomak.jpg","https://pl.wikipedia.org/wiki/Rosomak_tundrowy"],
["Sarna","sarna.jpg","https://pl.wikipedia.org/wiki/Sarna"],
["Sowa","sowa.jpg","https://pl.wikipedia.org/wiki/Sowy"],
["Szynszyla","szynszyla.jpg","https://pl.wikipedia.org/wiki/Szynszyla"],
["Świnska Morska","świnka morska.jpg","https://pl.wikipedia.org/wiki/Kawia_domowa"],
["Tapir","tapir.jpg","https://pl.wikipedia.org/wiki/Tapir_ameryka%C5%84ski"],
["Tygrys","tygrys.jpg","https://pl.wikipedia.org/wiki/Tygrys_azjatycki"],
["Wąż","wąż.jpg","https://pl.wikipedia.org/wiki/W%C4%99%C5%BCe"],
["Wiewiórka","wiewiorka.jpg","https://pl.wikipedia.org/wiki/Wiewi%C3%B3rka_pospolita"],
["Wilk","wilk.jpg","https://pl.wikipedia.org/wiki/Wilk_szary"],
["Wombat","wombat.jpg","https://pl.wikipedia.org/wiki/Wombatowate"],
["Wydra","wydra.jpg","https://pl.wikipedia.org/wiki/Wydra_europejska"],
["Zebra","zebra.jpg","https://pl.wikipedia.org/wiki/Zebra"],
["Żyrafa","żyrafa.jpg","https://pl.wikipedia.org/wiki/%C5%BByrafa"],
]





def home(request):
    print('Home')
    return render(request, 'home.html')


def about(request):
    print('About')
    return render(request, 'about.html')

def send_name(request):
    print('Send_Name')
    context = {}
    if request.method == 'POST':
        animal = random.choice(animals)
        user_name = request.POST['name']
        context = {
        "user_name": user_name,
        "name": animal[0],
        "image": animal[1],
        "link": animal[2],
        }

    return render(request, 'send_name.html', context)

def r_xor_p(x, y, r_xor_p='r'):
    ''' Pearson's r or its p
    Depending of what you would like to get.
    '''
    r, p = stats.pearsonr(x, y)

    if r_xor_p == 'r':
        return r
    else:
        return p
