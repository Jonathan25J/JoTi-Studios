import pygame, sys, time, random, os

pygame.init()

# Al eerder uitgelegd
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Asteroid Shooting')
pygame.display.set_icon(pygame.image.load('assets/objects/asteroid.png'))
AAS = pygame.font.Font("assets/fonts/AAS.ttf", 40)
game_speed, lt, score = 0, 0, 0


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y

        self.image = pygame.transform.scale(pygame.image.load('assets/objects/asteroid.png'), (119, 85))
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        self.x -= game_speed

        self.rect = self.image.get_rect(center=(self.x, self.y))


# Dit ook allemaal
def RetrieveMusic():
    pygame.mixer.fadeout(10)
    pygame.mixer.Sound('assets/music/' + random.choice(os.listdir('assets/music'))).play(-1).set_volume(0.03)


obstacles = pygame.sprite.Group()

RetrieveMusic()

while True:
    screen.blit(pygame.transform.scale(pygame.image.load('assets/background/background.jpg'), (1280, 720)), (0, 0))

    # Verandert hoe de muis eruit ziet
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
    clock = int((pygame.time.get_ticks() - lt) / 1000) / 2

    # Game speed gebaseerd op de tijd
    game_speed = clock * 0.1 + 0.5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Astroids
    if random.randint(1, 1000) < 20 + clock:
        obstacle = Object(1400, random.randint(30, 700))
        obstacles.add(obstacle)

    # Zelfde soort systeem als bij cleopatra om te decteren igv als de muis op de asteroid klikt
    if pygame.mouse.get_pressed()[0]:
        for s in obstacles.sprites():
            if pygame.mouse.get_pos()[0] - s.rect.x in range(-5,
                                                             80) \
                    and pygame.mouse.get_pos()[1] - s.rect.y in range(
                -60, 60):
                s.kill()
                score += 1

    # Als de asteroid voorbij de border is dan is de game afgelopen
    for s in obstacles.sprites():
        if s.rect.x < 0:
            lt = pygame.time.get_ticks()
            obstacles.empty()
            print('Your last score was ' + str(score))
            score = 0
            RetrieveMusic()

    obstacles.update()
    obstacles.draw(screen)
    screen.blit(
        AAS.render('Current score: ', True,
                   '#fc0303'),
        (5, 670))

    screen.blit(
        AAS.render(str(score), True,
                   '#ffffff'),
        (340, 670))
    pygame.display.update()
