import datetime
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
    name = input("Experiment's name: ")
    date = input("Date (dd/mm/yyyy): ") # Add date format verification
    category = input("Category: ") # Change it to restrict user's input
    results = list(input("List of results: ")) # Change to a for to avoid mistakes from user

    thisExperiment = Experiment(name,date,category,results)
    listOfExperiments.append(thisExperiment)
    print("\nExperiment successfully added.")
    input("\nPress Enter to continue...")

# This function will take the list of experiments called "listOfExperiments" as input
def printExperiments(listOfExperiments):
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

def removeExperiment(listOfExperiments):
    print("-----------------------------------")
    print("You will be removing an experiment.")
    print("-----------------------------------")
    # Add verfications
    experimentToRemove = int(input("Input the number of the experiment you want to remove, \nif you are not sure about the number, press 'v' to view the list of names: "))
    del listOfExperiments[experimentToRemove-1]
    print(f"\nExperiment #{experimentToRemove} removed successfully.")
    input("\nPress Enter to continue...")

# This function will take the list of experiments called "listOfExperiments" as input
def selectExperiment(listOfExperiments):
    print("--------------------")
    print("List of experiments:")
    print("--------------------")
    for i, thisExperiment in enumerate(listOfExperiments, start=1):
        print("----------------------------------------------------")   
        print(f"{i}. {thisExperiment.name}")
    print("--------------------")

def calculateStatistics(listOfExperiments):
    print("--------------------------------------------")
    print("Calculation of statistics for an experiment.")
    print("--------------------------------------------")    
    expNumber = int(input("Select the number of the experiment. \nIf you are not sure about the number of the experiment, \npress 'v' to view the list: ")) # Add verification
    print("--------------------------------------------")
    print(f"The results for this experiment are: {listOfExperiments[expNumber-1].results}")
    print(f"The average is: {statistics.mean(listOfExperiments[expNumber-1].results)}")
    print(f"The minimun value is: {min(listOfExperiments[expNumber-1].results)}")
    print(f"The maximum value is: {max(listOfExperiments[expNumber-1].results)}")
    input("\nPress Enter to continue...")

def compareExperiments(listOfExperiments):
    print("---------------------------------------")
    print("Comparision of two or more experiments.")
    print("---------------------------------------")
    listToCompare = []
    while True:
        # Add verification (the number should not exceed the number of experiments)
        # the input must be integer (try except)
        experiment = int(input("Type the number of the experiment to compare, \nif you want to stop selecting experiments, type 0: "))
        if experiment != 0:
            listToCompare.append(experiment)
        else:
            break
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
