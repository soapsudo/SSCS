from dependencies import *


class Stop:
    
    def __init__(self, callback):
        self.restartMenu = callback
    
    def run(self, option):
        if option == 1:
            self.stopOneContainer()
            
        if option == 2:
            self.stopAllContainers()
            
    def stopOneContainer(self):
        return 
    
    def stopAllContainers(self):
        return