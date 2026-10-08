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

        game_over = False

    while player_hp > 0 boss_hp > 0 and not game_over:
        print(f"Your HP: {player_hp} | Heals left: {player_heals}")
        print(f"Boss HP: {boss_hp}")
        print("\nChoose your action:")
        print("1. Attack")
        print("2. Shield")
        print("3. Heal")

    choice_fight =  input("Enter choice (1, 2, or 3: )")
    print()

    player_damage = 0
    shield_active = False

    if choice == "1":
        player_damage = random.randint(15, 25)

    elif choice_1 == "time shop":
        print("\nWelcome to the Time Shop!")

    elif choice_1 == "quit":
        game_life = False
        print("\nThanks for playing!")

    else:
        print("\nInvalid choice, try again.")



