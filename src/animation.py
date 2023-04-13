"""
    'Early Beginnings' is a 2D platformer written in Python
using the 'pygame' library.
All of the game art is under a different license, see directory 'data'.
    Copyright (C) <2023>  <Kristoffer R. Tandberg, "ktndbrg">

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import math
import pygame

"""
Class Animation_System
General features for the animation of sprites
"""
class Animation_System ():
    """
    sprite_name = "data/sprite_sheets/pink.png"
    idle_anim = False
    """
    def __init__ (self, sprite_name, idle_anim):
        self.image = pygame.image.load(sprite_name).convert_alpha()
        self.px_size = self.image.get_height () # ONLY HAVE THE SPRITE SHEET HORIZONTAL!
        # How many sprites?
        # The entire width |---------|, divided by the size of a single sprite, since you go left and right divide by 2.
        self.number_of_sprites = self.image.get_width () / (2 * self.px_size) # How many animation sprites?
        self.anim_step = True # True means go upwards, false means go downwards.
        self.ANI_SPRITE_LEN = 0.100 # Number of seconds each animation sprite lasts, Constant!
        self.anim_timer = self.ANI_SPRITE_LEN # Same as above, but tracks time left
        self.animation_frame = 1
        self.sprite_rect = [0, 0]
        self.idle_anim = idle_anim # Are we animating idle? See flybea.png

    def __call__ (self, clock, direction = "RIGHT", movement = True):
        # Standing still
        if movement == False and self.idle_anim == False:
            if direction == "LEFT":
                self.sprite_rect = [self.number_of_sprites * self.px_size, 0]
            elif direction == "RIGHT":
                self.sprite_rect = [0, 0]
        # Animate (player) movement
        else:
            self.anim_timer -= (clock.get_time () / 1000.0)
            if self.anim_timer < 0.0:
                self.anim_timer = self.ANI_SPRITE_LEN
                if self.anim_step == True:
                    self.animation_frame += 1
                    
                    # Are we done with the 'upwards' animations?
                    if self.animation_frame >= self.number_of_sprites:
                        # Yes, so go downwards
                        self.anim_step = False
                elif self.anim_step == False:
                    self.animation_frame -= 1
                    # Are we done with the 'downwards' animations?
                    if self.animation_frame == 1:
                        # Yes, so go upwards
                        self.anim_step = True
            
            if direction == "LEFT":
                self.sprite_rect[0] = (self.number_of_sprites + self.animation_frame - 1) * self.px_size
                
            elif direction == "RIGHT":
                self.sprite_rect[0] = 0 + (self.animation_frame - 1) * self.px_size
    
    """
        render (self, screen, camera, pos)
        Blit the sprite onto the screen based on where the camera is located.
    """
    def render (self, screen, camera, pos):
        screen.blit (self.image, (pos.row[0] - camera.position[0] - (self.px_size / 2.0), pos.row[1] - self.px_size), pygame.Rect (self.sprite_rect, (self.px_size, self.px_size)))
                


