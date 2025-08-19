import random
import string 

def gerar_senha(tamanho = 12):
    caracteres = string.ascii_letters + string.punctuation + string.digits

    senha = "". join(random.choice(caracteres) for _ in range (tamanho))
    
    return senha 

tamanho = int(input("Digite qual o tamanho da senha : "))
print("Senha gerada:", gerar_senha(tamanho))