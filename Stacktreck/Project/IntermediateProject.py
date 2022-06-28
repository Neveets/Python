import AdventureClasses
import AdventureStory
import os.path
import time

select_menu = True
while select_menu:
    menu = AdventureStory.homeScreen()
    if menu == '1':
        if not (os.path.exists('savedata.dat')):
            monster = AdventureStory.monsterSelect()
            select_menu = False
            AdventureStory.saveData(monster)
        else:
            answer = input("A saved file already exists. Do you want to overwrite the file? (Y/N): ")
            if (answer.lower() == 'y'):
                monster = AdventureStory.monsterSelect()
                select_menu = False
                AdventureStory.saveData(monster)
    elif menu == '2':
        if (os.path.exists('savedata.dat')):
            monster = AdventureStory.loadData()
            select_menu = False
        else:
            print("There is no saved file.")
            time.sleep(2)
    elif menu == '3':
        select_menu = False
        os._exit(1)

town_action = True
while town_action:
    action = AdventureStory.town(monster)
    if action == 'f':
        AdventureStory.searchEnemy(monster)
    elif action == 'h':
        AdventureStory.healingCenter(monster)
    elif action == 'b':
        AdventureStory.buyShop(monster)
    elif action == 'v':
        AdventureStory.viewStats(monster)
    elif action == 's':
        AdventureStory.saveData(monster)
        print("Data saved!")
        time.sleep(1)
    elif action == 'x':
        print("Thank you for playing!")
        town_action = False
        time.sleep(1)