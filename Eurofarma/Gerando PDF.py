# -*- coding: utf-8 -*-
"""
Created on Wed May 30 08:49:32 2018

@author: Matheus Gonçalves Peres
"""

from fpdf import FPDF, HTMLMixin

resultadoA = "Aprovado"
resultadoB = "Aprovado"
resultadoC = "Aprovado"
resultadoD = "Aprovado"
resultadoFinal = "Lote Liberado para Produção"

html = ("""
<p align="right">Pagina 1 de 1</p>
<p  align="center"><font size="22">Eurofarma Laboratórios SA</font></p>
<p align="center"><font size="18">Relatório de Início de Produção</font></p>
<p><p></p></p>

<table border="0" align="left" width="97%">
<tr>
<td width="30%" align="left">Valor Procurado:</td>
<td width="70%">"""+Lote+"""</td>
</tr>
<tr>
<td width="30%" align="left"> </td>
<td width="70%">"""+Fabricação+"""</td>
</tr>
<tr>
<td width="30%" align="left"> </td>
<td width="70%">"""+Validade+"""</td>
</tr>
</table>


<table border="0" align="left" width="97%">
<tr>
<td width="70%" align="left">Bolsa Posição A: """ + resultadoA + """</td>
<td widht="30%"><img src="teste.jpg" width="150" height="75"></td>
</tr>
</table>

<table border="0" align="left" width="97%">
<tr>
<td width="70%" align="left">Bolsa Posição A: """ + resultadoB + """</td>
<td widht="30%"><img src="teste1.jpg" width="150" height="75"></td>
</tr>
</table>

<table border="0" align="left" width="97%">
<tr>
<td width="70%" align="left">Bolsa Posição A: """ + resultadoC + """</td>
<td widht="30%"><img src="teste3.jpg" width="150" height="75"></td>
</tr>
</table>

<table border="0" align="left" width="97%">
<tr>
<td width="70%" align="left">Bolsa Posição A: """ + resultadoD + """</td>
<td widht="30%"><img src="teste2.jpg" width="150" height="75"></td>
</tr>
</table>

<p align="left">Avaliação Final: """ + resultadoFinal + """</p>

<p align="left">	______________________                                                                              ______________________     </p>
<p align="left">	  Assinatura do Operador                                                                             Assinatura do Lider do Processo</p>""")


class MyFPDF(FPDF, HTMLMixin):
    pass
 
pdf=MyFPDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.write_html(html)
pdf.output(Lote+'data.pdf','F')