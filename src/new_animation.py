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
    pixel_size = (18, 18)
    idle_anim = True
    """
    def __init__ (self, sprite_name, pixel_size, idle_anim):
        self.image = pygame.image.load(sprite_name).convert_alpha()
        self.pixel_size = pixel_size
        

    def __call__ (self, clock, animation = True):
        pass
    
    """
        render (self, screen, camera, pos)
        Blit the sprite onto the screen based on where the camera is located.
    """
    def render (self, screen, camera, pos):
        pass
                


