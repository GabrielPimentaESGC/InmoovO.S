import pygame
import os

# Inicializa o Pygame
pygame.init()

# Obtém informações sobre a tela atual
info_tela = pygame.display.Info()

# Obtém a resolução da tela
resolucao_tela = (info_tela.current_w, info_tela.current_h)

# Cria a janela fullscreen com a resolução da tela
janela = pygame.display.set_mode(resolucao_tela, pygame.FULLSCREEN)

# Carrega a imagem de background
caminho_imagem = '"C:\\Users\\Gabriel Pimenta\\Desktop\\ReposGitHub\\InmoovO.S\\app\\assets\\background_default.png"'  

imagem_background = pygame.transform.scale(imagem_background, resolucao_tela)

# Carrega os sprites dos botões
caminho_botao_pergunta = '"C:\\Users\\Gabriel Pimenta\\Desktop\\ReposGitHub\\InmoovO.S\\app\\assets\\buttons\\pt\\botao_pergunta.png"'  
caminho_botao_musica = '"C:\\Users\\Gabriel Pimenta\\Desktop\\ReposGitHub\\InmoovO.S\\app\\assets\\buttons\\pt\\botao_musica.png"'  
caminho_botao_factos = 'caminho\\para\\o\\sprite_factos.png'  # Substitua pelo caminho do sprite do botão factos com \\
caminho_botao_servos = 'caminho\\para\\o\\sprite_servos.png'  # Substitua pelo caminho do sprite do botão servos com \\
caminho_botao_settings = 'caminho\\para\\o\\sprite_settings.png'  # Substitua pelo caminho do sprite do botão settings com \\

# Define as dimensões dos botões
largura_botao = 100
altura_botao = 50

# Define as posições dos botões
posicao_x = (resolucao_tela[0] - (largura_botao * 3)) / 2
posicao_y = resolucao_tela[1] / 2

# Carrega os sprites dos botões redimensionados
botao_pergunta = pygame.image.load(caminho_botao_pergunta)
botao_pergunta = pygame.transform.scale(botao_pergunta, (largura_botao, altura_botao))

botao_musica = pygame.image.load(caminho_botao_musica)
botao_musica = pygame.transform.scale(botao_musica, (largura_botao, altura_botao))

botao_factos = pygame.image.load(caminho_botao_factos)
botao_factos = pygame.transform.scale(botao_factos, (largura_botao, altura_botao))

botao_servos = pygame.image.load(caminho_botao_servos)
botao_servos = pygame.transform.scale(botao_servos, (largura_botao, altura_botao))

botao_settings = pygame.image.load(caminho_botao_settings)
botao_settings = pygame.transform.scale(botao_settings, (largura_botao, altura_botao))

# Define o título da janela
pygame.display.set_caption("Sistema Operativo")

# Loop principal do programa
executando = True
while executando:
    # Verifica os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Desenha a imagem de background na janela
    janela.blit(imagem_background, (0, 0))

    # Obtém a posição do cursor do mouse
    posicao_mouse = pygame.mouse.get_pos()

    # Verifica se o cursor do mouse está sobre o botão factos e settings
    if 1 in [adm]:  # Substitua pelo valor da sua variável 'adm'
        if posicao_x <= posicao_mouse[0] <= posicao_x + largura_botao and posicao_y <= posicao_mouse[1] <= posicao_y + altura_botao:
            botao_factos_diminuido = pygame.transform.scale(botao_factos, (int(largura_botao * 0.95), int(altura_botao * 0.95)))
        else:
            botao_factos_diminuido = botao_factos

        if posicao_x + largura_botao <= posicao_mouse[0] <= posicao_x + largura_botao * 2 and posicao_y <= posicao_mouse[1] <= posicao_y + altura_botao:
            botao_settings_diminuido = pygame.transform.scale(botao_settings, (int(largura_botao * 0.95), int(altura_botao * 0.95)))
        else:
            botao_settings_diminuido = botao_settings
    else:
        botao_factos_diminuido = botao_factos
        botao_settings_diminuido = botao_settings

    # Desenha os botões na janela
    janela.blit(botao_pergunta, (posicao_x, posicao_y))
    janela.blit(botao_musica, (posicao_x + largura_botao, posicao_y))
    janela.blit(botao_factos_diminuido, (posicao_x + largura_botao * 2, posicao_y))
    janela.blit(botao_settings_diminuido, (posicao_x + largura_botao * 3, posicao_y))

    # Atualiza a janela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
