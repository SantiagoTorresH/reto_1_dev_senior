from datetime import datetime
import statistics

# Each experiment will be an object defined by the following attributes:
#       name, date, category, results

# This class will be used to create the experiments and their attributes
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
    name = input(">>> Experiment's name: ")

    # Date object: it needs verification with strptime
    while True:
        try:
            date_input = input(">>> Date (dd/mm/yyyy): ")
            date = datetime.strptime(date_input, "%d/%m/%Y")
            # This line will convert the datetime object to a date object
            date = datetime.date(date)
            break
        except ValueError:
            print("\n*** Attention ***")
            print("Invalid format, please try again.")
            print("\n")
    
    # String: It needs verification, to confirm if it is within the predifined categories
    category = input(">>> Specify the experiment's category. \nIt can be: Chemistry, Physics or Biology: ").capitalize()
    
    while category.capitalize() not in ["Chemistry", "Physics", "Biology"]:
        print("\n*** Attention ***")
        print("Invalid category.")
        print("\n")
        category = input(">>> Specify the experiment's category. \nIt can be: Chemistry, Physics or Biology: ").capitalize()
    
    # Float: verification required to make sure the input is a number
    results = []
    while True:
        try:
            numberOfResults = int(input(">>> You will be entering the results now. \nPlease enter the number of results (min 3, max 10): "))
            if 3 <= numberOfResults <=10:
                for i in range(numberOfResults):
                    while True:
                        try:
                            results.append(float(input(f"Result #{i+1}: ")))
                            break
                        except:
                            print("\n*** Attention ***")
                            print("Error, the value is not a number, try again.")
                            print("\n")
                break
            else:
                print("\n*** Attention ***")
                print("Invalid, input should be a positive integer between 3 and 10 (inclusive).")
                print("\n")
                continue
        except:
            print("\n*** Attention ***")
            print("Invalid, input should be a positive integer.")
            print("\n")
    
    # Object, the experiment is instanced. 
    thisExperiment = Experiment(name,date,category,results)
    listOfExperiments.append(thisExperiment)
    print("\nExperiment successfully added.")
    input("\nPress Enter to continue...")

# This function will take the list of experiments called "listOfExperiments" as input
def printExperiments(listOfExperiments):
    # This function will display a message if there are no experiments to display.
    if not listOfExperiments:
        print("*** No experiments to display. ***")
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

# This function will remove an experiment using its number ID
def removeExperiment(listOfExperiments):
    # This function will display a message if there are no experiments to remove.
    if not listOfExperiments:
        print("*** No experiments registered yet. ***")
        input("\nPress 'Enter' to continue...")
        return
    
    print("-----------------------------------")
    print("You will be removing an experiment.")
    print("-----------------------------------")
    # Make sure the input is an integer
    while True:
        try:
            experimentToRemove = int(input(">>> Input the number of the experiment you want to remove, \nif you are not sure about the number, press '0' to view the list of names: "))
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
                print("\n*** Attention ***")
                print("Not a valid input. Please try again.")
                print("\n")
                continue
        except:
            print("\n*** Attention ***")
            print("Error, the input is not an integer.")
            print("\n")

# This function will calculate the statistics for a single experiment
def calculateStatistics(listOfExperiments):
    # This function will display a message if there are no experiments to remove.
    if not listOfExperiments:
        print("*** No experiments registered yet. ***")
        input("\nPress 'Enter' to continue...")
        return

    print("--------------------------------------------")
    print("Calculation of statistics for an experiment.")
    print("--------------------------------------------")    
    
    while True:
        try:
            expNumber = int(input(">>> Select the number of the experiment. \nIf you are not sure about the number of the experiment, \npress 0 to view the list: ")) 
            # The number must be an integer between 1 and the number of experiments.
            if 1 <= expNumber <= len(listOfExperiments):
                print("--------------------------------------------")
                print(f"The results for this experiment are: {listOfExperiments[expNumber-1].results}")
                print(f"The average is: {statistics.mean(listOfExperiments[expNumber-1].results):.2f}")
                print(f"The minimum value is: {min(listOfExperiments[expNumber-1].results)}")
                print(f"The maximum value is: {max(listOfExperiments[expNumber-1].results)}")
                input("\nPress Enter to continue...")
                break
            elif expNumber == 0:
                displayExperimentsName(listOfExperiments)
                continue
            else:
                print("\n*** Attention ***")
                print("Not a valid input. Please try again.")
                print("\n")
                continue
        except:
            print("\n*** Attention ***")
            print("Error, the input is not an integer.")
            print("\n")

# This function will calculate the statistics for 2 or more experiments and compare them
def compareExperiments(listOfExperiments):
    # This function will display a message if there are no experiments or if there is only one experiment.
    if not listOfExperiments:
        print("*** No experiments registered yet.***")
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
        experiment = input(">>> Type the number of the experiment to compare, \nif you need to view the list of experiments, type 0, \nif you want to stop selecting experiments, type 'stop': ")
        # First we need to validate if the number is lower that the number of registered experiments. 
        try:
            if 1 <= int(experiment) <= len(listOfExperiments):
                # Add this experiment to the list of experiments to compare.
                listToCompare.append(int(experiment))
                print(f"\nExperiments to compare: {set(listToCompare)}")
                print("\n")
                continue
            elif int(experiment) == 0:
                displayExperimentsName(listOfExperiments)
                continue
            else:
                print("\n*** Attention ***")
                print("Invalid input, the experiment doesn't exist.")
                print("\n")
        except:
            # We will land here if the text can't be converted to a number
            # There are two options:
            # 1. The text is "stop" (The code should verify if there is enough data)
            # 2. The text is different than "stop" (The code should return a warning)

            # Condition 1. 
            if experiment.lower() == "stop":
                # Verify if there is enough data.
                if len(set(listToCompare))==1:
                    print("\n*** Attention ***")
                    print("You can't stop. Please enter another experiment. \nThere is only one experiment in the list to compare.")
                    print("\n")
                    continue
                elif len(set(listToCompare)) == 0:
                    print("\n*** Attention ***")
                    print("You can't stop. Please enter an experiment. \nThere are no experiments in the list to compare.")
                    print("\n")
                    continue
                else:
                    break
            # Condition 2. 
            else:
                print("\n*** Attention ***")
                print("Invalid input, it must be a positive integer or 0.")
                print("\n")
                continue
    
    # We need to make sure the elements are unique by converting the list to a set.
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
    print(f"Highest average: Experiment #{listOfMeans.index(max(listOfMeans))+1} with a value of {max(listOfMeans):.2f}")
    print(f"Lowest average: Experiment #{listOfMeans.index(min(listOfMeans))+1} with the value of {min(listOfMeans):.2f}")
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

# This function will generate a report with the experiments registered so far.
def generateReport(listOfExperiments):
    # This function will display a message if there are no experiments.
    if not listOfExperiments:
        print("*** No experiments registered yet. ***")
        input("\nPress 'Enter' to continue...")
        return
    
    print("--------------------")
    print("Generating report...")
    print("--------------------")

    #Open a file to write to. 
    with open('report_of_experiments.txt', 'w') as myFile:
        myFile.write("-------------------")
        myFile.write("\nLIST OF EXPERIMENTS")
        myFile.write("\n-------------------")
        for i, thisExperiment in enumerate(listOfExperiments, start=1):
            myFile.write(f"\n\n----- Experiment #: {i} -----")
            myFile.write(f"\nName: {thisExperiment.name}")
            myFile.write(f"\nDate: {thisExperiment.date}")
            myFile.write(f"\nCategory: {thisExperiment.category}")
            myFile.write(f"\nResults: {thisExperiment.results}")
            myFile.write(f"\nThe average is: {statistics.mean(thisExperiment.results):.2f}")
            myFile.write(f"\nThe minimum value is: {min(thisExperiment.results)}")
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
        myFile.write(f"\nHighest average: Experiment #{listOfMeans.index(max(listOfMeans))+1} with a value of {max(listOfMeans):.2f}")
        myFile.write(f"\nLowest average: Experiment #{listOfMeans.index(min(listOfMeans))+1} with the value of {min(listOfMeans):.2f}")
        myFile.write("\n----------------------------")
        myFile.write("\nComparision of minimum value:")
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

# This function will display the user menu
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
    
# This is the main function
def main():
    
    listOfExperiments=[]

    while True:
        userMenu()
        option = input("Select an option: ")

        if option == "1":
            addExperiment(listOfExperiments)
        elif option == "2":
            printExperiments(listOfExperiments)
        elif option == "3":
            removeExperiment(listOfExperiments)
        elif option == "4":
            calculateStatistics(listOfExperiments)
        elif option == "5":
            compareExperiments(listOfExperiments)
        elif option == "6":
            generateReport(listOfExperiments)
        elif option == "7":
            print("\nThanks for using this service.")
            break
        else:
            print("\n*** Attention ***")
            print("Invalid option")
            print("\n")


if __name__ == "__main__":  
    main()
