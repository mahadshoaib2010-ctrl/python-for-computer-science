import os, time, pygame

import random 

ascii_art = r""" .-') _    ('-. .-.   ('-.         _ .-') _                    .-') _               ('-.                    .-') _                                      .-') _          _   .-')       ('-.   
(  OO) )  ( OO )  / _(  OO)       ( (  OO) )                  ( OO ) )            _(  OO)                  ( OO ) )                                    (  OO) )        ( '.( OO )_   _(  OO)  
/     '._ ,--. ,--.(,------.       \     .'_  ,--. ,--.   ,--./ ,--,'  ,----.    (,------. .-'),-----. ,--./ ,--,'        .-'),-----.    ,------.      /     '._ ,-.-') ,--.   ,--.)(,------. 
|'--...__)|  | |  | |  .---'       ,`'--..._) |  | |  |   |   \ |  |\ '  .-./-')  |  .---'( OO'  .-.  '|   \ |  |\       ( OO'  .-.  '('-| _.---'      |'--...__)|  |OO)|   `.'   |  |  .---' 
'--.  .--'|   .|  | |  |           |  |  \  ' |  | | .-') |    \|  | )|  |_( O- ) |  |    /   |  | |  ||    \|  | )      /   |  | |  |(OO|(_\          '--.  .--'|  |  \|         |  |  |     
   |  |   |       |(|  '--.        |  |   ' | |  |_|( OO )|  .     |/ |  | .--, \(|  '--. \_) |  |\|  ||  .     |/       \_) |  |\|  |/  |  '--.          |  |   |  |(_/|  |'.'|  | (|  '--.  
   |  |   |  .-.  | |  .--'        |  |   / : |  | | `-' /|  |\    | (|  | '. (_/ |  .--'   \ |  | |  ||  |\    |          \ |  | |  |\_)|  .--'          |  |  ,|  |_.'|  |   |  |  |  .--'  
   |  |   |  | |  | |  `---.       |  '--'  /('  '-'(_.-' |  | \   |  |  '--'  |  |  `---.   `'  '-'  '|  | \   |           `'  '-'  '  \|  |_)           |  | (_|  |   |  |   |  |  |  `---. 
   `--'   `--' `--' `------'       `-------'   `-----'    `--'  `--'   `------'   `------'     `-----' `--'  `--'             `-----'    `--'             `--'   `--'   `--'   `--'  `------' """

print(ascii_art)

pygame.mixer.init()
pygame.mixer.music.load("Temple of Time - The Legend of Zelda Ocarina of Time OST.mp3")
pygame.mixer.music.play()



name = input("Enter name: ")

print(f"welcome {name} to THE DUNGEON OF TIME in this realm time is altered your job is to fix time and bring peace go through these doors and complete the 4 mini dungeons. Good Luck")


game_life = True

while game_life:

    choice_1 = input("\nWhere would you like to go (mini dungeon 1/time shop/quit): ").strip().lower()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Skyrim - Music & Ambience - Dungeons - Everness (192k).mp3")
    pygame.mixer.music.play()
   

    
    if choice_1 == "mini dungeon 1":
        start_1 = input("write 'enter' to enter (enter): ")
        print("Welcome to Mini Dungeon 1 here you will have to decode a code ")
        secret_code = "with time comes a dire price face a challenge to restore time slightly to its chosen path"
        scrambled_code = "twhi itme semco a erid icepr ecaf a llngechae ot sortere imet tlyhgils ot s'ti nesoch htap"
        print(f"here is your scrambled code: {scrambled_code}")

        is_correct = False
        while not is_correct:
            guess = input("Enter your guess: ")
            if guess.strip().lower() == secret_code.lower():
                print("\nSuccess! you decoded the message but your challenge awaits go through this door and good luck")
                print(f"-> {secret_code}")
                is_correct = True
            else:
                print("Try again!\n")

        mini_boss_room = input("type enter to enter (enter): ")

    if mini_boss_room == "enter":
        pygame.mixer.music.stop
        pygame.mixer.music.load("Gerudo Valley - The Legend of Zelda Ocarina Of Time - Halo2playa (192k).mp3")
        pygame.mixer.music.play()
        print("HUH FEEBLE HUMAN YOU DARE CHALLENGE ME TRY YOUR BEST!!")
       
        print("oh no it's the feared time giant you must defeat him to continue on")

        player_hp = 100
        player_heals = 0
        boss_hp = 150
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\003[33m'
        BLUE = '|033[34m'
        RESET = '\033[0m'
        game_over = False

    while player_hp > 0 and boss_hp > 0 and not game_over:
            print(f"{BLUE}Your HP: {player_hp} | Heals left: {player_heals} {RESET}")
            print(f"{RED}Boss HP: {boss_hp} {RESET}")
            print("\nChoose your action:")
            print("1. Attack")
            print("2. Shield")
            print("3. Heal")

    choice_fight =  input("Enter choice (1, 2, or 3: )")
    print()

    player_damage = 0
    shield_active = False

    if choice_fight == "1":
        player_damage = random.randint(15, 25)
        boss_hp = boss_hp - player_damage
        print(f"{BLUE}you struck the Time giant for {player_damage} {RESET}")
    elif choice_fight == "2":
        shield_active = True
        print(f"{BLUE}you raised your shield and blocked the Time giants attack {RESET}")

    elif choice_fight == "3":
        if player_heals > 0:
            heal_amount = 30
            player_hp = player_hp + heal_amount
            player_heals = player_heals - 1
            print(f"{BLUE} you used a potion a recovered {heal_amount} HP!!! {RESET}")
        else:
            print(f"{BLUE}you have no heals left (visit the Time shop to buy some more){RESET}")

    else:
        print("invalid choice! you lost your turn")

    if boss_hp > 0:
        boss_damage = random.randint(10, 20 )

        if shield_active:
            boss_damage = boss_damage // 2
            print(f"{RED}your shield blocked part of the hit! you took {boss_damage} damage {RESET} ")
        else:
            print(f"{RED}the Time giant hits you for {boss_damage} damage! {RESET}")

        player_hp = player_hp - boss_damage

    print("-" * 40)

if player_hp > 0 and boss_hp <= 0:
    print("\nVICTORY! you vanquished the Time giant!")

elif player_hp <= 0:
    print("\nDEFEAT you got killed by the Time giant")
    

            


    
    
    
    
    
    
    
    
    
    
    
elif choice_1 == "time shop":
    print("\nWelcome to the Time Shop!")

elif choice_1 == "quit":
        game_life = False
        print("\nThanks for playing!")

else:
        print("\nInvalid choice, try again.")



