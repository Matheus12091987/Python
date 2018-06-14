# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:25:39 2018

@author: matheus
"""

import cups

impressoras = []  #criação de uma lista
lista_impressoras = []

conn = cups.Connection ()
printers = conn.getPrinters ()

acumulador = 0

print("Área para seleção de impressora padrão do Sistema de Inspeção e Liberação de Produção\n\nImpressoras disponíveis!!!\n\n")

for printer in printers:
    impressoras = (printer, printers[printer]["device-uri"])
    print("[ " + str(acumulador) + " ] " + impressoras[0]) 
    lista_impressoras.append(impressoras[0])
    acumulador+=1
    
numero_impressora = int(input("Selecione qual impressora que utilizar(Apenas o Numero): "))

conn.printFile(lista_impressoras[numero_impressora], 'pdfReport.pdf', 'Eurofarma Laboratórios', {})