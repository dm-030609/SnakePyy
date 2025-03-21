import pygame
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

dis = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake game by DanielMacena')

gameOver = False

x1 = 300
y1 = 300

x1Change = 0
y1Change = 0

clock = pygame.time.Clock()

while not gameOver:
    for event in pygame.event.get():
        print(event) # Mostra todas as ações na tela
        if event.type == pygame.QUIT:
            gameOver = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1Change = -10
                y1Change = 0
            elif event.key == pygame.K_RIGHT:
                x1Change = 10
                y1Change = 0
            elif event.key == pygame.K_UP:
                y1Change = -10
                x1Change = 0
            elif event.key == pygame.K_DOWN:
                y1Change = 10
                x1Change = 0

    x1 += x1Change
    y1 = y1Change

    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])
    #pygame.draw.rect(dis, blue, [200,150,10,10])
    pygame.display.update()

    clock.tick(30) 

pygame.quit()
quit()