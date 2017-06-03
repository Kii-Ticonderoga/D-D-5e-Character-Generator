import random

print ("Ability Score Generation\n")

#statNumber = []
statList = []
statModifier = []

x=0
while (x<6):
	statNumber = []
	y=0
	while (y<3):
		statRoll = random.randint(2,6)
		statNumber.append(statRoll)
		#print (statNumber)
		y=y+1
	statList.append(sum(statNumber))
	modifier = ((statList[x] - 10)//2)
	statModifier.append((modifier))
	#print (sum(statNumber))	
	x=x+1


print ("Ability Scores:")
print (statList)

print ("\nAbility Modifiers:")
print (statModifier)

#print ("Ability Scores: " + statList + "\n")

#print ("Ability Modifiers: " + ("+" if statModifier >= 0) + statModifier + "\n")
