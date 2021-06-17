'''******************************************
ATHON
Programa de Introdução a Linguagem Python
Disiplina: Lógica de Programação
Professor: Francisco Tesifom Munhoz
Data: Primeiro Semestre 2021
*********************************************
Atividade: Lista 2 (Ex 6)
Autor: Yuri Pellini
Data: 12 de Maio de 2021
Comentários:
******************************************'''

#Entrada
Idade=int(input("Digite sua idade:"))
# Saida
if(Idade <= 18):
    print("Você ainda é menor de idade")
else:
    if(Idade>=65):
        print("Você está na pior idade")
    else:
        print("Você está na flor da idade")