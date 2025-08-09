letras = 0

p = input("digite uma frase:")

for caractere in p:
    if caractere.isalpha():
         letras += 1

print(f"sua frase tem um total de {letras} letras")
       