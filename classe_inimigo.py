import pygame as pg
import random

class Inimigo:
    def __init__(self, endereco_imagem):
        self.roupafeia = pg.image.load(endereco_imagem)

        self.roupafeia = pg.transform.scale(self.roupafeia, (80,80))
        self.pos_y_roupafeia = -10
    #criando um atributo
        self.pos_x_roupafeia = random.randint(150,720)
        self.velocidade = random.randint(1,2)

    #criando a mascara para utilizar na verf
        self.mascara = pg.mask.from_surface(self.roupafeia)


    def andar(self):
         self.pos_y_roupafeia = self.pos_y_roupafeia + self.velocidade

         if self.pos_y_roupafeia>900:
              self.voltar()


    def exibir(self,tela_do_jogo):tela_do_jogo.blit(self.roupafeia, (self.pos_x_roupafeia, self.pos_y_roupafeia))

    def voltar(self):
        self.pos_y_roupafeia = -100
        self.pos_x_roupafeia = random.randint(0,500)
        self.velocidade = random.randint(5,10)