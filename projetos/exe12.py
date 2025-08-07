valor = []
for i in range(5):
    valores = int(input(f'Digite o {i + 1}º valor:'))
    valor.append(valores)
maximo = max(valor)
print(maximo)