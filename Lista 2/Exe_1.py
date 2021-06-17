'''******************************************
ATHON
Programa de Introdução a Linguagem Python
Disiplina: Lógica de Programação
Professor: Francisco Tesifom Munhoz
Data: Primeiro Semestre 2021
*********************************************
Atividade: Lista 2 (Ex 1)
Autor: Yuri Pellini
Data: 12 de Maio de 2021
Comentários:
******************************************'''

#Entrada
Idade=int(input("Digite sua idade:"))
#Processamento
Faltam=int(18 - Idade)
# Saida
if(Idade >= 18):
    print("Você é maior de idade.")
else:
    print("Ainda faltam",Faltam,"anos para sua maioridade.")