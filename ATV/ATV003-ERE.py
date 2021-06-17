'''******************************************
ATHON
Programa de Introdução a Linguagem Python
Disiplina: Lógica de Programação
Professor: Francisco Tesifom Munhoz
Data: Primeiro Semestre 2021
*********************************************
Atividade: ATV003-ERE
Autor: Yuri Pellini
Data: 12 de Maio de 2021
Comentários:
******************************************'''

#Entrada
Shora=float(input("Coloque o seu salário a hora:R$"))
Horat=float(input("Coloque o números de horas trabalhadas:"))
INSS=float(input("Coloque o indíce do INSS em %:"))
#Processamento
Sbruto=float(Shora*Horat)
Sliquido=float(Sbruto-Sbruto*INSS*0.01)
#Saida
print("Seu salário bruto é de R$",Sbruto)
print("Seu salário líquido é de R$:",Sliquido)