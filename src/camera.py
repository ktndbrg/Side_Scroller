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

"""
    Where to draw the sprites etc.
    Relate Gameworld Coordinates into Screen Coordinates

    NB! We do not mess with Y-coordinate yet!
"""
class Camera ():
    """
    """
    def __init__ (self, screen_resolution, background_length):
        self.screen_resolution = screen_resolution
        self.position = [int (screen_resolution[0] / 2), 0]
        self.bg_len = background_length
    
    """
        Update the camera position based on players X-coordinate.
        Player *should* always be in the center of the screen.
    """
    def update (self, position, ):
        self.position[0] = int (position.row[0] - self.screen_resolution[0] / 2)

        # The camera will never move outside the gameworld.
        # This code below ensures it, first left side of screen < 0
        # then right side of screen >
        if self.position[0] < 0:
            self.position[0] = 0
        elif self.position[0] > self.bg_len - self.screen_resolution[0]:
            self.position[0] = self.bg_len - self.screen_resolution[0]


