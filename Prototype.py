from operator import index
import FindableFunctions
from random import randint
from random import randrange
from colorama import Fore, Back, Style, init
init()
player={
    "health":100,
    "shield":0,
    "deck":[],
}
oppenent={
    "health":100,
    "shield":0,
    "deck":[randint(1,4)]
}

game=True
turn=0
offers=["attack","block","heal","heavy"]
print(Fore.YELLOW+"❤❤❤SHOP TIME❤❤❤")
print(f"{offers}"+Style.RESET_ALL)
player_input=int(input("pick one "))-1
player["deck"].append(player_input + 1)

print(Fore.RED+f"your oppenent picks {oppenent["deck"]}"+Fore.RESET)

while game:
    turn+=1
    opp=oppenent["deck"][randrange(0,len(oppenent["deck"]))]
    if turn%2==1:#PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER
        print(Fore.BLUE+f"Current Deck:{player["deck"]}")
        print(f"Current health:{player["health"]}")
        move = int(input("what to play "))
        func = FindableFunctions.convert(int(index(player["deck"][move-1])))
        if func:
            if 0 <= move - 1 < len(player["deck"]):
                func(player, oppenent)
            else:
                print("Card not in deck")
        else:
            print("invalid move")
        oppenent["shield"]=0


    else: #NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC
        print(Fore.RED+f"oppenent health: {oppenent["health"]}")
        NPC_func=FindableFunctions.convert(opp)
        NPC_func(oppenent,player)
        print(f"oppenent plays {NPC_func.__name__}")
        player["shield"]=0


    if turn%8==0: #SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP
        print(Fore.YELLOW+"❤❤❤SHOP TIME❤❤❤")
        shop= offers[randint(0,3)]

        print(shop)
        player_input = int(input("pick one ")) - 1
        player["deck"].append(player_input + 1)
    print(f"******turn:{turn}******")
