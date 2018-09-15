# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 20:05:14 2018

@author: matheus
"""

# importa modulo
from tkinter import *
 
# Cria formulario
formulario = Tk()
 
# Cria um variave de Texto.
 
##texto = "Desenvolvimento Aberto\nHello World\nTkinter!!!!"
# Cria um novo label
##rotulo = Label(formulario, text = texto)
 
# Retira espaço desocupado na janela
##rotulo.pack()
 
# Roda o loop principal do tcl
mainloop()

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 10
        self.sair.bind("<Button-1>", self.mudarTexto)
        self.sair.pack ()
        
        self.widget1 = tkinter.DoubleVar()
        self.widget1.set(1000.0)
        
    def mudarTexto(self, event):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"
root = Tk()
Application(root)
root.mainloop()