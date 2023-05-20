import pygame
import random
import time

# Screen size
WIDTH, HEIGHT = 600, 600

# Colors
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0,255,0)
BLUE = (50, 153, 213)

# Snake parameters
snake_pos = [100, 50]
snake_speed = [10, 0]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, WIDTH//10)*10, random.randrange(1, HEIGHT//10)*10]
food_spawn = True
score = 0
FPS = 10  # <--- NEW: Initial speed

# Initialize Pygame
pygame.init()

# Set up display
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WIDTH/2, HEIGHT/4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and snake_speed[1] != 10:
        snake_speed = [0, -10]
    if keys[pygame.K_DOWN] and snake_speed[1] != -10:
        snake_speed = [0, 10]
    if keys[pygame.K_LEFT] and snake_speed[0] != 10:
        snake_speed = [-10, 0]
    if keys[pygame.K_RIGHT] and snake_speed[0] != -10:
        snake_speed = [10, 0]

    snake_pos[0] += snake_speed[0]
    snake_pos[1] += snake_speed[1]

    # Game over conditions
    if snake_pos[0] >= WIDTH or snake_pos[0] < 0 or snake_pos[1] >= HEIGHT or snake_pos[1] < 0:
        game_over()
    for body_part in snake_body[1:]:
        if snake_pos == body_part:
            game_over()

    if not food_spawn:
        food_pos = [random.randrange(1, WIDTH//10)*10, random.randrange(1, HEIGHT//10)*10]
    food_spawn = True

    screen.fill(BLUE)

    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, WHITE, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    if snake_pos == food_pos:
        score += 1
        food_spawn = False
        snake_body.insert(0, list(snake_pos))
        FPS += 1  # <--- NEW: Increase speed each time the snake eats
    else:
        snake_body.pop()

    snake_body.insert(0, list(snake_pos))

    pygame.display.update()
    clock.tick(FPS)  # <--- MODIFIED: Control
