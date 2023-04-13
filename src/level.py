

"""
"""
class Level ():
   """
   Open and load the filename into memory (python dictionary).
   See the readme file for information about the format for .ldf (level data file) files.
   """
   def __init__ (self, filename="data/levels/demo.ldf"):
       self.filename = filename # save it incase we need the name later on.
       #level_file = open (file=filename, mode='r')
       # This is to be closed after read.
       # This would be a memory problem with big games.
       
       ## Load the map data into a python dictionary.
       #self.background_image = # filename of the bg image, animatin is added in a later version
       #self.foreground_image = # same as above
       #self.items = # List of location of all items, what type etc
       #self.enemies = # List of location of enemies and their type
       #self.


