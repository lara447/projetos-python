#Faça um programa que leia 5 números e informe a soma e a média dos números.

valor = []

for i in range(5):
    valores = int(input(f"Digite o {i +1}º valor:"))
    valor.append(valores)
    soma = sum(valor)
    media = soma / 5

print(f"A soma dos números {valor} é de {soma} e a média é {media}")