import pygame
import time
import random
pygame.init()

white = (255,255,255)
yellow = (255,255,102)
black = (0,0,0)
red = (213,50,80)
green = (0,255,0)
blue = (50,153,213)

disWidth = 600
disHeight = 400

dis = pygame.display.set_mode((disWidth,disHeight))
pygame.display.set_caption('Snake game by DanielMacena')

gameOver = False

snakeBlock = 10
snakeSpeed = 15

clock = pygame.time.Clock()

fontStyle = pygame.font.SysFont("comicsasms", 25)
scoreFont = pygame.font.SysFont("comicssams", 35)

def yourScore(score):
    value = scoreFont.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def ourSnake(snakeBlock, snakeList):
    for x in snakeList:
        pygame.draw.rect(dis, black, [x[0], x[1], snakeBlock, snakeBlock])


def message(msg, color):
    msg = fontStyle.render(msg, True, color)
    dis.blit(msg, [disWidth/6, disHeight/3])

def gameLoop():
    gameOver = False
    gameClose = False

    x1 = disWidth / 2
    y1 = disHeight / 2

    x1Change = 0
    y1Change = 0

    snakeList = []
    LenghtOfSnake = 1

    foodx = round(random.randrange(0, disWidth - snakeBlock) /  10.0) * 10.0
    foody = round(random.randrange(0, disHeight - snakeBlock) / 10.0) * 10.0

    while not gameOver:
        while gameClose == True:
            dis.fill(blue)
            message("You lost! Press Q-quit or C-Play Again", red)
            yourScore(LenghtOfSnake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_c:
                        gameLoop()


    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1Change = -snakeBlock
                    y1Change = 0
                elif event.key == pygame.K_RIGHT:
                    x1Change = snakeBlock
                    y1Change = 0
                elif event.key == pygame.K_UP:
                    y1Change = -snakeBlock
                    x1Change = 0
                elif event.key == pygame.K_DOWN:
                    y1Change = snakeBlock
                    x1Change = 0

        if x1 >= disWidth or x1 < 0 or y1 >= disHeight or y1 < 0:
            gameClose = True

        x1 += x1Change
        y1 += y1Change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snakeBlock, snakeBlock])
        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)
        snakeList.append(snakeHead)
        if len(snakeList) > LenghtOfSnake:
            del snakeList[0]

        for x in snakeList[:-1]:
            if x == snakeHead:
                gameClose = True

        ourSnake(snakeBlock, snakeList)
        yourScore(LenghtOfSnake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, disWidth - snakeBlock) / 10.0) * 10.0
            foody = round(random.randrange(0, disHeight - snakeBlock) / 10.0) * 10.0
            LenghtOfSnake += 1
            
        clock.tick(snakeSpeed) 

    pygame.quit()
    quit()

gameLoop()