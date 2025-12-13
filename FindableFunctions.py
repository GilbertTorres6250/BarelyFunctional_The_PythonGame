from random import randint

def check_shield(target, damage):
    if target["shield"] > 0:
        absorbed = min(damage, target["shield"])
        target["shield"] -= absorbed
        damage -= absorbed
        print(f"🛡🛡🛡BLOCKED {absorbed} DAMAGE🛡🛡🛡")
    return damage

def attack(user, target, level):
    damage = 10 * level
    print(f"⚔⚔⚔SLASH, {damage} DAMAGE DEALT⚔⚔⚔")
    damage = check_shield(target,damage)
    target["health"] -= damage

def block(user, target, level):
    user["shield"]+= 10 * level
    print(f"🛡🛡🛡BLOCK, +{user['shield']} SHIELD🛡🛡🛡")

def heal(user, target, level):
    user["health"]+= 10 * level
    print(f"❣❣❣HEALED {10* level} HEALTH TO {user['health']} HEALTH❣❣❣")

def heavy(user, target, level):
    damage = randint(5,20) + ((level-1)*10)
    damage = check_shield(target,damage)
    target["health"] -= damage
    print(f"⚒⚒⚒WHACKED, {damage} DAMAGE⚒⚒⚒")

def chance(user, target, level):
    print("!!!FLAIL!!!")
    hit = randint(1,3)
    if hit % 2 != 0:
        damage = 0
        print("✖✖✖MISS✖✖✖")
    else:
        damage = 20 * level
        print(f"✔✔✔LANDED {damage} DAMAGE✔✔✔")
        damage = check_shield(target, damage)
    target["health"] -= damage

function_map = {
    1: attack,
    2: block,
    3: heal,
    4: heavy,
    5: chance
}

def convert(move):
    move = int(move)
    return function_map.get(move)

def get_card_level(deck, card_id):
    return deck.count(card_id)
