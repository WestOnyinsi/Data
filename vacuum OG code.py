
import random
import time

class Environment(object):
    def __init__(self):
        self.location = ["A", "B", "C", "D"]
        self.mode = ["t", "l"]
        self.locationCondition = {"A": "0", "B": "0", "C": "0", "D": "0"}
        self.cleaningMethod = {"A": "t", "B": "t", "C": "t", "D": "t"}
        self.vacuumLoc = random.choice(self.location) # pick the location randomly
        self.locationCondition["A"] = random.randint(0, 1)
        self.locationCondition["B"] = random.randint(0, 1)
        self.locationCondition["C"] = random.randint(0, 1)
        self.locationCondition["D"] = random.randint(0, 1)
        self.cleaningMethod["A"] = random.choice(self.mode)
        self.cleaningMethod["B"] = random.choice(self.mode)
        self.cleaningMethod["C"] = random.choice(self.mode)
        self.cleaningMethod["D"] = random.choice(self.mode)


class agent(Environment): # inherit from the class environment
    def __init__(self, Environment):#inherit the constructor of the class above
        print("RoverLocation", Environment.vacuumLoc)
        print("Location condition", Environment.locationCondition)
        

        count = 0
        while count < 4:
            if Environment.locationCondition[Environment.vacuumLoc] == 1:
                if Environment.cleaningMethod[Environment.vacuumLoc] == "l":
                    Environment.cleaningMethod [Environment.vacuumLoc] = "t"
                else:
                    Environment.cleaningMethod[Environment.vacuumLoc] = "l"
                    Environment.locationCondition[Environment.vacuumLoc] = 0
                    print("Location", Environment.vacuumLoc, " Rocks Sampled")
            else:
                print("Location", Environment.vacuumLoc,  "has no rocks")

            newIndex = Environment.location.index (Environment.vacuumLoc) + 1
            if newIndex == 4:
                newIndex = 0
            Environment.vacuumLoc = Environment.location[newIndex]
            count += 1

        print("Rocks sampled", Environment.locationCondition)
        print(Environment.locationCondition)
        print(Environment.cleaningMethod)

theEnvironment = Environment()
theAgent = agent(theEnvironment)




#creating objects
result= {}
count=0
theEnvironment= Environment()
while count<6:
        print()
        print("........Run ",count+1,"........")
        print()
        theEnvironment.locationCondition["A"] = random.randint(0, 1)
        theEnvironment.locationCondition["B"] = random.randint(0, 1)
        theEnvironment.locationCondition["C"] = random.randint(0, 1)
        theEnvironment.locationCondition["D"] = random.randint(0, 1)
        theCleaner= agent(theEnvironment)
        result.update(theEnvironment.locationCondition)
        count+=1
        time.sleep(0.5)
        
        result=  theEnvironment.locationCondition
        print(result)

        
print()
print("Shift Over")