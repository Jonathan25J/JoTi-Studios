import pygame
import sys
import random
import os

# Start
pygame.init()
pygame.display.set_icon(pygame.transform.scale(pygame.image.load('assets/characters/wizard_1.png'), (90, 90)))
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Cleopatra")
font = pygame.font.Font("assets/fonts/Font.ttf", 40)
font_1 = pygame.font.Font("assets/fonts/Font.ttf", 13)
theme = random.randint(1, 3)
character = random.choice(['wizard', 'lizard', 'knight', 'elf'])
background = pygame.transform.scale(pygame.image.load('assets/backgrounds/background_' + str(theme) + '.png'),
                                    (1280, 720))

bg_x = 0
time_track = 0
up_press = False
down_press = False
lgt = 0
score = 0


def RetrieveMusic():
    pygame.mixer.fadeout(10)
    pygame.mixer.Sound('assets/music/' + random.choice(os.listdir('assets/music'))).play(-1).set_volume(0.03)


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.walking = []

        self.walking.append(
            pygame.transform.scale(pygame.image.load('assets/characters/' + character + '_1.png'), (150, 150)))
        self.walking.append(
            pygame.transform.scale(pygame.image.load('assets/characters/' + character + '_2.png'), (150, 150)))
        self.walking.append(
            pygame.transform.scale(pygame.image.load('assets/characters/' + character + '_3.png'), (150, 150)))
        self.walking.append(
            pygame.transform.scale(pygame.image.load('assets/characters/' + character + '_4.png'), (150, 150)))

        self.x = x
        self.y = y

        self.current_motion = 0

        self.image = self.walking[self.current_motion]
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        self.current_motion += 0.20
        if self.current_motion >= 4:
            self.current_motion = 0
        self.image = self.walking[int(self.current_motion)]

    def up(self):
        if self.rect.centery == 510:
            self.rect.centery -= 120
        elif self.rect.centery == 635:
            self.rect.centery -= 125

    def down(self):
        if self.rect.centery == 510:
            self.rect.centery += 125
        elif self.rect.centery == 390:
            self.rect.centery += 120


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y1, y2, y3):
        super().__init__()

        self.x = x
        self.y = random.choice([y1, y2, y3])
        self.image = pygame.transform.scale(pygame.image.load('assets/obstacles/obstacle_' + str(theme) + '.png'),
                                            (128, 120))
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        self.x -= game_speed

        self.rect = self.image.get_rect(center=(self.x, self.y))


characterS = Character(150, 635)
characterS_group = pygame.sprite.GroupSingle()
characterS_group.add(characterS)

obstacles_group = pygame.sprite.Group()

RetrieveMusic()


def e_a_b():
    global score, lgt, game_speed, theme, character, background, characterS
    lgt = pygame.time.get_ticks()
    game_speed = 0
    obstacles_group.empty()
    print('Your highscore was ' + str(int(score)))
    score = 0
    RetrieveMusic()
    theme = random.randint(1, 3)
    characterS_group.empty()
    character = random.choice(['wizard', 'lizard', 'knight', 'elf'])
    characterS = Character(150, 635)
    characterS_group.add(characterS)
    background = pygame.transform.scale(
        pygame.image.load('assets/backgrounds/background_' + str(theme) + '.png'),
        (1280, 720))


# Loop
while True:
    game_speed = 1 + ((pygame.time.get_ticks() - lgt) / 100 * 0.025)
    score += 0.1

    keys = pygame.key.get_pressed()

    if not keys[pygame.K_w]:
        up_press = False
    if not keys[pygame.K_s]:
        down_press = False

    if keys[pygame.K_w]:
        if not up_press:
            characterS.up()
            up_press = True

    if keys[pygame.K_s]:
        if not down_press:
            characterS.down()
            down_press = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    bg_x -= game_speed

    screen.blit(background, (bg_x, 0))
    screen.blit(background, (bg_x + 1280, 0))
    if bg_x <= -1280:
        bg_x = 0

    time_track += 1

    if time_track >= random.randint(int(50 - (game_speed * 2)), 200):

        if game_speed > 3.2:
            hole = Obstacle(1460, 420, 540, 660)
            if random.choice([0, 1]) == 1:
                hole = Obstacle(1660, 420, 540, 660)
        else:
            hole = Obstacle(1460, 420, 800, 660)

        obstacles_group.add(hole)
        time_track = 0

    for s in obstacles_group.sprites():
        if characterS_group.sprite.rect.x - s.rect.x in range(-55,
                                                              55) and characterS_group.sprite.rect.y - s.rect.y in range(
            -55, 55):
            e_a_b()

    obstacles_group.update()
    obstacles_group.draw(screen)

    characterS_group.update()
    characterS_group.draw(screen)

    screen.blit(
        font_1.render('Cleopatra v1.0', True, str('#' + ''.join([random.choice('ABCDEF0123456789') for i in range(6)]))),
        (5, 5))

    screen.blit(
        font_1.render('Made by Jonaqhan', True,
                      str('#' + ''.join([random.choice('ABCDEF0123456789') for i in range(6)]))),
        (5, 18))

    screen.blit(
        font.render(str(int(score)), True, str('#' + ''.join([random.choice('ABCDEF0123456789') for i in range(6)]))),
        (1100, 50))
    pygame.display.update()
