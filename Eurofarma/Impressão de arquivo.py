# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:25:39 2018

@author: matheus
"""

import sqlite3   # Importa o modulo Python que interfaceia com o gerenciador sqlite
 
import sys
import codecs
import os
import cups


conn= cups.Connection() #conecta com o cups
printers = conn.getPrinters () #obtem a lista de nomes de impressoras
nImp=0
for printer in printers: # mostra os elementos da lista
    strImp= str(nImp)
    ++nImp
    print ("(" + strImp + ")" + printer, printers[printer]["device-uri"])
    
    
strSelImp = input("Impressora: ")

printer_name= printers.keys()[int(strSelImp)]

conn.printFile(printer_name, 'pdfReport.pdf', 'pdfReport.pdf', {})
