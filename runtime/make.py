from dependencies import *

class Make:
    
    def __init__ (self, callback):
        self.utils = Utility()
        self.database = Database()
        self.restartMenu = callback
    
    def run(self):
        self.utils.clearTerminal()
        
        containerType = self.containerTypeChoice()
        containerName = self.containerNaming(containerType)
        portNumber = self.portChoice()
                
        self.utils.executeBash(["./make.sh", containerType, containerName])
        
        self.insertContainerRecord(containerType, containerName, portNumber)
        self.restartMenu()        
                           
                           
    def portChoice(self):
        portNumber = input("Input a port to use on your host machine (9000-9999): ")
                
        while self.utils.portCheck(portNumber) == False:
            portNumber = input(f"{bcolors.FAIL}Invalid input. Please choose one of the available ports.{bcolors.ENDC}")
        
        return portNumber    
    
    
    def containerNaming(self, containerType):
        
        containerName = input("Name your container: ")
        
        while(containerName.strip() == ""):
            containerName = input(f"{bcolors.FAIL}Invalid input. Please name your container.{bcolors.ENDC}")
                       
        while(self.utils.containerNameCheck(containerName) == False):
            containerName = input(f"{bcolors.FAIL}You have already made a container with that name, pick another:{bcolors.ENDC}")
        
        return containerName
    
    
    def containerTypeChoice(self):
        containerTypes = self.database.runQuery("SELECT name FROM type")
        enum = 0
        
        print("Choose the type of the container:")
        
        for containerType in containerTypes:
            enum += 1
            print(str(enum) + ". " + containerType)
        
        containerChoice = input()
        
        while self.utils.inputCheck(containerChoice, 1, enum) == False:
            containerChoice = input(f"{bcolors.FAIL}Invalid input. Please choose one of the available options.{bcolors.ENDC}")
            
        containerChoice = self.database.runQuery(f"SELECT name FROM type WHERE type_id = '{int(containerChoice)}'")[0]    
        
        return str(containerChoice)
    
    
    def insertContainerRecord(self, containerType, containerName, portNumber):
        self.database.runQuery(f"""
                                INSERT INTO container (name, local_port, type_id) 
                                VALUES ('{containerName}', '{portNumber}', '{containerType}')
                                """)