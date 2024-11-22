from datetime import datetime
import statistics

# Lindsey's branch.

# Each experiment will be an object defined by the following attributes:
#       name, date, category, results
class Experiment:

    # The constructor method will initialize an instance for each experiment
    def __init__(self,name,date,category,results):
        self.name = name
        self.date = date
        self.category = category
        self.results = results
    

# This function will take the list of experiments called "listOfExperiments" as input
def addExperiment(listOfExperiments):
    print("\n---------------------------------------------------")
    print("You will be entering the data for a new experiment.")
    print("---------------------------------------------------")
    # String: It doesn't need verification.
    name = input("Experiment's name: ")

    # Datetime object: it needs verification with strptime
    while True:
        try:
            date_input = input("Date (dd/mm/yyyy): ")
            date = datetime.strptime(date_input, "%d/%m/%Y")
            break
        except ValueError:
            print("Invalid format, please try again.")
    
    # String: User will not type it, it will be selected.
    print("Select a number according to the category:")
    print("1. Biology.")
    print("2. Physics")
    print("3. Chemistry")
    # Verification required, to make sure the input is a valid integer
    while True:
        try:
            categoryOpt = int(input("Type a number: ")) # Change it to restrict user's input
            if categoryOpt == 1:
                category = "Biology"
                break
            elif categoryOpt == 2:
                category = "Physics"
                break
            elif categoryOpt == 3:
                category = "Chemistry"
                break
            elif categoryOpt <=0:
                print("Invalid input, please try again.")
            else:
                print("Input is a non-existent category, please try again")
                continue
        except:
            print("Invalid input, please try again.")

    # Float: verification required to make sure the input is a number
    results = []
    while True:
        try:
            numberOfResults = int(input("\nYou will be entering the results now. \nPlease enter the number of results (max 10): "))
            if 0 <= numberOfResults <=10:
                for i in range(numberOfResults):
                    while True:
                        try:
                            results.append(float(input(f"Result #{i+1}: ")))
                            break
                        except:
                            print("Error, the value is not a number, try again.")
                break
            else:
                print("\nInvalid, input should be a positive integer.")
                continue
        except:
            print("\nInvalid, input should be a positive integer.")


    
    # Object, the experiment is instanced. 
    thisExperiment = Experiment(name,date,category,results)
    listOfExperiments.append(thisExperiment)
    print("\nExperiment successfully added.")
    input("\nPress Enter to continue...")

# This function will take the list of experiments called "listOfExperiments" as input
def printExperiments(listOfExperiments):
    # This function will display a message if there are no experiments to display.
    if not listOfExperiments:
        print("No experiments to display.")
        input("\nPress 'Enter' to continue...")
        return

    print("----------------------------------------------------")
    print("This is the list of experiments you have documented.")
    
    for i, thisExperiment in enumerate(listOfExperiments, start=1):
        print("----------------------------------------------------")   
        print(f"Experiment #{i}")
        print(f"Name: {thisExperiment.name}")
        print(f"Date: {thisExperiment.date}")
        print(f"Category: {thisExperiment.category}")
        print(f"Results: {thisExperiment.results}")
    input("\nPress Enter to continue...")

# This function will display the list of experiments (only by name)
def displayExperimentsName(listOfExperiments):
    print("--------------------")
    print("List of experiments:")
    print("--------------------")
    for i, thisExperiment in enumerate(listOfExperiments, start=1): 
        print(f"{i}. {thisExperiment.name}")
    print("--------------------")

def removeExperiment(listOfExperiments):
    # This function will display a message if there are no experiments to remove.
    if not listOfExperiments:
        print("No experiments registered yet.")
        input("\nPress 'Enter' to continue...")
        return
    
    print("-----------------------------------")
    print("You will be removing an experiment.")
    print("-----------------------------------")
    # Make sure the input is an integer
    while True:
        try:
            experimentToRemove = int(input("\nInput the number of the experiment you want to remove, \nif you are not sure about the number, press '0' to view the list of names: "))
            # The number must be an integer between 1 and the number of experiments.
            if 1 <= experimentToRemove <= len(listOfExperiments):
                del listOfExperiments[experimentToRemove-1]
                print(f"\nExperiment #{experimentToRemove} removed successfully.")
                input("\nPress Enter to continue...")
                break
            elif experimentToRemove == 0:
                displayExperimentsName(listOfExperiments)
                continue
            else:
                print("\nNot a valid input. Please try again.")
                continue
        except:
            print("\nError, the input is not an integer.")


def calculateStatistics(listOfExperiments):
    # This function will display a message if there are no experiments to remove.
    if not listOfExperiments:
        print("No experiments registered yet.")
        input("\nPress 'Enter' to continue...")
        return

    print("--------------------------------------------")
    print("Calculation of statistics for an experiment.")
    print("--------------------------------------------")    
    
    while True:
        try:
            expNumber = int(input("\nSelect the number of the experiment. \nIf you are not sure about the number of the experiment, \npress 0 to view the list: ")) 
            # The number must be an integer between 1 and the number of experiments.
            if 1 <= expNumber <= len(listOfExperiments):
                print("--------------------------------------------")
                print(f"The results for this experiment are: {listOfExperiments[expNumber-1].results}")
                print(f"The average is: {statistics.mean(listOfExperiments[expNumber-1].results)}")
                print(f"The minimun value is: {min(listOfExperiments[expNumber-1].results)}")
                print(f"The maximum value is: {max(listOfExperiments[expNumber-1].results)}")
                input("\nPress Enter to continue...")
                break
            elif expNumber == 0:
                displayExperimentsName(listOfExperiments)
                continue
            else:
                print("\nNot a valid input. Please try again.")
                continue
        except:
            print("\nError, the input is not an integer.")


def compareExperiments(listOfExperiments):
    # This function will display a message if there are no experiments or if there is only one experiment.
    if not listOfExperiments:
        print("No experiments registered yet.")
        input("\nPress 'Enter' to continue...")
        return

    elif len(listOfExperiments) == 1:
        print("\nThere is only one experiment, nothing to compare.")
        input("\nPress 'Enter' to continue...")
        return
    
    print("---------------------------------------")
    print("Comparision of two or more experiments.")
    print("---------------------------------------")
    listToCompare = []

    # This loop will be used so that the user can input as many experiments as they need to compare.
    while True:
        experiment = input("\nType the number of the experiment to compare, \nif you need to view the list of experiments, type 0, \nif you want to stop selecting experiments, type 'stop': ")
        # First we need to validate if the number is lower that the number of registered experiments. 
        try:
            if 1 <= int(experiment) <= len(listOfExperiments):
                # Add this experiment to the list of experiments to compare.
                listToCompare.append(int(experiment))
                print(f"\nExperiments to compare: {set(listToCompare)}")
                continue
            elif int(experiment) == 0:
                displayExperimentsName(listOfExperiments)
                continue
            else:
                print("\n*** Attention ***")
                print("\nInvalid input, the experiment doesn't exist.")
        except:
            # We will land here if the text can't be converted to a number
            # There are two options:
            # 1. The text is "stop" (The code should verify if there is enough data)
            # 2. The text is different than "stop" (The code should return a warning)

            # Condition 1. 
            if experiment.lower() == "stop":
                # Verify if there is enough data.
                if len(set(listToCompare))<=1:
                    print("\n*** Attention ***")
                    print("\nYou can't stop. Please enter another experiment. \nThere is only one experiment in the list.")
                    continue
                else:
                    break
            # Condition 2. 
            else:
                print("\n*** Attention ***")
                print("\nInvalid input, it must be an integer or 0.")
                continue
    
    # We need to make sure the elements are unique
    listToCompare = sorted(set(listToCompare))
    listOfMeans = []
    listOfMins = []
    listOfMaxs = []
    for experiment in listToCompare:
        listOfMeans.append(statistics.mean(listOfExperiments[experiment-1].results))
        listOfMins.append(min(listOfExperiments[experiment-1].results))
        listOfMaxs.append(max(listOfExperiments[experiment-1].results))

    print("--------------------")
    print("Comparision of mean:")
    print("--------------------")
    print(f"Highest average: Experiment #{listOfMeans.index(max(listOfMeans))+1} with a value of {max(listOfMeans)}")
    print(f"Lowest average: Experiment #{listOfMeans.index(min(listOfMeans))+1} with the value of {min(listOfMeans)}")
    print("----------------------------")
    print("Comparision of minimum value:")
    print("----------------------------")
    print(f"Highest Min Value: Experiment #{listOfMins.index(max(listOfMins))+1} with a value of {max(listOfMins)}")
    print(f"Lowest Min Value: Experiment #{listOfMins.index(min(listOfMins))+1} with the value of {min(listOfMins)}")
    print("-----------------------------")
    print("Comparision of maximum value:")
    print("-----------------------------")
    print(f"Highest Max Value: Experiment #{listOfMaxs.index(max(listOfMaxs))+1} with a value of {max(listOfMaxs)}")
    print(f"Lowest Max Value: Experiment #{listOfMaxs.index(min(listOfMaxs))+1} with the value of {min(listOfMaxs)}")
    input("\nPress Enter to continue...")

def generateReport(listOfExperiments):
    # This function will display a message if there are no experiments.
    if not listOfExperiments:
        print("No experiments registered yet.")
        return
    
    print("--------------------")
    print("\nGenerating report...")
    print("\n--------------------")

    #Open a file to write to. 
    with open('report_of_experiments.txt', 'w') as myFile:
        myFile.write("\n\n-------------------")
        myFile.write("\nLIST OF EXPERIMENTS")
        myFile.write("\n-------------------")
        for i, thisExperiment in enumerate(listOfExperiments, start=1):
            myFile.write(f"\n\n----- Experiment #: {i} -----")
            myFile.write(f"\nName: {thisExperiment.name}")
            myFile.write(f"\nDate: {thisExperiment.date}")
            myFile.write(f"\nCategory: {thisExperiment.category}")
            myFile.write(f"\nResults: {thisExperiment.results}")
            myFile.write(f"\nThe average is: {statistics.mean(thisExperiment.results)}")
            myFile.write(f"\nThe minimun value is: {min(thisExperiment.results)}")
            myFile.write(f"\nThe maximum value is: {max(thisExperiment.results)}")
        myFile.write("\n\n-------------------------------")
        myFile.write("\nCOMPARISION BETWEEN EXPERIMENTS")
        myFile.write("\n-------------------------------")

        listOfMeans = []
        listOfMins = []
        listOfMaxs = []
        for thisExperiment in listOfExperiments:
            listOfMeans.append(statistics.mean(thisExperiment.results))
            listOfMins.append(min(thisExperiment.results))
            listOfMaxs.append(max(thisExperiment.results))
        

        myFile.write("\n\n--------------------")
        myFile.write("\nComparision of mean:")
        myFile.write("\n--------------------")
        myFile.write(f"\nHighest average: Experiment #{listOfMeans.index(max(listOfMeans))+1} with a value of {max(listOfMeans)}")
        myFile.write(f"\nLowest average: Experiment #{listOfMeans.index(min(listOfMeans))+1} with the value of {min(listOfMeans)}")
        myFile.write("\n----------------------------")
        myFile.write("\nComparision of minium value:")
        myFile.write("\n----------------------------")
        myFile.write(f"\nHighest Min Value: Experiment #{listOfMins.index(max(listOfMins))+1} with a value of {max(listOfMins)}")
        myFile.write(f"\nLowest Min Value: Experiment #{listOfMins.index(min(listOfMins))+1} with the value of {min(listOfMins)}")
        myFile.write("\n-----------------------------")
        myFile.write("\nComparision of maximum value:")
        myFile.write("\n-----------------------------")
        myFile.write(f"\nHighest Max Value: Experiment #{listOfMaxs.index(max(listOfMaxs))+1} with a value of {max(listOfMaxs)}")
        myFile.write(f"\nLowest Max Value: Experiment #{listOfMaxs.index(min(listOfMaxs))+1} with the value of {min(listOfMaxs)}")
    
    print("Report successfully generated.")
    input("\nPress Enter to continue...")

def userMenu():
    print("===Main Menu====")
    
    print("===Management of experiments====")
    print("1. Add an experiment")
    print("2. View experiments")
    print("3. Delete an experiment")
    
    print("===Analysis of data====")
    print("4. Calculate statistics ")
    print("5. Compare experiments ")
    
    print("===Reports====")
    print("6. Generate a report")
    print("====Exit====")
    print("7. Exit")
    

def main():
    
    listOfExperiments=[]

    while True:
        userMenu()
        option = int(input("Select an option: "))

        if option == 1:
            addExperiment(listOfExperiments)
        elif option == 2:
            printExperiments(listOfExperiments)
        elif option == 3:
            removeExperiment(listOfExperiments)
        elif option == 4:
            calculateStatistics(listOfExperiments)
        elif option == 5:
            compareExperiments(listOfExperiments)
        elif option == 6:
            generateReport(listOfExperiments)
        elif option == 7:
            break
        else:
            print("Invalid option")


if __name__ == "__main__":  # es lo mismo al main pero mas avanzado, 
    main()
