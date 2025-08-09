#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de
#cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
medias = []  # Lista para armazenar as médias


for aluno in range(10):
    soma_notas = 0  # Zera a soma das notas 

    # Pede 4 notas 
    for nota in range(4):
        valor = float(input("Digite a {}º nota do aluno {}: ".format(nota + 1, aluno + 1)))
        soma_notas += valor

    media = soma_notas / 4  # Calcula a média do aluno
    medias.append(media)    # Guarda a média na lista

# Conta os alunos com média maior ou igual a 7
contador_aprovados = 0

for media in medias:
    if media >= 7.0:
        contador_aprovados += 1

print('Número de alunos com média maior ou igual a 7.0: {}'.format(contador_aprovados))


