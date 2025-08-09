#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
#população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
#número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de
#crescimento.


populacao_a = 80000           #população 
populacao_b = 200000

taxa_de_a = 0.03
taxa_de_b = 0.015                #taxa de crscimento 

anos = 0 

while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_de_a    
    populacao_b += populacao_b * taxa_de_b
    anos += 1
print("Levará {} para que  a população do país A ultrapasse ou iguale a população do país B ".format(anos))   