import pygame
import sys
import random
import os

# Init
pygame.init()
# Zet icon
pygame.display.set_icon(pygame.transform.scale(pygame.image.load('assets/characters/wizard_1.png'), (90, 90)))

# Groote display
screen = pygame.display.set_mode((1280, 720))

# Titel scherm
pygame.display.set_caption("Cleopatra")

# Fonts
font = pygame.font.Font("assets/fonts/Font.ttf", 40)
font_1 = pygame.font.Font("assets/fonts/Font.ttf", 13)

# Random theme
theme = random.randint(1, 3)

# Random Character
character = random.choice(['wizard', 'lizard', 'knight', 'elf'])

# Achtergrond van grootte veranderen en van het juiste theme pakken
background = pygame.transform.scale(pygame.image.load('assets/backgrounds/background_' + str(theme) + '.png'),
                                    (1280, 720))
# Variables
bg_x = 0
time_track = 0
up_press = False
down_press = False
lgt = 0
score = 0

# Laad de muziek uitgaan en zet dan een nieuw liedje op dat random is van de bestanden die in de muziek folder staan
def RetrieveMusic():
    pygame.mixer.fadeout(10)
    pygame.mixer.Sound('assets/music/' + random.choice(os.listdir('assets/music'))).play(-1).set_volume(0.03)

# Main Character class
class Character(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Folder voor de movements
        self.walking = []

        self.walking.append(
            pygame.transform.scale(pygame.image.load('assets/characters/' + character + '_1.png'), (150, 150)))
        self.walking.append(
            pygame.transform.scale(pygame.image.load('assets/characters/' + character + '_2.png'), (150, 150)))
        self.walking.append(
            pygame.transform.scale(pygame.image.load('assets/characters/' + character + '_3.png'), (150, 150)))
        self.walking.append(
            pygame.transform.scale(pygame.image.load('assets/characters/' + character + '_4.png'), (150, 150)))

        # X en y worden de x en y van input
        self.x = x
        self.y = y

        # De afbeelding die wordt gedisplayed
        self.current_motion = 0

        # Het displayen ervan
        self.image = self.walking[self.current_motion]

        # Waar de afbeelding komt te staan
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        # Afbeelding op verloop van tijd updaten
        self.current_motion += 0.20

        # Resetten van afbeelding nadat de laatste afbeelding geweest is
        if self.current_motion >= 4:
            self.current_motion = 0
        self.image = self.walking[int(self.current_motion)]

    # Wanneer de up toets wordt gebruikt wordt deze functie geroepen en die laat gebaseerd op de locatie hem omhoog gaan
    def up(self):
        if self.rect.centery == 510:
            self.rect.centery -= 120
        elif self.rect.centery == 635:
            self.rect.centery -= 125

    # Zelfde geld voor down dat dan de down toets wordt gebruikt etc..
    def down(self):
        if self.rect.centery == 510:
            self.rect.centery += 125
        elif self.rect.centery == 390:
            self.rect.centery += 120


# Obstacle class hiermee wordt obstacle geladen
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y1, y2, y3):
        super().__init__()

        self.x = x

        # Random y gebaseerd op de y inputs
        self.y = random.choice([y1, y2, y3])

        # Transformeren van afbeelding en class te zetten naar die afbeelding
        self.image = pygame.transform.scale(pygame.image.load('assets/obstacles/obstacle_' + str(theme) + '.png'),
                                            (128, 120))
        self.rect = self.image.get_rect(center=(self.x, self.y))

    # Update functie waarbij de x wordt aangepast aan de gamespeed en de locatie wordt geupdate
    def update(self):
        self.x -= game_speed

        self.rect = self.image.get_rect(center=(self.x, self.y))


# Het crearen van de character en de meegegeven x en y
characterS = Character(150, 635)

# Groep maken voor de character en aangeven dat het een single group is omdat het de enige sprite is
characterS_group = pygame.sprite.GroupSingle()

# Character toevoegen aan de groep
characterS_group.add(characterS)

# Obstacles groep maken voor alle obstacles
obstacles_group = pygame.sprite.Group()

# Muziek functie roepen om muziek af te laten spelen
RetrieveMusic()

# End after beginning, functie die geroepen wordt nadat iemand dood/af gaat
def e_a_b():
    # Scores globaal zetten omdat je anders de scores buiten de functie om niet kan gebruiken
    global score, lgt, game_speed, theme, character, background, characterS
    # Tijd krijgen om zo de oude tijd te kunnen gebruiken om de huidige tijd na dood gaan berekent kan worden
    lgt = pygame.time.get_ticks()
    game_speed = 0
    # Alle obstacles verwijderen
    obstacles_group.empty()

    #Higher score printen om later terug te kunnen kijken
    print('Your highscore was ' + str(int(score)))

    # Score resetten
    score = 0

    # Opnieuw muziek laten afspelen
    RetrieveMusic()

    # Weer een random theme pakken
    theme = random.randint(1, 3)

    # Character verwijderen om een nieuwe weer te pakken die ook weer random geselecteerd wordt
    characterS_group.empty()
    character = random.choice(['wizard', 'lizard', 'knight', 'elf'])
    characterS = Character(150, 635)
    characterS_group.add(characterS)
    background = pygame.transform.scale(
        pygame.image.load('assets/backgrounds/background_' + str(theme) + '.png'),
        (1280, 720))


# Loop
while True:
    # Game snelheid wordt gebaseerd op tijd van spelen en lgt staat dus voor de tijd voordat de persoon is dood gegaan want dient als een reset
    game_speed = 1 + ((pygame.time.get_ticks() - lgt) / 100 * 0.025)
    score += 0.1

    # Toetsen die gedrukt worden
    keys = pygame.key.get_pressed()

    # Als de K toets niet ingedrukt is om zo de functie weer uit te kunnen zetten dat die ingedrukt is
    if not keys[pygame.K_w]:
        up_press = False
    # Zelfde geld ook voor de S toets
    if not keys[pygame.K_s]:
        down_press = False

    # Kijken als de W toets ingedrukt is
    if keys[pygame.K_w]:
        # Als die niet meer ingedrukt wordt dan wordt de omhoog functie geroepen om de character omhoog te laten gaan
        if not up_press:
            characterS.up()
            up_press = True

    # Zelfde geld ook voor de S
    if keys[pygame.K_s]:
        if not down_press:
            characterS.down()
            down_press = True

    # Kijkt als er een event geroepen wordt en als er dus op het kruisje gedrukt wordt en laat dan alles afsluiten
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Achtergrond x
    bg_x -= game_speed

    # Achtergrond op de y is 0 en de x verandert dus gebaseerd op de game speed
    screen.blit(background, (bg_x, 0))

    # Naast de achtergrond nog een achtergrond die ingeladen wordt als de andere uitgeladen wordt
    screen.blit(background, (bg_x + 1280, 0))

    # Als de x kleiner of gelijk is aan -128- dan wordt die weer gereset waardoor je oneindig bewegende achtergrond krijgt
    if bg_x <= -1280:
        bg_x = 0

    # Traceren van hoeveel tijd er ongeveer voorbij is
    time_track += 1

    # Deze functie wordt gerunt wanneer een random getal groter is dan de huidige tijd en dat getal is onder de 200
    if time_track >= random.randint(int(50 - (game_speed * 2)), 200):

        # Als de game speed hoger dan 3.2 is wordt dit gerunt en dit is om te voorkomen dat je bij het begin instant dood gaat
        if game_speed > 3.2:
            # het creeeren van de obstacle
            hole = Obstacle(1460, 420, 540, 660)
            # 50/50 kans dat er daarna nog een obstacle wordt gespawnt
            if random.choice([0, 1]) == 1:
                hole = Obstacle(1660, 420, 540, 660)
        # Anders wordt er een obstacle expres ver weg geplaatst
        else:
            hole = Obstacle(1460, 420, 800, 660)

        # Obstacle toevoegen aan groep
        obstacles_group.add(hole)
        time_track = 0

    # Systeem om te kijken als de character in aanraking komt met de obstacle
    for s in obstacles_group.sprites():
        if characterS_group.sprite.rect.x - s.rect.x in range(-55,
                                                              55) and characterS_group.sprite.rect.y - s.rect.y in range(
            -55, 55):
            e_a_b()

    # Roept de update functie van de sprites in de obstacles group op
    obstacles_group.update()

    # Geeft de obstacles op het scherm weer
    obstacles_group.draw(screen)

    # Zelfde ook voor character
    characterS_group.update()
    characterS_group.draw(screen)

    # Text op scherm
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

    # Updaten van scherm
    pygame.display.update()
