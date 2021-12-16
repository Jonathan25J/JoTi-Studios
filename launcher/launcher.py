import pygame, sys, random, time, os

# Start
pygame.init()

# Scherm grootte
screen = pygame.display.set_mode((1280, 720))

# Titel van het scherm
pygame.display.set_caption('JoTi Studios')

# Achtergrond
pygame.display.set_icon(pygame.transform.scale(pygame.image.load('assets/promotescreen/logo.PNG'), (30, 30)))

# Muis onzichtbaar maken
pygame.mouse.set_visible(False)

# De fonts
font_s = pygame.font.SysFont('impact', 120)
font_p = pygame.font.SysFont('arial', 30)

# Titel scherm
screen.fill('white', (0, 0, screen.get_width(), screen.get_height()))
screen.blit(pygame.transform.scale(pygame.image.load('assets/promotescreen/logo.PNG'), (600, 600)),
            pygame.image.load('assets/promotescreen/logo.PNG').get_rect(midleft=(325, 200)))

# Scherm updaten
pygame.display.update()

# Cooldown van 3 seconden
time.sleep(3)

# Load time
l_time = random.randint(2, 4)

# Percentage per seconde
pes = 10 / l_time

# Totale progress en tracken van hoever het is
tp, track = 0, 0

# Random color
color = '#' + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])

# images
screen.blit(pygame.transform.scale(pygame.image.load('assets/loadscreen/background.jpg'), (1280, 720)), (0, 0))

loadingBar = pygame.image.load('assets/loadscreen/LoadingBar.png')

gamebox = pygame.image.load('assets/gamesoverview/list/gamebox.png')

# Load loop
while True:
    # Sluit het systeem af als je op het kruisje drukt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Als de tijd bij een bepaalde hoogte is dan stopt hij de loop
    if track >= (l_time + 1) * 100:
        break

    # Progress bar
    for i in range((l_time + 1) * 100):

        # Berekenen lengte progressbar
        tp = i / ((l_time + 1) * 100) * 620
        bar = pygame.transform.scale(loadingBar, (int(tp), 50))

        # Vullen met de kleur
        bar.fill(color)
        # screen.blit(pygame.transform.scale(pygame.image.load('assets/loadscreen/background.jpg'),
        # (1280, 720)), (0, 0))
        # screen.fill(color, (570, 600, 130, 50))

        # Achtergrond opnieuw inladen
        screen.blit(pygame.transform.scale(pygame.image.load('assets/loadscreen/background.jpg'), (1280, 720)), (0, 0))

        # Laadbar
        screen.blit(bar, loadingBar.get_rect(midleft=(300, 860)))
        screen.blit(pygame.transform.scale(pygame.image.load('assets/loadscreen/ldb_background.png'), (620, 50)),
                    loadingBar.get_rect(midleft=(300, 860)))

        # Laad balk
        screen.blit(font_p.render(str(round(tp / 6.2 + 0.1, 1)) + '%', True, 'white'), (580, 600))

        # Scherm weer updaten
        pygame.display.update()

        # Onderdeel van bijhouden van tijd
        track += 15

# Games
# Vertraging van 1 min
time.sleep(1)

# Muis weer zichtbaar
pygame.mouse.set_visible(True)

# Achtergrond
screen.blit(pygame.transform.scale(pygame.image.load('assets/gamesoverview/list/games_background.jpg'), (1280, 720)),
            (0, 0))

# Afsluit functie
def close():
    pygame.quit()
    sys.exit()


# First line, de game boxen
screen.blit(pygame.transform.scale(pygame.image.load('assets/gamesoverview/list/gamebox_1.png'), (200, 200)),
            gamebox.get_rect(topleft=(100, 60)))

screen.blit(pygame.transform.scale(pygame.image.load('assets/gamesoverview/list/gamebox_2.png'), (200, 200)),
            gamebox.get_rect(topleft=(550, 60)))

screen.blit(pygame.transform.scale(pygame.image.load('assets/gamesoverview/list/gamebox_3.png'), (200, 200)),
            gamebox.get_rect(topleft=(1000, 60)))

# Second line
screen.blit(pygame.transform.scale(pygame.image.load('assets/gamesoverview/list/gamebox_4.png'), (200, 200)),
            gamebox.get_rect(topleft=(100, 460)))

screen.blit(pygame.transform.scale(gamebox, (200, 200)), gamebox.get_rect(topleft=(550, 460)))
screen.blit(pygame.transform.scale(gamebox, (200, 200)), gamebox.get_rect(topleft=(1000, 460)))

pygame.display.update()

while True:
    # Voor wanneer je weer op het kruisje drukt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Coords bij muisklik
    if pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Game 1
        # de x en y van de box van de game
        if mouse_x in range(100, 300) and mouse_y in range(60, 250):
            # Verandert de directory waar vanuit uitgevoerd wordt
            os.chdir(os.getcwd() + '/assets/gamesoverview/cleopatra')

            # Opent vanuit die nieuwe directory de start.py file
            exec(open('start.py').read())
            close()

        # Game 2
        if mouse_x in range(550, 750) and mouse_y in range(60, 250):
            os.chdir(os.getcwd() + '/assets/gamesoverview/astroidshooter')
            exec(open('start.py').read())
            close()

        # Game 3
        if mouse_x in range(1000, 1200) and mouse_y in range(60, 250):
            os.chdir(os.getcwd() + '/assets/gamesoverview/tic-tac-toe')
            exec(open('start.py').read())
           # close()

        # Game 4
        if mouse_x in range(100, 300) and mouse_y in range(460, 650):
            os.chdir(os.getcwd() + '/assets/gamesoverview/snake')
            exec(open('start.py').read())
            close()

        # Game 5
        if mouse_x in range(550, 750) and mouse_y in range(460, 650):
            close()

        # Game 6
        if mouse_x in range(1000, 1200) and mouse_y in range(460, 650):
            close()
