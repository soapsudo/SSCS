from dependencies import *

class Setup:
    
    def __init__(self):
        self.utils = Utility
    
    def run(self):        

        scripts = ["initial.sh", "build.sh", "delete.sh", "make.sh", "run.sh", "stop.sh"]
                
        for script in scripts:
            self.utils.executeBash(Utility(), ["ls", "-al"])
            script.strip("'")
            self.utils.executeBash(Utility(), ["sudo", "chmod", "a+x", f"{script}"])
            
        self.utils.executeBash(Utility(), ["./initial.sh"])        



