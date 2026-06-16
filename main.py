#importando pygame e colocando apelido
import pygame as pg
from classe_inimigo import Inimigo
from classe_jogador import Jogador
from classe_roupabonita import Roupabonita
from classe_bonus import Item
from caminho_relativo import resource_path as rp


pg.init() #inicializa os módulos básicos do pygame

clock = pg.time.Clock()

###### Variaveis para o controlar a duração do poder #########
tempo_inicio_poder = 0
poder_ativo = False
fonte_poder = pg.font.SysFont("Segoe UI Emoji", 100)

#criando a tela
tela = pg.display.set_mode((1200, 720))

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
fundo = pg.image.load(rp("scr/fundobarbie.png"))
tela_final = pg.image.load(rp("scr/tela_final.png"))
tela_vitoria = pg.image.load(rp("scr/tela_vitoria.png"))

#diminuindo tamanho da imagem
roupabonita1 = pg.transform.scale(roupabonita1, (80,100))
roupabonita2 = pg.transform.scale(roupabonita2, (80,100))
roupabonita3 = pg.transform.scale(roupabonita3, (80,100))
roupabonita4 = pg.transform.scale(roupabonita4, (80,100))
roupabonita5 = pg.transform.scale(roupabonita5, (80,100))
roupabonita6 = pg.transform.scale(roupabonita6, (80,100))
roupabonita7 = pg.transform.scale(roupabonita7, (80,100))
roupabonita8 = pg.transform.scale(roupabonita8, (80,100))
roupafeia = pg.transform.scale(roupafeia, (80,100))
roupafeia2 = pg.transform.scale(roupafeia2, (80,100))
roupafeia3 = pg.transform.scale(roupafeia3, (80,100))
barbie = pg.transform.scale(barbie, (120,200))
tela_inicial = pg.transform.scale(tela_inicial, (1200,720))
fundo = pg.transform.scale(fundo, (1200,720))
tela_final = pg.transform.scale(tela_final, (1200, 720))
tela_vitoria = pg.transform.scale(tela_vitoria, (1200, 720))

fonte = pg.font.SysFont("Segoe UI Emoji", 50)

#criando um inimigo
roupafeia = [Inimigo(rp("scr/roupafeia-removebg.png")),
                 Inimigo(rp("scr/roupafeia2-removebg.png")),
                 Inimigo(rp("scr/roupafeia3-removebg.png"))]

roupabonita = [Roupabonita(rp("scr/roupabonita1.PNG")),
               Roupabonita(rp("scr/roupabonita2.PNG")),
               Roupabonita(rp("scr/roupabonita3.PNG")),
               Roupabonita(rp("scr/roupabonita4.PNG")),
               Roupabonita(rp("scr/roupabonita5.PNG")),
               Roupabonita(rp("scr/roupabonita6.PNG")),
               Roupabonita(rp("scr/roupabonita7.PNG")),]



barbie = Jogador()

status_jogo = "INICIO"
contador_pontos = 0
contador_mortes = 0
#Placares
total_vidas = 4
vida_atual = total_vidas
pontuacao = 0


rodando = True
while rodando:
    lista_eventos = pg.event.get() #pego todos os eventos que acontece na janela
    for evento in lista_eventos: #percorro os eventos
        if evento.type == pg.QUIT: #verifico se um dos eventos é para sair
            rodando = False #encerro o jogo

    #pegando a lista de teclas pressionadas
    teclas_pressionadas = pg.key.get_pressed()

    


    if status_jogo == "INICIO":
        tela.blit(tela_inicial, (0,0))
            
        if teclas_pressionadas[pg.K_KP_ENTER] or teclas_pressionadas[pg.K_RETURN]:
            status_jogo = "JOGANDO"
    


    if status_jogo == "JOGANDO":

        #exibindo o fundo
        tela.blit(fundo,(0,0))


        #Placar de pontos
        texto_pontuacao = fonte.render(f"Pontos: {pontuacao}", True, (255, 255, 255))
        tela.blit(texto_pontuacao, (10, 10))


    #inserindo a barbie
        barbie.exibir(tela)
        barbie.andar(teclas_pressionadas)

    ###### Verifica se ele apertou espaço para ativar o poder ######
        if teclas_pressionadas[pg.K_SPACE] and not poder_ativo:
            poder_ativo = True  # Ativa o poder
            tempo_inicio_poder = pg.time.get_ticks() # Armazena o tempo de início do poder
            
        ##### Verifica se o poder está ativo e se já passou o tempo de duração (5 segundos) ######
        if poder_ativo == True:
            tempo_decorrido = int((pg.time.get_ticks() - tempo_inicio_poder)/1000) # Calcula o tempo decorrido em segundos
            texto_tempo = fonte_poder.render(f"{tempo_decorrido}", True, (255, 100, 100))
            tela.blit(texto_tempo, (500, 200))
            if tempo_decorrido >= 5: # 5 segundos
                poder_ativo = False # Desativa o poder
                for inimigo in roupabonita: # Reseta a velocidade horizontal dos bônus
                    inimigo.velocidade_x = 0

    #fazendo o inimigo andar
        for inimigo in roupabonita:
            inimigo.andar()
            inimigo.exibir(tela)

            if barbie.mascara.overlap(inimigo.mascara, (inimigo.pos_y_roupabonita - barbie.pos_y, inimigo.pos_x_roupabonita - barbie.pos_x)):
                barbie.pontos()
                pontuacao = pontuacao + 1
                inimigo.voltar()
                if pontuacao == 25:
                    status_jogo = "VITORIA"
                    barbie.VITORIA()
                    ######### Se o poder estiver ativo, calcula a velocidade horizontal para o bônus se mover em direção ao jogador #########
            if poder_ativo == True:
                offset_x = barbie.pos_x - inimigo.pos_x_roupabonita
                offset_y = barbie.pos_y - inimigo.pos_y_roupabonita
                if offset_y != 0: # Evita divisão por zero
                    inimigo.velocidade_x = offset_x * inimigo.velocidade_y/offset_y


    #fazendo o inimigo andar
        for inimigo in roupafeia:
            inimigo.andar()
            inimigo.exibir(tela)

            if barbie.mascara.overlap(inimigo.mascara, (inimigo.pos_y_roupafeia - barbie.pos_y, inimigo.pos_x_roupafeia - barbie.pos_x)):
                barbie.gritar()
                barbie.voltar()
                inimigo.voltar()
                contador_mortes += 1
                if contador_mortes == 4:
                    status_jogo = "PERDEU"
                    barbie.perder()
                    contador_mortes=0
                    contador_pontos=0


    if status_jogo == "PERDEU":
        tela.blit(tela_final, (0,0))
        if teclas_pressionadas[pg.K_KP_ENTER] or teclas_pressionadas[pg.K_RETURN]:
            status_jogo = "JOGANDO"

    if status_jogo == "VITORIA":
        tela.blit(tela_vitoria,(0,0))
        if teclas_pressionadas[pg.K_KP_ENTER] or teclas_pressionadas[pg.K_RETURN]:
            status_jogo = "JOGANDO"

    #atualizando a tela
    pg.display.update()

    #controlar o FPS
    clock.tick(60)





