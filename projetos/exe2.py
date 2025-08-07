#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa


valores = [] #armazena os valore


for i in range(10): #loop
    valor = int(input("Digite o {}º valor:".format(i+1)))
    valores.reverse() #inverte os valores
    
    valores.append(valor) #armazena 

print(valores)#mostra