# -*- coding: utf-8 -*-
"""
Created on Wed May 30 08:49:32 2018

@author: matheus
"""

from fpdf import FPDF, HTMLMixin

resultadoA = "Aprovado"
resultadoB = "Aprovado"
resultadoC = "Aprovado"
resultadoD = "Aprovado"
resultadoFinal = "Lote Liberado para Produção"

html = ("""
	<p align="center"> 
	Eurofarma Laboratórios SA
	</p>
 
     <p align="center"> 
	Relatório de inicio de Produção
	</p> 
 
     <p align="left"> 
	Valor Procurado: """ + teste + """
	</p>

     <p align="left"> 
	Bolsa Posição A: """ + resultadoA + """
	</p>

     <p align="center">
	<img alt="html image example" src="teste.jpg" width="150" height="75">
	</p>      
     
     <p align="left"> 
	Bolsa Posição B: """ + resultadoB + """
	</p>

     <p align="center">
	<img alt="html image example" src="teste1.jpg" width="150" height="75">
	</p>  
 
     <p align="left"> 
	Bolsa Posição C: """ + resultadoC + """
	</p>
 
     <p align="center">
	<img alt="html image example" src="teste3.jpg" width="150" height="75">
	</p>
 
     <p align="left"> 
	Bolsa Posição D: """ + resultadoD + """
	</p>
 
     <p align="center">
	<img alt="html image example" src="teste2.jpg" width="150" height="75">
	</p>
 
     <p align="left"> 
	Avaliação Final: """ + resultadoFinal + """
	</p>
     
     <p></p><p></p>
          
     <p align="left"> 
	______________________                                                                              ______________________     
	</p>
     
     <p align="left"> 
	  Assinatura do Operador                                                                             Assinatura do Lider do Processo
	</p>
     
     """)

class MyFPDF(FPDF, HTMLMixin):
    pass
 
pdf=MyFPDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.write_html(html)
pdf.output('pdfReport.pdf','F')