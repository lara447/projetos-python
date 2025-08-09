import turtle

# Pergunta ao usuário se deseja desenhar quadrado ou retângulo
escolha = input("Desenhar quadrado (1) ou retângulo (2)? ").strip().lower()

if escolha == '1':
    lado = int(input("Informe o lado do quadrado: "))
    for _ in range(4):
        turtle.forward(lado)
        turtle.right(90)

elif escolha == '2':
    lado1 = int(input("Informe o lado 1 do retângulo: "))
    lado2 = int(input("Informe o lado 2 do retângulo: "))
    for _ in range(2):
        turtle.forward(lado1)
        turtle.right(90)
        turtle.forward(lado2)
        turtle.right(90)

else:
    print("Escolha inválida!")

turtle.done()
