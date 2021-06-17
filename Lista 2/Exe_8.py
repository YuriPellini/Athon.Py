'''******************************************
ATHON
Programa de Introdução a Linguagem Python
Disiplina: Lógica de Programação
Professor: Francisco Tesifom Munhoz
Data: Primeiro Semestre 2021
*********************************************
Atividade: Lista 2 (Ex 3)
Autor: Yuri Pellini
Data: 19 de Maio de 2021
Comentários:
******************************************'''

#Entrada
X=float(input("Coloque o tamanho do lado do triângulo em cm:"))
Y=float(input("Coloque o segundo valor:"))
Z=float(input("Coloque o último valor:"))
# Saida
if(X==Y and Y==Z):
    print("Isso é um triângulo equilátero")
else:
    if(X==Y or Y==Z or X==Z):
        print("Isso é um triângulo isósceles")
    else:
        print("Isso é um triângulo escaleno")