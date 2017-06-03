import random

print ("Ability Score Generation\n")

statList = []
statModifier = []
statName = ["STR","DEX","CON","INT","WIS","CHA"]

for x in range(0,5):
	statNumber = []
	for y in range(0,2):
		statRoll = random.randint(2,6)
		statNumber.append(statRoll)
	statList.append(sum(statNumber))
	modifier = ((statList[x] - 10)//2)
	statModifier.append((modifier))

print ("Ability Scores:\n")

for x in range(0,5):
        print(str(statName[x]) + " = " + str(statList[x]) + " -> " + ("+" if statModifier[x] > 0 else "") + str(statModifier[x]) + "\n")
