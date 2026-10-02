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

choice_1 = input("Where would you like to go (mini dungeon 1/time shop): ")
pygame.mixer.music.stop()


flag = True

while flag == True:
    if choice_1 == "mini dungeon 1":
        print("Welcome to Mini Dungeon 1 here you will have to decode a code ")
        secret_code = "with time comes a dire price face a challenge to restore time slightly to it's chosen path"
        scrambled_code = "twhi itme a erid icepr ecaf a llngechae ot sortere imet tlyhgils ot s'ti nesoch htap"
        print(f"here is your scrambled code: {scrambled_code}")
        guess = input("Enter your guesss: ")
elif guess.strip().lower() == secret_code.lower():
        

