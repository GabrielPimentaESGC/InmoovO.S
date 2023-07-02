import pygame

# Inicializa o Pygame
pygame.init()

# Define a resolução da janela
resolucao_tela = (800, 600)  # Substitua pelos valores desejados

# Cria a janela
janela = pygame.display.set_mode(resolucao_tela)

# Define as cores
COR_BG = (255, 255, 255)  # Branco
COR_BOTAO = (0, 0, 255)  # Azul

# Define as dimensões e margens dos botões
largura_botao = 100
altura_botao = 50
margem_horizontal = 20
margem_vertical = 10

# Calcula as posições dos botões
num_botoes = 5
total_botoes = 3 + num_botoes
espaco_vertical = (resolucao_tela[1] - (total_botoes * altura_botao) - ((total_botoes - 1) * margem_vertical)) // 2
posicoes_botao = []
for i in range(num_botoes):
    x = (resolucao_tela[0] - largura_botao) // 2
    y = espaco_vertical + (i // 2) * (altura_botao + margem_vertical)
    if i % 2 == 1:
        x += largura_botao + margem_horizontal
    posicoes_botao.append((x, y))

# Loop principal do programa
executando = True
while executando:
    # Verifica os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Obtém a posição do mouse
    pos_mouse = pygame.mouse.get_pos()

    # Limpa a tela
    janela.fill(COR_BG)

    # Desenha os botões
    for posicao in posicoes_botao:
        # Define a área do botão
        botao_rect = pygame.Rect(posicao[0], posicao[1], largura_botao, altura_botao)

        # Verifica se o mouse está sobre o botão
        if botao_rect.collidepoint(pos_mouse):
            # Diminui o tamanho do botão em 5%
            botao_diminuido = botao_rect.inflate(-largura_botao * 0.05, -altura_botao * 0.05)
            pygame.draw.rect(janela, COR_BOTAO, botao_diminuido)
        else:
            pygame.draw.rect(janela, COR_BOTAO, botao_rect)

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
