# Exercício 5 – Controle com Teclado
# Faça um programa interativo onde o usuário possa mover a tartaruga usando o teclado:
# • Use as teclas Seta para cima, baixo, esquerda e direita.
# • A tartaruga deve se mover na direção pressionada, 20 pixels por vez.
# • Implemente as funções de movimento e associe-as aos eventos do teclado

import turtle

class turtle2:
    def __init__(self):
        self.screen = turtle.Screen()
        self.t = turtle.Turtle()

        self.screen.bgcolor("white")
        self.screen.setup(height=600, width=400)

        self.t.pensize(3)
        self.t.color("orange")
    
    def cima(self):
        self.t.setheading(90)
        self.t.forward(20)

    def baixo(self):
        self.t.setheading(270)
        self.t.forward(20)
    
    def lado_esquerdo(self):
        self.t.setheading(180)
        self.t.forward(20)

    def lado_direito(self):
        self.t.setheading(0)
        self.t.forward(20)

    def controle(self):
        self.screen.onkey(self.cima, "w")
        self.screen.onkey(self.baixo, "s")
        self.screen.onkey(self.lado_esquerdo, "a")
        self.screen.onkey(self.lado_direito, "d")
        self.screen.listen()

    def iniciar(self):
        turtle.done()

# Executando
recebe = turtle2()
recebe.controle()
recebe.iniciar()
