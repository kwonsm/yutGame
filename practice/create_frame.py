import pygame

pygame.init()

screen_width = 720
screen_height = 1080
screen = pygame.display.set_mode((screen_height, screen_width))

pygame.display.set_caption(("yut Game"))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()