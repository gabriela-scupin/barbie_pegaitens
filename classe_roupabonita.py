import pygame as pg
import random

class Roupabonita:
    def __init__(self, endereco_imagem):
        self.roupabonita = pg.image.load(endereco_imagem)

        self.roupabonita = pg.transform.scale(self.roupabonita, (80,80))
        self.pos_y_roupabonita = -10
    #criando um atributo
        self.pos_x_roupabonita = random.randint(0,500)
        self.velocidade = random.randint(1,2)

    #criando a mascara para utilizar na verf
        self.mascara = pg.mask.from_surface(self.roupabonita)


    def andar(self):
         self.pos_y_roupabonita = self.pos_y_roupabonita + self.velocidade

         if self.pos_y_roupabonita>900:
              self.voltar()


    def exibir(self,tela_do_jogo):tela_do_jogo.blit(self.roupabonita, (self.pos_x_roupabonita, self.pos_y_roupabonita))

    def voltar(self):
        self.pos_y_roupabonita = -100
        self.pos_x_roupabonita = random.randint(0,500)
        self.velocidade = random.randint(5,10)