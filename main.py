import pygame
import random
import sys
import math 
import os

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
frameimg = pygame.image.load("assets/frame.png").convert_alpha()
victoryimg = pygame.image.load("assets/frame.png").convert_alpha()
gameoverimg = pygame.image.load("assets/gameover.png").convert_alpha()
playagainimg = pygame.image.load("assets/play again.png").convert_alpha()
scribblebgimg = pygame.image.load("assets/scribblebg.png").convert_alpha()
clicksound = pygame.mixer.Sound("assets/buttonclick.mp3")

gta_imagespath = "gta images"
gtaimages = os.listdir(gta_imagespath)
gtaimagesrandlist = random.sample(gtaimages, k=5)

for i in range(5):
    gtaimagesrandlist[i] = os.path.join(gta_imagespath, gtaimagesrandlist[i])

real_imagespath = "real images"
realimages = os.listdir(real_imagespath)
realimagesrandlist = random.sample(realimages, k=5)

for i in range(5):
    realimagesrandlist[i] = os.path.join(real_imagespath, realimagesrandlist[i])

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
randomimage1 = random.randint(0,1)
randomimage2 = random.randint(0,1)
randomimage3 = random.randint(0,1)
randomimage4 = random.randint(0,1)
randomimage5 = random.randint(0,1)


if randomimage1 == 1:
    displayimage1 = gtaimagesrandlist[0]
else:
    displayimage1 = realimagesrandlist[0]

if randomimage2 == 1:
    displayimage2 = gtaimagesrandlist[1]
else:
    displayimage2 = realimagesrandlist[1]

if randomimage3 == 1:
    displayimage3 = gtaimagesrandlist[2]
else:
    displayimage3 = realimagesrandlist[2]

if randomimage4 == 1:
    displayimage4 = gtaimagesrandlist[3]
else:
    displayimage4 = realimagesrandlist[3]

if randomimage5 == 1:
    displayimage5 = gtaimagesrandlist[4]
else:
    displayimage5 = realimagesrandlist[4]



displayimage1 = pygame.image.load(displayimage1).convert_alpha()
displayimage2 = pygame.image.load(displayimage2).convert_alpha()
displayimage3 = pygame.image.load(displayimage3).convert_alpha()
displayimage4 = pygame.image.load(displayimage4).convert_alpha()
displayimage5 = pygame.image.load(displayimage5).convert_alpha()

displayimage1 = pygame.transform.scale(displayimage1, (500, 500))
displayimage2 = pygame.transform.scale(displayimage2, (500, 500))
displayimage3 = pygame.transform.scale(displayimage3, (500, 500))
displayimage4 = pygame.transform.scale(displayimage4, (500, 500))
displayimage5 = pygame.transform.scale(displayimage5, (500, 500))

frameimg = pygame.transform.scale(frameimg, (600, 600))


displayimage1rect = displayimage1.get_rect(center=(640, 360))
displayimage2rect = displayimage2.get_rect(center=(640, 360))
displayimage3rect = displayimage3.get_rect(center=(640, 360))
displayimage4rect = displayimage4.get_rect(center=(640, 360))
displayimage5rect = displayimage5.get_rect(center=(640, 360))
framerect = frameimg.get_rect(center=(640, 360))

gtabuttonimg = pygame.transform.scale(gtabuttonimg, (500, 500))
notgtabuttonimg = pygame.transform.scale(notgtabuttonimg, (500, 500))


gtabuttonrect = gtabuttonimg.get_rect(center=(170, 360))
notgtabuttonrect = notgtabuttonimg.get_rect(center=(1110, 360))

choicebuttonstate = False
choicebuttonchangetime = 0

rounds = 1

while maingame == True and rounds <= 5:


    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if rounds == 1:
            print("round1")


    if current_time - last_jitter_time > jitterscribbledelay:
        last_jitter_time = current_time
        angle = random.randint(-150, 15)
        scribble_img = pygame.transform.rotate(scribblebgimg, angle)
        offset_x = random.randint(-50, 50)
        offset_y = random.randint(-50, 50)
        new_center = (scribble_base_pos[0] + offset_x, scribble_base_pos[1] + offset_y)
        scribble_rect = scribble_img.get_rect(center=new_center)

    mouse_pos = pygame.mouse.get_pos()


    is_hoveredgta = gtabuttonrect.collidepoint(mouse_pos)

    is_hoverednotgta = notgtabuttonrect.collidepoint(mouse_pos)



    draw_buttongta = gtabuttonrect.inflate(-20, -10) if is_hovered else gtabuttonrect
    if is_hoveredgta:
        gta_draw_rect = gtabuttonrect.inflate(-20, -10)
        draw_buttongta = pygame.transform.smoothscale(gtabuttonimg, gta_draw_rect.size)
    else:
        gta_draw_rect = gtabuttonrect
        draw_buttongta = gtabuttonimg


    draw_buttonnotgta = startbutton.inflate(-20, -10) if is_hovered else notgtabuttonrect
    if is_hoverednotgta:
        notgta_draw_rect = notgtabuttonrect.inflate(-20, -10)
        draw_buttonnotgta = pygame.transform.smoothscale(notgtabuttonimg, notgta_draw_rect.size)
    else:
        notgta_draw_rect = notgtabuttonrect
        draw_buttonnotgta = notgtabuttonimg

    screen.fill((100, 20, 56)) 
    screen.blit(scribble_img, scribble_rect)

    screen.blit(displayimage5, displayimage5rect)
   
    screen.blit(frameimg, framerect)
    
    screen.blit(draw_buttongta, gtabuttonrect)
    screen.blit(draw_buttonnotgta, notgtabuttonrect)

    if choicebuttonstate == True and choicebuttonchangetime >= 500 and rounds < 5:
        #show banner on basis of lose or win and
        choicebuttonstate  = False

    elif choicebuttonstate == True and choicebuttonchangetime >= 500 and rounds == 5:
        #show the play again button aswell
        choicebuttonstate  = False

    else:
        #hide banner
        choicebuttonstate  = False


    pygame.display.flip()
    clock.tick(60)

