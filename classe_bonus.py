import pygame
import random

class Item:

    def __init__(self,imagem):
        self.imagem = imagem
        
        self.pos_y = -200
        self.pos_x = random.randint(100, 850)

        self.velocidade_y = random.randint(3, 10)
        
        self.velocidade_x = 0 #Não tem velocidade horizontal, mas será utilizado para o poder magnetismo

        self.mascara = pygame.mask.from_surface(self.imagem)
    

    def movimenta(self):
        self.pos_y = self.pos_y + self.velocidade_y
        self.pos_x = self.pos_x + self.velocidade_x
        if self.pos_y > 700:
            self.voltar()

    def desenhar(self, tela):
        tela.blit(self.imagem,(self.pos_x,self.pos_y))    
        
    def voltar(self):
        self.pos_y = -200
        self.pos_x = random.randint(100, 850)
        self.velocidade_y = random.randint(3, 10)