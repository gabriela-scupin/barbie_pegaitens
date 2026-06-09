import pygame as pg
from caminho_relativo import resource_path as rp

class Jogador:
    def __init__(self):
        self.imagem = pg.image.load(rp("scr/barbiebailarina.png"))
        self.imagem = pg.transform.scale(self.imagem,(60,100))