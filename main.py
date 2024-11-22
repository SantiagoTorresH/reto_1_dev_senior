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
            
    category = input('Ingrese la categoria, puede ser "Quimica", "fisica" o "Biologia": ').capitalize()            
            
    # Asegurarse de que la categoría esté entre las opciones permitidas
    while category not in ["Quimica", "Fisica", "Biologia"]:
        print("Categoría no válida. Por favor ingrese una de las siguientes: 'Quimica', 'Fisica' o 'Biologia'.")
        category = input('Ingrese la categoría, puede ser "Quimica", "Fisica" o "Biologia": ').capitalize()            
    
    while True:
        try:
            numberOfResults = int(input("\nYou will be entering the results now. \nPlease enter the number of results (max 10), ) (MIN 3): "))
            if 3 <= numberOfResults <=10:
                for i in range(numberOfResults):
                    while True:
                        try:
                            results.append(float(input(f"Result #{i+1}: ")))
                            break
                        except:
                            print("Error, the value is not a number, try again.")
                break
            else:
                print("\nInvalid, input should be a positive integer. DEBE SER MINIMO 3 RESULTADOS A 10 RSULTADOS")
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
        try:
            experiment = input("\nType the number of the experiment to compare, \nif you need to view the list of experiments, type 0, \nif you want to stop selecting experiments, type 'stop': ")
            # First we need to validate if the number is lower that the number of registered experiments. 
            try:
                if 1 <= int(experiment) <= len(listOfExperiments):
                    # Add this experiment to the list of experiments to compare.
                    listToCompare.append(experiment)
                    continue
                elif int(experiment) == 0:
                    displayExperimentsName(listOfExperiments)
                    continue
            except:
                # Now, we will verified if the user selected at lest 2 experiments, if they didn't,
                # they will be asked for more input
                if len(set(listToCompare))<=1:
                    if experiment.lower() == "stop":
                        print("\nYou can't stop. Please enter another experiment. \nthere is only one experiment in the list.")
                        continue
                if experiment.lower() == "stop":
                    break            
            
        except:
            print("\nInvalid input, it must be an integer or 0.")

    listOfMeans = []
    listOfMins = []
    listOfMaxs = []
    for experiment in listToCompare:
        listOfMeans.append(listOfExperiments[experiment].results)
        listOfMins.append(listOfExperiments[experiment].results)
        listOfMaxs.append(listOfExperiments[experiment].results)

    print("--------------------")
    print("Comparision of mean:")
    print("--------------------")
    print(f"Highest average: Experiment #{listToCompare.index(max(listOfMeans)+1)} with a value of {max(listOfMeans)}")
    print(f"Lowest average: Experiment #{listToCompare.index(min(listOfMeans)+1)} with the value of {min(listOfMeans)}")
    print("----------------------------")
    print("Comparision of minium value:")
    print("----------------------------")
    print(f"Highest Min Value: Experiment #{listToCompare.index(max(listOfMins)+1)} with a value of {max(listOfMins)}")
    print(f"Lowest Min Value: Experiment #{listToCompare.index(min(listOfMins)+1)} with the value of {min(listOfMins)}")
    print("-----------------------------")
    print("Comparision of maximum value:")
    print("-----------------------------")
    print(f"Highest Max Value: Experiment #{listToCompare.index(max(listOfMaxs)+1)} with a value of {max(listOfMaxs)}")
    print(f"Lowest Max Value: Experiment #{listToCompare.index(min(listOfMaxs)+1)} with the value of {min(listOfMaxs)}")
    input("\nPress Enter to continue...")

def generateReport(listOfExperiments):
    # This function will display a message if there are no experiments.
    if not listOfExperiments:
        print("No experiments registered yet.")
        return
    
    print("--------------------")
    print("Generating report...")
    print("--------------------")

    #Open a file to write to. 
    with open('report_of_experiments.txt', 'w') as myFile:
        myFile.write("-------------------")
        myFile.write("LIST OF EXPERIMENTS")
        myFile.write("-------------------")
        for i, thisExperiment in enumerate(listOfExperiments, start=1):
            myFile.write(f"\n----- Experiment #: {i} -----")
            myFile.write(f"Name: {thisExperiment.name}")
            myFile.write(f"Date: {thisExperiment.date}")
            myFile.write(f"Category: {thisExperiment.category}")
            myFile.write(f"Results: {thisExperiment.results}")
            myFile.write(f"The average is: {statistics.mean(thisExperiment.results)}")
            myFile.write(f"The minimun value is: {min(thisExperiment.results)}")
            myFile.write(f"The maximum value is: {max(thisExperiment.results)}")
        myFile.write("\n-------------------------------")
        myFile.write("COMPARISION BETWEEN EXPERIMENTS")
        myFile.write("-------------------------------")

        listOfMeans = []
        listOfMins = []
        listOfMaxs = []
        for thisExperiment in listOfExperiments:
            listOfMeans.append(thisExperiment.results)
            listOfMins.append(thisExperiment.results)
            listOfMaxs.append(thisExperiment.results)

        myFile.write("\n--------------------")
        myFile.write("Comparision of mean:")
        myFile.write("--------------------")
        myFile.write(f"Highest average: Experiment #{listOfExperiments.index(max(listOfMeans))+1} with a value of {max(listOfMeans)}")
        myFile.write(f"Lowest average: Experiment #{listOfExperiments.index(min(listOfMeans))+1} with the value of {min(listOfMeans)}")
        myFile.write("----------------------------")
        myFile.write("Comparision of minium value:")
        myFile.write("----------------------------")
        myFile.write(f"Highest Min Value: Experiment #{listOfExperiments.index(max(listOfMins))+1} with a value of {max(listOfMins)}")
        myFile.write(f"Lowest Min Value: Experiment #{listOfExperiments.index(min(listOfMins))+1} with the value of {min(listOfMins)}")
        myFile.write("-----------------------------")
        myFile.write("Comparision of maximum value:")
        myFile.write("-----------------------------")
        myFile.write(f"Highest Max Value: Experiment #{listOfExperiments.index(max(listOfMaxs))+1} with a value of {max(listOfMaxs)}")
        myFile.write(f"Lowest Max Value: Experiment #{listOfExperiments.index(min(listOfMaxs))+1} with the value of {min(listOfMaxs)}")
    
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
            break
        else:
            print("Invalid option")


if __name__ == "__main__":  # es lo mismo al main pero mas avanzado, 
    main()
