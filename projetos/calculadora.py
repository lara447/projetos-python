n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))
operador = input("Digite o operador (/, *, -, +):")

if operador == "/":
    print("Resultado:", n1 / n2)
elif operador == "+":
    print("Resultado:", n1 + n2)
elif operador == "-":
    print("Resultado", n1 - n2)
elif operador == "*":
    print("Resultado:", n1 * n2)
else:
    print("Digite um operador válido!")