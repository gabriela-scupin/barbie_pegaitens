import pygame as pg
from caminho_relativo import resource_path as rp

class Jogador:
    def __init__(self):
        self.imagem = pg.image.load(rp("scr/barbiebailarina.png"))
        self.imagem = pg.transform.scale(self.imagem,(120,200))

        self.pos_x = 800
        self.pos_y = 520

        self.som1 = pg.mixer.Sound(rp("sound/som1.mp3"))
        self.som2 = pg.mixer.Sound(rp("sound/som2.mp3"))
        self.som3 = pg.mixer.Sound(rp("sound/som3.mp3"))
        self.som4 = pg.mixer.Sound(rp("sound/som4.mp3"))

    def andar(self, teclas_pressionadas):
      #verifico se a tecla da direita está pressionada
        if teclas_pressionadas[pg.K_RIGHT]:
            self.pos_x=self.pos_x + 5
        elif teclas_pressionadas[pg.K_LEFT]:
            self.pos_x=self.pos_x - 5

        # Limites
        if self.pos_x < 0:
            self.pos_x = 0

        if self.pos_x > 1080:
            self.pos_x = 1080



    def exibir(self,tela_do_jogo):
        tela_do_jogo.blit(self.imagem, (self.pos_x, self.pos_y))

        #criando a mascara para utilizar na verf
        self.mascara = pg.mask.from_surface(self.imagem)

    def voltar(self):
        self.pos_x = 800
        self.pos_y = 520

    def  gritar(self):
        self.som1.play()
    
    def perder(self):
        self.som3.play()

    def ganhar(self):
        self.som2.play()

    def pontos(self):
        self.som4.play()
