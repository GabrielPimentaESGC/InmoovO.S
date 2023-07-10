import pygame
import urllib.request
import io

# Configurações
BACKGROUND_URL = "https://github.com/GabrielPimentaESGC/InmoovO.S/blob/main/app/assets/background_default.png?raw=true"
BUTTON_NORMAL_URL = "https://github.com/GabrielPimentaESGC/InmoovO.S/blob/main/app/assets/buttons/pt/botao_pergunta.png?raw=true"
BUTTON_HOVER_SCALE = 0.85
BUTTON_PRESSED_SCALE = 1.15

# Inicialização do Pygame
pygame.init()

# Obtém a resolução do monitor
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Carrega as imagens do background e do botão
background_image_data = urllib.request.urlopen(BACKGROUND_URL).read()
background_image = pygame.image.load(io.BytesIO(background_image_data))
button_normal_image_data = urllib.request.urlopen(BUTTON_NORMAL_URL).read()
button_normal_image = pygame.image.load(io.BytesIO(button_normal_image_data))

# Define as escalas inicial e atual do botão
button_scale = 1.0
button_current_scale = 1.0

# Função para desenhar o botão centralizado na tela
def draw_button():
    button_rect = button_normal_image.get_rect()
    button_rect.center = (screen_width // 2, screen_height // 2)
    button_scaled_width = int(button_rect.width * button_current_scale)
    button_scaled_height = int(button_rect.height * button_current_scale)
    button_image_scaled = pygame.transform.scale(button_normal_image, (button_scaled_width, button_scaled_height))
    screen.blit(button_image_scaled, button_rect)

# Cria a janela em tela cheia
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Loop principal do jogo
running = True
while running:
    # Verifica eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botão esquerdo do mouse pressionado
                button_current_scale = BUTTON_PRESSED_SCALE
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Botão esquerdo do mouse solto
                button_current_scale = 1.0

    # Atualiza a escala do botão quando o mouse está sobre ele
    mouse_pos = pygame.mouse.get_pos()
    button_rect = button_normal_image.get_rect()
    button_rect.center = (screen_width // 2, screen_height // 2)
    button_scaled_rect = pygame.Rect(button_rect)
    button_scaled_rect.width *= button_current_scale
    button_scaled_rect.height *= button_current_scale
    if button_scaled_rect.collidepoint(mouse_pos):
        button_current_scale = BUTTON_HOVER_SCALE
    else:
        button_current_scale = 1.0

    # Redimensiona a janela se a resolução do monitor mudou
    if screen_width != screen_info.current_w or screen_height != screen_info.current_h:
        screen_width = screen_info.current_w
        screen_height = screen_info.current_h
        screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    # Desenha o background
    background_image_scaled = pygame.transform.scale(background_image, (screen_width, screen_height))
    screen.blit(background_image_scaled, (0, 0))

    # Desenha o botão
    draw_button()

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
