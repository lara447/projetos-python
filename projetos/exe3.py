#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares
#no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

impares = [] #armazena 
pares = []
for i in range (20):
    valor = int(input("Digite o {}º valor:".format(i+1)))

    if valor % 2 == 0:
        pares.append(valor)     #separa os valores
    else:
        impares.append(valor)

print('Valores pares:{}'.format(pares))   #mostra os valores separados
print('Valores impares:{}'.format(impares))