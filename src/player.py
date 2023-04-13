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
from vector import Vector
from animation import Animation_System

"""
Player class.
Everything it sounds like.
Contains the position, velocity, acceleration, sprite_image etc etc.
"""
class Player ():
    def __init__ (self, sprite="data/sprite_sheets/pink.png", idle_anim = False, pos=[0, 0]):
        # Sprite and Animation system
        self.anim = Animation_System (sprite, idle_anim)
        self.sprite_rect = (0, 0)
        self.direction = "RIGHT" # Left right in the game world 

        # Game related
        self.FULL_HP = 3
        self.hp = self.FULL_HP
        self.movement = False

        # These might be a separate class, 'Movement'
        self.pos = Vector (pos)
        self.vel = Vector ([0, 0])
        
    """
    update.
    Do player stuff, like updating the position, hp, etc
    """
    def update (self, clock, inputs):
    
        # Reset velocity
        self.vel = Vector ([0, 0])
        
        # Move left/right
        if inputs["LEFT"] == True and inputs["RIGHT"] == False:
            # Player can walk twice his length each second
            # TODO: Add powerup that makes movement faster
            # Remove the *5, it is not intended
            self.vel -= Vector ([24.0 * 2.0 , 0.0])
            self.direction = "LEFT"
            self.movement = True
        if inputs["RIGHT"] == True and inputs["LEFT"] == False:
            # Player can walk twice his length each second
            # TODO: Add powerup that makes movement faster
            self.vel += Vector ([24.0 * 2.0 , 0.0])
            self.direction = "RIGHT"
            self.movement = True
        
        if inputs["LEFT"] == False and inputs["RIGHT"] == False:
            self.movement = False

        # Update player position
        self.pos += self.vel * (clock.get_time () / 1000.0)

        # Update the player's animation
        self.anim (clock, self.direction, self.movement)

    """
    Did we collide with something? An enemy maybe?
    """
    def collision (self):
        # Not yet implemented!
        pass

    """
    Player got hit, loose a life.
    """
    def hurt (self):
        self.hp -= 1

    """
    Render the player onto the screen,
    Pass/give all of the information over to animation system,
    it will do the rendering for us
    """
    def render (self, screen, camera):
        self.anim.render (screen, camera, self.pos)


