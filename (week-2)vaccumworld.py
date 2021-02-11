import random


class Environment(object): #This class is defined to represent our Room Environment consisting of 2 rooms "A" and "B" as of such
    def __init__(self):
        # instantiate locations and conditions
        # 0 indicates Clean and 1 indicates Dirty
        self.locationCondition = {'A': '0', 'B': '0'} #Init conditions of the room

        # randomize conditions in locations A and B
        self.locationCondition['A'] = random.randint(0, 1)
        self.locationCondition['B'] = random.randint(0, 1)


class SimpleReflexVacuumAgent(Environment):
    def __init__(self, Environment):
        print (Environment.locationCondition)
        # performance measurement is donne
        perform = 0
        # place vacuum at random location
        vacuumLocation = random.randint(0, 1)
        # if vacuum at A
        if vacuumLocation == 0:
            print ("Vacuum is randomly placed at Location A.")
            # and Location A is Dirty.
            if Environment.locationCondition['A'] == 1:
                print ("Location A has Dirt.")
                # clean the dirt  and mark it clean
                Environment.locationCondition['A'] = 0;
                perform += 1
                print ("The dirt in Location A has been Cleaned.")
                # move to B
                print ("Going on to Location B...")
                perform -= 1
                # if B is Dirty
                if Environment.locationCondition['B'] == 1:
                    print ("Location B has Dirt.")
                    # clean it and mark clean
                    Environment.locationCondition['B'] = 0;
                    perform += 1
                    print ("The dirt in Location B has been Cleaned.")
            else:
                # move to B
                perform -= 1
                print ("Going to Location B...")
                # if B is Dirty
                if Environment.locationCondition['B'] == 1:
                    print ("Location B has Dirt.")
                    # cleann it and mark clean
                    Environment.locationCondition['B'] = 0;
                    perform += 1
                    print ("The dirt in Location B has been Cleaned.")

        elif vacuumLocation == 1:
            print ("Vacuum randomly placed at Location B.")
            # and B is Dirty
            if Environment.locationCondition['B'] == 1:
                print ("Location B has Dirt.")
                # clean it and mark clean
                Environment.locationCondition['B'] = 0;
                perform += 1
                print ("The dirt in Location B has been Cleaned.")
                # move to A
                perform -= 1
                print ("Going to Location A...")
                # if A is Dirty
                if Environment.locationCondition['A'] == 1:
                    print ("Location A has Dirt.")
                    # clean it and mark clean
                    Environment.locationCondition['A'] = 0;
                    perform += 1
                    print ("The dirt in Location A has been Cleaned.")
            else:
                # move to A
                print ("Going to Location A...")
                perform -= 1
                # if A is Dirty
                if Environment.locationCondition['A'] == 1:
                    print ("Location A has Dirt.")
                    # clean it and mark clean
                    Environment.locationCondition['A'] = 0;
                    perform += 1
                    print ("The dirt in Location A has been Cleaned.")
        # done cleaning
        print (Environment.locationCondition)
        print ("Performance Measurement: " + str(perform))

theVacuum = SimpleReflexVacuumAgent(Environment())
