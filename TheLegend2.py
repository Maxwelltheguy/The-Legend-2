#Programmer: Maxwell
#Date: 3-15-2024
#Program: The Legend 2

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Legend 2: The Carl epilouge")

# Load player image
player_image = pygame.image.load("Player.png").convert_alpha()

# Load background image
background_image = pygame.image.load("Background.png").convert()

# Player properties
player_rect = player_image.get_rect()
player_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
player_speed = 5

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # Boundary check
    player_rect.x = max(0, min(player_rect.x, SCREEN_WIDTH - player_rect.width))
    player_rect.y = max(0, min(player_rect.y, SCREEN_HEIGHT - player_rect.height))

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Draw the player
    screen.blit(player_image, player_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
