#!/usr/bin/python3
import requests, bs4

for i in range(1, 34):

    site = ("http://www.guiainvest.com.br/lista-acoes/default.aspx?listaacaopage=" + str(i))
    
    web=requests.get(site)
    websp=bs4.BeautifulSoup(web.content, 'lxml')
    
    now=websp.find_all('tr',class_='rgRow')
    now2=websp.find_all('tr',class_='rgAltRow')
    
    print("Página ", i," -----------------------------------")
    
    for link in now:
        
        if str(link).find('a')>0 and str(link).find('td'):
            
            Recebe = link.getText()
            Recebe2=str(Recebe).split('\n')
            print("--------------------------------------------------------")
            print (Recebe2[2],"\n")
            print ((Recebe2[3])[0:5],"\n")
            print ((Recebe2[3])[5:],"\n")
            
    for link2 in now2:
        
        if str(link2).find('a')>0 and str(link2).find('td'):
            
            Recebe00 = link2.getText()
            Recebe3=str(Recebe00).split('\n')
            print("--------------------------------------------------------")
            print (Recebe3[2],"\n")
            print ((Recebe3[3])[0:5],"\n")
            print ((Recebe3[3])[5:],"\n")
            