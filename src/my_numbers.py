from animation import Animation_System

"""
The flag gameobject.
"""
class My_Numbers ():
    """
    Init a flag at the desired location
    """
    def __init__ (self, pos):
        self.pos = pos
        self.anim = Animation_System (sprite_name="data/sprite_sheets/numbers.png", idle_anim = True)
    
    def update (self, clock):
        self.anim (clock)

    def render (self, screen, camera):
        self.anim.render (screen, camera, self.pos)


