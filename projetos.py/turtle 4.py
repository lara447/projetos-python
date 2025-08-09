# Exercício 4 – Animação com Círculos Crescentes
# Desenvolva uma pequena animação com turtle que desenhe círculos que vão crescendo:
# • Pergunte ao usuário quantos círculos quer desenhar.
# • Solicite um tempo de espera entre um círculo e outro (em segundos).
# • A cada iteração, desenhe um novo círculo maior que o anterior, centralizado na tela

import turtle
import time
soma = 0
t = turtle.Turtle()
valor = int(input("Digite a quantidade de circulos:"))                       

t.pensize(3) 
t.speed(2)

raio_inicial = 20
raio_aumentado = 20
for i in range(valor):
    t.penup()
    t.goto(0, -raio_inicial - i * raio_aumentado)
    t.pendown()
    t.circle(raio_inicial + i * raio_aumentado)
turtle.done()