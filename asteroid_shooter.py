import pygame, sys

def laser_update(laser_list, speed = 300):
    for laser in laser_list:
        laser.y -= speed * dt
        if laser.bottom < 0:
            laser_list.remove(laser)

def meteor_update(meteor_list, speed = 300):
    for meteor in meteor_list:
        meteor.y += speed * dt
        if meteor.top > WINDOW_HEIGHT:
            meteor_list.remove(meteor)

def display_score():
    score_text = f'score: {pygame.time.get_ticks() // 1000}'
    text_surf = font.render(score_text, True, 'White')
    text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, 'white', text_rect.inflate(30,30), width= 5, border_radius= 20)
   
def laser_timer(can_shoot, duration = 500):
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - shoot_time > duration:
            can_shoot = True
    return can_shoot

# game init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Poew Poew Poew")
clock = pygame.time.Clock()

# ship import
ship_surf = pygame.image.load('graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# background
bckgr_surf = pygame.image.load('graphics/background.png').convert()

# laser import
laser_surf = pygame.image.load('graphics/laser.png').convert_alpha()
laser_list = []

# laser timer
can_shoot = True
shoot_time = None

# font import
font = pygame.font.Font('graphics/subatomic.ttf', 50)

# meteor
meteor_surf = pygame.image.load('graphics/meteor.png').convert_alpha()
meteor_list = []

# meteor timer
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)

while True:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            
            #laser
            laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)
            laser_list.append(laser_rect)

            #timer
            can_shoot = False
            shoot_time = pygame.time.get_ticks()

        if event.type == meteor_timer:
            meteor_rect = meteor_surf.get_rect(center = (640, -100))
            meteor_list.append(meteor_rect)

    # framerate limit
    dt = clock.tick(120) / 1000

    # mouse input
    ship_rect.center = pygame.mouse.get_pos()

    # update
    laser_update(laser_list)
    meteor_update(meteor_list)
    can_shoot = laser_timer(can_shoot, 500)

    # drawing
    display_surface.fill((0, 0, 0))
    display_surface.blit(bckgr_surf, (0, 0))
 
    display_score()

    for laser in laser_list:
        display_surface.blit(laser_surf, laser)
        
    for meteor in meteor_list:
        display_surface.blit(meteor_surf, meteor)
    
    display_surface.blit(ship_surf, ship_rect)
    
    # draw the final frame
    pygame.display.update()