#Jogo de Adivinhação → O computador escolhe um número aleatório e o usuário tenta adivinhar.

import random
tentativas = 0
valores = random.randint (1,10)


while True:
    p = int(input("Digite um número de 1 até 10: "))
    if valores == p:
        print("Você adivinhou!!!!")
        break
    else:
        print("Você perdeu, tente novamente.")
tentativas += 1
    