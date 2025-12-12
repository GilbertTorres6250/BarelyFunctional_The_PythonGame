from operator import index
import FindableFunctions
from random import randint
from random import randrange
from colorama import Fore, Style, init
init()
player={
    "health":100,
    "shield":0,
    "deck":[],
}
oppenent={
    "health":100,
    "shield":0,
    "deck":[randint(1,4),randint(1,4),]
}
shop={
    "offers":["attack","block","heal","heavy","chance"],
}
game=True
turn=0
print(Fore.YELLOW+"❤❤❤SHOP TIME❤❤❤")
print(f"{shop["offers"]}"+Style.RESET_ALL)
player_input=int(input("pick one "))-1
FindableFunctions.convert(player_input)
player["deck"].append(player_input + 1)

print(Fore.RED+f"your oppenent picks {oppenent["deck"]}"+Fore.RESET)

while game:
    turn+=1
    opp=oppenent["deck"][randrange(0,len(oppenent["deck"]))]
    if turn%2==1:#PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER
        hand = []
        #print(Fore.BLUE+f"Current Deck:{player["deck"]}")
        for x in player["deck"]:
            y=FindableFunctions.convert(x)
            hand.append(y.__name__)
        print(Fore.BLUE+f"Current Deck:{hand}")
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
        print(f"oppenent plays {NPC_func.__name__}")
        NPC_func(oppenent,player)
        player["shield"]=0


    if turn%10==0: #SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP
        current_shop = [shop["offers"][randint(0,3)], shop["offers"][randint(0,3)]]
        print(Fore.YELLOW + "❤❤❤SHOP TIME❤❤❤")
        print(current_shop)
        player_input = int(input("pick one: ")) - 1
        picked_move = current_shop[player_input]
        picked_move=shop["offers"].index(picked_move)
        player["deck"].append(picked_move+1)
    print(f"******turn:{turn}******")

    #END END END END END END END END END END END END END END END END END END END END END END END END
    if player["health"]<= 0:
        game= False
        print(Fore.RESET+f"YOU DIED\nTurn {turn}")
    if oppenent["health"]<= 0:
        game= False
        print(Fore.RESET+f"YOU WON\nTurn {turn}")
