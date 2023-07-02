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
caminho_botao_factos = 'C:\\Users\\Gabriel Pimenta\\Desktop\\ReposGitHub\\InmoovO.S\\app\\assets\\buttons\\pt\\botao_factos.png'  
caminho_botao_servos = 'C:\\Users\\Gabriel Pimenta\\Desktop\\ReposGitHub\\InmoovO.S\\app\\assets\\buttons\\pt\\botao_servo.png'  
caminho_botao_settings = 'C:\\Users\\Gabriel Pimenta\\Desktop\\ReposGitHub\\InmoovO.S\\app\\assets\\buttons\\pt\\botao_settings.png'  
caminho_botao_voltar = 'C:\\Users\\Gabriel Pimenta\\Desktop\\ReposGitHub\\InmoovO.S\\app\\assets\\exit_adm.png'  

# Define as dimensões dos botões
largura_botao = int(resolucao_tela[0] * 0.15)
altura_botao = int(resolucao_tela[1] * 0.10)

# Define as dimensões do botao adm exit
largura_botaoex = int(resolucao_tela[0] * 0.25)
altura_botaoex = int(resolucao_tela[1] * 0.25)

# Define as posições dos botões
posicao_x = (resolucao_tela[0] - ((largura_botao * 3 + 100) * 3)) / 2
posicao_y = resolucao_tela[1] / 2

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
botao_voltar = pygame.transform.scale(botao_voltar, (int(largura_botaoex * 0.2), int(altura_botaoex * 0.2)))

# Define o título da janela
pygame.display.set_caption("Sistema Operativo")

# Variável 'adm'
adm = 1

# Define as cores
VERMELHO = (255, 0, 0)
ALPHA = 40

# Define a fonte e tamanho do texto
fonte = pygame.font.SysFont("Arial", 24)

# Loop principal do programa
executando = True
while executando:
    # Verifica os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Obtém a posição do cursor do mouse
    posicao_mouse = pygame.mouse.get_pos()

    # Desenha a imagem de background na janela
    janela.blit(imagem_background, (0, 0))

    # Desenha o texto "modo administrador" se adm for igual a 1
    if adm == 1:
        texto_modo_admin = fonte.render("Modo Administrador", True, VERMELHO)
        texto_modo_admin.set_alpha(ALPHA)
        janela.blit(texto_modo_admin, (resolucao_tela[0] // 2 - texto_modo_admin.get_width() // 2, 20))

        # Desenha o botão "Voltar" com a mesma opacidade abaixo do texto "Modo Administrador"
        posicao_botao_voltar = (resolucao_tela[0] // 2 - botao_voltar.get_width() // 2, 60)
        if posicao_botao_voltar[0] <= posicao_mouse[0] <= posicao_botao_voltar[0] + int(largura_botao * 0.2) and posicao_botao_voltar[1] <= posicao_mouse[1] <= posicao_botao_voltar[1] + int(altura_botao * 0.2):
            botao_voltar_diminuido = pygame.transform.scale(botao_voltar, (int(largura_botao * 0.2 * 0.95), int(altura_botao * 0.2 * 0.95)))
        else:
            botao_voltar_diminuido = botao_voltar

        janela.blit(botao_voltar_diminuido, posicao_botao_voltar)

    # Verifica se o cursor do mouse está sobre o botão factos e settings quando adm for igual a 1
    if adm == 1:
        if posicao_x <= posicao_mouse[0] <= posicao_x + largura_botao and posicao_y <= posicao_mouse[1] <= posicao_y + altura_botao:
            botao_factos_diminuido = pygame.transform.scale(botao_factos, (int(largura_botao * 0.95), int(altura_botao * 0.95)))
        else:
            botao_factos_diminuido = botao_factos
    else:
        botao_factos_diminuido = None
# Define as posições dos botões
posicao_x = (resolucao_tela[0] - ((largura_botao * 2.5 + 20) * 5)) // 2
posicao_y = resolucao_tela[1] // 2

# Desenha os botões na janela
janela.blit(botao_pergunta, (posicao_x, posicao_y))
janela.blit(botao_musica, (posicao_x + largura_botao * 2.5 + 20, posicao_y))
if botao_factos_diminuido:
    janela.blit(botao_factos_diminuido, (posicao_x + (largura_botao * 2.5 + 20) * 2, posicao_y))
janela.blit(botao_servos, (posicao_x + (largura_botao * 2.5 + 20) * 3, posicao_y))
janela.blit(botao_settings, (posicao_x + (largura_botao * 2.5 + 20) * 4, posicao_y))


# Atualiza a janela
pygame.display.flip()
# Encerra o Pygame
pygame.quit()