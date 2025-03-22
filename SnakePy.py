import pygame
import time
import random
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)

disWidth = 800
disHeight = 600
dis = pygame.display.set_mode((disWidth,disHeight))
pygame.display.set_caption('Snake game by DanielMacena')

gameOver = False



snakeBlock = 10
snakeSpeed = 30



clock = pygame.time.Clock()


fontStyle = pygame.font.SysFont("comic sans", 50)

def message(msg, color):
    msg = fontStyle.render(msg, True, color)
    dis.blit(msg, [disWidth/3, disHeight/3])

def gameLoop():
    gameOver = False
    gameClose = False

    x1 = disWidth / 2
    y1 = disHeight / 2

    x1Change = 0
    y1Change = 0

    foodx = round(random.randrage(0, disWidth - snakeBlock) /  10.0) * 10.0
    foody = round(random.randrange(0, disWidth - snakeBlock) / 10.0) * 10.0

    while not gameOver:
        while gameClose == True:
            dis.fill(white)
            message("You lost! Press Q-quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = True
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
        dis.fill(white)
        pygame.draw.rect(dis, black, [foodx, foody, snakeBlock, snakeBlock])
        pygame.draw.rect(dis, black, [x1, y1, snakeBlock, snakeBlock])
        #pygame.draw.rect(dis, blue, [200,150,10,10])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(snakeSpeed) 

    pygame.quit()
    quit()

gameLoop()