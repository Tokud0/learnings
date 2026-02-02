class Vehicle:
    wheels = 0
    weight = 0
    type = None

    def __init__(self):
        self.wheels = 4
        self.weight = 1000
        self.type = "default"

    __color = "#000"
    
    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color
    
    def __start(self):
        pass

    def run(self):
        return 10
    
    def __repr__(self):
        return f'type: {self.type}, wheels: {self.wheels}'
