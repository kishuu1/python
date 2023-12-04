import pygame
import time
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
FPS = 15
BLOCK_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control the game loop speed
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 30)

# Snake initial position and speed
snake_block = 10
snake_speed = 15

# Initialize snake
snake = [(WIDTH / 2, HEIGHT / 2)]
snake_direction = "RIGHT"

# Initialize food
food = [random.randrange(1, (WIDTH // snake_block)) * snake_block,
        random.randrange(1, (HEIGHT // snake_block)) * snake_block]

# Functions
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], snake_block, snake_block])

def draw_food(food):
    pygame.draw.rect(screen, RED, [food[0], food[1], snake_block, snake_block])

def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"
            elif event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"

    # Move the snake
    if snake_direction == "UP":
        snake[0] = (snake[0][0], snake[0][1] - snake_block)
    elif snake_direction == "DOWN":
        snake[0] = (snake[0][0], snake[0][1] + snake_block)
    elif snake_direction == "LEFT":
        snake[0] = (snake[0][0] - snake_block, snake[0][1])
    elif snake_direction == "RIGHT":
        snake[0] = (snake[0][0] + snake_block, snake[0][1])

    # Check for collisions with walls
    if snake[0][0] >= WIDTH or snake[0][0] < 0 or snake[0][1] >= HEIGHT or snake[0][1] < 0:
        game_over = True

    # Check for collisions with itself
    for segment in snake[1:]:
        if snake[0][0] == segment[0] and snake[0][1] == segment[1]:
            game_over = True

    # Check if the snake eats the food
    if snake[0][0] == food[0] and snake[0][1] == food[1]:
        food = [random.randrange(1, (WIDTH // snake_block)) * snake_block,
                random.randrange(1, (HEIGHT // snake_block)) * snake_block]
    else:
        # If not, remove the last segment of the snake
        snake.pop()

    # Draw everything
    screen.fill(BLACK)
    draw_snake(snake)
    draw_food(food)

    # Update the display
    pygame.display.update()

    # Control the game speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
