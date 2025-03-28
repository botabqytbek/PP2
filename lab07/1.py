import pygame 
import datetime
screen = pygame.display.set_mode((800,600))

min = pygame.image.load("min_hand.png")
sec = pygame.image.load("sec_hand.png")
platform = pygame.image.load("clock.png")

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    now = datetime.datetime.now()
    screen.fill((255, 255, 255))

    screen.blit(platform, (0,0))


    rotated_sec = pygame.transform.rotate(sec, - (now.second * 6 - 54))  
    rect = rotated_sec.get_rect(center=(400, 300))
    screen.blit(rotated_sec, rect)
    print(now.second)

    rotated_min = pygame.transform.rotate(min, - (now.minute * 6 + 54))  
    rect = rotated_min.get_rect(center=(400, 300))
    screen.blit(rotated_min, rect)
    
    print(now.minute)
    print("------------")
    pygame.display.flip()
    clock.tick(60)
