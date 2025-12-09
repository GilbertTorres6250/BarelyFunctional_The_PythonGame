def attack(target):
    target["health"] -= 10

def block(user):
    pass

def heal(self):
    pass

def heavy(target):
    target["health"] -= 10


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
