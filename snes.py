import pygame

pygame.init()

clk = pygame.time.Clock()

size = width, height = 528, 281
screen = pygame.display.set_mode(size)
background_image = pygame.image.load('control.png').convert()
frameRect = pygame.Rect( (0,0), (width, height))

crosshair = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshair, pygame.Color("yellow"), (5,5), 5, 0)

crosshairb= pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshairb, pygame.Color("red"), (5,5), 5, 0)

while True:

    pygame.event.pump()

    screen.blit(background_image, (0, 0))

    Keys=pygame.key.get_pressed()

    if Keys[pygame.K_x]: screen.blit(crosshair, (415, 128) )
    if Keys[pygame.K_a]: screen.blit(crosshair, (465, 172) )
    if Keys[pygame.K_y]: screen.blit(crosshair, (360, 172) )
    if Keys[pygame.K_b]: screen.blit(crosshair, (415, 210) )
    if Keys[pygame.K_e]: screen.blit(crosshair, (270, 176) )
    if Keys[pygame.K_q]: screen.blit(crosshair, (215, 176) )
    if Keys[pygame.K_t]: screen.blit(crosshair, (100, 50) )
    if Keys[pygame.K_u]: screen.blit(crosshair, (415, 50) )

    x = -1 if Keys[pygame.K_LEFT] else 1 if Keys[pygame.K_RIGHT] else 0

    y = -1 if Keys[pygame.K_UP] else 1 if Keys[pygame.K_DOWN] else 0



    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(crosshairb,((x*30)+115-5,(y*30)+172-5))
    pygame.display.flip()

    clk.tick(40)
