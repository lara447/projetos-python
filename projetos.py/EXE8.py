#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma
#mensagem de erro e voltando a pedir as informações.
while True:
    pergunta = input("Digite o seu nome:")
    senha = input("Digite uma senha:")

    if(senha == pergunta):
        print("ERRO! DIGITE MA SENHA DIFERENTE DO SEU NOME.")
        break
        
    else:
        print("SENHA CRIADA")