from random import randint

def attack(user, target):
    damage = 10
    if target["shield"] > 0:
        absorbed = min(damage, target["shield"])
        target["shield"] -= absorbed
        damage -= absorbed
        print("BLOCKED")
    target["health"] -= damage


def block(user, target):
    user["shield"]+= 10
    print("BLOCK")

def heal(user, target):
    user["health"]+=10
    print(f"HEALED 10 HEALTH")
    print(f"The {user} now has {user['health']} health")

def heavy(user, target):
    damage = randint(5,20)
    if target["shield"] > 0:
        absorbed = min(damage, target["shield"])
        target["shield"] -= absorbed
        damage -= absorbed
    target["health"] -= damage
    print(f"WHACKED, {damage} DAMAGE")


# map the numbers in your deck to real functions
function_map = {
    1: attack,
    2: block,
    3: heal,
    4: heavy
}

def convert(move):
    move = int(move)
    return function_map.get(move, None)
