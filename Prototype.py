import GameFunctions as GF
import GameClasses as GC
from random import randint
from random import randrange
from operator import index
from colorama import Fore


human = GC.Player()
dan = GC.Bee()
dave = GC.Bee()
turn = 0
shop = GC.Shop(5,human).open_shop()
for enemyEntity in GC.Enemy.enemy_id:
	enemyEntity.add_card(randrange(1, 5))
game=True

while game:
	turn += 1
	human.hand=[]
	human.convert_hand()
	if turn%2==1:
		human.display_health()
		human.show_hand()
		enemy_index=0
		for enemyEntity in GC.Enemy.enemy_id:
			enemy_index+=1
			print(enemy_index,enemyEntity.__class__.__name__,"| HEALTH:", enemyEntity.health)
		target = int(input("WHICH ENEMY?(1,2,3,4): "))
		monster=GC.Enemy.enemy_id[target-1]
		move = int(input("WHAT MOVE?(1,2,3,4): "))
		try:
			card_id = index(list(dict.fromkeys(human.deck))[move - 1])  #? this is the move in the function map
		except LookupError:
			card_id = index(list(dict.fromkeys(human.deck))[0])  #? this is the move in the function map
		func = GF.convert(card_id)  #? this is the function out of the function map being preformed
		level = GF.get_card_level(human.deck, card_id)  #? number of dupes
		if 0 <= move - 1 < len(human.deck):  #? ensures var(move) is in the range of the hand
			func(human, monster, level)  #? passes user, target, and level
		else:
			print("MOVE NOT IN DECK")
		for enemyEntity in GC.Enemy.enemy_id:
			enemyEntity.shield=0
			enemyEntity.check_living()
	else:
		for enemyEntity in GC.Enemy.enemy_id:
			enemyEntity.display_health()
			enemyEntity.convert_hand()
			enemyEntity.show_hand()
			enemyEntity.play_card(human)

			enemyEntity.hand = []

	if turn%3==0:
		shop = GC.Shop(5,human).open_shop()
		for enemyEntity in GC.Enemy.enemy_id:
			enemyEntity.add_card(randrange(1, 5))

	print(f"************TURN:{turn}************")
	if human.health <= 0:
		print(Fore.RESET+f"YOU DIED\nTurn {turn}")
		game= False
	if len(GC.Enemy.enemy_id) == 0:
		print(Fore.RESET+f"YOU WON\nTurn {turn}")
		game = False

