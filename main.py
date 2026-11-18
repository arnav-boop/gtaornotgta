import pygame
import random
import sys
import math 

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("assets/background music.mp3")
pygame.mixer.music.set_volume(0.5)  # Range: 0.0 to 1.0
pygame.mixer.music.play(-1) 

#calling images
bannerimg = pygame.image.load("assets/openingname.png").convert_alpha()
startbuttonimg = pygame.image.load("assets/startgamebutton.png").convert_alpha()
gtabuttonimg = pygame.image.load("assets/gtabutton.png").convert_alpha()
notgtabuttonimg = pygame.image.load("assets/notgtabutton.png").convert_alpha()
round1img = pygame.image.load("assets/round1.png").convert_alpha()
round2img = pygame.image.load("assets/round2.png").convert_alpha()
round3img = pygame.image.load("assets/round3.png").convert_alpha()
round4img = pygame.image.load("assets/round4.png").convert_alpha()
round5img = pygame.image.load("assets/round5.png").convert_alpha()
frameleftimg = pygame.image.load("assets/frame.png").convert_alpha()
framerightimg = pygame.image.load("assets/frame.png").convert_alpha()
victoryimg = pygame.image.load("assets/frame.png").convert_alpha()
gameoverimg = pygame.image.load("assets/gameover.png").convert_alpha()
playagainimg = pygame.image.load("assets/play again.png").convert_alpha()
scribblebgimg = pygame.image.load("assets/scribblebg.png").convert_alpha()

clicksound = pygame.mixer.Sound("assets/buttonclick.mp3")

#image resizing
startbuttonimg = pygame.transform.scale(startbuttonimg, (200, 200))
bannerimg = pygame.transform.scale(bannerimg, (600, 600))
scribblebgimg = pygame.transform.scale(scribblebgimg, (3000, 3000))


#imgtorect
banner = bannerimg.get_rect(center=(640, 250))
startbutton = startbuttonimg.get_rect(center=(640, 600))
scribble_base_pos = (640, 360)
scribblebg = scribblebgimg.get_rect(center=scribble_base_pos)
last_jitter_time = 0
jitterscribbledelay = 1000

scribble_img = scribblebgimg
scribble_rect = scribblebg

def drawstartscreen():

    return

def drawmaingame():
    numberofrounds = 5
play = True
while play:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if startbutton.collidepoint(event.pos):
                clicksound.play()
                print("button")
                play = False

    if current_time - last_jitter_time > jitterscribbledelay:
        last_jitter_time = current_time
        angle = random.randint(-150, 15)
        scribble_img = pygame.transform.rotate(scribblebgimg, angle)
        offset_x = random.randint(-5, 5)
        offset_y = random.randint(-5, 5)
        new_center = (scribble_base_pos[0] + offset_x, scribble_base_pos[1] + offset_y)
        scribble_rect = scribble_img.get_rect(center=new_center)



    def imgleftrightrandomizer(left,right):
        left = random.randint(0,1)
        if left == 0:
           right = 1 
           return right
        else:
            right =  0
            return right

    mouse_pos = pygame.mouse.get_pos()
    is_hovered = startbutton.collidepoint(mouse_pos)

    draw_rect = startbutton.inflate(-20, -10) if is_hovered else startbutton
    if is_hovered:
       draw_img = pygame.transform.smoothscale(startbuttonimg, draw_rect.size)
    else:
      draw_img = startbuttonimg

    screen.fill((100, 20, 56))
    screen.blit(scribble_img, scribble_rect)
    screen.blit(draw_img, draw_rect)
    screen.blit(bannerimg, banner)



    pygame.display.flip()
    clock.tick(60)

maingame = True

rounds = 1 
while maingame == True:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    if current_time - last_jitter_time > jitterscribbledelay:
        last_jitter_time = current_time
        angle = random.randint(-150, 15)
        scribble_img = pygame.transform.rotate(scribblebgimg, angle)
        offset_x = random.randint(-5, 5)
        offset_y = random.randint(-5, 5)
        new_center = (scribble_base_pos[0] + offset_x, scribble_base_pos[1] + offset_y)
        scribble_rect = scribble_img.get_rect(center=new_center)

    mouse_pos = pygame.mouse.get_pos()
    is_hovered = startbutton.collidepoint(mouse_pos)

    screen.fill((100, 20, 56)) 
    screen.blit(scribble_img, scribble_rect)


    pygame.display.flip()
    clock.tick(60)

