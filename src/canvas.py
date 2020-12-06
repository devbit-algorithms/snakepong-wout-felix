from array import *


class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = [ [ '' for i in range(width) ] for j in range(height) ]
    def clearScreen(self):
        for x in self.width:
            for y in self.height:
                self.screen[x][y] = ' '
    def draw_symbol(self, x ,y , symbol):
        self.screen[x][y] = symbol
    def outputToTerminal(self):
        for x in self.width:
            for y in self.height:
                print(self.screen[x][y])
