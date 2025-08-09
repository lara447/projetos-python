#Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = input("Digite o seu nome:")
    idade = int(input("Digite a sua idade:"))
    salário = int(input("Digite o seu salário:"))
    sexo = input("Digite o seu sexo 'f' ou 'm':")
    estado_civil = input("Digite seu Estado Civil('s', 'c', 'v', 'd'):")
    car = len(nome)
    if (car < 3):
        print("aaaa")
    else:
        print("bb")

