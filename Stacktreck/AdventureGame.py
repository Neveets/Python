import os
import time
import random

starter_mon = ["Flaremon", "Aquamon", "Galemon"]
actions = ["Attack", "Skill", "Run"]
mon_attack_damage = {"Flaremon":"4", "Aquamon":"3", "Galemon":"3"}
mon_hp = {"Flaremon":"15", "Aquamon":"25", "Galemon":"20"}
enemy_mon = ["Slime", "Orc", "Worm", "Golem"]
enemy_attack_damage = {"Slime": "2", "Orc":"3", "Worm":"4", "Golem":"5"}
enemy_hp = {"Slime": "10", "Orc":"12", "Worm":"15", "Golem":"20"}
selected_mon = None
enemy = None

clear = lambda: os.system('cls')

def intro():
    global selected_mon
    clear()
    print("""Welcome to Adventure Monster Game!\n
As you celebrate your 18th birthday, you went to the town professor to get your awaited gift.
He presented you 3 monsters to accompany you in your journey:\n
Flaremon = Fire / Attack Type
Aquamon = Water / Defense Type
Galemon = Wind / Speed Type\n""")
    correct_answer = False
    while correct_answer == False:
        monster = input("Choose your monster (Flaremon/Aquamon/Galemon): ")
        for mon in starter_mon:
            if (monster.upper() == mon.upper()):
                selected_mon = mon
                correct_answer = True

def scene1():
    clear()
    print(f"You have chosen {selected_mon} to join you in your journey!")
    print("\nLet's begin!")
    print("\nYou have been instructed by the professor to go to the next town to get the Next Town Badge.")
    print("As you travel, monsters are in the way and you need to defeat them to proceed.")

def searchenemy():
    global enemy
    enemy = random.choice(enemy_mon)
    time.sleep(3)
    print(f"\n{enemy} appeared!\n")
    time.sleep(1)
    fight()

def fight():
    mhp = int(mon_hp[selected_mon])
    mad = int(mon_attack_damage[selected_mon])
    mskill = int(mad) * 3

    ehp = int(enemy_hp[enemy])
    ead = int(enemy_attack_damage[enemy])
    eskill = int(ead) * 2

    correct_answer = False
    is_dead = False
    while ehp > 0 and mhp > 0:
        print("********************************")
        print(f"| {enemy}\t\t\tHP: {ehp:02} |")
        print("********************************\n")
        print("********************************")
        print(f"| {selected_mon}\t\tHP: {mhp:02} |")
        print("********************************")
        print("Choose your action in battle:\n")
        for act in actions:
            print(act)
        correct_answer = False
        action = input("\nEnter action: ")
        for act in actions:
            if (act.lower() == action.lower()):
                correct_answer = True
                if (act.lower() == "attack"):
                    print(f"You attacked the enemy! You dealt {mad} damage")
                    time.sleep(1)
                    ehp -= mad
                elif (act.lower() == "skill"):
                    print(f"You used skill!")
                    time.sleep(1)
                    print("WOOOOOSH!")
                    time.sleep(1)
                    print(f"You dealt {mskill} damage")
                    ehp -= mskill
                elif (act.lower() == "run"):
                    if (selected_mon == "Galemon"):
                        print("You escaped successfully!")
                        time.sleep(1)
                        return
                    else:
                        print("You tried to run but cannot escape! (If only you have Galemon)")
                        time.sleep(1)
                
                if (ehp > 0):
                    print(f"Enemy hp left: {ehp}")
                    time.sleep(1)
                    eaction = random.randrange(0,3)
                    if (eaction == 3):
                        print(f"Enemy used skill!")
                        time.sleep(1)
                        print(f"GRAAAAH!")
                        time.sleep(1)
                        print(f" You received {eskill} damage")
                        mhp -= eskill
                    else:
                        print(f"Enemy attacked you! You received {ead} damage")
                        time.sleep(1)
                        mhp -= ead
                else:
                    time.sleep(1)
                    print("Enemy is dead")

                if (mhp > 0):
                    print(f"{selected_mon} hp left: {mhp}")
                    if (ehp <= 0):
                        time.sleep(1)
                        print(f"{selected_mon} received 5 experience points!")
                else:
                    time.sleep(1)
                    print(f"{selected_mon} died. You went to the hospital")

        if (correct_answer == False):
            print("Enemy is laughing at you. What are you doing?")


        time.sleep(1)
            

intro()
scene1()
continue_game = True
while continue_game:
    searchenemy()
    print("""\nWould you like to continue? 
(c) Continue
(r) Rest""")
    ask_continue = True
    while ask_continue:
        answer = input("Enter letter: ")
        if (answer.lower() == "r"):
            continue_game = False
            ask_continue = False
        elif (answer.lower() == "c"):
            ask_continue = False
            clear()
