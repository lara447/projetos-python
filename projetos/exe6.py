#faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20
#elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

valores_A = []
valores_B = []
valores_intercalados = []

for i in range(10):
    valor = int(input('Digite o {}º valor para o vetor A: '.format(i + 1)))   # Lendo os 10 valores do vetor A
    valores_A.append(valor)


for i in range(10):
    valor = int(input('Digite o {}º valor para o vetor B: '.format(i + 1)))   # Lendo os 10 valores do vetor B
    valores_B.append(valor)
for i in range(10):
    valores_intercalados.append(valores_A)          #intercala os valores
    valores_intercalados.append(valores_B)

print('Vetores intercalados:{}'.format(valores_intercalados))