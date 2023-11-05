from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time, datetime


#input = kosten, output=lijst met autos onder deze prijs
# data nodig is, URL voor autos bij deze website lijst, onder bepaalde prijs, jouw prijs
#Systeem van data over deze autos opslaan, met html

#2 objecten, marktplaats en autoscout24
# input - query, locatie + type property + price range
 

"""
def testmarktplaats(paginaindex, prijsvancent,prijstotcent):
    for number in paginaindex:
        urlmarktplaats = 'https://www.marktplaats.nl/l/auto-s/p/'+str(number)+'/#PriceCentsFrom:'+str(prijsvancent)+'|PriceCentsTo:'+str(prijstotcent)
        print(urlmarktplaats)
        html_rauw = requests.get(urlmarktplaats).content
        html_ = BeautifulSoup(html_rauw, 'lxml')
        for link in html_.find_all('li'):

            if link.find(class_="mp-Listing-title") != None:
                print(link.find(class_="mp-Listing-title"))
                print(link.find(class_="mp-Listing-price mp-text-price-label"))
                print('www.marktplaats.nl/'+link.find(class_="mp-Listing-coverLink").get('href'))
        time.sleep(3)
                

testurl = 'https://www.marktplaats.nl/l/auto-s/p/2/#PriceCentsFrom:100000|PriceCentsTo:140000'
pgindx = [1,2,3,4]
testmarktplaats(pgindx,10000,14000)
"""


# input - query, locatie + type property + price range
def Facebook(paginaindex, prijsvancent,prijstotcent):
    file1 = open("auto_test", 'w')
    for number in paginaindex:
        urlautoscout = 'https://www.autoscout24.nl/lst?sort=standard&desc=0&atype=C&ustate=N%2CU&powertype=kw&pricefrom='+str(prijsvancent)+'&priceto='+str(prijstotcent)+'&search_id=1egt0h2adij&page='+str(number)
        print(urlautoscout)
        html_rauw = requests.get(urlautoscout).content
        html_ = BeautifulSoup(html_rauw, 'lxml')

        for link in html_.find_all('article'):

           print(link.get('data-make')+' '+link.get('data-model') + ' '+link.get('data-price'))
           print('https://www.autoscout24.nl'+link.find(class_='ListItem_title__znV2I Link_link__pjU1l').get('href'))
           file1.write(link.get('data-make')+' '+link.get('data-model')+','+link.get('data-price')+','+'https://www.autoscout24.nl'+link.find(class_='ListItem_title__znV2I Link_link__pjU1l').get('href'))
           file1.write('\n')
        

        time.sleep(3)

def Avito(paginaindex, prijsvancent,prijstotcent, plek):
    #https://www.avito.ma/fr/oujda/maisons_et_villas?price_min=50000&price_max=2000000
    #https://www.avito.ma/fr/sidi_yahya/maisons_et_villas/belle_maison__53854771.htm

    file1 = open("auto_test", 'w')
    for number in paginaindex:
        urlautoscout = 'https://www.autoscout24.nl/lst?sort=standard&desc=0&atype=C&ustate=N%2CU&powertype=kw&pricefrom='+str(prijsvancent)+'&priceto='+str(prijstotcent)+'&search_id=1egt0h2adij&page='+str(number)
        print(urlautoscout)
        urlautoscout = 'https://www.avito.ma/fr/'+str(plek)+'maisons_et_villas?price_min='+str(prijsvancent)+'&price_max='+str(prijstotcent)
        html_rauw = requests.get(urlautoscout).content
        html_ = BeautifulSoup(html_rauw, 'lxml')

        for link in html_.find_all('article'):

           print(link.get('data-make')+' '+link.get('data-model') + ' '+link.get('data-price'))
           print('https://www.autoscout24.nl'+link.find(class_='ListItem_title__znV2I Link_link__pjU1l').get('href'))
           file1.write(link.get('data-make')+' '+link.get('data-model')+','+link.get('data-price')+','+'https://www.autoscout24.nl'+link.find(class_='ListItem_title__znV2I Link_link__pjU1l').get('href'))
           file1.write('\n')
        

        time.sleep(3)
                
def Muwabab(paginaindex, prijsvancent,prijstotcent):
    file1 = open("auto_test", 'w')
    for number in paginaindex:
        urlautoscout = 'https://www.autoscout24.nl/lst?sort=standard&desc=0&atype=C&ustate=N%2CU&powertype=kw&pricefrom='+str(prijsvancent)+'&priceto='+str(prijstotcent)+'&search_id=1egt0h2adij&page='+str(number)
        print(urlautoscout)
        html_rauw = requests.get(urlautoscout).content
        html_ = BeautifulSoup(html_rauw, 'lxml')

        for link in html_.find_all('article'):

           print(link.get('data-make')+' '+link.get('data-model') + ' '+link.get('data-price'))
           print('https://www.autoscout24.nl'+link.find(class_='ListItem_title__znV2I Link_link__pjU1l').get('href'))
           file1.write(link.get('data-make')+' '+link.get('data-model')+','+link.get('data-price')+','+'https://www.autoscout24.nl'+link.find(class_='ListItem_title__znV2I Link_link__pjU1l').get('href'))
           file1.write('\n')
        

        time.sleep(3)

def Sarouty(paginaindex, prijsvancent,prijstotcent):
    file1 = open("auto_test", 'w')
    for number in paginaindex:
        urlautoscout = 'https://www.autoscout24.nl/lst?sort=standard&desc=0&atype=C&ustate=N%2CU&powertype=kw&pricefrom='+str(prijsvancent)+'&priceto='+str(prijstotcent)+'&search_id=1egt0h2adij&page='+str(number)
        print(urlautoscout)
        html_rauw = requests.get(urlautoscout).content
        html_ = BeautifulSoup(html_rauw, 'lxml')

        for link in html_.find_all('article'):

           print(link.get('data-make')+' '+link.get('data-model') + ' '+link.get('data-price'))
           print('https://www.autoscout24.nl'+link.find(class_='ListItem_title__znV2I Link_link__pjU1l').get('href'))
           file1.write(link.get('data-make')+' '+link.get('data-model')+','+link.get('data-price')+','+'https://www.autoscout24.nl'+link.find(class_='ListItem_title__znV2I Link_link__pjU1l').get('href'))
           file1.write('\n')
        

        time.sleep(3)

def pap(paginaindex, prijsvancent,prijstotcent):
    file1 = open("auto_test", 'w')
    for number in paginaindex:
        urlautoscout = 'https://www.autoscout24.nl/lst?sort=standard&desc=0&atype=C&ustate=N%2CU&powertype=kw&pricefrom='+str(prijsvancent)+'&priceto='+str(prijstotcent)+'&search_id=1egt0h2adij&page='+str(number)
        print(urlautoscout)
        html_rauw = requests.get(urlautoscout).content
        html_ = BeautifulSoup(html_rauw, 'lxml')

        for link in html_.find_all('article'):

           print(link.get('data-make')+' '+link.get('data-model') + ' '+link.get('data-price'))
           print('https://www.autoscout24.nl'+link.find(class_='ListItem_title__znV2I Link_link__pjU1l').get('href'))
           file1.write(link.get('data-make')+' '+link.get('data-model')+','+link.get('data-price')+','+'https://www.autoscout24.nl'+link.find(class_='ListItem_title__znV2I Link_link__pjU1l').get('href'))
           file1.write('\n')
        

        time.sleep(3)

def seloger(paginaindex, prijsvancent,prijstotcent):
    file1 = open("auto_test", 'w')
    for number in paginaindex:
        urlautoscout = 'https://www.autoscout24.nl/lst?sort=standard&desc=0&atype=C&ustate=N%2CU&powertype=kw&pricefrom='+str(prijsvancent)+'&priceto='+str(prijstotcent)+'&search_id=1egt0h2adij&page='+str(number)
        print(urlautoscout)
        html_rauw = requests.get(urlautoscout).content
        html_ = BeautifulSoup(html_rauw, 'lxml')

        for link in html_.find_all('article'):

           print(link.get('data-make')+' '+link.get('data-model') + ' '+link.get('data-price'))
           print('https://www.autoscout24.nl'+link.find(class_='ListItem_title__znV2I Link_link__pjU1l').get('href'))
           file1.write(link.get('data-make')+' '+link.get('data-model')+','+link.get('data-price')+','+'https://www.autoscout24.nl'+link.find(class_='ListItem_title__znV2I Link_link__pjU1l').get('href'))
           file1.write('\n')
        

        time.sleep(3)

def immomaroc(paginaindex, prijsvancent,prijstotcent):
    file1 = open("auto_test", 'w')
    for number in paginaindex:
        urlautoscout = 'https://www.autoscout24.nl/lst?sort=standard&desc=0&atype=C&ustate=N%2CU&powertype=kw&pricefrom='+str(prijsvancent)+'&priceto='+str(prijstotcent)+'&search_id=1egt0h2adij&page='+str(number)
        print(urlautoscout)
        html_rauw = requests.get(urlautoscout).content
        html_ = BeautifulSoup(html_rauw, 'lxml')

        for link in html_.find_all('article'):

           print(link.get('data-make')+' '+link.get('data-model') + ' '+link.get('data-price'))
           print('https://www.autoscout24.nl'+link.find(class_='ListItem_title__znV2I Link_link__pjU1l').get('href'))
           file1.write(link.get('data-make')+' '+link.get('data-model')+','+link.get('data-price')+','+'https://www.autoscout24.nl'+link.find(class_='ListItem_title__znV2I Link_link__pjU1l').get('href'))
           file1.write('\n')
        

        time.sleep(3)

#testurl = 'https://www.autoscout24.nl/lst?sort=standard&desc=0&atype=C&ustate=N%2CU&powertype=kw&pricefrom=1000&priceto=1500&search_id=1egt0h2adij&page=2'


pgindx = [1,2,3,4]
testautoscout(pgindx,1000,1400)



