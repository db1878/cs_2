import pygame
from level_map_data import *
from pygame.locals import *


pygame.init()

#define screen variables
screen_width = 1024
screen_height = 736
tile_size = 16
#display and caption
screen = pygame.display.set_mode((screen_width, screen_height))
#sprite group
enemy_group = pygame.sprite.Group()


def check_collision(player, blocks):
    for block in blocks:
        if player.rect.colliderect(block[1].x, block[1].y - 1, block[1].width, 1):
            return True
    return False


#class world for the grass layer
class World_Grass_Layer():
    def __init__(self, data):
        self.tile_list = []
        #load images
        block_2 = pygame.image.load('Map/levels/images/blocks/grass_blocks/2.png').convert_alpha()
        block_3 = pygame.image.load('Map/levels/images/blocks/grass_blocks/3.png').convert_alpha()
        block_4 =pygame.image.load('Map/levels/images/blocks/grass_blocks/4.png').convert_alpha()
        block_26 =pygame.image.load('Map/levels/images/blocks/grass_blocks/26.png').convert_alpha()
        block_28 =pygame.image.load('Map/levels/images/blocks/grass_blocks/28.png').convert_alpha()
        block_30 =pygame.image.load('Map/levels/images/blocks/grass_blocks/30.png').convert_alpha()
        block_51 =pygame.image.load('Map/levels/images/blocks/grass_blocks/51.png').convert_alpha()
        block_53 =pygame.image.load('Map/levels/images/blocks/grass_blocks/53.png').convert_alpha()
        block_55 =pygame.image.load('Map/levels/images/blocks/grass_blocks/55.png').convert_alpha()
        block_76 =pygame.image.load('Map/levels/images/blocks/grass_blocks/76.png').convert_alpha()
        block_80 =pygame.image.load('Map/levels/images/blocks/grass_blocks/80.png').convert_alpha()
        block_103 =pygame.image.load('Map/levels/images/blocks/grass_blocks/103.png').convert_alpha()
        #go through the mega list and place ablock where the block id is equal to the number 
        row_count = 0
        for row in data:
            #counts where about on the mega list the tile is supposed to be, and that is then the x coordinate
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(block_2,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(block_3,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(block_4,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 5:
                    img = pygame.transform.scale(block_26,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 7:
                    img = pygame.transform.scale(block_28,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 9:
                    img = pygame.transform.scale(block_30,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 10:
                    img = pygame.transform.scale(block_51,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 11:
                    img = pygame.transform.scale(block_28,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 12:
                    img = pygame.transform.scale(block_53,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 13:
                    img = pygame.transform.scale(block_28,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 14:
                    img = pygame.transform.scale(block_55,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 15:
                    img = pygame.transform.scale(block_76,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img and rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 16:
                    img = pygame.transform.scale(block_28,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 17:
                    img = pygame.transform.scale(block_28,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 18:
                    img = pygame.transform.scale(block_28,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 19:
                    img = pygame.transform.scale(block_80,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 21:
                    img = pygame.transform.scale(block_76,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 22:
                    img = pygame.transform.scale(block_103,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 23:
                    img = pygame.transform.scale(block_80,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 6:
                    img = pygame.transform.scale(block_28,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 8:
                    img = pygame.transform.scale(block_28,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            #pygame.draw.rect(screen,(255,255,255), tile[1], 2)
    

class World_Plants_Layer():
    def __init__(self, data):
        self.tile_list = []
        #load images
        block_0 = pygame.image.load('Map/levels/images/blocks/plants/block_0_0.png').convert_alpha()
        block_1 = pygame.image.load('Map/levels/images/blocks/plants/block_0_1.png').convert_alpha()
        block_2 = pygame.image.load('Map/levels/images/blocks/plants/block_0_2.png').convert_alpha()
        block_3 = pygame.image.load('Map/levels/images/blocks/plants/block_0_3.png').convert_alpha()
        block_4 = pygame.image.load('Map/levels/images/blocks/plants/block_0_4.png').convert_alpha()
        block_12 = pygame.image.load('Map/levels/images/blocks/plants/block_1_0.png').convert_alpha()
        block_13 = pygame.image.load('Map/levels/images/blocks/plants/block_1_1.png').convert_alpha()
        block_14 = pygame.image.load('Map/levels/images/blocks/plants/block_1_2.png').convert_alpha()
        block_15 = pygame.image.load('Map/levels/images/blocks/plants/block_1_3.png').convert_alpha()
        block_16 = pygame.image.load('Map/levels/images/blocks/plants/block_1_4.png').convert_alpha()
        block_24 = pygame.image.load('Map/levels/images/blocks/plants/block_2_0.png').convert_alpha()
        block_25 = pygame.image.load('Map/levels/images/blocks/plants/block_2_1.png').convert_alpha()
        block_26 = pygame.image.load('Map/levels/images/blocks/plants/block_2_2.png').convert_alpha()
        block_28 = pygame.image.load('Map/levels/images/blocks/plants/block_2_4.png').convert_alpha()
        block_29 = pygame.image.load('Map/levels/images/blocks/plants/block_2_5.png').convert_alpha()
        block_40 = pygame.image.load('Map/levels/images/blocks/plants/block_3_4.png').convert_alpha()
        block_49 = pygame.image.load('Map/levels/images/blocks/plants/block_4_1.png').convert_alpha()
        #go through the mega list and place ablock where the block id is equal to the number 
        row_count = 0
        for row in data:
            #counts where about on the mega list the tile is supposed to be, and that is then the x coordinate
            col_count = 0
            for tile in row:
                if tile == 0:
                    img = pygame.transform.scale(block_0,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 1:
                    img = pygame.transform.scale(block_1,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(block_2,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(block_3,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    img = pygame.transform.scale(block_4,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 12:
                    img = pygame.transform.scale(block_12,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 13:
                    img = pygame.transform.scale(block_13,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 14:
                    img = pygame.transform.scale(block_14,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 15:
                    img = pygame.transform.scale(block_15,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 16:
                    img = pygame.transform.scale(block_16,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 24:
                    img = pygame.transform.scale(block_24,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 25:
                    img = pygame.transform.scale(block_25,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 26:
                    img = pygame.transform.scale(block_26,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 28:
                    img = pygame.transform.scale(block_28,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 29:
                    img = pygame.transform.scale(block_29,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 40:
                    img = pygame.transform.scale(block_40,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 49:
                    img = pygame.transform.scale(block_49,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


class World_Spike_Layer():
    def __init__(self, data):
        self.tile_list = []
        #load images
        block_3 = pygame.image.load('Map/levels/images/blocks/spike/211.png')
        block_50 = pygame.image.load('Map/levels/images/blocks/spike/115.png')
        block_51 = pygame.image.load('Map/levels/images/blocks/spike/116.png')
        block_52 = pygame.image.load('Map/levels/images/blocks/spike/117.png')
        #go through the mega list and place ablock where the block id is equal to the number 
        row_count = 0
        for row in data:
            #counts where about on the mega list the tile is supposed to be, and that is then the x coordinate
            col_count = 0
            for tile in row:
                if tile == 3:
                    img = pygame.transform.scale(block_3,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 50:
                    img = pygame.transform.scale(block_50,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 51:
                    img = pygame.transform.scale(block_51,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 52:
                    img = pygame.transform.scale(block_52,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            
class World_Enemy_Layer():
    def __init__(self, data):
        self.tile_list = []
        
        row_count = 0
        for row in data:
            #counts where about on the mega list the tile is supposed to be, and that is then the x coordinate
            col_count = 0
            for tile in row:
                if tile == 1:
                    skelly1 = Enemy(col_count * tile_size , row_count * tile_size -16)
                    enemy_group.add(skelly1)
                col_count += 1
            row_count += 1











#PLAYER CLASS
#PLAYERCLASS



world_grass = World_Grass_Layer(grass_layer_world_data)


jump_sound = pygame.mixer.Sound('Map/sound/Minifantasy_Dungeon_SFX/12_human_jump_2.wav')
class Player():
    def __init__(self, x ,y):
        #animation
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0 
        for num in range(0,7):
            img_right = pygame.image.load(f'Map/levels/images/player/run_{num}.png')
            img_right = pygame.transform.scale(img_right,(26,32))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.sound_cooldown = 300  
        self.last_sound_time = 0
        #velocity of jump
        # Load the walking sound effects
        self.walk_sounds = [
            pygame.mixer.Sound('Map/sound/Minifantasy_Dungeon_SFX/16_human_walk_stone_1.wav'),
            pygame.mixer.Sound('Map/sound/Minifantasy_Dungeon_SFX/16_human_walk_stone_2.wav'),
            pygame.mixer.Sound('Map/sound/Minifantasy_Dungeon_SFX/16_human_walk_stone_3.wav')
        ]
    def update(self, ground_blocks):
        dx = 0
        dy = 0
        walk_cooldown = 8
        #change in y and change in x
    #time
        current_time = pygame.time.get_ticks()
        #get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx -= 5
            self.counter  += 1
            self.direction = -1
            if current_time - self.last_sound_time > self.sound_cooldown:
                self.walk_sounds[0].play()
                self.last_sound_time = current_time
            #time delay
        if key[pygame.K_d]:
            dx += 5
            self.counter += 1
            self.direction = 1
            if current_time - self.last_sound_time > self.sound_cooldown:
                self.walk_sounds[1].play()
                self.last_sound_time = current_time
        if key[pygame.K_d] and key[pygame.K_a]:
                self.counter = 0
        if key[pygame.K_SPACE] and self.jumped == False:
            if check_collision(self, ground_blocks):  # Check collision here
                self.vel_y = -12
                self.jumped = True
                jump_sound.play()
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_a] == False and key[pygame.K_d] == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

        #animation handling 
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1 
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]
            
        



        #add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        #check for collison
        for tile in world_grass.tile_list:
            #check for x collison
            if tile[1].colliderect(self.rect.x+dx, self.rect.y, self.width, self.height):
                dx = 0

            # check for y collison
            if tile[1].colliderect(self.rect.x, self.rect.y +dy, self.width, self.height):
                #check if below or on top collison
                #below
                #+ vel = falling - vel = jumping
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                
                

        #update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        

        #draw player on the screen
        screen.blit(self.image, self.rect)
        #pygame.draw.rect(screen,(255,55,55), self.rect, 2)
#2 = skele
#4 = orc


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Map/levels/images/Pixel Crawler - FREE - 1.8/Enemy/Skeleton Crew/Skeleton - Base/Run/run1.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter =0
    
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if self.move_counter >=50:
            self.move_direction *= -1
            self.move_counter = 0
    



            











