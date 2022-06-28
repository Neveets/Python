import os
import random
import time
import AdventureClasses
import pickle

clear = lambda: os.system('cls')
enemy_monsters_forest = ["Slime", "Goblin", "Orc"]
enemy_monsters_cave = ["Wolf", "Worm", "Golem"]

def saveData(monster):
    file = open("savedata.dat", "wb")
    pickle.dump(monster, file)
    file.close()

def loadData():
    file = open("savedata.dat", "rb")
    monster = pickle.load(file)
    file.close()
    print("Load successfully!")
    time.sleep(1)
    return monster

def homeScreen():
    menu = ''
    while menu not in ['1','2', '3']:
        clear()
        print("===========================================================================================")
        print("| Adventure Monsters     |   Created by: Steven Romero   |   Created Date: 27/06/2022     |")
        print("===========================================================================================")
        print(r"""

    █▀▀█ █▀▀▄ ▀█ █▀ █▀▀ █▀▀▄ ▀▀█▀▀ █  █ █▀▀█ █▀▀   █▀▄▀█ █▀▀█ █▀▀▄ █▀▀ ▀▀█▀▀ █▀▀ █▀▀█ █▀▀ 
    █▄▄█ █  █  █▄█  █▀▀ █  █   █   █  █ █▄▄▀ █▀▀   █ ▀ █ █  █ █  █ ▀▀█   █   █▀▀ █▄▄▀ ▀▀█ 
    ▀  ▀ ▀▀▀    ▀   ▀▀▀ ▀  ▀   ▀    ▀▀▀ ▀ ▀▀ ▀▀▀   ▀   ▀ ▀▀▀▀ ▀  ▀ ▀▀▀   ▀   ▀▀▀ ▀ ▀▀ ▀▀▀
        """)
        print(r"""
                                       /\
                                  /\  //\\
                           /\    //\\///\\\        /\
                          //\\  ///\////\\\\  /\  //\\
             /\          /  ^ \/^ ^/^  ^  ^ \/^ \/  ^ \
            / ^\    /\  / ^   /  ^/ ^ ^ ^   ^\ ^/  ^^  \
           /^   \  / ^\/ ^ ^   ^ / ^  ^    ^  \/ ^   ^  \       *
          /  ^ ^ \/^  ^\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \     /|\
         / ^ ^  ^ \ ^  _\___________________|  |_____^ ^  \   /||o\
        / ^^  ^ ^ ^\  /______________________________\ ^ ^ \ /|o|||\
       /  ^  ^^ ^ ^  /________________________________\  ^  /|||||o|\
      /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||\
     / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |
    / ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooooooo
    ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
        """)
        print("1. New Game")
        print("2. Load Game")
        print("3. Exit")
        menu = input("Enter menu: ")

    return menu

def monsterSelect():
    selected = ''
    while selected not in ['flaremon', 'aquamon', 'galemon']:
        clear()
        print("""Welcome to Adventure Monster Game!\n
As you celebrate your 18th birthday, you went to the town professor to get your awaited gift.
He presented you 3 monsters to accompany you in your journey:""")
        print(r"""
              ██  ██                ██ ███                         ████
         ██  █▓█ █▓█               █░▒█░▒▒█                      ██▒▒▒▒██
    ████ █▓██▓▓██▓▓█               █▒▒░▒░░███                   █▓▒▒▒▒▒▒▒█
   █▓▓▓▓██▓▓█▓▓▓▓▓█                █░░░▓░░░▓█                   ███▓▒▒▒▒▒█
  █▓▓▓██▓█▓▒▓░▓▓▓▓█              ██░░░██▓░░███                      ██▓▓▓▒▓█
  █▓▓█░░░▓█░▓░▓░░▓██            █░░▒░░██▓░░▒▓█                        █▒░▓▒░█
 █▓▓█░░░░░█░░░░▓▓▓▓█            █░█░░░░░░▒░▒█                        █░░░░░░▒█
 █▓▓█░░██░▓▒░░░░▒▓█             █▒░░██▒█▒░░░▓█ █                     █░▒▒░░░░░█
█▓▓▓░░█░░░██▒░░▒▓██              ███▓▓▓▓░░░▒░██▓██                  █░▒░█▒░░░██
█▓▓░░░░░░▒▓███░░▒▓▓█               █▓▓▒░░█▒░░░█▓▒█                  █░▒░█░░░░██
█▓░███▒▒░░░░▓██▓████               █░░░██▒▓░░░░█▒█                ██░░░░██░░▒░█
 ██░█░█░░█▒░░████                   ███▒▒▒▒██░█▓█                █▒▓▒░░░░░▒▒░█
     ██░█░░█░░█                      █▒▒▒▓░▒▓██▒█                █▓▒▒▓░░░░░░░▓█
      █▒░██░░░█                      █▒▒▓░░░▒▓▒█                 █▒▒▒▒▒░▓░░▓░█
     █░░▒░▒░░█                      █░█▒▓░░░▒██                  █▒▒▒▒▒▒▒▒░░▒█
      ██████▒█                       █████▒▒██                   █▒▒▒▒▒▒▒▒▒▒░█
          █░░█                           █░░█                     ███▒▒▒▒▒███
           ██                             ███                        █████
           
     Flaremon                          Aquamon                       Galemon
    Attack Type                      Defense Type                   Speed Type""")
        selected = input("Choose your starter monster (Flaremon/Aquamon/Galemon): ").strip().lower()
    
    print(f"You have chosen {selected.capitalize()} to join you in your journey!")
    if selected.capitalize() == 'Flaremon':
        monster = AdventureClasses.Monster(selected.capitalize(), 23, 6, 3, 3, 3, 0)
    elif selected.capitalize() == 'Aquamon':
        monster = AdventureClasses.Monster(selected.capitalize(), 30, 5, 5, 3, 3, 0)
    elif selected.capitalize() == 'Galemon':
        monster = AdventureClasses.Monster(selected.capitalize(), 26, 5, 4, 5, 3, 0)
    time.sleep(2)
    return monster

def viewFlaremon():
    print(r"""
              ██  ██
         ██  █▓█ █▓█
    ████ █▓██▓▓██▓▓█
   █▓▓▓▓██▓▓█▓▓▓▓▓█
  █▓▓▓██▓█▓▒▓░▓▓▓▓█
  █▓▓█░░░▓█░▓░▓░░▓██
 █▓▓█░░░░░█░░░░▓▓▓▓█
 █▓▓█░░██░▓▒░░░░▒▓█
█▓▓▓░░█░░░██▒░░▒▓██
█▓▓░░░░░░▒▓███░░▒▓▓█
█▓░███▒▒░░░░▓██▓████
 ██░█░█░░█▒░░████
     ██░█░░█░░█
      █▒░██░░░█
     █░░▒░▒░░█
      ██████▒█
          █░░█
           ██""")

def viewAquamon():
    print(r"""
    ██ ███
   █░▒█░▒▒█
   █▒▒░▒░░███
   █░░░▓░░░▓█
 ██░░░██▓░░███
█░░▒░░██▓░░▒▓█
█░█░░░░░░▒░▒█
█▒░░██▒█▒░░░▓█ █
 ███▓▓▓▓░░░▒░██▓██
   █▓▓▒░░█▒░░░█▓▒█
   █░░░██▒▓░░░░█▒█
    ███▒▒▒▒██░█▓█
     █▒▒▒▓░▒▓██▒█
     █▒▒▓░░░▒▓▒█
    █░█▒▓░░░▒██
     █████▒▒██
         █░░█
          ███""")

def viewGalemon():
    print(r"""
   ████
 ██▒▒▒▒██
█▓▒▒▒▒▒▒▒█
 ███▓▒▒▒▒▒█
    ██▓▓▓▒▓█
      █▒░▓▒░█
     █░░░░░░▒█
     █░▒▒░░░░░█
    █░▒░█▒░░░██
    █░▒░█░░░░██
  ██░░░░██░░▒░█
 █▒▓▒░░░░░▒▒░█
 █▓▒▒▓░░░░░░░▓█
 █▒▒▒▒▒░▓░░▓░█
 █▒▒▒▒▒▒▒▒░░▒█
 █▒▒▒▒▒▒▒▒▒▒░█
  ███▒▒▒▒▒███
     ██▒░█
       ██""")


def town(monster):
    action = ''
    while action not in ['f', 'h', 'b', 'v', 's', 'x']:
        clear()
        print("*********************************************************")
        print(f"Lv. {monster.level} {monster.name}\t\tHP: {monster.current_health}/{monster.max_health}\t\tMP: {monster.current_mana}/{monster.max_mana}")
        print("*********************************************************")
        print(r"""
                       .|
                       | |
                       |'|            ._____
               ___    |  |            |.   |' .---"|
       _    .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
        print(r"""
    (F) Fight Monsters      (B) Buy in Shop
    (H) Healing Center      (V) View Stats
    (S) Save                (X) Rest / Exit""")
        action = input('\nWhere do you want to go? ')
    
    return action

def buyShop(monster):
    shop_items = []
    shop_item = None
    clear()
    print("***********************************")
    print(f" Shop\tGold: {monster.gold}\tPotions: {monster.potions} ")
    print("***********************************")
    print(r"""
           |
.-. _______|
|=|/     /  \
| |_____|_SM_|
|_|_[-]_|____|""")
    if not (os.path.exists('shopitems.dat')):
        file = open("shopitems.dat", "wb")
        item_potion = AdventureClasses.ShopItems("1", "Potion", "20", "Heals monster for 20 health")
        pickle.dump(item_potion, file)
        file.close()
    print("\nWhat would you like to buy?\n")
    file = open("shopitems.dat", "rb")
    while True:
        try:
            content = pickle.load(file)
            print(f"({content.id}) {content.name}\t{content.price}g\t{content.description}")
            shop_items.append(content.id)
        except EOFError:  # Nothing to read
            break
    file.close()
    print("(0) Cancel")
    print("\n")
    buy_item = ''
    while buy_item not in shop_items:
        buy_item = input("What would you like to buy? ")
        if buy_item == '0':
            break
    if buy_item == '0':
        return
    quantity = ''
    while not quantity.isnumeric():
        quantity = input("How many would you like to buy? ")
        if quantity == '0':
            break
    
    search_shop = True
    file = open("shopitems.dat", "rb")
    while search_shop:
        try:
            content = pickle.load(file)
            if buy_item == content.id:
                shop_item = content
                search_shop = False
        except EOFError:  # Nothing to read
            break
    file.close()

    if int(quantity) > 0:
        total_price = int(quantity) * float(shop_item.price)
        if (monster.gold >= total_price):
            monster.potions += int(quantity)
            monster.gold -= int(total_price)
            print(f"Successfully bought {quantity} {shop_item.name}!")
            time.sleep(2)
        else:
            print("Not enough gold")
            time.sleep(2)

def healingCenter(monster):
    clear()
    print("****************************")
    print(f" \tHealing Center\t   ")
    print("****************************")
    print(r"""
            |   _   _
      . | . H .|.|-|.|
   |\ ./.\-/.\-|.|.|.|
~~~|.|_|.|_|.|.|.|_|.|~~~""")
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    monster.current_health = monster.max_health
    monster.current_mana = monster.max_mana
    print(monster.name, 'is fully restored!')
    time.sleep(2)

def viewStats(monster):
    clear()
    print("*************************")
    print(f"\t{monster.name}")
    print("*************************")
    if (monster.name == "Flaremon"):
        viewFlaremon()
    elif (monster.name == "Aquamon"):
        viewAquamon()
    elif (monster.name == "Galemon"):
        viewGalemon()

    print("Level: ", monster.level)
    print(f"HP: {monster.max_health}\t\t\tMP: {monster.max_mana}")
    print(f"Attack: {monster.attack}\t\tDefense: {monster.defense}")
    print(f"Speed: {monster.speed}\t\tHit: {monster.hit}")
    exp_required = monster.level * 4
    print(f"Experience: {monster.experience}/{exp_required}")
    input("\nEnter any key to continue")

def searchEnemy(monster):
    clear()
    enemy_name = ''
    if monster.level <= 4:
        print("You went inside a dark forest")
        enemy_name = random.choice(enemy_monsters_forest)
    elif monster.level <= 8:
        print("You went inside a dangerous cave")
        enemy_name = random.choice(enemy_monsters_cave)
    else:
        enemy_name = random.choice(enemy_monsters_cave)
    enemy_monster = setEnemy(enemy_name)
    time.sleep(1)
    print(f"{enemy_name} appeared!\n")
    time.sleep(1)
    fightEnemy(monster, enemy_monster)

def setEnemy(enemy_name):
    enemy_monster = None
    if enemy_name == 'Slime':
        enemy_monster = AdventureClasses.Monster(enemy_name, 10, 4, 2, 2, 2, 3)
    elif enemy_name == 'Goblin':
        enemy_monster = AdventureClasses.Monster(enemy_name, 18, 8, 4, 3, 3, 7)
    elif enemy_name == 'Orc':
        enemy_monster = AdventureClasses.Monster(enemy_name, 26, 11, 5, 4, 4, 13)
    elif enemy_name == 'Wolf':
        enemy_monster = AdventureClasses.Monster(enemy_name, 30, 10, 6, 12, 10, 15)
    elif enemy_name == 'Worm':
        enemy_monster = AdventureClasses.Monster(enemy_name, 50, 16, 9, 8, 8, 18)
    elif enemy_name == 'Golem':
        enemy_monster = AdventureClasses.Monster(enemy_name, 80, 20, 15, 3, 10, 24)

    return enemy_monster

def fightEnemy(monster, enemy_monster):
    correct_answer = False
    is_dead = False
    while monster.current_health > 0 and enemy_monster.current_health > 0:
        print("******************************************")
        print(f" {enemy_monster.name}\t\t\tHP: {enemy_monster.current_health}/{enemy_monster.max_health} ")
        print("******************************************\n")
        print(r"""
        ░░  ██▓▓▓▓  ▒▒░░    
        ████▓▓▓▓▓▓▓▓▓▓░░    
        ██▓▓▓▓▓▓▓▓▓▓██░░    
          ▓▓▓▓▓▓▓▓▓▓        
          ▓▓▓▓████▓▓        
          ▓▓▓▓▓▓▓▓▓▓        
          ▓▓▓▓▓▓▓▓          
        ▓▓▒▒▒▒▓▓▓▓          
        ▓▓▒▒▒▒▓▓▓▓▒▒▒▒░░░░░░
          ▓▓▓▓████
          ██    ▓▓
        """)
        print("******************************************")
        print(f" {monster.name}\tHP: {monster.current_health:}/{monster.max_health}\tMP: {monster.current_mana}/{monster.max_mana}")
        print("******************************************")
        print("Choose your action in battle:\n")
        print("(A) Attack\t\t(P) Use Potion")
        print("(S) Skill - 4MP\t\t(R) Run\n")
        action = ''
        while action not in ['a', 's', 'p', 'r']:
            action = input("Enter action: ").lower()
            if action == 'a':
                print(f"{monster.name} attacked the enemy!")
                time.sleep(1)
                hit = hitMonster(monster.hit, enemy_monster.speed)
                if hit:
                    damage = monster.attack - (enemy_monster.defense // 2)
                    enemy_monster.current_health -= damage
                    print(f"{monster.name} dealt {damage} damage")
                else:
                    print(f"{enemy_monster.name} is so fast it missed!")

            elif action == 's':
                if monster.current_mana >= 4:
                    print(f"{monster.name} used skill!")
                    time.sleep(1)
                    print("WOOOOOSH!")
                    time.sleep(1)
                    monster.current_mana -= 4
                    damage = monster.attack * 2 - (enemy_monster.defense // 2)
                    enemy_monster.current_health -= damage
                    print(f"{monster.name} dealt {damage} damage")
                else:
                    print(f"{monster.name} does not have enough MP")

            elif action == 'p':
                if monster.potions > 0:
                    print(f"You used potion on {monster.name}!")
                    time.sleep(1)
                    monster.potions -= 1
                    monster.current_health += 20
                    if monster.current_health > monster.max_health:
                        monster.current_health = monster.max_health
                    print(f"{monster.name} restored health points!")
                else:
                    print("You do not have potions")

            elif action == 'r':
                print("You tried to run!")
                time.sleep(1)
                run = random.randint(0, 3)
                if run == 3:
                    print(f"{enemy_monster.name} keeps chasing you. Cannot escape!")
                else:
                    print("Escaped successfully!")
                    time.sleep(1)
                    return

            time.sleep(1)

        # Enemy Turn
        if (enemy_monster.current_health > 0):
            enemy_action = random.randrange(0,3)
            if enemy_action == 3:
                damage = enemy_monster.attack * 2 - (monster.defense // 2)
                print(f"{enemy_monster.name} used skill!")
                time.sleep(1)
                print(f"GRAAAAH!")
                time.sleep(1)
                monster.current_health -= damage
                print(f"{monster.name} received {damage} damage")
            else:
                print(f"{enemy_monster.name} attacked {monster.name}!")
                time.sleep(1)
                hit = hitMonster(enemy_monster.hit, monster.speed)
                if hit:
                    damage = enemy_monster.attack - (monster.defense // 2)
                    monster.current_health -= damage
                    print(f"{monster.name} received {damage} damage")
                else:
                    print(f"{monster.name} is so fast it missed!")
        else:
            print(f"{enemy_monster.name} is dead")
            time.sleep(1)
            monster.experience += enemy_monster.experience
            print(f"{monster.name} won and gained {enemy_monster.experience} experience points!")
            time.sleep(1)
            gold = enemy_monster.experience - 2
            monster.gold += gold
            print(f"You gained {gold} gold")
            checkLevelUp(monster)

        time.sleep(1)
        if (monster.current_health <= 0):
            print(f"{monster.name} died")
            time.sleep(1)
            print(f"GAME OVER")
            time.sleep(1)
            os._exit(1)
            
def hitMonster(attacker_hit, defender_speed):
    hitChance = int(100 - ((float(defender_speed) - float(attacker_hit)) * 10))
    evade = random.randint(1, 100)
    if evade > hitChance:
        return False
    else:
        return True

def checkLevelUp(monster):
    exp_required = monster.level * 4
    while monster.experience >= exp_required:
        time.sleep(1)
        monster.level += 1
        monster.experience -= exp_required
        if (monster.name == "Flaremon"):
            monster.max_health += 3
            monster.current_health = monster.max_health
            monster.max_mana += 2
            monster.current_mana = monster.max_mana
            monster.attack += 2
            monster.defense += 1
            monster.speed += 1
            monster.hit += 1
        elif (monster.name == "Aquamon"):
            monster.max_health += 5
            monster.current_health = monster.max_health
            monster.max_mana += 3
            monster.current_mana = monster.max_mana
            monster.attack += 1
            monster.defense += 2
            monster.speed += 1
            monster.hit += 1
        elif (monster.name == "Galemon"):
            monster.max_health += 4
            monster.current_health = monster.max_health
            monster.max_mana += 3
            monster.current_mana = monster.max_mana
            monster.attack += 1
            monster.defense += 1
            monster.speed += 2
            monster.hit += 2
        print(f"{monster.name} leveled up to {monster.level}!")
        time.sleep(1)