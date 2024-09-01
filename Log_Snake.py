print('Welcome to snake!')
import random 
import pygame
import time

def Write(x, y, size, color, text):
    f = pygame.font.SysFont('Comic Sans MS', size)
    t = f.render(text, False, color)
    screen.blit(t, (x, y))

pygame.init()

block_width_x = 15
block_width_y = 15
world_width = 40
world_height = 40


screen = pygame.display.set_mode((world_width * block_width_x,
                                  world_height * block_width_y))

bricks = []
for i in range(world_width):
  bricks.append((i, 0))
  bricks.append((i, world_height - 1))
for i in range(world_height):
  bricks.append((0, i))
  bricks.append((world_width - 1, i))
for i in range(5):
  bricks.append((random.randint(0, world_width - 1),
                 random.randint(0, world_height - 1)))




running = True
snake = [
  (10, 10),
  (11, 10),
  (12, 10)
]


vx = 1
vy = 0

apple_x = 20
apple_y = 25

crash_timer = 0
bite_timer = 0
high_score = 0

while running:
    eating_apple = False
    time.sleep(0.1)
    screen.fill((0, 0, 0))
    if len(snake)>high_score:
        high_score=len(snake)

    Write(40, 500, 30, (200, 200, 200), 'Your length is ' + str(len(snake))+', your high score is ' + str(high_score))

    my_font = pygame.font.SysFont(
        'Comic Sans MS', 50 - crash_timer)
    text_surface = my_font.render(
        'Crashed!', False, (250, 100, 100))
    bite_text_surface = my_font.render("You've Bitten yourself!", False, (255, 255, 0))
    if bite_timer > 0:
        screen.blit(bite_text_surface, (40, 40))
        bite_timer -=1
    if crash_timer > 0:
      screen.blit(text_surface, (40,40))
      crash_timer -= 1
    pygame.draw.rect(
        screen, 
        (250,200,20), 
        pygame.Rect(
            apple_x * block_width_x, apple_y * block_width_y,
            block_width_x - 2, block_width_y - 2))
    for x, y in snake:
        pygame.draw.rect(
            screen, 
            (20,230,20), 
            pygame.Rect(
                x * block_width_x, y * block_width_y,
                block_width_x - 2, block_width_y - 2))
    for x, y in bricks:
        pygame.draw.rect(
            screen, 
            (200,200,200), 
            pygame.Rect(
                x * block_width_x, y * block_width_y,
                block_width_x - 2, block_width_y - 2))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vx = -1
                vy = 0
            if event.key == pygame.K_RIGHT:
                vx = 1
                vy = 0
            if event.key == pygame.K_UP:
                vx = 0
                vy = -1
            if event.key == pygame.K_DOWN:
                vx = 0
                vy = 1

    head_x, head_y = snake[-1]
    head_x += vx
    head_y += vy

    if head_x == apple_x and head_y == apple_y:
        eating_apple = True
        apple_x=0
        apple_y=0
        while (apple_x, apple_y) in bricks:
            apple_x = random.randint(0, 39)
            apple_y = random.randint(0, 39)

    snake += [(head_x, head_y)]
    if not eating_apple:
        snake = snake[1:]

    if snake[-1] in snake[:-1]:
        snake=[snake[-1]]
        bite_timer = 10


    if snake[-1] in bricks:
        x=random.randint(1, world_width-2)
        y=random.randint(1, world_height-2)
        snake=[(x, y)]
        crash_timer = 10

