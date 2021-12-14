import sys, pygame
pygame.init()

size = width, height = 1920,1080
speed = [1,1]
black = 0,0,0

screen = pygame.display.set_mode(size)


hero = pygame.image.load("images/hero.png")
herorect = hero.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    if pygame.key.get_pressed()[pygame.K_a]:
        herorect.x -= 5
    if pygame.key.get_pressed()[pygame.K_d]: 
        herorect.x += 5
    if pygame.key.get_pressed()[pygame.K_s]:
        herorect.y += 5
    if pygame.key.get_pressed()[pygame.K_w]:    
        herorect.y -= 5


    #herorect = herorect.move(speed)
    if herorect.left < 0 or herorect.right > width:
        herorect = herorect.move([0,0])
   # if herorect.top < 0 or herorect.bottom > height:
    #    speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(hero, herorect)
    pygame.display.flip()