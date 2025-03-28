import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1500, 600))
play_img = pygame.image.load("play.png")
pause_img = pygame.image.load("pause.png")
next_button = pygame.image.load("next.png")
prev_button = pygame.image.load("prev.png")

songs = ["Blinding.mp3", "Shape.mp3"]
running = True
paused = False
clock = pygame.time.Clock()

pygame.mixer.music.load(songs[0]) 
pygame.mixer.music.play()

def play_next_song():
    global songs
    songs = songs[1:] + [songs[0]]
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()

def play_prev_song():
    global songs
    songs = [songs[-1]] + songs[:-1]
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not paused:
                    pygame.mixer.music.pause()
                    paused = True
                else:
                    pygame.mixer.music.unpause()
                    paused = False
            if event.key == pygame.K_RIGHT:
                play_next_song()
            if event.key == pygame.K_LEFT:
                play_prev_song()
    
    screen.fill((255, 255, 255))
    
    screen.blit(prev_button, (0, 50))
    screen.blit(next_button, (1000, 50))
    
    if paused:
        screen.blit(play_img, (500, 50))
    else:
        screen.blit(pause_img, (500, 50))
    
    pygame.display.flip()
    clock.tick(60)
