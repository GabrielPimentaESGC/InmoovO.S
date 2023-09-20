import pygame
import requests
from io import BytesIO
import sys

# Inicializar o Pygame
pygame.init()

# Configurações da tela
screen_width = 1366
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# URL da imagem de fundo
background_url = "https://github.com/GabrielPimentaESGC/InmoovO.S/raw/main/app/assets/background_default.png"

# Carregar a imagem de fundo a partir da URL
try:
    response = requests.get(background_url)
    response.raise_for_status()
    background_data = BytesIO(response.content)
    original_background = pygame.image.load(background_data).convert()
except requests.exceptions.RequestException as e:
    print(f"Erro ao carregar a imagem de fundo: {e}")
    sys.exit()

# Redimensionar a imagem de fundo para preencher a tela
background = pygame.transform.scale(original_background, (screen_width, screen_height))

# Variável para controlar o estado do menu
menu_aberto = 1

# Velocidade da animação (0.7 segundos)
animation_speed = 0.7

# Cores
cor_cinza = (64, 64, 64)  # #404040
cor_preta = (0, 0, 0)

# Loop principal do jogo
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Verifique se o clique do mouse ocorreu no botão
            if menu_aberto == 1 and button_rect.collidepoint(event.pos):
                # Atualize a variável menu_aberto para 2
                menu_aberto = 2
                # Envie uma mensagem de log para a linha de comandos
                print("Botão clicado! menu_aberto agora é 2")

    # Desenhar o background na tela
    screen.blit(background, (0, 0))

    if menu_aberto == 1:
        # Verifique se o mouse está sobre o botão
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            # Se o mouse estiver sobre o botão, interpole o tamanho para criar uma animação suave
            target_size = hovered_button_size
        else:
            # Caso contrário, use o tamanho original
            target_size = button_size

        # Interpolação do tamanho do botão com duração de 0.7 segundos
        current_size = button.get_size()
        size_diff = (target_size[0] - current_size[0], target_size[1] - current_size[1])
        scale_factor = (size_diff[0] * (1 - animation_speed), size_diff[1] * (1 - animation_speed))
        new_size = (int(current_size[0] + scale_factor[0]), int(current_size[1] + scale_factor[1]))
        button = pygame.transform.scale(original_button, new_size)

        # Recalcular a posição do botão para mantê-lo centrado
        button_rect = button.get_rect(center=(screen_width // 2, screen_height // 2))

        # Desenhar o botão na tela
        screen.blit(button, button_rect.topleft)
    elif menu_aberto == 2:
        # Desenhar o retângulo quando menu_aberto for igual a 2
        retangulo = pygame.Rect((screen_width // 2) - 350, (screen_height // 2) - 50, 700, 100)
        pygame.draw.rect(screen, cor_cinza, retangulo)
        pygame.draw.rect(screen, cor_preta, retangulo, 2)  # Borda preta de 2px

    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
sys.exit()
