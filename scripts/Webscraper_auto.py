from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time, datetime


#input = kosten, output=lijst met autos onder deze prijs
# data nodig is, URL voor autos bij deze website lijst, onder bepaalde prijs, jouw prijs
#Systeem van data over deze autos opslaan, met html

#2 objecten, marktplaats en autoscout24
 

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


def testautoscout(paginaindex, prijsvancent,prijstotcent):
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
                

testurl = 'https://www.autoscout24.nl/lst?sort=standard&desc=0&atype=C&ustate=N%2CU&powertype=kw&pricefrom=1000&priceto=1500&search_id=1egt0h2adij&page=2'
pgindx = [1,2,3,4]
testautoscout(pgindx,1000,1400)



