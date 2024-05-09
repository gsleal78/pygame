import pygame
import random
from os import path

from definindo_imagens import imagens

FPS = 30
ini = 0
jogo = 1
sair = 2

def init_screen(tela):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(imagens, 'background_i')).convert()
    background_rect = background.get_rect()

    rodando = True
    while rodando:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                estado = sair
                rodando = False

            if event.type == pygame.KEYUP:
                estado = jogo
                rodando = False

        # A cada loop, redesenha o fundo e os sprites
        tela.fill(0,0,0)
        tela.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return estado
