'''******************************************
ATHON
Programa de Introdução a Linguagem Python
Disiplina: Lógica de Programação
Professor: Francisco Tesifom Munhoz
Data: Primeiro Semestre 2021
*********************************************
Atividade: Lista 2 (Ex 9)
Autor: Yuri Pellini
Data: 19 de Maio de 2021
Comentários:
******************************************'''

#Entrada
â=float(input("Coloque o primeiro valor do ângulo do triângulo:"))
b=float(input("Coloque o segundo valor:"))
c=float(input("Coloque o último valor:"))
#Processamento
# Saida
if(â==90 or b==90 or c==90):
    print("Esse triângulo é retângulo")
else:
    if(â>90 or b>90 or c>90):
        print("Esse triângulo é obtusângulo")
    else:
        print("Esse triângulo é acutângulo")