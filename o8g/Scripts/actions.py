import time

Food = ("Food", "289aef4e-91b1-4dad-9a32-d6dacadeea86")
FoodMeat = ("FoodMeat", "230d65c4-aa76-4e2a-9f8f-25a174b7c62e")
Population = ("Population", "ec300ded-d726-4a64-88a2-6a023a78c369")
Size = ("Size", "f8f1bdac-eaa3-46dc-b77e-a4d49969ef61")
Lock = ("Lock", "2e3052e2-dc07-46b1-81a8-17ba0b816a8d")

BoardWidth = 1100
Spacing = 92
HeroY = 70
StagingStart = -530
StagingWidth = 750
StagingY = -224
StagingSpace = 82
QuestStartX = 331
QuestStartY = -246
DoneColour = "#D8D8D8" # Grey
WaitingColour = "#FACC2E" # Orange
ActiveColour = "#82FA58" # Green
EliminatedColour = "#FF0000" # Red
showDebug = False #Can be changed to turn on debug - we don't care about the value on game reconnect so it is safe to use a python global

def debug(str):
	if showDebug:
		whisper(str)
		
def toggleDebug(group, x=0, y=0):
	global showDebug
	showDebug = not showDebug
	if showDebug:
		notify("{} turns on debug".format(me))
	else:
		notify("{} turns off debug".format(me))