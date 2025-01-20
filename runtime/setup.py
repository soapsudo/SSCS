from dependencies import *

class Setup:
    
    def __init__(self):
        self.utils = Utility()
        self.database = Database()
    
    
    def run(self):        

        self.database.setup()

        scripts = ["initial.sh", "build.sh", "delete.sh", "make.sh", "run.sh", "stop.sh"]
                
        for script in scripts:
            self.utils.executeBash(["sudo", "chmod", "a+x", f"{script}"])
            
        self.utils.executeBash(["./initial.sh"])        



