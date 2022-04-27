import pygame
import random

pygame.init()

screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption(("yut Game"))

background = pygame.image.load("D:/project/yut Game/background/table.png")
running = True

yut1 = pygame.image.load("D:/project/yut Game/entity/yut1.png")
yut2 = pygame.image.load("D:/project/yut Game/entity/yut3.png")
yut_size = yut1.get_rect().size
yut_width = yut_size[0]
yut_height = yut_size[1]
yut = [0, 0, 0, 0]

button1 = pygame.image.load("D:/project/yut Game/entity/red button.png")
button2 = pygame.image.load("D:/project/yut Game/entity/green button.png")
button_size = button1.get_rect().size
button_width = button_size[0]
button_height = button_size[1]
button_x_pos = (8 * screen_width / 9) - (button_width / 2)
button_y_pos = (6 * screen_height / 7) - (button_height / 2)
push = False


def redraw(push):
    screen.blit(background, (0, 0))  # 배경 그리기
    if push:
        screen.blit(button1, (button_x_pos, button_y_pos))
    else:
        screen.blit(button2, (button_x_pos, button_y_pos))
    for i in range(3, 6 + 1):
        if yut[i - 3] == 0:
            screen.blit(yut1, ((i * screen_width / 9) - (yut_width / 2), (screen_height / 2) - (yut_height / 2)))
        else:
            screen.blit(yut2, ((i * screen_width / 9) - (yut_width / 2), (screen_height / 2) - (yut_height / 2)))


def button():
    push = True
    yut.clear()
    for i in range(4):
        yut.append(random.randrange(0, 1 + 1))
    print(yut)
    return push



