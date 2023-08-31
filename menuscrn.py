import pygame
from pygame.locals import *
from world_class import *
from level_map_data import *
from button import Button
import pygame.mixer



pygame.init()
pygame.mixer.init()
#mouse visibilty
pygame.mouse.set_visible(True)

#define screen variables
screen_width = 1024
screen_height = 736
#define font
main_font = pygame.font.SysFont('ArcadeClassic', 50)#cambria if dont work
#menu variables
menu_state ='main'
game_paused = 0
#0 = true, 1 = false and 2 = options 3= credits 4= volume settings

#display and caption
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('gme.0.0.1.6')
#define game variables
tile_size = 16
FPS = 60
clock = pygame.time.Clock()
#cloud sizes
w = 384
h = 216
#credits size
credits_h = 713
#define colours 
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25 , 25)
BLUE = (138, 206, 220)
#load images
sky = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/sky_fc.png').convert_alpha()
cloud1 = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/clouds_front_fc.png').convert_alpha()
cloud2 = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/clouds_mid_fc.png').convert_alpha()
mountains1  = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/far_mountains_fc.png').convert_alpha()
mountains2 = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/grassy_mountains_fc.png').convert_alpha()
cloud_single = pygame.image.load('Map/Background IMG/mountains/Glacial-mountains-parallax-background_vnitti_v3/Glacial-mountains-parallax-background_vnitti/Layers/cloud_lonely.png').convert_alpha()
sky_blue = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers/sky_blu.png').convert_alpha()
credits = pygame.image.load('Map/credits.png').convert_alpha()
#change height and width
sky_img = pygame.transform.scale(sky, (screen_width, screen_height))
cloud1_img = pygame.transform.scale(cloud1,  (screen_width, screen_height))
cloud2_img = pygame.transform.scale(cloud2, (screen_width, screen_height))
mountains1_img = pygame.transform.scale(mountains1, (screen_width, screen_height))
mountains2_img = pygame.transform.scale(mountains2, (screen_width, screen_height))
cloud_1 = pygame.transform.scale(cloud_single, (w,h))
cloud_2 = pygame.transform.scale(cloud_single, (w +200, h+200))
cloud_3 = pygame.transform.scale(cloud_single, (w-100, h-100))
sky_blue = pygame.transform.scale(sky_blue,(screen_width,screen_height))
credits_resized = pygame.transform.scale(credits,(478,713))
# Initialize background positions
cloud1_x = 0
cloud2_x = 0
cloud3_x = 0
scroll_Speed_1 = 0.8
scroll_Speed_2 = 0.6
scroll_Speed_3 = 0.4
credits_y = 736
credits_speed = 0.5
#music/sounds
initial_volume = (0.3)
is_mute = False

    
songs = [
    'Map/sound/Adventure pack 1 ogg/Adventure pack 1 ogg/arcade.ogg','Map/sound/Adventure pack 1 ogg/Adventure pack 1 ogg/chibi-robot-b.ogg','Map/sound/Adventure pack 1 ogg/Adventure pack 1 ogg/fantasy Dragon.ogg',  
    'Map/sound/Adventure pack 1 ogg/Adventure pack 1 ogg/dark-happy-world.ogg','Map/sound/Adventure pack 1 ogg/Adventure pack 1 ogg/exploration.ogg', 
    'Map/sound/Adventure pack 1 ogg/Adventure pack 1 ogg/Going Up.ogg','Map/sound/Adventure pack 1 ogg/Adventure pack 1 ogg/happywalking.ogg','Map/sound/Adventure pack 1 ogg/Adventure pack 1 ogg/hurry_up_and_run.ogg',
]

current_song_index = 0

def play_current_song():
    pygame.mixer.music.load(songs[current_song_index])
    pygame.mixer.music.set_volume(initial_volume)
    pygame.mixer.music.play()
    
play_current_song()

    
    


#button images 
button_background = pygame.image.load('Map/levels/images/blocks/spike/116.png').convert_alpha()
button_background = pygame.transform.scale(button_background,(250,150))
pause_background = pygame.image.load('Map/levels/images/blocks/spike/pause.png').convert_alpha()
pause_background = pygame.transform.scale(pause_background,(100,100))
blue_background = pygame.transform.scale(sky_blue,(250,150))
square_background = pygame.transform.scale(button_background,(100,100))
#button instances
play_button = Button(512, 200, button_background,'play', main_font)
options_button =Button(512, 350, button_background,'options', main_font)
quit_button = Button(512, 650, button_background,'quit',main_font)
credits_button = Button(512, 500, button_background, 'credits', main_font)
pause_button = Button(64,64,pause_background,'',main_font)
back_button = Button(150,64, button_background,'back',main_font)
volume_button = Button(512,100, blue_background, 'volume settings',main_font)
mute_button = Button(512,325, blue_background, 'mute volume',main_font)
#unmute_button = Button(512,250,blue_background, 'unmute volume',main_font)
onehundred_percent_button = Button(812,450, square_background, '100',main_font)
twenty_percent_button = Button(212,450, square_background, '20',main_font)
forty_percent_button = Button(362,450, square_background, '40',main_font)
sixty_percent_button = Button(512,450, square_background, '60',main_font)
eighty_percent_button = Button(662,450, square_background, '80',main_font)
#class player

player = Player(32, screen_height - 128)
#player is drawn on the coordinates (tile_size * 2, screen_height - 16* 7 ) because it is the second block across and 7 blocks up from the bottom

world_plants = World_Plants_Layer(plants_layer_world_data)
world_spike = World_Spike_Layer(spike_world_data)
world_enemy = World_Enemy_Layer(level_enemy)




#game loop
run = True
while run:
    clock.tick(FPS)


    #cloud movement
    cloud1_x -= scroll_Speed_1
    cloud2_x -= scroll_Speed_2
    cloud3_x -=scroll_Speed_3
    #if cloud goes off screen
    if cloud1_x <= -w:
        cloud1_x = screen_width
    if cloud2_x <= -w:
        cloud2_x = screen_width
    if cloud3_x <= -w:
        cloud3_x = screen_width
    
    #credits movement
    credits_y -= credits_speed
    #credits goes off screen
    if credits_y <= -credits_h:
        credits_y = screen_height
    
    
    

    
    # check if the current song has finished playing
    if not pygame.mixer.music.get_busy():
        # move to the next song index
        current_song_index = (current_song_index + 1) % len(songs)
        # play the next song
        play_current_song()



    
    #shows the game window
    if game_paused == 1:
        if menu_state == 'game':
            
        
            
            #draw background
            screen.blit(sky_img,(0, 0))
            screen.blit(mountains1_img,(0, 0))
            screen.blit(mountains2_img,(0, 0))
            screen.blit(cloud1_img,(0, 0))
            screen.blit(cloud2_img,(0, 0))
            screen.blit(cloud_1,(cloud1_x,104))
            screen.blit(cloud_2,(cloud2_x,262))
            screen.blit(cloud_3,(cloud3_x,34))
            #draw
            #  foregroubd
            pause_button.update(screen)
            world_grass.draw()
            world_plants.draw()
            world_spike.draw()
            enemy_group.update()
            enemy_group.draw(screen)
            player.update(world_grass.tile_list)
            #pause the game
            if pause_button.draw(screen):
                    game_paused = 0
                    menu_state = 'main'
            pause_button.update(screen)
            
    

    #check if game is paused
    if game_paused == 0:
        menu_state = 'main'
        if menu_state =='main':
            #music
            #draw background and have clouds moving
            screen.blit(sky_img,(0, 0))
            screen.blit(mountains1_img,(0, 0))
            screen.blit(mountains2_img,(0, 0))
            screen.blit(cloud2_img, (0, 0))
            screen.blit(cloud1_img, (0, 0))
            screen.blit(cloud_1,(cloud1_x,164))
            screen.blit(cloud_2,(cloud2_x,364))
            screen.blit(cloud_3,(cloud3_x,64))
            #music
            #plays the game 
            if play_button.draw(screen):
                game_paused = 1
                menu_state = 'game'
            #puts onto the options screen
            if options_button.draw(screen):
                game_paused = 2
                menu_state = 'options'
            #quits the game
            if quit_button.draw(screen):
                run = False
            if credits_button.draw(screen):
                game_paused = 3
                menu_state = 'credits'
            #displays the text
            play_button.update(screen)
            options_button.update(screen)
            quit_button.update(screen)
            credits_button.update(screen)
            play_button.changecolour(main_font)
            options_button.changecolour(main_font)
            quit_button.changecolour(main_font)
            credits_button.changecolour(main_font)
            

    if game_paused == 2:
        menu_state = 'options'
        if menu_state == 'options':
            screen.blit(sky_blue,(0,0))
            if back_button.draw(screen):
                game_paused = 0
                menu_state = 'main'
            back_button.update(screen)
            back_button.changecolour(main_font)
            if volume_button.draw(screen):
                game_paused = 4
                menu_state = 'volume'
            volume_button.update(screen)
            volume_button.changecolour(main_font)
            
            
            
    if game_paused == 4:
            menu_state = 'volume'
            screen.blit(sky_blue,(0,0))
            if mute_button.draw(screen):
                initial_volume = 0
                pygame.mixer.music.set_volume(initial_volume)
            if onehundred_percent_button.draw(screen):
                initial_volume = 0.5#sets volume to 50% because i think 1 is too loud
                pygame.mixer.music.set_volume(initial_volume)
            if twenty_percent_button.draw(screen):
                initial_volume = 0.1#sets volume to 10% 
                pygame.mixer.music.set_volume(initial_volume)
            if forty_percent_button.draw(screen):
                initial_volume = 0.2#sets volume to 20% 
                pygame.mixer.music.set_volume(initial_volume)
            if sixty_percent_button.draw(screen):
                initial_volume = 0.3 #sets volume to 30% 
                pygame.mixer.music.set_volume(initial_volume)
            if eighty_percent_button.draw(screen):
                initial_volume = 0.4 #sets volume to 40% because i think 0.8 is too loud
                pygame.mixer.music.set_volume(initial_volume)
            
            #update button view
            eighty_percent_button.changecolour(main_font)
            eighty_percent_button.update(screen)
            #80%
            sixty_percent_button.changecolour(main_font)
            sixty_percent_button.update(screen)
            #60%
            forty_percent_button.changecolour(main_font)
            forty_percent_button.update(screen)
            #40%
            twenty_percent_button.changecolour(main_font)
            twenty_percent_button.update(screen)
            #20%
            onehundred_percent_button.changecolour(main_font)
            onehundred_percent_button.update(screen)
            #100%
            mute_button.changecolour(main_font)
            mute_button.update(screen)
            #0%

            if back_button.draw(screen):
                game_paused = 2
                menu_state = 'options'
            back_button.update(screen)
            back_button.changecolour(main_font)
    
    if game_paused == 3:
        menu_state = 'credits'
        if menu_state == 'credits':
            screen.fill(BLUE)
            screen.blit(credits_resized,(273,credits_y))
            if back_button.draw(screen):
                game_paused = 0
                menu_state = 'main'
            back_button.update(screen)
            back_button.changecolour(main_font)








    
    
    


    


    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    pygame.display.update()
    

pygame.quit()