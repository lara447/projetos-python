#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os
numeros = []  #recebe os números

for i in range (5): #pede os valores e repete a pergunta 
    numero = int(input("Digite o {}º valor:".format(i + 1)))
    numeros.append(numero)
print("Os números digitados foram:{}".format(numeros))

    
