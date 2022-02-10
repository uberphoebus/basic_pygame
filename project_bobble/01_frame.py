import pygame

pygame.init()

# 화면, 제목
screen_width, screen_height = 448, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Puzzle Bobble')

# FPS
clock = pygame.time.Clock()


# 게임루프
running = True
while running:
    clock.tick(60) # FPS 60
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

