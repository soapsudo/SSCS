from runtime.setup import Setup

import os
import platform
import subprocess

class Main:
   
    def __init__(self):
        self.setup = Setup
       
   
    def start(self, alreadyRun):
        
        self.clearTerminal()
        
        if alreadyRun == False:
            self.setup.run(Setup())
            self.clearTerminal()
        
        print("========SSCS========")
        print("Choose one of the following options:")
        print("1. Add a container to the host")
        print("2. Start all containers")
        print("3. Start a single container")
        print("4. Stop all containers")
        print("5. Stop a single container")
        print("6. Delete a container")
        
    
    def clearTerminal(self):
        command = "cls" if platform.system() == "Windows" else "clear"
        subprocess.run(command, shell=True)
    
main = Main()
main.start(False)