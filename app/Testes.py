import pygame
import sys

pygame.init()

# Constants for the window and textbox dimensions
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
TEXTBOX_WIDTH, TEXTBOX_HEIGHT = 200, 50
OUTLINE_WIDTH = 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font settings
FONT_SIZE = 20
FONT_COLOR = BLACK
FONT_NAME = None  # Default font

# Initialize the window and font
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

# Create a Rect object for the textbox
textbox_rect = pygame.Rect((WINDOW_WIDTH - TEXTBOX_WIDTH) // 2, (WINDOW_HEIGHT - TEXTBOX_HEIGHT) // 2, TEXTBOX_WIDTH, TEXTBOX_HEIGHT)

# Initialize the text input variables
input_text = ""
input_active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    # Handle text input when the user presses Enter (you can implement custom behavior here)
                    print("Entered text:", input_text)
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    # Remove the last character from the input_text
                    input_text = input_text[:-1]
                else:
                    # Add the pressed character to the input_text
                    input_text += event.unicode

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is within the textbox's boundaries
            if textbox_rect.collidepoint(event.pos):
                input_active = True
            else:
                input_active = False

    # Clear the screen
    window.fill(WHITE)

    # Draw the outline of the textbox
    pygame.draw.rect(window, BLACK, textbox_rect, OUTLINE_WIDTH)

    # Render the text and make sure it fits within the textbox
    text_surface = font.render(input_text, True, FONT_COLOR)
    text_rect = text_surface.get_rect()
    if text_rect.width > textbox_rect.width - OUTLINE_WIDTH * 2:
        # If the text exceeds the width of the textbox, truncate it to fit
        text_surface = font.render(input_text[-(textbox_rect.width // font.size("A")[0]):], True, FONT_COLOR)
    text_rect = text_surface.get_rect(center=textbox_rect.center)

    # Draw the text surface onto the window
    window.blit(text_surface, text_rect)

    # Update the display
    pygame.display.update()
