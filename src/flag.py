from animation import Animation_System

"""
The flag gameobject.
"""
class Flag ():
    """
    Init a flag at the desired location
    """
    def __init__ (self, pos, direction):
        self.pos = pos
        self.direction = direction
        self.anim = Animation_System (sprite_name="data/sprite_sheets/flag.png", idle_anim = True)
    
    def update (self, clock):
        self.anim (clock, self.direction, True)

    def render (self, screen, camera):
        self.anim.render (screen, camera, self.pos)


