from dependencies import *

class Setup:
    
    def run(self):
        os.system("sudo chmod a+x /scripts")
        os.system("./scripts/initial.sh")