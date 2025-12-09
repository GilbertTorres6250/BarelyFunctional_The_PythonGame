import FindableFunctions
from random import randint
from random import randrange
from colorama import Fore, Back, Style, init
init()
player={
    "health":100,
    "deck":[],
}
openent={
    "health":100,
    "deck":[randint(1,2),randint(3,4)]
}

game=True
turn=0
offers=["attack",2,3,4]
print(Fore.YELLOW+"❤❤❤SHOP TIME❤❤❤")
print(f"{offers}"+Style.RESET_ALL)
player_input=int(input("pick one "))-1
player["deck"].append(offers[player_input])

print(Fore.RED+f"your oppenent picks {openent["deck"]}"+Fore.RESET)

while game:
    turn+=1
    opp=openent["deck"][randrange(0,len(openent["deck"]))]
    if turn%2==1:#PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER
        print(Fore.RESET+f"Current Deck:{player["deck"]}")
        print(f"Current health:{player["health"]}")
        move = int(input("what to play "))
        func = FindableFunctions.convert(move)
        if func:
            func(openent)
        else:
            print("invalid move")


    else: #NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC
        print(Fore.RED+f"oppenent health: {openent["health"]}")
        NPC_func=FindableFunctions.convert(opp)
        NPC_func(player)
        print(f"oppenent plays {NPC_func}")


    if turn%8==0: #SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP
        print(Fore.YELLOW+"❤❤❤SHOP TIME❤❤❤")
        shop=[randint(1,4),randint(1,4)]
        print(shop)
        player_input = int(input("pick one ")) - 1
        player["deck"].append(offers[player_input])
    print(f"******turn:{turn}******")


