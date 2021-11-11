import pygame, sys, random

# Start
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('JoTi Studios')
font = pygame.font.SysFont('arial', 12)

# Load time
time = random.randint(5, 10)
pes = 10 / time
tp, track = 0, 0

# Random color
color = '#'+''.join([random.choice('ABCDEF0123456789') for i in range(6)])

# Images
background = pygame.image.load('screen.jpg')
screen.blit(pygame.transform.scale(background, (1280, 720)), (0, 0))

loadingBar = pygame.image.load('loadingbar.png')

loadingBar_b = pygame.image.load('ldb_background.png')
# Load loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if track >= (time + 1) * 100:
        continue
    for i in range((time + 1) * 100):
        tp = i / ((time + 1) * 100) * 620
        bar = pygame.transform.scale(loadingBar, (int(tp), 50)); bar.fill(color)
        screen.blit(bar, loadingBar.get_rect(midleft=(300, 860))); screen.blit(pygame.transform.scale(loadingBar_b, (620, 50)), loadingBar.get_rect(midleft=(300, 860)))
        pygame.display.update()
        track += 1
