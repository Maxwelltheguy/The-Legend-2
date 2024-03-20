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
pygame.display.set_caption("The Legend 2: The Clark Epilogue")

# Load player image
player_image = pygame.image.load("Player.png").convert_alpha()

# Load background images
background_images = {
    "Background": pygame.image.load("Background.png").convert(),
    "House": pygame.image.load("House.png").convert(),
    "Cave": pygame.image.load("Cave.png").convert(),
    "Sleep": pygame.image.load("SleepyEnding.png").convert()
}

# Player properties
player_rect = player_image.get_rect()
player_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
player_speed = 5

# Font for displaying player position
font = pygame.font.Font(None, 36)

# Current map
current_map = "Background"

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # Check if the player is in the specific area to switch the map
            if current_map == "Background" and 910 <= player_rect.x <= 1115 and 0 <= player_rect.y <= 150:
                current_map = "House"
            elif current_map == "House" and 910 <= player_rect.x <= 1115 and 0 <= player_rect.y <= 150:
                current_map = "Background"
            elif current_map == "House" and 118 <= player_rect.x <= 443 and 198 <= player_rect.y <= 448:
                current_map = "Sleep"
                pass

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
    screen.blit(background_images[current_map], (0, 0))

    # Draw the player
    screen.blit(player_image, player_rect)

    # Display player's position
    position_text = font.render(f"Player Position: ({player_rect.x}, {player_rect.y})", True, (255, 255, 255))
    screen.blit(position_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
