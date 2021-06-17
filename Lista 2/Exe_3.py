'''******************************************
ATHON
Programa de Introdução a Linguagem Python
Disiplina: Lógica de Programação
Professor: Francisco Tesifom Munhoz
Data: Primeiro Semestre 2021
*********************************************
Atividade: Lista 2 (Ex 3)
Autor: Yuri Pellini
Data: 12 de Maio de 2021
Comentários:
******************************************'''

#Entrada
Salário=float(input("Coloque seu salário:R$"))
Prest=float(input("Coloque o valor da prestação:R$"))
#Processamento
vinte=float(Salário/5)
# Saida
if(Salário<=vinte):
    print("Empréstimo  não  pode  ser concedido!")
else:
    print("Empréstimo  pode  ser concedido!")