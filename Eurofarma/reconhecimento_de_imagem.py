# -*- coding: utf-8 -*-
"""
Created on Wed May 16 19:51:41 2018

@author: matheus
"""

from PIL import Image

import pytesseract as ocr
#import shutil

phrase = ocr.image_to_string(Image.open('teste.jpg'), lang='por')

print(phrase)

teste = ('LOTE: 560568\nDATA FAB: 05/18\nDATA VAL: 05/20')

print("\n"+teste+"\n")

if (phrase == teste):
    print("Deu certo")
  
else:
    print("Deu errado")
    
#shutil.copy(teste,"/dev/lp0")
    
        