# -*- coding: utf-8 -*-
"""
Created on Wed May 16 19:51:41 2018

@author: matheus
"""

from PIL import Image

import pytesseract as ocr

phrase = ocr.image_to_string(Image.open('teste.jpg'), lang='por')

print("\nValor Encontrado:\n\n"+phrase)

teste = (Lote + "\n" + Fabricação + "\n" + Validade)
#teste = ('LOTE: 560568\nDATA FAB: 05/18\nDATA VAL: 05/20')

print("\nValor Testado:\n\n"+teste+"\n\nO Resultado do teste foi:\n")

if (phrase == teste):
    print("Positivo")
  
else:
    print("Negativo")
        