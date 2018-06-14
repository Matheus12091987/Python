# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 20:01:54 2018

@author: matheus
"""
# Importar modulo do sistema operacional
import os
 
Lote = ("LOTE: "+input("Informe o numero do Lote: "))

Fabricação = ("DATA FAB: "+input("Informe a data de fabricação incluindo a "+"/"+": "))

Validade = ("DATA VAL: "+input("Informe a data de validade incluindo a "+"/"+": "))

os.system("python reconhecimento_de_imagem.py")