import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("my first pygame")

# 이미지 로딩
image = pygame.image.load('snake.jpg')
image_rect = image.get_rect()
image_rect.topleft = (100, 100)

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  
    screen.fill((160, 32, 240))
    screen.blit(image, image_rect)

    pygame.draw.rect(screen, (255, 0, 0), (150, 150, 200, 100))
    pygame.draw.circle(screen, (0, 255, 0), (400, 300), 50)
    pygame.draw.line(screen, (0, 0, 255), (0, 0), (800, 600), 5)

    pygame.display.flip()

pygame.quit()
sys.exit()
