import random

print ("Ability Score Generation")

statNumber = []
statList = []

x=1
while (x<7):
	y=1
	while (y<4):
		firstRoll = random.randint(2,6)
		statNumber.append(firstRoll)
		#print (statNumber)
		y=y+1
	statList.append(sum(statNumber))
	#print (sum(statNumber))
	statNumber = []
	x=x+1


print (statList)

