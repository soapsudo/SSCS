from dependencies import *

class Main:
   
    def __init__(self):
        self.setup = Setup
        self.make = Make
        self.startContainer = Start
        self.stopContainer = Stop
        self.deleteContainer = Delete
        self.utils = Utility
       
   
    def start(self, alreadyRun):
        
        self.utils.clearTerminal(Utility())
        
        if alreadyRun == False:
            self.setup.run(Setup())
            self.utils.clearTerminal(Utility())
        
        print("||================SSCS================||")
        print("||Choose one of the following options:||")
        print("||1. Add a container to the host======||")
        print("||2. Start all containers=============||")
        print("||3. Start a single container=========||")
        print("||4. Stop all containers==============||")
        print("||5. Stop a single container==========||")
        print("||6. Delete a container===============||")
        print("||===============>>><<<===============||")
        
        chosenOption = input()
        
        if self.utils.inputCheck(Utility(), chosenOption, 1, 6):
            
            chosenOption = int(chosenOption)
            
            if chosenOption == 1:
                self.make.run(Make())
            elif chosenOption == 2:
                self.startContainer.run(Start(), 1)
            elif chosenOption == 3:
                self.startContainer.run(Start(), 2)
            elif chosenOption == 4: 
                self.stopContainer.run(Stop(), 1)
            elif chosenOption == 5:
                self.stopContainer.run(Stop(), 2)
            elif chosenOption == 6:
                self.deleteContainer.run(Delete())
                
        else:
            print(f"{bcolors.WARNING}Invalid input. Please choose one of the available options.{bcolors.ENDC}")
            time.sleep(2)
            self.start(False)


main = Main()
main.start(False)