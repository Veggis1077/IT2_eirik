import pygame
pygame.init()

SCREEN_WITH = 500
SCREEN_HEIGTH = 500

screen = pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGTH))

pygame.display.set_caption('Spritescheets')

BG = (50, 50, 50)
sprite_sheet_image = pygame.image.load("char_blue.png")
br = 56

def get_image(sheet, xcor, ycor):
    image = pygame.Surface((56, 56)).convert_alpha()
    image.blit(sheet, (0, 0), ((xcor-1)*br, (ycor-1)*br, 56, 56))
    return image


frame_0 = get_image(sprite_sheet_image, 6, 6)
frame_1 = get_image(sprite_sheet_image, 1, 1)
a = pygame.transform.flip(frame_1, True, False)
run = True
while run:
    #Update background
    screen.fill(BG)

    #temporarily

    screen.blit(frame_0, (56, 56))
    screen.blit(a,(200, 200))
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
