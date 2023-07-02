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
caminho_imagem = 'C:\\Users\\Gabriel Pimenta\\Desktop\\ReposGitHub\\InmoovO.S\\app\\assets\\background_default.png'
imagem_background = pygame.image.load(caminho_imagem)
imagem_background = pygame.transform.scale(imagem_background, resolucao_tela)

# Carrega os sprites dos botões
caminho_botao_pergunta = 'C:\\Users\\Gabriel Pimenta\\Desktop\\ReposGitHub\\InmoovO.S\\app\\assets\\buttons\\pt\\botao_pergunta.png'
caminho_botao_musica = 'C:\\Users\\Gabriel Pimenta\\Desktop\\ReposGitHub\\InmoovO.S\\app\\assets\\buttons\\pt\\botao_musica.png'
caminho_botao_factos = 'C:\\Users\\Gabriel Pimenta\\Desktop\\ReposGitHub\\InmoovO.S\\app\\assets\\buttons\\pt\\botao_factos.png'  # Substitua pelo caminho do botao do botão factos com \\
caminho_botao_servos = 'C:\\Users\\Gabriel Pimenta\\Desktop\\ReposGitHub\\InmoovO.S\\app\\assets\\buttons\\pt\\botao_servo.png'  # Substitua pelo caminho do botao do botão servos com \\
caminho_botao_settings = 'C:\\Users\\Gabriel Pimenta\\Desktop\\ReposGitHub\\InmoovO.S\\app\\assets\\buttons\\pt\\botao_settings.png'  # Substitua pelo caminho do botao do botão settings com \\
caminho_botao_voltar = 'C:\\Users\\Gabriel Pimenta\\Desktop\\ReposGitHub\\InmoovO.S\\app\\assets\\exit_adm.png'  # Substitua pelo caminho do botão "Voltar" com \\

# Define as dimensões dos botões
largura_botao = 70
altura_botao = 50

# Define as posições dos botões
posicao_x = (resolucao_tela[0] - ((largura_botao * 2.5 + 20) * 5)) // 2
posicao_y = resolucao_tela[1] // 2

# Calcula o espaçamento entre os botões
espacamento = 1

# Carrega os botões redimensionados
botao_pergunta = pygame.image.load(caminho_botao_pergunta)
botao_pergunta = pygame.transform.scale(botao_pergunta, (int(largura_botao * 2.5), int(altura_botao * 2.5)))

botao_musica = pygame.image.load(caminho_botao_musica)
botao_musica = pygame.transform.scale(botao_musica, (int(largura_botao * 2.5), int(altura_botao * 2.5)))

botao_factos = pygame.image.load(caminho_botao_factos)
botao_factos = pygame.transform.scale(botao_factos, (int(largura_botao * 2.5), int(altura_botao * 2.5)))

botao_servos = pygame.image.load(caminho_botao_servos)
botao_servos = pygame.transform.scale(botao_servos, (int(largura_botao * 2.5), int(altura_botao * 2.5)))

botao_settings = pygame.image.load(caminho_botao_settings)
botao_settings = pygame.transform.scale(botao_settings, (int(largura_botao * 2.5), int(altura_botao * 2.5)))

botao_voltar = pygame.image.load(caminho_botao_voltar)
botao_voltar = pygame.transform.scale(botao_voltar, (int(largura_botao * 0.2), int(altura_botao * 0.2)))

# Calcula a posição do botão de voltar
posicao_botao_voltar = (20, resolucao_tela[1] - altura_botao * 0.2 - 20)

# Variável de controle do modo administrador
modo_administrador = False

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
    if posicao_botao_voltar[0] <= posicao_mouse[0] <= posicao_botao_voltar[0] + int(largura_botao * 0.2) and posicao_botao_voltar[1] <= posicao_mouse[1] <= posicao_botao_voltar[1] + int(altura_botao * 0.2):
        # Reduz o tamanho do botão de voltar em 5%
        botao_voltar_diminuido = pygame.transform.scale(botao_voltar, (int(largura_botao * 0.2 * 0.95), int(altura_botao * 0.2 * 0.95)))
    else:
        botao_voltar_diminuido = botao_voltar

    # Lista de botões visíveis
    botoes_visiveis = [botao_pergunta, botao_musica]

    # Verifica se o modo administrador está ativado
    if modo_administrador:
        botoes_visiveis.extend([botao_factos, botao_settings])
    else:
        botoes_visiveis.extend([botao_servos, botao_voltar_diminuido])

    # Calcula a largura total dos botões visíveis
    largura_botoes_visiveis = sum([botao.get_width() for botao in botoes_visiveis])

    # Calcula o espaçamento entre os botões visíveis
    espacamento_visiveis = (resolucao_tela[0] - largura_botoes_visiveis) // (len(botoes_visiveis) - 1)

    # Calcula a posição inicial dos botões visíveis
    posicao_x_visiveis = (resolucao_tela[0] - largura_botoes_visiveis - espacamento_visiveis * (len(botoes_visiveis) - 1)) // 2
    posicao_y_visiveis = resolucao_tela[1] // 2

    # Desenha a imagem de background na janela
    janela.blit(imagem_background, (0, 0))

    # Desenha os botões visíveis na janela
    posicao_x_atual = posicao_x_visiveis
    for botao in botoes_visiveis:
        janela.blit(botao, (posicao_x_atual, posicao_y_visiveis))
        posicao_x_atual += botao.get_width() + espacamento_visiveis

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
