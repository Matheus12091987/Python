# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 19:36:00 2018

@author: matheus
"""

import requests  #leitura do link
import bs4       #examinar o html do link
import sys       #acesso de sistema


print ("to aqui 1")
site = requests.get('http://www.guiainvest.com.br/lista-acoes/default.aspx')
print ("To aqui 2")
sitesp = bs4.BeautifulSoup(site.content, "lxml")
print ("Indo pro for")


for link in sitesp.find_all('tr'):
    
    if str(link).find('class') >= 0 and str(link).find('td') > 0:
        
        recebe = str(link).split('/td><td>')        
        
        print ("\n", recebe)