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
yellow = pygame.Color(200, 200, 0)

player1_color = green
player2_color = yellow

# Window size and title
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake IO")

# Snake initial position and properties
symbol_size = 13
snake1_speed = 5
snake2_speed = 5
snake_length = 10

snake1_position = [100, 50]
snake2_position = [width-100, 50]

snake1_body = []
for l in range(0, snake_length):
    snake1_body.insert(0, (snake1_position[0], snake1_position[1]+2*symbol_size))

snake2_body = []
for l in range(0, snake_length):
    snake2_body.insert(0, (snake2_position[0], snake2_position[1]+2*symbol_size))

# Food initial positions
foods = []
food_count = 5

for _ in range(food_count):
    food_position = [random.randrange(1, (width // symbol_size)) * symbol_size, random.randrange(1, (height // symbol_size)) * symbol_size]
    foods.append(food_position)

# Initial direction
direction1 = 'RIGHT'
snake1_direction = direction1

direction2 = 'LEFT'
snake2_direction = direction2

# Score
score1 = 0
score2 = 0

# Game Over flag
game_over = False

# Clock for controlling the game speed
clock = pygame.time.Clock()

# Function to display score on the screen
def show_score():
    font = pygame.font.SysFont('consolas', 20)
    score1_surface = font.render('Player 1 Score: ' + str(score1), True, player1_color)
    score2_surface = font.render('Player 2 Score: ' + str(score2), True, player2_color)
    window.blit(score1_surface, (10, 10))
    window.blit(score2_surface, (width - score2_surface.get_width() - 10, 10))


# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake1_direction = 'RIGHT'
            if event.key == pygame.K_LEFT:
                snake1_direction = 'LEFT'
            if event.key == pygame.K_UP:
                snake1_direction = 'UP'
            if event.key == pygame.K_DOWN:
                snake1_direction = 'DOWN'
            if event.key == pygame.K_d:
                snake2_direction = 'RIGHT'
            if event.key == pygame.K_a:
                snake2_direction = 'LEFT'
            if event.key == pygame.K_w:
                snake2_direction = 'UP'
            if event.key == pygame.K_s:
                snake2_direction = 'DOWN'
            if event.key == pygame.K_SPACE:
                score2 += 20 

    # Update snake1 position
    if snake1_direction == 'RIGHT':
        snake1_position[0] += snake1_speed
    if snake1_direction == 'LEFT':
        snake1_position[0] -= snake1_speed
    if snake1_direction == 'UP':
        snake1_position[1] -= snake1_speed
    if snake1_direction == 'DOWN':
        snake1_position[1] += snake1_speed

    # Update snake2 position
    if snake2_direction == 'RIGHT':
        snake2_position[0] += snake2_speed
    if snake2_direction == 'LEFT':
        snake2_position[0] -= snake2_speed
    if snake2_direction == 'UP':
        snake2_position[1] -= snake2_speed
    if snake2_direction == 'DOWN':
        snake2_position[1] += snake2_speed

    # Snake body mechanism
    snake1_body.insert(0, list(snake1_position))
    snake2_body.insert(0, list(snake2_position))

    close_distance = symbol_size

    snake1_found_food = None
    for food_position in foods :
        if (abs(snake1_position[0] - food_position[0]) < close_distance and (abs(snake1_position[1] - food_position[1]) < close_distance)) :
            snake1_found_food = food_position
            continue

    snake2_found_food = None
    for food_position in foods :
        if (abs(snake2_position[0] - food_position[0]) < close_distance and (abs(snake2_position[1] - food_position[1]) < close_distance)) :
            snake2_found_food = food_position
            continue

    if (snake1_found_food != None) :
        score1 += 1
        foods.remove(snake1_found_food)
    else:
        snake1_body.pop()

    if (snake2_found_food != None) :
        score2 += 1
        foods.remove(snake2_found_food)
    else:
        snake2_body.pop()

    # Food spawn
    if len(foods) < food_count:
        food_position = [random.randrange(1, (width // symbol_size)) * symbol_size, random.randrange(1, (height // symbol_size)) * symbol_size]
        foods.append(food_position)

    # Background
    window.fill(black)

    # Snake 1 body
    for pos in snake1_body:
        pygame.draw.rect(window, player1_color, pygame.Rect(pos[0], pos[1], symbol_size, symbol_size))

    pygame.draw.rect(window, red, pygame.Rect(snake1_body[0][0], snake1_body[0][1], symbol_size, symbol_size))

    # Snake 2 body
    for pos in snake2_body:
        pygame.draw.rect(window, player2_color, pygame.Rect(pos[0], pos[1], symbol_size, symbol_size))

    pygame.draw.rect(window, red, pygame.Rect(snake2_body[0][0], snake2_body[0][1], symbol_size, symbol_size))

    # Snake food
    food_color = white
    if (score1 > 0 and score1 % 10 == 0):
        food_color = blue

    for food_position in foods:
        pygame.draw.rect(window, food_color, pygame.Rect(food_position[0], food_position[1], symbol_size, symbol_size))

    # Wrap snake 1
    if snake1_position[0] < 0 :
        snake1_position[0] = width - symbol_size
    if snake1_position[0] > width - symbol_size :
        snake1_position[0] = 0
    if snake1_position[1] < 0 :
        snake1_position[1] = height - symbol_size
    if snake1_position[1] > height - symbol_size :
        snake1_position[1] = 0

    # Wrap snake 2
    if snake2_position[0] < 0 :
        snake2_position[0] = width - symbol_size
    if snake2_position[0] > width - symbol_size :
        snake2_position[0] = 0
    if snake2_position[1] < 0 :
        snake2_position[1] = height - symbol_size
    if snake2_position[1] > height - symbol_size :
        snake2_position[1] = 0

    # Game Over conditions
    crash_distance = symbol_size / 2
    for snake2pos in snake2_body:
      if (abs(snake1_position[0] - snake2pos[0]) < crash_distance and abs(snake1_position[1] - snake2pos[1]) < crash_distance):
          game_over = True
          score2 += 20
    
    for snake1pos in snake1_body:
      if (abs(snake2_position[0] - snake1pos[0]) < crash_distance and abs(snake2_position[1] - snake1pos[1]) < crash_distance):
          game_over = True
          score1 += 20

    # Display score
    show_score()

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
show_score()
pygame.display.update()

time.sleep(20)

pygame.quit()
quit()
