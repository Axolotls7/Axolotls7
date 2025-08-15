# Kessel Sabacc
# As seen in Star Wars: Outlaws
# No shift tokens for now, but I plan to add them later
# also no cheating, which I do not plan to add
import random
newlines = False
def calibrate():
	print("calibrating... type 'yes' if you can no longer see previous text. Otherwise, type anything else.")
	lorem = "Lorem ipsum dolor sit amet. Blah blah blah. The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues."
	i = 0
	while true:
		print(lorem)
		for j in i:
			print("\n")
		if input() == "yes":
			newlines = ("\n" * i)
		else:
			i += 1
class Deck:
	def __init__(self, b):
		self.cards = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,"s","i","i","i"] # s for sylop, i for impostor
		self.blood = b
	def deal(self):
		random.shuffle(self.cards)
		for i in players:
			if self.blood:
				i.blood = self.cards.pop()
			else:
				i.sand = self.cards.pop()
		# note to self: add discard pile
def startGame():
	if newlines:
		calibrate()
	num = max(int(input("How many players?\n\t")), 2)
	for i in range(num):
		players.append(Player(input("Name?\n\t")))
	sandD = Deck(False)
	bloodD = Deck(True)
	# note to self: add actual while loop
players = []
class Player:
	def __init__(self, name):
		players += self
		self.chips = 6
		self.invest = 0
		self.name = name
		self.sand = None
		self.blood = None
	def turn(self):
		print(newlines + self.name = "'s turn:")
		action = input("#0: Stand\n\tSkip turn (if you're happy with your hand)\n#1: Draw\n\tInvest a chip to draw a card\n#")
		match int(action):
			case 0:
				return
			case 1 if self.chips > 0:
				self.chips -= 1
				self.invest += 1 # note to self: add getting the chips back
# this is very unfinished
