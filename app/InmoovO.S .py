import pygame
import requests
from io import BytesIO

# Inicialização do Pygame
pygame.init()

# Definição de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configurações da janela em tela cheia
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()
pygame.display.set_caption("Menu Principal")

# URLs das imagens
background_url = "https://github.com/GabrielPimentaESGC/InmoovO.S/raw/main/app/assets/background_default.png"
button_urls = [
    "https://github.com/GabrielPimentaESGC/InmoovO.S/raw/main/app/assets/buttons/pt/botao_musica.png",
    "https://github.com/GabrielPimentaESGC/InmoovO.S/raw/main/app/assets/buttons/pt/botao_pergunta.png",
    "https://github.com/GabrielPimentaESGC/InmoovO.S/raw/main/app/assets/buttons/pt/botao_factos.png",
    "https://github.com/GabrielPimentaESGC/InmoovO.S/raw/main/app/assets/buttons/admin_mode.png",
    "https://img.freepik.com/premium-vector/smart-house-logo-template-design-vector-emblem-design-concept-creative-symbol-icon_316488-1066.jpg"
]

# Carregando imagens
print("Carregando imagens...")
response = requests.get(background_url)
background_image = pygame.image.load(BytesIO(response.content))
print("Imagem de fundo carregada.")

button_images = []
button_names = ["Música", "Perguntas", "Factos", "Admin", "Smart Home"]

for i, url in enumerate(button_urls):
    response = requests.get(url)
    button_images.append(pygame.image.load(BytesIO(response.content)))
    print(f"Imagem do botão {button_names[i]} carregada.")

# Redimensionando botões
button_width = 210  # Aumentei o tamanho dos botões
button_height = 170  # Aumentei o tamanho dos botões
for i in range(len(button_images)):
    button_images[i] = pygame.transform.scale(button_images[i], (button_width, button_height))

# Posições dos botões
button_positions = [
    (screen_width // 1.35 - button_width // 2, screen_height // 3 - button_height // 2),  # Botão de Factos
    (screen_width // 4 - button_width // 2, 2 * screen_height // 6 - button_height // 2),  # Botão de Música
    (screen_width // 2 - button_width // 2, 2 * screen_height // 6 - button_height // 2),  # Botão de Perguntas
    (screen_width // 2.72 - button_width // 2, 4 * screen_height // 6 - button_height // 2),  # Botão de Admin
    (screen_width // 1.6 - button_width // 2, 4 * screen_height // 6 - button_height // 2)  # Botão de Smart Home
]

# Variável para controlar o tamanho dos botões
button_scale = [1.2] * len(button_images)  # Tamanho normal é 20% maior do que o tamanho atual

# Variáveis para a animação
animation_duration = 0.2  # Duração da animação em segundos
frame_rate = 60  # Taxa de quadros por segundo
frame_count = int(animation_duration * frame_rate)
frame_delay = 1.0 / frame_rate

is_animating = False  # Flag para controlar se uma animação está em andamento
button_clicked = -1  # Índice do botão clicado (-1 significa nenhum botão clicado)

# Variável para controlar o menu aberto (1 = Menu Principal)
menu_aberto = 1

print("Iniciando loop principal...")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Fechando a janela...")
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not is_animating:
            # Quando um botão é clicado, inicia a animação de redução
            for i in range(len(button_images)):
                button_x, button_y = button_positions[i]
                if button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height:
                    button_scale[i] = 0.9
                    is_animating = True  # Define que uma animação está em andamento
                    button_clicked = i  # Registra qual botão foi clicado
                    if i == 2:  # Se o botão de Perguntas foi clicado, muda para o menu de Perguntas (por exemplo)
                        menu_aberto = 2
                        print(f"Executada animação de click no botão {button_names[i]}.")

        elif event.type == pygame.MOUSEBUTTONUP and is_animating and button_clicked != -1:
            # Quando o botão do mouse é liberado, remove a imagem do botão clicado da lista
            button_x, button_y = button_positions[button_clicked]
            if button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height:
                if button_clicked != 2:  # Verifica se o botão de Perguntas não foi clicado
                    button_images.pop(button_clicked)
                    button_positions.pop(button_clicked)
                    button_scale.pop(button_clicked)
                print(f"Executada animação de voltar ao normal no botão {button_names[button_clicked]}.")
            is_animating = False  # A animação foi concluída
            button_clicked = -1  # Nenhum botão está mais clicado

    screen.fill(WHITE)
    screen.blit(background_image, (0, 0))

    if menu_aberto == 1:  # Menu Principal
        # Verificar hover dos botões e desenhar botões
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for i in range(len(button_images)):
            button_x, button_y = button_positions[i]

            if button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height:
                if button_scale[i] < 1.2:
                    button_scale[i] += 0.1
                    print(f"Executada animação de hover no botão {button_names[i]}.")
            else:
                if button_scale[i] > 1.0:
                    button_scale[i] -= 0.1
                    print(f"Executada animação de voltar ao normal no botão {button_names[i]}.")

            # Apenas desenha o botão se a escala não for zero
            if button_scale[i] > 0:
                button = pygame.transform.scale(button_images[i], (int(button_width * button_scale[i]), int(button_height * button_scale[i])))
                screen.blit(button, (button_x + (button_width - int(button_width * button_scale[i])) // 2, button_y + (button_height - int(button_height * button_scale[i])) // 2))

    pygame.display.flip()
    pygame.time.delay(int(frame_delay * 1000))

pygame.quit()
