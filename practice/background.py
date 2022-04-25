import pygame

pygame.init()

screen_width = 720
screen_height = 1080
screen = pygame.display.set_mode((screen_height, screen_width))

pygame.display.set_caption(("yut Game"))

background = pygame.image.load("D:/project/yut Game/background/table.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0)) #배경 그리기

    pygame.display.update() #게임 화면을 다시 그리기
pygame.quit()
