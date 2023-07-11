import pygame
import urllib.request
import io
import openai

# Configurações
BACKGROUND_URL = "https://github.com/GabrielPimentaESGC/InmoovO.S/blob/main/app/assets/background_default.png?raw=true"
BUTTON_NORMAL_URL = "https://github.com/GabrielPimentaESGC/InmoovO.S/blob/main/app/assets/buttons/pt/botao_pergunta.png?raw=true"
BUTTON_HOVER_SCALE = 0.85
BUTTON_PRESSED_SCALE = 1.15
QUESTION_BOX_WIDTH = 750
QUESTION_BOX_HEIGHT = 45
QUESTION_BOX_COLOR = (89, 89, 89)  # Cor #595959
QUESTION_BOX_OUTLINE_COLOR = (0, 0, 0)  # Cor preta
QUESTION_BOX_OUTLINE_WIDTH = 3
TEXT_BUBBLE_COLOR_USER = (174, 214, 241)  # Cor azul clara para mensagens do usuário
TEXT_BUBBLE_PADDING = 10
TEXT_BUBBLE_MARGIN = 20
TEXT_BUBBLE_FONT_SIZE = 17
TEXT_BUBBLE_FONT_COLOR = (0, 0, 0)  # Cor preta
GPT_API_KEY = "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"

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

# Define o estado do menu
menu_open = False
question_box = pygame.Rect((screen_width - QUESTION_BOX_WIDTH) // 2, 60, QUESTION_BOX_WIDTH, QUESTION_BOX_HEIGHT)
question_box_active = False
question_box_text = ""
text_bubbles = []

# Define as fontes
font_question_box = pygame.font.Font(None, 32)
font_text_bubble = pygame.font.Font(None, TEXT_BUBBLE_FONT_SIZE)

# Define a API do OpenAI
openai.api_key = GPT_API_KEY

# Função para enviar uma pergunta para o ChatGPT e obter uma resposta
def ask_openai(question):
    prompt = "A partir de agora irás responder como um robô impresso em uma impressora de 3 dimensões chamado InMoov Plus feito pela equipe Choninhas coordenada pelo doutor Pimentinha e seus ajudantes, que são alunos da Escola Secundária Gago Coutinho em Portugal. Tu falas português de Portugal e alguém acaba de te fazer esta pergunta:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt + " " + question + " [PARA_DE_COMPLETAR]",
        max_tokens=1000,
        temperature=0.7,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip().replace("[PARA_DE_COMPLETAR]", "")

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
                if not menu_open:
                    button_rect = button_normal_image.get_rect()
                    button_rect.center = (screen_width // 2, screen_height // 2)
                    if button_rect.collidepoint(event.pos):
                        menu_open = True
                        question_box_active = True
                        question_box_text = ""
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if menu_open:
                    menu_open = False
                    question_box_active = False
                    question_box_text = ""
                    text_bubbles.clear()
            elif event.key == pygame.K_RETURN:
                if menu_open and question_box_active and question_box_text:
                    response_text = ask_openai(question_box_text)
                    text_bubbles.append((question_box_text, TEXT_BUBBLE_COLOR_USER))
                    text_bubbles.append((response_text, TEXT_BUBBLE_COLOR_USER))
                    print("Usuário:", question_box_text)
                    print("ChatGPT:", response_text)
                    question_box_text = ""
            elif question_box_active:
                if event.key == pygame.K_BACKSPACE:
                    question_box_text = question_box_text[:-1]
                else:
                    question_box_text += event.unicode

    # Atualiza o estado do botão
    mouse_pos = pygame.mouse.get_pos()
    button_rect = button_normal_image.get_rect()
    button_rect.center = (screen_width // 2, screen_height // 2)
    if button_rect.collidepoint(mouse_pos):
        button_current_scale = BUTTON_HOVER_SCALE
    else:
        button_current_scale = button_scale

    # Preenche a tela com a imagem de fundo
    screen.blit(background_image, (0, 0))

    if menu_open:
        # Desenha o menu de pergunta
        pygame.draw.rect(screen, QUESTION_BOX_COLOR, question_box, border_radius=10)
        pygame.draw.rect(screen, QUESTION_BOX_OUTLINE_COLOR, question_box, QUESTION_BOX_OUTLINE_WIDTH, border_radius=10)
        if question_box_active:
            question_text = question_box_text
            if font_question_box.size(question_text)[0] > QUESTION_BOX_WIDTH - 30:
                while font_question_box.size(question_text + "...")[0] > QUESTION_BOX_WIDTH - 30:
                    question_text = question_text[:-1]
                question_text += "..."
            question_box_text_surface = font_question_box.render(question_text, True, (255, 255, 255))
            question_box_text_rect = question_box_text_surface.get_rect(center=question_box.center)
            screen.blit(question_box_text_surface, question_box_text_rect)

    # Desenha as text bubbles
    text_bubble_y = question_box.bottom + TEXT_BUBBLE_MARGIN
    for bubble_text, bubble_color in text_bubbles:
        bubble_surface = font_text_bubble.render(bubble_text, True, TEXT_BUBBLE_FONT_COLOR)
        bubble_rect = bubble_surface.get_rect()
        bubble_rect.width += TEXT_BUBBLE_PADDING * 2
        bubble_rect.height += TEXT_BUBBLE_PADDING * 2
        bubble_rect.right = question_box.right
        bubble_rect.y = text_bubble_y
        pygame.draw.rect(screen, bubble_color, bubble_rect, border_radius=10)
        text_surface = font_text_bubble.render(bubble_text, True, TEXT_BUBBLE_FONT_COLOR)
        text_rect = text_surface.get_rect(center=bubble_rect.center)
        screen.blit(text_surface, text_rect)
        text_bubble_y += bubble_rect.height + TEXT_BUBBLE_MARGIN

    # Esconde o botão se o menu estiver aberto
    if menu_open:
        button_rect_scaled = button_normal_image.get_rect()
        button_current_scale = 0.0

    # Desenha o botão
    button_scaled_width = int(button_normal_image.get_width() * button_current_scale)
    button_scaled_height = int(button_normal_image.get_height() * button_current_scale)
    button_scaled_image = pygame.transform.scale(button_normal_image, (button_scaled_width, button_scaled_height))
    button_rect_scaled = button_scaled_image.get_rect()
    button_rect_scaled.center = (screen_width // 2, screen_height // 2)
    screen.blit(button_scaled_image, button_rect_scaled)

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
