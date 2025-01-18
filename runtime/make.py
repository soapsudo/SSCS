from dependencies import *

class Make:
    
    def __init__ (self):
        self.utils = Utility()
        self.database = Database()
    
    def run(self):
        self.utils.clearTerminal()
        
        containerName = input("Name your container (leave empty for default): ")
        portNumber = input("Input a port to use on your host machine (9000-9999): ")
                
        while self.utils.portCheck(portNumber) == False:
            portNumber = input(f"{bcolors.FAIL}Invalid input. Please choose one of the available ports.{bcolors.ENDC}")        
        
        containerType = input("Choose the type of the container:")
        
        self.utils.executeBash(["./make.sh", containerName, portNumber])
                