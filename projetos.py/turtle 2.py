import turtle
import random

t = turtle.Turtle()

def cor_aleatoria():
    return random.choice(["red", "green", "blue", "black", "yellow", "pink"])

def posicao_aleatoria():
    return random.randint(-300, 300), random.randint(-300, 300)

quantidade = int(input("Digite a quantidade de quadrados: "))
lados = int(input("Digite o tamanho dos lados: "))

def desenhar_quadrado(t, lados):
    t.color(cor_aleatoria())
    t.penup()
    t.goto(posicao_aleatoria())
    t.pendown()
    
    for _ in range(4):
        t.forward(lados)
        t.right(90)

for _ in range(quantidade):
    desenhar_quadrado(t, lados)

turtle.done()
