# Written by ChatGPT with minor modifications by me

import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
ARM_LENGTH = 100
ROTATION_SPEED = 0.02
ROTATION_SPEED2 = 0.05

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Arms")

# Initial angles for the two arms
angle1 = 0
angle2 = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Calculate the positions of the ends of the arms
    x1 = WIDTH // 2 + ARM_LENGTH * math.cos(angle1)
    y1 = HEIGHT // 2 + ARM_LENGTH * math.sin(angle1)

    x2 = x1 + ARM_LENGTH * math.cos(angle2)
    y2 = y1 + ARM_LENGTH * math.sin(angle2)

    # Draw the arms
    pygame.draw.line(screen, WHITE, (WIDTH // 2, HEIGHT // 2), (int(x1), int(y1)), 5)
    pygame.draw.line(screen, WHITE, (int(x1), int(y1)), (int(x2), int(y2)), 5)

    # Update angles for rotation
    angle1 += ROTATION_SPEED
    angle2 += ROTATION_SPEED2

    # Update the display
    pygame.display.flip()

    # Control the speed of the simulation
    pygame.time.Clock().tick(120)


