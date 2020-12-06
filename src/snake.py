class snake:
    def __init__(self,x,y,length):
        self.x = x
        self.y = y
        self.length = length
    def changePosition(self,x,y):
        self.x = x
        self.y = y
    def GetY(self):
        return self.y
    def GetX(self):
        return self.x