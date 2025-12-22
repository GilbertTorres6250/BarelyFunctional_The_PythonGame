import GameFunctions as GF
from random import randint
from random import randrange
from colorama import Fore, Style, init

class Character:
	id = []
	def __init__(self, group, health):
		self.health = health
		self.max_health = health
		self.group = group
		self.shield = 0
		self.deck = []
		self.hand = []
		Character.id.append(self)
	def add_card(self, card):
		self.deck.append(card)
	def show_hand(self):
		print(f"♾♾♾DECK: {list(dict.fromkeys(self.hand))}♾♾♾")
	def convert_hand(self):
		for card in self.deck:
			converted_card= GF.convert(card)
			level = GF.get_card_level(self.deck, card) #?counts the duplicates and stacks them
			self.hand.append(f"{converted_card.__name__} (Lvl {level})")
	def display_health(self):
		full = "█"
		empty = "░"
		current_health = int(self.health)
		missing_health = int(self.max_health - current_health)
		if self.group == "player_group":
			color = Fore.BLUE
		else:
			color = Fore.RED
		name = self.__class__.__name__
		print(color+f"[{name}:{full * current_health}{empty * missing_health}]")

class Player(Character):
	def __init__(self):
		super().__init__("player_group", 10)

class Enemy(Character):
	enemy_id = []

	def __init__(self, health=100):
		super().__init__("enemy_group", health)
		Enemy.enemy_id.append(self)

class Bee(Enemy):
	def __init__(self):
		super().__init__(health=8)
class Zombie(Enemy):
	def __init__(self):
		super().__init__(health=10)
class Brute(Enemy):
	def __init__(self):
		super().__init__(health=12)

monster_map = {
    1: Bee,
    2: Zombie,
    3: Brute,
}

class Shop:
	offers = ["attack", "block", "heal", "heavy", "chance"]
	current_shop = []
	def __init__(self,size,user):
		self.size=size
		self.user=user

	def open_shop(self):
		Shop.current_shop.clear()
		for _ in range(self.size):
			Shop.current_shop.append(Shop.offers[randrange(0, 5)])
		print(Fore.YELLOW + "$$$SHOP TIME$$$")
		print(Shop.current_shop)#Prints shop
		player_choice = int(input("PICK (1234): "))-1
		if 0 <= player_choice < len(Shop.current_shop):
			picked_move = Shop.current_shop[player_choice]
			picked_move= Shop.offers.index(picked_move)
			print(f"YOU JUST BOUGHT {GF.convert(picked_move+1).__name__.upper()}"+ Fore.RESET)
			self.user.add_card(picked_move+1)
		else:
			print("WE DONT HAVE THAT IN STOCK"+ Fore.RESET)
		self.user.convert_hand()
