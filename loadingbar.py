import pygame, sys, threading, random

pygame.init()

# screen settings
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('caption')

font = pygame.font.SysFont('arial', 12)

# load time
time = random.randint(3, 8)

progress_each_second = 10 / time

total_progress, track = 0, 0

loading_bar = pygame.image.load("Loading Bar.png")
loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))

while True:
    screen.fill('#32C2FF')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not track >= (time + 1) * 100:
        for i in range((time + 1) * 100):
            total_progress = i / ((time + 1) * 100) * 720
            loading_bar = pygame.transform.scale(loading_bar, (int(total_progress), 100))
            loading_bar.fill('#25E6B9')
            loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))
            screen.blit(loading_bar, loading_bar_rect)
            pygame.display.update()
            track += 1
