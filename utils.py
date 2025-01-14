from dependencies import *

class Utility:
    def inputCheck(self, input, lowerBound, upperBound):    
        if input.isnumeric():
            return int(input) >= lowerBound and int(input) <= upperBound
            
        return False        
        
    def clearTerminal(self):
        command = "cls" if platform.system() == "Windows" else "clear"
        subprocess.run(command, shell = True)    
    
    def portCheck(self, portNumber):
        return portNumber.isnumeric() and int(portNumber) >= 9000 and int(portNumber) <= 9999
            
    def executeBash(self, command, wd = "scripts"):
        subprocess.run(command, cwd = wd, check = True)