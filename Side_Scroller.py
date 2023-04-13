"""
    'Early Beginnings' is a 2D platformer written in Python
using the pygame library.
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

"""
Import all of the pre-required library stuff.
Then all the game defined classes
"""
import sys
import math
import pygame
# This next line is a 'hack', should not be used in production!
sys.path.insert (1, 'src')
from vector import Vector

from camera import Camera
from level import Level
from player import Player
from flag import Flag

from my_numbers import My_Numbers

"""
TODO: I can see a separate Parent class 'object' which contains
an implementation of a general animation system would be useful!
(and needed later on!!).
"""

"""
Class which contains the actual game, levels and all.
"""
class Game ():
# Generic game related inputs
    keyboard = {"A": False,
                "B": False,
                "LEFT": False,
                "RIGHT": False,
                "UP": False,
                "DOWN": False}
    
    """
        Initialize a game session, load given level etc.
        screen_resolution: (Tuple), the screen resolution.
    """
    def __init__ (self, screen_resolution = (320, 240), level_name="demo.ldf"):
        pygame.init ()
        self.screen_resolution = screen_resolution
        self.screen = pygame.display.set_mode (self.screen_resolution, flags = pygame.SCALED)# | pygame.NOFRAME) # Look up pygame.display
        
        self.level = Level (filename=level_name) # Load the level file
        
        

        self.test_sprite = pygame.image.load('first_map.png')
        self.player = Player (sprite="data/sprite_sheets/player.png", idle_anim = False, pos=[0, 162])#Player (sprite='data/sprite_sheets/flybea.png', idle_anim = True, pos=[0, 162]) # sprite='data/sprite_sheets/player.png'
        
        self.camera = Camera (screen_resolution, self.test_sprite.get_width())
        
        self.tick = 0 # Internal gamerate
        self.clock = pygame.time.Clock () # Pygame does the fps for us
        self.clock.tick ()
        
        self.flag1 = Flag (pos=Vector ([145, 162]), direction="RIGHT")
        self.flag2 = Flag (pos=Vector ([109, 162]), direction="LEFT")
        self.numbers = My_Numbers (pos=Vector([320-18,18]))

    """
        The actual gameloop
    """
    def run (self):
        self.run_flag = True

        # Da game loop
        while self.run_flag == True:
            # Pull events
            self.events ()  # Events/Input
            
            # Update the game physics
            self.update ()  # Logic
            
            # Render the game world
            self.render ()  # Display
            
            # How long did this process take? And limit fps to 30 (pygame can limit)
            self.clock.tick (30) # Set framerate
            self.tick += 1 # My own time keeping (if needed by update ())

        # Cleanup Afterwards
        pygame.quit ()
        quit ()
    
    """
        Input method.
        For simulations; just use events.
    """
    def events (self):
        # Loop through all events, and store the game controller input
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                self.run_flag = False
            elif event.type == pygame.KEYDOWN:
                #print (f"Keydown: {event.key}")
                # 113 == 'Q' for quit
                if event.key == 113:
                    self.run_flag = False

                elif event.key == 1073741904:
                    self.keyboard["LEFT"] = True

                elif event.key == 1073741903:
                    self.keyboard["RIGHT"] = True

                elif event.key == 1073741906:
                    self.keyboard["UP"] = True

                elif event.key == 1073741905:
                    self.keyboard["DOWN"] = True

                # 32 == Spacebar
                elif event.key == 32:
                    self.keyboard["A"] = True

            # Testing what keycode the button is
            #print ("We pressed %s" % (event.key))
            elif event.type == pygame.KEYUP:
                if event.key == 1073741904:
                    self.keyboard["LEFT"] = False

                elif event.key == 1073741903:
                    self.keyboard["RIGHT"] = False

                elif event.key == 1073741906:
                    self.keyboard["UP"] = False

                elif event.key == 1073741905:
                    self.keyboard["DOWN"] = False

                # 32 == Spacebar
                elif event.key == 32:
                    self.keyboard["A"] = False


    """
        Game Logic, physics stuff
    """
    def update (self):
        self.player.update (clock=self.clock, inputs=self.keyboard)
        self.camera.update (self.player.pos)
        self.flag1.update (clock=self.clock)
        self.flag2.update (clock=self.clock)
        self.numbers.update (clock=self.clock)
        
    """
        Render method.
        Blit all sprites to screen and flip it
    """
    def render (self):
        # Background color.
        # Paint over everything so we start out clean
        DARK_GREY = (45, 45, 45)
        self.screen.fill (DARK_GREY)
        self.screen.blit (self.test_sprite, (0 - self.camera.position[0], 0))
        self.flag1.render (self.screen, self.camera)
        self.flag2.render (self.screen, self.camera)
        self.numbers.render (self.screen, self.camera)
        self.player.render (self.screen, self.camera)
        
        # Flip the table
        pygame.display.flip ()
    # ldf (Level Data File) python dictionary dumb, use JSON for later
"""
Load a selected level into memory and ready it up for a Game.run () call.
"""

if __name__ == "__main__":
    # Main_Menu ()
    game = Game ()
    game.run ()

