from dependencies import *

class Start:
    
    def __init__(self, callback):
        self.restartMenu = callback
        self.database = Database()
        self.utils = Utility()
    
    
    def run(self, option):
        if option == 1:
            self.runOneContainer()
            
        if option == 2:
            self.runAllContainers()
            
            
    def runOneContainer(self):
        containers = self.database.runQuery("SELECT name FROM container")
        ports = self.database.runQuery("SELECT local_port FROM container")
        
        if(containers == []):
            print("There are no containers to start.")
            time.sleep(2)
        else:
            print("Choose a container to start:")
            for i in range(len(containers)):
                print(f"{i+1}. {containers[i]}")
                
            chosenContainer = input()
            
            if self.utils.inputCheck(chosenContainer, 1, len(containers)):
                chosenContainer = int(chosenContainer)
                self.utils.executeBash(["./run.sh", containers[chosenContainer-1], ports[chosenContainer-1]])
                print(f"{containers[chosenContainer-1]} has been started.")
                time.sleep(2)
            else:
                print(f"{bcolors.WARNING}Invalid input. Please choose one of the available containers.{bcolors.ENDC}")
                time.sleep(2)
                self.runOneContainer()
        
        self.restartMenu()
        
    
    def runAllContainers(self):
        containers = self.database.runQuery("SELECT name FROM container")
        ports = self.database.runQuery("SELECT local_port FROM container")
        
        if(containers == []):
            print("There are no containers to start.")
            time.sleep(2)            
            
        else:
            for i in range(len(containers)):
                self.utils.executeBash(["./run.sh", containers[i], ports[i]]) 
            print("All containers have been started.")    
                
        self.restartMenu()