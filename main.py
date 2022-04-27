from yut_1 import *

if __name__ == '__main__':
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    push = button()
            if event.type == pygame.KEYUP:
                push1 = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                push = button()
            if event.type == pygame.MOUSEBUTTONUP:
                push = False
        redraw(push)
        pygame.display.update()  # 게임 화면을 다시 그리기
    pygame.quit()