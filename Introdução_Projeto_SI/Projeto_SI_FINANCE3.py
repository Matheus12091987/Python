#!/usr/bin/python3
import requests, bs4
file=open('tabgeral.csv','w')
for i in range(65, 92):

    site = ("https://br.advfn.com/bolsa-de-valores/bovespa/" + str(chr(i)))
    print (site)
    web=requests.get(site)
    websp=bs4.BeautifulSoup(web.content, 'lxml')
    x=[]
    y=[]
    
    now=websp.find_all('td' ,class_='String Column1')
    now2=websp.find_all('td',class_='String Column2 ColumnLast')
    
    #print("Página ", i," -----------------------------------")
    
    for link in now:
        x.append(link.getText())
    for link2 in now2:
        y.append(link2.getText())
    #print(x)
    n=0
    for math in x:
        file.write ((str(x[n])+'\t'+str(y[n]))+"\n")
        n+=1
        
        #if str(link).find('a')>0 and str(link).find('td'):
            
        #Recebe = link.getText()
            #Recebe2=str(Recebe).split('\n')
            #print("--------------------------------------------------------")
            #print (Recebe2[2],"\n")
            #print ((Recebe2[3])[0:5],"\n")
            #print ((Recebe2[3])[5:],"\n")'''
        #print(Recebe)
            
    
        
        
        #if str(link2).find('a')>0 and str(link2).find('td'):
            
         #   Recebe00 = link2.getText()
         #   '''Recebe3=str(Recebe00).split('\n')
          #  print("--------------------------------------------------------")
           # print (Recebe3[2],"\n")
            #print ((Recebe3[3])[0:5],"\n")
            #print ((Recebe3[3])[5:],"\n")'''
          #  print(Recebe00)"""
            