from dependencies import *

class Main:
   
    def __init__(self):
        self.setup = Setup()
        self.utils = Utility()
        self.make = Make(self.start)
        self.startContainer = Start(self.start)
        self.stopContainer = Stop(self.start)
        self.deleteContainer = Delete(self.start)
    
    def start(self, alreadyRun = True):
        
        self.utils.clearTerminal()
        
        if alreadyRun == False:
            self.setup.run()
            self.utils.clearTerminal()
        
        print("||================SSCS================||")
        print("||Choose one of the following options:||")
        print("||1. Add a container to the host======||")
        print("||2. Start all containers=============||")
        print("||3. Start a single container=========||")
        print("||4. Stop all containers==============||")
        print("||5. Stop a single container==========||")
        print("||6. Delete a container===============||")
        print("||7. Exit=============================||")
        print("||===============>>><<<===============||")
        
        chosenOption = input()
        
        if self.utils.inputCheck(chosenOption, 1, 7):
            
            chosenOption = int(chosenOption)
            
            if chosenOption == 1:
                self.make.run()
            elif chosenOption == 2:
                self.startContainer.run(2)
            elif chosenOption == 3:
                self.startContainer.run(1)
            elif chosenOption == 4: 
                self.stopContainer.run(1)
            elif chosenOption == 5:
                self.stopContainer.run(2)
            elif chosenOption == 6:
                self.deleteContainer.run()
            elif chosenOption == 7:
                exit()    
        else:
            print(f"{bcolors.WARNING}Invalid input. Please choose one of the available options.{bcolors.ENDC}")
            time.sleep(2)
            self.start(False)

def startMenu(alreadyRun):
    main = Main()
    main.start(alreadyRun)
    
startMenu(False)    