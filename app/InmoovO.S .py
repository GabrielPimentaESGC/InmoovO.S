import pygame
import requests
from io import BytesIO

# Initialize Pygame
pygame.init()

# Get the screen size
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Download the image from the URL
image_url = "https://github.com/GabrielPimentaESGC/InmoovO.S/blob/main/app/assets/background_default.png?raw=true"
response = requests.get(image_url)
image_data = response.content

# Load the image from the downloaded data
image = pygame.image.load(BytesIO(image_data))

# Scale the image to fit the screen
image = pygame.transform.scale(image, (screen_width, screen_height))

# Download the button image from the URL
button_url = "https://github.com/GabrielPimentaESGC/InmoovO.S/blob/main/app/assets/buttons/pt/botao_pergunta.png?raw=true"
response = requests.get(button_url)
button_data = response.content

# Load the button image from the downloaded data
button_image = pygame.image.load(BytesIO(button_data))
button_width = int(screen_width * 0.15)
button_height = int(screen_height * 0.15)
button_image = pygame.transform.scale(button_image, (button_width, button_height))

# Define the initial and scaled sizes for the button
button_scale_normal = (button_width, button_height)
button_scale_hover = (int(button_width * 0.85), int(button_height * 0.85))
button_scale_pressed = (int(button_width * 1.2), int(button_height * 1.2))

# Set the initial button position
button_pos = (int(screen_width * 0.5 - button_width * 0.5), int(screen_height * 0.5 - button_height * 0.5))

# Define chatbox parameters
chatbox_width = int(screen_width * 0.6)
chatbox_height = int(screen_height * 0.6)
chatbox_pos = (int(screen_width * 0.5 - chatbox_width * 0.5), int(screen_height * 0.5 - chatbox_height * 0.5))
chatbox_color = (255, 255, 255)
chatbox_border_color = (0, 0, 0)
chatbox_border_width = 2

# Define chat bubble parameters
bubble_margin = 20
bubble_radius = 10
user_bubble_color = (255, 255, 255)
agent_bubble_color = (0, 0, 255)
text_color = (0, 0, 0)
font_size = 20
font = pygame.font.SysFont(None, font_size)

# Main game loop
running = True
is_chat_open = False  # Flag to check if the chatbox is open
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the button is pressed
            if button_pos[0] <= event.pos[0] <= button_pos[0] + button_width and \
                    button_pos[1] <= event.pos[1] <= button_pos[1] + button_height:
                is_chat_open = True

    # Check for mouse hover on the button
    mouse_pos = pygame.mouse.get_pos()
    is_hover = button_pos[0] <= mouse_pos[0] <= button_pos[0] + button_width and \
               button_pos[1] <= mouse_pos[1] <= button_pos[1] + button_height

    # Scale the button based on hover and press status
    if is_hover:
        button_image_scaled = pygame.transform.scale(button_image, button_scale_hover)
    elif is_chat_open:
        button_image_scaled = pygame.transform.scale(button_image, button_scale_pressed)
    else:
        button_image_scaled = pygame.transform.scale(button_image, button_scale_normal)

    # Draw the image and button on the screen
    screen.blit(image, (0, 0))
    screen.blit(button_image_scaled, button_pos)

    if is_chat_open:
        # Draw the chatbox
        pygame.draw.rect(screen, chatbox_border_color, (chatbox_pos[0], chatbox_pos[1], chatbox_width, chatbox_height),
                         chatbox_border_width)
        pygame.draw.rect(screen, chatbox_color,
                         (chatbox_pos[0] + chatbox_border_width, chatbox_pos[1] + chatbox_border_width,
                          chatbox_width - 2 * chatbox_border_width, chatbox_height - 2 * chatbox_border_width))

        # Draw user question bubble
        user_question = "Olá! Qual é a sua pergunta?"
        user_question_surface = font.render(user_question, True, text_color)
        user_question_width = user_question_surface.get_width()
        user_question_height = user_question_surface.get_height()
        user_bubble_pos = (chatbox_pos[0] + bubble_margin, chatbox_pos[1] + bubble_margin)
        pygame.draw.rect(screen, user_bubble_color,
                         (user_bubble_pos[0], user_bubble_pos[1], user_question_width + 2 * bubble_margin,
                          user_question_height + 2 * bubble_margin), bubble_radius)
        screen.blit(user_question_surface, (user_bubble_pos[0] + bubble_margin, user_bubble_pos[1] + bubble_margin))

        # Draw agent answer bubble
        agent_answer = "Aguarde, estou buscando uma resposta..."
        agent_answer_surface = font.render(agent_answer, True, text_color)
        agent_answer_width = agent_answer_surface.get_width()
        agent_answer_height = agent_answer_surface.get_height()
        agent_bubble_pos = (chatbox_pos[0] + bubble_margin,
                            user_bubble_pos[1] + bubble_margin + user_question_height + bubble_margin)
        pygame.draw.rect(screen, agent_bubble_color,
                         (agent_bubble_pos[0], agent_bubble_pos[1], agent_answer_width + 2 * bubble_margin,
                          agent_answer_height + 2 * bubble_margin), bubble_radius)
        screen.blit(agent_answer_surface, (agent_bubble_pos[0] + bubble_margin, agent_bubble_pos[1] + bubble_margin))

        # TODO: Implement API integration to get responses and add them to the chatbox

    pygame.display.flip()

# Quit Pygame
pygame.quit()
