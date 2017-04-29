import random

print ("Ability Score Generation")

#statNumber = []
statList = []
statModifier = []

x=0
while (x<6):
	statNumber = []
	y=1
	while (y<4):
		statRoll = random.randint(2,6)
		statNumber.append(firstRoll)
		#print (statNumber)
		y=y+1
	statList.append(sum(statNumber))
	modifier = ((statList[x] - 10)/2)
	statModifier.append(modifier)
	#print (sum(statNumber))	
	x=x+1

print (statModifier)
print (statList)

