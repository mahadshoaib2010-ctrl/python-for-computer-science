import random
dice_roll = random. randint(1, 6)

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\003[33m'
RESET = '\033[0m'

player_hp = 50
bad_guy_hp = 30
player_attack = 0
bad_guy_attack = 0
flag = False

print("You run into a bad guy\n")

while flag == False:
    user_input = int(input("1. fight | 2. sheild"))
    if user_input == 1:
        player_attack = random. randint(1, 10)
        bad_guy_attack = random. randint(1, 7)
        print(f"{GREEN}player attacks for {player_attack} {RESET} | {RED}bad guy attacks for {bad_guy_attack} {RESET}")
        player_hp-=bad_guy_attack
        bad_guy_hp-=player_attack
    print(f"{GREEN} player has {player_hp}HP left. {RESET} | {RED}bad guy has {bad_guy_hp}HP left {RESET}")
    if player_hp <= 0 or bad_guy_hp <= 0:
        flag = True
        print("game over!")