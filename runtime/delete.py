from dependencies import *

class Delete:
    
    def __init__(self, callback):
        self.restartMenu = callback
        self.database = Database()
        self.utils = Utility()
    
    
    def run(self):
        containers = self.database.runQuery("SELECT name FROM container")
        
        if(containers == []):
            print("There are no containers to delete.")
            time.sleep(2)            
        else:
            print("Choose a container to delete:")
            
            for i in range(len(containers)):
                print(f"{i+1}. {containers[i]}")
                    
            container = input()
    
            if self.utils.inputCheck(container, 1, len(containers)):
                container = int(container)
                self.utils.executeBash(["./delete.sh", containers[container-1]])
                
                self.database.runQuery(f"DELETE FROM container WHERE name = '{containers[container-1]}'")
                
                print(f"{containers[container-1]} has been deleted.")
                time.sleep(2)        
        
        self.restartMenu()        