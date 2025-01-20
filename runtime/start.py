from dependencies import *

class Start:
    
    def __init__(self, callback):
        self.restartMenu = callback
    
    
    def run(self, option):
        if option == 1:
            self.runOneContainer()
            
        if option == 2:
            self.runAllContainers()
            
            
    def runOneContainer(self):
        return 
    
    
    def runAllContainers(self):
        return