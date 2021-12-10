import pygame, sys, random, time, os

# Start
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('JoTi Studios')
pygame.display.set_icon(pygame.transform.scale(pygame.image.load('assets/promotescreen/logo.PNG'), (30, 30)))
pygame.mouse.set_visible(False)
font_s = pygame.font.SysFont('impact', 120)
font_p = pygame.font.SysFont('arial', 30)

# Promote screen
screen.fill('white', (0, 0, screen.get_width(), screen.get_height()))
screen.blit(pygame.transform.scale(pygame.image.load('assets/promotescreen/logo.PNG'), (600, 600)),
            pygame.image.load('assets/promotescreen/logo.PNG').get_rect(midleft=(325, 200)))
pygame.display.update()
time.sleep(3)

# Load time
l_time = random.randint(6, 10)
pes = 10 / l_time
tp, track = 0, 0

# Random color
color = '#' + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])

# Images
screen.blit(pygame.transform.scale(pygame.image.load('assets/loadscreen/background.jpg'), (1280, 720)), (0, 0))

loadingBar = pygame.image.load('assets/loadscreen/LoadingBar.png')

gamebox = pygame.image.load('assets/gamesoverview/list/gamebox.png')

# Load loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if track >= (l_time + 1) * 100:
        break

    for i in range((l_time + 1) * 100):
        tp = i / ((l_time + 1) * 100) * 620
        bar = pygame.transform.scale(loadingBar, (int(tp), 50))
        bar.fill(color)
        # screen.blit(pygame.transform.scale(pygame.image.load('assets/loadscreen/background.jpg'),
        # (1280, 720)), (0, 0))
        screen.fill(color, (570, 600, 130, 50))
        screen.blit(bar, loadingBar.get_rect(midleft=(300, 860)))
        screen.blit(pygame.transform.scale(pygame.image.load('assets/loadscreen/ldb_background.png'), (620, 50)),
                    loadingBar.get_rect(midleft=(300, 860)))
        screen.blit(font_p.render(str(round(tp / 6.2 + 0.1, 1)) + '%', True, 'white'), (580, 600))
        pygame.display.update()
        track += 1

# Games
time.sleep(1)
pygame.mouse.set_visible(True)
screen.blit(pygame.transform.scale(pygame.image.load('assets/gamesoverview/list/games_background.jpg'), (1280, 720)),
            (0, 0))


def close():
    pygame.quit()
    sys.exit()


# First line
screen.blit(pygame.transform.scale(pygame.image.load('assets/gamesoverview/list/gamebox_1.png'), (200, 200)),
            gamebox.get_rect(topleft=(100, 60)))

screen.blit(pygame.transform.scale(pygame.image.load('assets/gamesoverview/list/gamebox_2.png'), (200, 200)),
            gamebox.get_rect(topleft=(550, 60)))

screen.blit(pygame.transform.scale(gamebox, (200, 200)), gamebox.get_rect(topleft=(1000, 60)))

# Second line
screen.blit(pygame.transform.scale(gamebox, (200, 200)), gamebox.get_rect(topleft=(100, 460)))
screen.blit(pygame.transform.scale(gamebox, (200, 200)), gamebox.get_rect(topleft=(550, 460)))
screen.blit(pygame.transform.scale(gamebox, (200, 200)), gamebox.get_rect(topleft=(1000, 460)))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Game 1
        if mouse_x in range(100, 300) and mouse_y in range(60, 250):
            print('game 1')
            os.chdir(os.getcwd() + '/assets/gamesoverview/cleopatra')
            exec(open('start.py').read())

        # Game 2
        if mouse_x in range(550, 750) and mouse_y in range(60, 250):
            print('game 2')
            os.chdir(os.getcwd() + '/assets/gamesoverview/astroidshooter')
            exec(open('start.py').read())
            close()

        # Game 3
        if mouse_x in range(1000, 1200) and mouse_y in range(60, 250):
            print('game 3')
            close()

        # Game 4
        if mouse_x in range(100, 300) and mouse_y in range(460, 650):
            print('game 4')
            close()

        # Game 5
        if mouse_x in range(550, 750) and mouse_y in range(460, 650):
            print('game 5')
            close()

        # Game 6
        if mouse_x in range(1000, 1200) and mouse_y in range(460, 650):
            print('game 6')
            close()
