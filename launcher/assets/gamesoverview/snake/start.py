import pygame
import time
import random

# intializeer pygame
pygame.init()

# kleur variabelen
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# scherm grootte
dis_width = 600
dis_height = 400

# scherm en naam
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Pygame Snake')

# clock voor tijd
clock = pygame.time.Clock()

# Snake blok grootte en snelheid
snake_block = 10
snake_speed = 15

# lettertype
font_style = pygame.font.SysFont("Arial", 25)
score_font = pygame.font.SysFont("Arial", 35)


# score
def Your_score(score):
    value = score_font.render("Points: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


# waar snake is
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


# message style
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


# loopt de game
def gameLoop():
    game_over = False
    game_close = False

    # variabele voor locatie bepaling
    x1 = dis_width / 2
    y1 = dis_height / 2

    # variabele voor begin positie
    x1_change = 0
    y1_change = 0

    # begin lengte snake
    snake_List = []
    Length_of_snake = 1

    # randomizer voor locatie food
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # message voor afgaan + de 'message'
    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("Git Gud, press C for restart and Q to quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # zorgt voor dat je af bent en loopt game weer
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # als je de game restart en zorgt ervoor dat movement van snake niet diagonaal gaat
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        # achtergrond
        dis.fill(blue)

        # tekent alle entities
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # waar snake is
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # lengte snake 0 dan -1 bij score
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        # update de display als je meer punten haalt
        pygame.display.update()

        # als snakexy zelfde is als foodxy dan punt
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # clock voor snelheid snake
        clock.tick(snake_speed)

    pygame.quit()
    quit()


# zorgt dat game altijd loopt
gameLoop()
