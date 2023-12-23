import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SHIP_SPEED = 5

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cosmic Crust Cruiser")

# Load the background image
background_img = pygame.image.load('background.png')
#background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))


# Load spaceship image
ship_img = pygame.image.load("spaceship.png")
ship_rect = ship_img.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

# Load asteroid image
asteroid_img = pygame.image.load("asteroid.png")
asteroid_rect = asteroid_img.get_rect(topleft=(800, random.randint(0, SCREEN_HEIGHT)))
asteroids = []

# Function to create a new asteroid
def create_asteroid():
    new_asteroid = asteroid_img.get_rect(topleft=(random.randint(800, 1600), random.randint(0, 600)))
    asteroids.append(new_asteroid)

# Function to move and draw asteroids
def move_asteroids():
    for asteroid in asteroids:
        asteroid.x -= 5  # Move asteroid to the left
        if asteroid.x < -50:  # If asteroid is off-screen, remove it
            asteroids.remove(asteroid)
        screen.blit(asteroid_img, asteroid)

def detect_collisions():
    for asteroid in asteroids:
        if ship_rect.colliderect(asteroid):  # Check if the spaceship rectangle collides with an asteroid
            return True
    return False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Movement keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ship_rect.left > 0:
        ship_rect.x -= SHIP_SPEED
    if keys[pygame.K_RIGHT] and ship_rect.right < SCREEN_WIDTH:
        ship_rect.x += SHIP_SPEED
    if keys[pygame.K_UP] and ship_rect.top > 0:
        ship_rect.y -= SHIP_SPEED
    if keys[pygame.K_DOWN] and ship_rect.bottom < SCREEN_HEIGHT:
        ship_rect.y += SHIP_SPEED

    # Obstacle: Create a new asteroid every so often
    if random.randint(1, 50) == 1:
        create_asteroid()
    move_asteroids()
    #if detect_collisions():
        #print("Collision detected! Game over.")
          
    # Drawing
    #screen.fill((0,0,0)) # Fills the screen with black space
    screen.blit(background_img, (0, 0))
    screen.blit(ship_img, ship_rect) # Draws the spaceship

    pygame.display.flip() # Update the display

# Clean up
pygame.quit()
sys.exit()