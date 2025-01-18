from dependencies import *

class Utility:
    
    def __init__(self):
        self.database = Database()
    
    def inputCheck(self, input, lowerBound, upperBound):    
        if input.isnumeric():
            return int(input) >= lowerBound and int(input) <= upperBound
            
        return False        
        
        
    def clearTerminal(self):
        command = "cls" if platform.system() == "Windows" else "clear"
        subprocess.run(command, shell = True)    
    
    
    def portCheck(self, portNumber):
        check1 = portNumber.isnumeric() and int(portNumber) >= 9000 and int(portNumber) <= 9999
        check2 = False
        
        if check1:
            check2 = self.database.runQuery(f"SELECT container_id FROM container WHERE port_number = {portNumber}")
            
            if not check2:
                check2 = True
        
        return check1 and check2
            
            
    def executeBash(self, command, wd = "scripts"):
        subprocess.run(command, cwd = wd, check = True)
    
    
    def containerNameCheck(self, containerName):
        result = self.database.runQuery(f"SELECT name FROM container WHERE name = {containerName}")
        
        if not result:
            return True
            
        else:
            return False