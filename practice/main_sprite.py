import pygame

pygame.init()

screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption(("yut Game"))

background = pygame.image.load("D:/project/yut Game/background/table.png")

yut1 = pygame.image.load("D:/project/yut Game/image/yut1.png")
yut_size = yut1.get_rect().size
yut_width = yut_size[0]
yut_height = yut_size[1]
yut1_x_pos = (3 * screen_width / 9) - (yut_width / 2)
yut1_y_pos = (screen_height / 2) - (yut_height / 2)

yut2 = pygame.image.load("D:/project/yut Game/image/yut1.png")
yut2_x_pos = (4 * screen_width / 9) - (yut_width / 2)
yut2_y_pos = (screen_height / 2) - (yut_height / 2)

yut3 = pygame.image.load("D:/project/yut Game/image/yut1.png")
yut3_x_pos = (5 * screen_width / 9) - (yut_width / 2)
yut3_y_pos = (screen_height / 2) - (yut_height / 2)

yut4 = pygame.image.load("D:/project/yut Game/image/yut1.png")
yut4_x_pos = (6 * screen_width / 9) - (yut_width / 2)
yut4_y_pos = (screen_height / 2) - (yut_height / 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0)) #배경 그리기
    screen.blit(yut1, (yut1_x_pos, yut1_y_pos))
    screen.blit(yut2, (yut2_x_pos, yut2_y_pos))
    screen.blit(yut3, (yut3_x_pos, yut3_y_pos))
    screen.blit(yut4, (yut4_x_pos, yut4_y_pos))
    pygame.display.update() #게임 화면을 다시 그리기
pygame.quit()
