banana=3000 #initial number of bananas
distance=1000 #distance to be travelled
load=1000 #max load the camel can lift (in terms of bananas)
lose=0 #initial amount of bananas the camel has eaten
start=banana #initial bananas
for i in range(distance):
    while start>0: #loop will run till bananas become zero
        start=start-load #bananas left after load is carried to chekpoint
        if start==1: #case where one banana is left at initial point, why waste 2 bananas to get 1 back, incuring a lose of a banana
            lose=lose-1
        lose=lose+2 #banana for each km front and back
    lose=lose-1 #case when end is reached, no need to go back
    start=banana-lose
print(start)
