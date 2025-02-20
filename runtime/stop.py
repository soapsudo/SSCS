from dependencies import *


class Stop:
    
    def __init__(self, callback):
        self.restartMenu = callback
        self.database = Database()
        self.utils = Utility()
    
    
    def run(self, option):
        if option == 2:
            self.stopOneContainer()
            
        if option == 1:
            self.stopAllContainers()
            
            
    def stopOneContainer(self):
        containers = self.database.runQuery("SELECT name FROM container")
        
        if(containers == []):
            print("There are no containers to stop.")
           
        else:
            for i in range(len(containers)):
               print(f"{i+1}. {containers[i]}")
               
            print("Choose a container to stop:")   
            chosenContainer = input()
            
            if self.utils.inputCheck(chosenContainer, 1, len(containers)):
                chosenContainer = int(chosenContainer)
                self.utils.executeBash(["./stop.sh", containers[chosenContainer-1]])
                time.sleep(2)
            else:
                print(f"{bcolors.WARNING}Invalid input. Please choose one of the available containers.{bcolors.ENDC}")
                time.sleep(2)
                self.stopOneContainer()
        
        self.restartMenu()        
    
    def stopAllContainers(self):
        containers = self.database.runQuery("SELECT name FROM container")
        
        if(containers == []):
            print("There are no containers to stop.")
            time.sleep(2)
            
        else:
            for i in range(len(containers)):
                self.utils.executeBash(["./stop.sh", containers[i]]) 
            time.sleep(2)
            
        self.restartMenu()    