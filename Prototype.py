import GameFunctions as GF
import GameClasses as GC
from random import randint
from random import randrange
from operator import index


human = GC.Player()
dan = GC.Bee()
dave = GC.Bee()
turn = 0
shop = GC.Shop(5,human).open_shop()
game=True

while game:
	turn += 1
	human.hand=[]
	human.convert_hand()
	if turn%2==1:
		human.display_health()
		human.show_hand()
		enemy_index=0
		for x in GC.Enemy.enemy_id:
			enemy_index+=1
			print(enemy_index,x.__class__.__name__,"| HEALTH:", x.health)
		target = int(input("WHICH ENEMY?(1,2,3,4): "))
		monster=GC.Enemy.enemy_id[target-1]
		move = int(input("WHAT MOVE?(1,2,3,4): "))
		try:
			card_id = index(list(dict.fromkeys(human.deck))[move - 1])  # ?this is the move in the function map
		except LookupError:
			card_id = index(list(dict.fromkeys(human.deck))[0])  # ?this is the move in the function map
		func = GF.convert(card_id)  # ?this is the function out of the function map being preformed
		level = GF.get_card_level(human.deck, card_id)  # ? number of dupes
		if 0 <= move - 1 < len(human.deck):  # ?ensures var(move) is in the range of the hand
			func(human, monster, level)  # ?passes user, target, and level
		else:
			print("MOVE NOT IN DECK")
		for x in GC.Enemy.enemy_id:
			x.shield=0
	else:
		dan.display_health()
		dave.display_health()

	if turn%3==0:
		shop = GC.Shop(5,human).open_shop()
