'''******************************************
ATHON
Programa de Introdução a Linguagem Python
Disiplina: Lógica de Programação
Professor: Francisco Tesifom Munhoz
Data: Primeiro Semestre 2021
*********************************************
Atividade: Lista 2 (Ex 2)
Autor: Yuri Pellini
Data: 12 de Maio de 2021
Comentários:
******************************************'''

#Entrada
Num_1=float(input("Digite o primeiro número:"))
Num_2=float(input("Digite o segundo número:"))
#Processamento
Soma=float(Num_1+Num_2)
# Saida
if(Soma < 10):
    print("O resultado é menor que 10.")
else:
    print("A soma resultou em:",Soma)