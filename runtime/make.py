from dependencies import *

class Make:
    
    def __init__ (self):
        self.utils = Utility()
        self.database = Database()
    
    def run(self):
        self.utils.clearTerminal()
        
        containerName = input("Name your container (leave empty for default): ")
        portNumber = input("Input a port to use on your host machine (9000-9999): ")
        
        self.containerType()
                
        while self.utils.portCheck(portNumber) == False:
            portNumber = input(f"{bcolors.FAIL}Invalid input. Please choose one of the available ports.{bcolors.ENDC}")        
        
        self.utils.executeBash(["./make.sh", containerName, portNumber])
        
    def containerType(self):
        types = self.database.runQuery("SELECT name FROM type")
        
        for type in types:
            print(type)
        
        time.sleep(15)    