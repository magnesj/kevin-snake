## snake by kevin

import pygame
import time
import random

pygame.init()

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Window size and title
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake IO")

# Snake initial position and properties
symbol_size = 13
snake_position = [100, 50]
snake_body = [snake_position, [snake_position[0], snake_position[1]+symbol_size], [snake_position[0], snake_position[1]+2*symbol_size]]
snake_speed = 5


# Food initial position
food_position = [random.randrange(1, (width // symbol_size)) * symbol_size, random.randrange(1, (height // symbol_size)) * symbol_size]
food_spawn = True

# Initial direction
direction = 'RIGHT'
change_to = direction

# Score
score = 0

# Game Over flag
game_over = False

# Clock for controlling the game speed
clock = pygame.time.Clock()

# Function to display score on the screen
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (width / 10, 15)
    else:
        score_rect.midtop = (width / 2, height / 1.25)
    window.blit(score_surface, score_rect)

def show_food(choice, color, font, size, food_position):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Food: ' + str(food_position), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (width / 10, height / 5)
    else:
        score_rect.midtop = (width / 2, height / 1.25)
    window.blit(score_surface, score_rect)

def show_snake(choice, color, font, size, snake_position):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('snake: ' + str(snake_position), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (width / 8, height / 3)
    else:
        score_rect.midtop = (width / 2, height / 1.25)
    window.blit(score_surface, score_rect)

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Making sure the snake cannot move in the opposite direction instantaneously
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    # Update snake position [x, y]
    if direction == 'RIGHT':
        snake_position[0] += snake_speed
    if direction == 'LEFT':
        snake_position[0] -= snake_speed
    if direction == 'UP':
        snake_position[1] -= snake_speed
    if direction == 'DOWN':
        snake_position[1] += snake_speed

    # Snake body mechanism
    snake_body.insert(0, list(snake_position))

    close_distance = symbol_size

    x_is_close = False
    y_is_close = False
    if abs(snake_position[0] - food_position[0]) < close_distance :
        x_is_close=True

    if abs(snake_position[1] - food_position[1]) < close_distance :
        y_is_close=True

    if x_is_close and y_is_close:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Food spawn
    if not food_spawn:
        food_position = [random.randrange(1, (width // symbol_size)) * symbol_size, random.randrange(1, (height // symbol_size)) * symbol_size]
    food_spawn = True

    # Background
    window.fill(black)

    # Snake body
    for pos in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], symbol_size, symbol_size))

    pygame.draw.rect(window, red, pygame.Rect(snake_body[0][0], snake_body[0][1], symbol_size, symbol_size))

    # Snake food
    food_color = white
    if (score > 0 and score % 10 == 0):
        food_color = blue

    pygame.draw.rect(window, food_color, pygame.Rect(food_position[0], food_position[1], symbol_size, symbol_size))

    # Game Over conditions
    if snake_position[0] < 0 :
        snake_position[0] = width - symbol_size
    if snake_position[0] > width - symbol_size :
        snake_position[0] = 0
    if snake_position[1] < 0 :
        snake_position[1] = height - symbol_size
    if snake_position[1] > height - symbol_size :
        snake_position[1] = 0

    #for block in snake_body[1:]:
    #    if snake_position[0] == block[0] and snake_position[1] == block[1]:
     #       game_over = Trueq

    # Display score
    show_score(1, white, 'consolas', 20)
    #show_food(1, white, 'consolas', 20, food_position)
    #show_snake(1, white, 'consolas', 20, snake_position)


    # Refresh game screen
    pygame.display.update()

    # Frame speed
    clock.tick(20)

# Game over message
font = pygame.font.SysFont('consolas', 60)
game_over_surface = font.render('Game Over', True, red)
game_over_rect = game_over_surface.get_rect()
game_over_rect.midtop = (width / 2, height / 4)
window.blit(game_over_surface, game_over_rect)
show_score(0, red, 'consolas', 20)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()
