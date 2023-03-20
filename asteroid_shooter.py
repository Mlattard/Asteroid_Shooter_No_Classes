import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Poew Poew Poew")
clock = pygame.time.Clock()

ship_surf = pygame.image.load('graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
bckgr_surf = pygame.image.load('graphics/background.png').convert()

font = pygame.font.Font('graphics/subatomic.ttf', 50)
text_surf = font.render('Space', True, 'White')
text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(120)

    ship_rect.center = pygame.mouse.get_pos()

    display_surface.fill((0, 0, 0))
    display_surface.blit(bckgr_surf, (0, 0))
    display_surface.blit(ship_surf, ship_rect)
    display_surface.blit(text_surf, text_rect)
   
    pygame.display.update()