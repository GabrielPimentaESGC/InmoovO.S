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
caminho_imagem = 'background_default.png'
imagem_background = pygame.image.load(caminho_imagem)
imagem_background = pygame.transform.scale(imagem_background, resolucao_tela)

# Carrega os sprites dos botões
caminho_botao_pergunta = 'InmoovO.S\\app\\assets\\buttons\\pt\\botao_pergunta.png'
caminho_botao_musica = 'InmoovO.S\\app\\assets\\buttons\\pt\\botao_musica.png'
caminho_botao_factos = 'InmoovO.S\\app\\assets\\buttons\\pt\\botao_factos.png'  # Substitua pelo caminho do botao do botão factos com \\
caminho_botao_servos = 'InmoovO.S\\app\\assets\\buttons\\pt\\botao_servo.png'  # Substitua pelo caminho do botao do botão servos com \\
caminho_botao_settings = 'InmoovO.S\\app\\assets\\buttons\\pt\\botao_settings.png'  # Substitua pelo caminho do botao do botão settings com \\
caminho_botao_voltar = 'InmoovO.S\\app\\assets\\exit_adm.png'  # Substitua pelo caminho do botão "Voltar" com \\

# Define as dimensões dos botões
largura_botao = 240
altura_botao = 170

# Define o espaçamento entre os botões
espacamento = 30

# Calcula a posição x inicial dos botões para centralizá-los
posicao_x_inicial = (resolucao_tela[0] - (largura_botao + espacamento) * 4) // 2

# Define a posição y dos botões
posicao_y = resolucao_tela[1] // 2

# Carrega os botões redimensionados
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

botao_voltar = pygame.image.load(caminho_botao_voltar)
botao_voltar = pygame.transform.scale(botao_voltar, (int(largura_botao * 0.2), int(altura_botao * 0.2)))

# Calcula a posição do botão de voltar
posicao_botao_voltar = (20, resolucao_tela[1] - altura_botao * 0.2 - 20)

# Define se o modo administrador está ativo
administrador_ativo = False

# Loop principal do jogo
rodando = True
while rodando:
    # Verifica os eventos do Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # Obtém a posição do mouse
    posicao_mouse = pygame.mouse.get_pos()

    # Verifica se o botão de voltar foi pressionado
    if administrador_ativo and posicao_botao_voltar[0] <= posicao_mouse[0] <= posicao_botao_voltar[0] + int(largura_botao * 0.2) and posicao_botao_voltar[1] <= posicao_mouse[1] <= posicao_botao_voltar[1] + int(altura_botao * 0.2):
        # Reduz o tamanho do botão de voltar em 5%
        botao_voltar_diminuido = pygame.transform.scale(botao_voltar, (int(largura_botao * 0.2 * 0.95), int(altura_botao * 0.2 * 0.95)))
    else:
        botao_voltar_diminuido = botao_voltar

    # Desenha a imagem de background na janela
    janela.blit(imagem_background, (0, 0))

    # Calcula a posição x atual dos botões
    posicao_x = posicao_x_inicial

    # Desenha os botões na janela
    janela.blit(botao_pergunta, (posicao_x, posicao_y))
    posicao_x += largura_botao + espacamento

    janela.blit(botao_musica, (posicao_x, posicao_y))
    posicao_x += largura_botao + espacamento

    if administrador_ativo:
        janela.blit(botao_factos, (posicao_x, posicao_y))
        posicao_x += largura_botao + espacamento

    janela.blit(botao_servos, (posicao_x, posicao_y))
    posicao_x += largura_botao + espacamento

    if administrador_ativo:
        janela.blit(botao_settings, (posicao_x, posicao_y))
        posicao_x += largura_botao + espacamento

    # Desenha o botão de voltar na janela
    if administrador_ativo:
        janela.blit(botao_voltar_diminuido, posicao_botao_voltar)

    # Atualiza a janela do Pygame
    pygame.display.update()

# Encerra o Pygame
pygame.quit()
