from operator import index
import FindableFunctions
from random import randint
from random import randrange
from colorama import Fore, Style, init
init()
player={
    "health":100,
    "shield":0,
    "deck":[],#backend deck
    "hand":[] #frontend deck
}
oppenent={
    "health":100,
    "shield":0,
    "deck":[randint(1,5),randint(1,5),]
}
shop={
    "offers":["attack","block","heal","heavy","chance"],
}
game=True
turn=0
print(Fore.YELLOW+"$$$SHOP TIME$$$")
print(f"{shop["offers"]}, (1-5)"+Style.RESET_ALL)
player_input=int(input(Fore.BLUE +"pick one "))-1
FindableFunctions.convert(player_input)
print(f"YOU JUST GOT {FindableFunctions.convert(player_input + 1).__name__.upper()}")
player["deck"].append(player_input + 1)#backend deck

print(Fore.RED+f"YOUR OPPONENT PICKED {oppenent["deck"]}"+Fore.RESET)

while game:
    turn+=1
    player["hand"]=[]
    opp=oppenent["deck"][randrange(0,len(oppenent["deck"]))]#opponent move randomizer
    if turn%2==1:#PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER PLAYER
        for x in player["deck"]:
            y=FindableFunctions.convert(x) #converts each move to function
            level = FindableFunctions.get_card_level(player["deck"], x) #counts the duplicates and stacks them
            player["hand"].append(f"{y.__name__} (Lv{level})")#hand becomes the function name and function ammount(level)
        print(Fore.BLUE + f"♾♾♾DECK: {list(dict.fromkeys(player['hand']))}♾♾♾")#prints the hand formated as move (lvl)
        print(f"❤❤❤HEALTH:{player["health"]} ❤❤❤")#health duh
        move = int(input("WHAT MOVE?(1,2,3,4): "))#asks for which move the player wants to make
        card_id = index(list(dict.fromkeys(player['deck']))[move-1])#this is the move in the function map
        func = FindableFunctions.convert(card_id)#this is the function out of the function map being preformed
        level = FindableFunctions.get_card_level(player["deck"], card_id)# number of dupes
        if func:
            if 0 <= move - 1 < len(player["deck"]):#ensures var(move) is in the range of the hand
                func(player, oppenent, level) #passes user, target, and level
            else:
                print("MOVE NOT IN DECK")
        else:
            print("INVALID MOVE")
        oppenent["shield"]=0 #opponent shield reset

    else: #NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC NPC
        print(Fore.RED + f"❤❤❤OPPONENT HEALTH: {oppenent["health"]}❤❤❤")#opponent health
        NPC_func = FindableFunctions.convert(opp)
        print(f"OPPONENT PLAYS {NPC_func.__name__.upper()}")
        level = FindableFunctions.get_card_level(oppenent["deck"], opp)
        NPC_func(oppenent, player, level)
        player["shield"] = 0

    if turn%2==0: #SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP SHOP
        current_shop = [shop["offers"][randint(0,4)],shop["offers"][randint(0,4)]]
        print(Fore.YELLOW + "$$$SHOP TIME$$$")
        print(current_shop)
        player_input = int(input("pick one: ")) - 1
        if 0 <= player_input < len(current_shop[player_input]):
            picked_move = current_shop[player_input]
            picked_move=shop["offers"].index(picked_move)
            print(f"YOU JUST BOUGHT {FindableFunctions.convert(picked_move+1).__name__.upper()}")
            player["deck"].append(picked_move+1)
        else:
            print("CARD NOT IN SHOP")
        rand=randint(1,5)
        oppenent["deck"].append(rand)
        print(f"OPPONENT ADDED {FindableFunctions.convert(rand).__name__.upper()} TO THEIR DECK")
    print(f"******turn:{turn}******")

    #END END END END END END END END END END END END END END END END END END END END END END END END
    if player["health"]<= 0:
        game= False
        print(Fore.RESET+f"YOU DIED\nTurn {turn}")
    if oppenent["health"]<= 0:
        game= False
        print(Fore.RESET+f"YOU WON\nTurn {turn}")
