#importando pygame e colocando apelido
import pygame as pg

from caminho_relativo import resource_path as rp

pg.init() #inicializa os módulos básicos do pygame

clock = pg.time.Clock()

#criando a tela
tela = pg.display.set_mode((1200,900))

#configurando a tela
pg.display.set_caption("Feito por: Gabriela Scupin")

#carregando imagens
tela_inicial = pg.image.load(rp("scr/tela_inicial.png"))
barbie = pg.image.load(rp("scr/barbiebailarina.png"))
roupabonita1 = pg.image.load(rp("scr/roupabonita1.PNG"))
roupabonita2 = pg.image.load(rp("scr/roupabonita2.PNG"))
roupabonita3 = pg.image.load(rp("scr/roupabonita3.PNG"))
roupabonita4 = pg.image.load(rp("scr/roupabonita4.PNG"))
roupabonita5 = pg.image.load(rp("scr/roupabonita5.PNG"))
roupabonita6 = pg.image.load(rp("scr/roupabonita6.PNG"))
roupabonita7 = pg.image.load(rp("scr/roupabonita7.PNG"))
roupabonita8 = pg.image.load(rp("scr/roupabonita8.PNG"))
roupafeia = pg.image.load(rp("scr/roupafeia-removebg.png"))
roupafeia2 = pg.image.load(rp("scr/roupafeia2-removebg.png"))
roupafeia3 = pg.image.load(rp("scr/roupafeia3-removebg.png"))
fundo = pg.image.load(rp("scr/fundobarbie.jpg"))

#


rodando = True
while rodando:
    lista_eventos = pg.event.get() #pego todos os eventos que acontece na janela
    for evento in lista_eventos: #percorro os eventos
        if evento.type == pg.QUIT: #verifico se um dos eventos é para sair
            rodando = False #encerro o jogo



