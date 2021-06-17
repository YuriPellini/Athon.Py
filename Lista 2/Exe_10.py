'''******************************************
ATHON
Programa de Introdução a Linguagem Python
Disiplina: Lógica de Programação
Professor: Francisco Tesifom Munhoz
Data: Primeiro Semestre 2021
*********************************************
Atividade: Lista 2 (Ex 10)
Autor: Yuri Pellini
Data: 19 de Maio de 2021
Comentários:
******************************************'''

#Entrada
Sal=float(input("Coloque seu salário: R$"))
#Processamento
G1=float(Sal*0.08)
G2=float(Sal*0.09)
G3=float(Sal*0.11)
# Saida
if(Sal<=1174.86):
    print("Você paga uma taxa INSS de 8% e o valor que deve-se pagar é de R$",G1)
else:
    if(Sal<=1958.10):
        print("Você paga uma taxa INSS de 9% e o valor que deve-se pagar é de R$",G2)
    else:
        if(Sal<=3916.20):
            print("Você paga uma taxa INSS de 11% e o valor que deve-se pagar é de R$",G3)
        else:
            print("Você paga uma taxa INSS fixa no valor de R$430.78")