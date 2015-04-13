import time

Food = ("Food", "289aef4e-91b1-4dad-9a32-d6dacadeea86")
FoodMeat = ("FoodMeat", "230d65c4-aa76-4e2a-9f8f-25a174b7c62e")
Population = ("Population", "f2b0b9ef-b1ec-4c96-8675-2448c348d134")
Size = ("Size", "f8f1bdac-eaa3-46dc-b77e-a4d49969ef61")
Lock = ("Lock", "2e3052e2-dc07-46b1-81a8-17ba0b816a8d")

Spacing = 92
PlayerY = 70
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

#Triggered event OnGameStart
def startOfGame(): 
	mute()

#Triggered event OnLoadDeck
def deckLoaded(player, groups): 
	mute()

#---------------------------------------------------------------------------
# Randoms
#---------------------------------------------------------------------------

def flipCoin(group, x = 0, y = 0):
    mute()
    n = rnd(1, 2)
    if n == 1:
        notify("{} flips heads.".format(me))
    else:
        notify("{} flips tails.".format(me))

def randomNumber(group, x=0, y=0):
	mute()
	max = askInteger("Random number range (1 to ....)", 6)
	if max == None: return
	notify("{} randomly selects {} (1 to {})".format(me, rnd(1,max), max))


#---------------------------------------------------------------------------
# Table card actions
#---------------------------------------------------------------------------

def defaultAction(card, x = 0, y = 0):
	mute()
	flipcard(card, x, y)

def flipcard(card, x = 0, y = 0):
	mute()
	if card.controller != me:
		notfiy("{} gets {} to flip card".format(me, card.controller()))
		remoteCall(card.controller, "flipcard", card)
		return

	if card.isFaceUp:
		card.isFaceUp = False
		notify("{} turns '{}' face down.".format(me, card))        
	else:
		card.isFaceUp = True
		notify("{} turns '{}' face up.".format(me, card))

def addFood(card, x = 0, y = 0):
	addToken(card, Food)

def subFood(card, x = 0, y = 0):
	subToken(card, Food)

def addPopulation(card, x = 0, y = 0):
	addToken(card, Population)

def subPopulation(card, x = 0, y = 0):
	subToken(card, Population)

def addSize(card, x = 0, y = 0):
	addToken(card, Size)

def subSize(card, x = 0, y = 0):
	subToken(card, Size)


def discard(card, x=0, y=0):
	mute()
	if card.controller != me:
		whisper("{} does not control '{}' - discard cancelled".format(me, card))
		return

	card.moveTo(traitDiscard())


def traitDeck():
	return shared.piles['Trait Deck']

def traitDiscard():
	return shared.piles['Trait Discard Pile']




#------------------------------------------------------------------------------
# Pile Actions
#------------------------------------------------------------------------------

def draw(group, x = 0, y = 0):
	mute()
	if len(group) == 0: return
	card = group[0]
	card.moveTo(me.hand)
	notify("{} draws '{}'".format(me, card))

def shuffle(group):
	mute()
	if len(group) > 0:
		update()
		group.shuffle()
		notify("{} shuffles {}".format(me, group.name))

def drawMany(group, count = None):
	mute()
	if len(group) == 0: return
	if count is None:
		count = askInteger("Draw how many cards?", 6)
	if count is None or count <= 0:
		whisper("drawMany: invalid card count")
		return
	for c in group.top(count):
		c.moveTo(me.hand)
		notify("{} draws '{}'".format(me, c))

def moveAllToDraw(group):
	mute()
	if confirm("Shuffle all cards from {} to Trait Deck?".format(group.name)):
		for c in group:
			c.moveTo(traitDeck())
		notify("{} moves all cards from {} to the Trait Deck".format(me, group.name))
		shuffle(traitDeck())

def playCard(card, x=0, y=0):
	card.moveToTable(x, y)
	card.select()