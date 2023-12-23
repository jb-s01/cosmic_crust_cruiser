import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SHIP_SPEED = 5

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cosmic Crust Cruiser")

# Load spaceship image
ship_img = pygame.image.load("spaceship.png")
ship_rect = ship_img.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Movement keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship_rect.x -= SHIP_SPEED
    if keys[pygame.K_RIGHT]:
        ship_rect.x += SHIP_SPEED
    if keys[pygame.K_UP]:
        ship_rect.y -= SHIP_SPEED
    if keys[pygame.K_DOWN]:
        ship_rect.y += SHIP_SPEED
    
    # Drawing
    screen.fill((0,0,0)) # Fills the screen with black space
    screen.blit(ship_img, ship_rect) # Draws the spaceship

    pygame.display.flip() # Update the display

# Clean up
pygame.quit()
sys.exit()