#Exercício 3 – Zig Zag Colorido
#Faça um programa que desenhe um padrão em zig-zag:
#• O número de voltas pode ser fixo ou controlado por uma variável.
#• A cada troca de direção (zig ou zag), alterne a cor da linha.
#• Use lista de cores e estrutura de repetição.
import random
import turtle

t = turtle.Turtle()
valor = int(input("Digite a quantidade de zig zag:"))                       
cores = ['blue', 'orange', 'pink', 'yellow', 'purple', 'red', 'black']     # Sequencia de cores


t.pensize(3) 
t.speed(2)

t.penup()
t.goto(-380, 0)
t.pendown()

i = 0
t.right(45)

for i in range(valor):
    t.color(random.choice(cores)) # Puxa a bibliote random e pega uma das cores da variavel "cores"
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
turtle.done() # Finaliza
