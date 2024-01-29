import pygame
pygame.init()

clock = pygame.time.Clock() #Lager klokke som skal tikke
SCREEN_WITH = 500 #Skjerm bredde
SCREEN_HEIGTH = 500 #Skjerm høyde
screen = pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGTH)) # Lager skjermen

pygame.display.set_caption('Spritescheets') #Navn

BG = (50, 50, 50) # Bakgrunnsfarge
sprite_sheet_image = pygame.image.load("char_blue.png") #Importerer inn karakteren
br = 56

def get_image(sheet, xcor, ycor): #Egentlig samme funksjon som running
    image = pygame.Surface((56, 56)).convert_alpha()
    image.blit(sheet, (0, 0), ((xcor-1)*br, (ycor-1)*br, 56, 56))
    return image

def running(sheet, rad,a): #Velger riktig del av char_blue.png og returnerer den delen
    image = pygame.Surface((56,56)).convert_alpha()
    image.blit(sheet, (0, 0), ((a)*br, (rad-1) * br, 56, 56))

    return image





#frame_running = running(sprite_sheet_image)
"""Slik flipper du fyren din"""
#a = pygame.transform.flip(frame_1, True, False)

counter = 1 #Counter for løpe hoppe og slå animasjon

b = running(sprite_sheet_image, 3, counter) #Løpende figur
c = running(sprite_sheet_image, 2, counter) #Slå figur
time_elapsed_since_last_action = 0 #For å få riktig animasjon
run = True

x_pos = 150 #x posisjon til foreløpig løpe mannen
y_cor = 150

hopp = False
lope = False
hoyre = True
sla = False
spacbar_down_time = 0
while run:
    #Update background
    screen.fill(BG)

    #temporarily


    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spacbar_down_time = pygame.time.get_ticks()
                lope = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                spacbar_down_time = (pygame.time.get_ticks() - spacbar_down_time)/1000
                print("Spacebar held down for", spacbar_down_time, "seconds")
        elif event.type == pygame.K_Delete:
            sla = True





    keys = pygame.key.get_pressed()
    x_pos += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 1.5

    if x_pos > SCREEN_WITH:
        x_pos -= (SCREEN_WITH + 40)
    elif x_pos < -40:
        x_pos += SCREEN_WITH

    if keys[pygame.K_LEFT] and not hopp:
        lope = True
        hoyre = False
    elif keys[pygame.K_RIGHT]:
        lope = True
        hoyre = True
    else:
        lope = False
        hoyre = True




    dt = clock.tick()

    time_elapsed_since_last_action += dt
    # dt is measured in milliseconds, therefore 250 ms = 0.25 seconds
    if time_elapsed_since_last_action > 100:
        if lope:
            b = running(sprite_sheet_image, 3,counter%8)
        else:
            b = running(sprite_sheet_image, 1, counter%6)

        c = running(sprite_sheet_image, 2, counter % 6)
        time_elapsed_since_last_action = 0



        counter+=1

    if hoyre:
        screen.blit(b, (x_pos, y_cor))
    else:
        screen.blit(pygame.transform.flip(b, True, False), (x_pos, y_cor))
    screen.blit(c, (150, 350))
    pygame.display.update()

pygame.quit()
