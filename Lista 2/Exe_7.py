'''******************************************
ATHON
Programa de Introdução a Linguagem Python
Disiplina: Lógica de Programação
Professor: Francisco Tesifom Munhoz
Data: Primeiro Semestre 2021
*********************************************
Atividade: Lista 2 (Ex 7)
Autor: Yuri Pellini
Data: 12 de Maio de 2021
Comentários:
******************************************'''

#Entrada
Peso=float(input("Coloque seu peso em Kg:"))
Altura=float(input("Coloque sua altura em metros:"))
#Processamento
IMC=float(Peso/(Altura*Altura))
# Saida
print("Seu IMC é:",IMC)
if(IMC<18.5):
    print("Abaixo do peso normal.")
else:
    if(18.5<=IMC and IMC<=25):
        print("Peso normal.")
    else:
        if(IMC>25 and IMC<=30):
            print("Acima do peso normal.")
        else:
            print("Obesidade")