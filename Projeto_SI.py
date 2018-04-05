# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 19:36:00 2018

@author: matheus
"""

import requests  #leitura do link
import bs4       #examinar o html do link
import sys       #acesso de sistema

##############################################################################
## Area das funções definidas                                               ##
##############################################################################
def examina_link(store):
    sitio = requests.get(store)
    s = bs4.BeautifulSoup(sitio.content, "lxml")
    for link in s.find_all("a"):
        if str(link.get('href')).find('=.epub')!=-1:
            file = open('livro_lelivros','a')
            file.write (str(link.get('href'))+'\n')
            file.close()
##############################################################################
## Rotina principal                                                         ##
##############################################################################
arq = open('links_lelivro','w')         #Abertura de um arquivo de escrita 'w'
file = open('livro_lelivros','w')      #Abertura de um arquivo de escrita 'w'
ant = 0         #Zerando a variavel ant

x = int(input("Qual é o numero de paginas que voce quer examinar? "))

for i in range(x):
    site = requests.get('http://lelivros.love/page/'+str(i)+'/')
    sitesp = bs4.BeautifulSoup(site.content, "lxml")
    for link in sitesp.find_all("a"):
        if len(str(link.get('href')))>65:
            atual = link.get('href')
            if atual != ant:
                arq.write (str(link.get('href'))+'\n')
                ant = atual
                examina_link(str(link.get('href')))
    arq.write('Pagina '+str(i+1)+ '\n')
arq.close()

