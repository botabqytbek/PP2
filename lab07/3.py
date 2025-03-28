import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
done = False
color = (0, 128, 255)
x = 30
y = 30
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: 
        if(y>=25):y-=1
    if pressed[pygame.K_DOWN]:
        if(y<=575):y+=1
    if pressed[pygame.K_RIGHT]:
        if(x<=775): x+=1
    if pressed[pygame.K_LEFT]:
        if(x>=25): x-=1
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, color, (x, y), 25)
    pygame.display.flip()
    clock.tick(60)
