import math, random, copy

defaultHealth = 100
questStep = 0
enemyStunned = False

levelData = [
    100,
    200,
    300,
    400,
    500
]


playerData = {
    "Stats":{
        "Health": 100,
        "Attack": 10,
        "Defence": 0, 
        "Agility": 10,
        "Level": 0,
        "Exp": 0,
        "Gold": 0
    },

    "Inventory":{
        "Slot0": ("Old Shortsword", "Weapon", 10),
        "Slot1": ("Bruised Iron Leggings", "Legs", 5),
        "Slot2": None,
        "Slot3": None,
        "Slot4": None,
        "Slot5": None,
        "Slot6": None,
        "Slot7": None,
        "Slot8": None,
        "Slot9": None,
        "Slot10": None
    },

    "EquippedItems":{
        "Weapon": ("Fist", "Melee", 1),
        "Shield": ("Ragged Leather Sheild", "Shield", 1),
        "Head": None,
        "Chest": None,
        "Arms": None,
        "Hands": None,
        "Legs": None,
        "Feet": None
    }
}

enemies = {
    "Goblin": {
        "Stats":{
            "Health": 25,
            "Attack": 5,
            "Agility": 25,
            "ExpValue": 10
        },

        "Drops":{
            "Rusty Dagger": ("Rusty Dagger", "Weapon", 5),
            "Musty Skullcap": ("Musty Skullcap", "Head",  2)
            
        },

        "DefaultHealth": 25,

        "DropChance": 100
    },

    "Skeleton": {
        "Stats":{
            "Health": 50,
            "Attack": 10,
            "Agility": 5,
            "ExpValue": 35
        },

        "Drops":{
            "Old Shortsword": ("Old Shortsword", "Weapon", 10),
            "Bruised Iron Leggings": ("Bruised Iron Leggings", "Legs", 5)
        },

        "DefaultHealth": 50,

        "DropChance": 100
    }

}

# EXP, GOLD, ATTACK
randomEvents = {
    "Treasure Chest":{
        "Exp": 0,
        "Gold": 25,
        "Attack": 0,
        "HealthRestore": False,
        "EventDescription": "You find A chest full of gold and plunder!"
    },
    "Ancient Statue": {
        "Exp": 100,
        "Gold": 10,
        "Attack": 1,
        "HealthRestore": True,
        "EventDescription": "You stumble upon an ancient, glowing statue..."
    }
}

# This is for randomizing drops and encounters.
# random_item = random.choice(list(plrData.keys()))
# randomChoice = plrData[random_item]

# whenever the player moves forward, 75% chance of random event
# 25% chance of enemy encounter. After a certain number of turns,
# the player must fight a final boss with the random items they
# aquired.

## Creates copies of player and enemy data
defaultPlayerData = copy.deepcopy(playerData)
defaultEnemysData = copy.deepcopy(enemies)

## Resets everything when player dies
def cleanupFunction():
    global playerData, enemies
    print("You died, your quest is over.")

    # Resets player's and enemies data
    playerData = defaultPlayerData
    enemies = defaultEnemysData

    while True:
        restartQuest = str.upper(input("Restart? Yes(Y): "))  

        if restartQuest == "Y":
            questBegin()
        
        else:
            print("Invalid input")

def inventory():
    print(playerData["Inventory"])
    gameLoop()

def equipItem():
    
    print("player's inventory", playerData["Inventory"])

    while True:
        equipItemInput = int(input("Which item do you want to equip, input 0 for first slot, etc."))
        # Player can input 0-10, the number they input equals
        # the item that they want to equip. So prompt the user
        # with the items that are in their inventory, and 
        # what ever item them they select, it automatically gets
        # equipped to it's respective slot.

        if equipItemInput == 0:
            print("bogos")

            if playerData["Inventory"]["Slot0"] == None:
                print("No item in slot 0")
                gameLoop()

            else:

                inventoryItemSelected = playerData["Inventory"]["Slot0"] # == ('Old Shortsword', 'Weapon', 10)
                inventoryItemName = inventoryItemSelected[0]
                inventoryItemType = inventoryItemSelected[1]
                inventoryItemStat = inventoryItemSelected[2]

                for equipSlotName, equipSlot, in playerData["EquippedItems"].items():
                    if not equipSlotName == None:
                        print("That slot isn't empty, unequip the item in it's slot")
                        equip()

                    elif inventoryItemType == equipSlotName:
                        playerData["EquippedItems"][equipSlotName] = inventoryItemSelected
                        print("player equipped items", playerData["EquippedItems"])
                        break

        elif equipItemInput == 1:
            print("bogos")

            inventoryItemSelected = playerData["Inventory"]["Slot1"] # == ('Old Shortsword', 'Weapon', 10)
            inventoryItemName = inventoryItemSelected[0]
            inventoryItemType = inventoryItemSelected[1]
            inventoryItemStat = inventoryItemSelected[2]

            for equipSlotName, equipSlot, in playerData["EquippedItems"].items():
                if inventoryItemType == equipSlotName:
                    playerData["EquippedItems"][equipSlotName] = inventoryItemSelected
                    print("player equipped items", playerData["EquippedItems"])
                    break
        



        else:
            print("Invalid input")

def unequipItem():
    print("Unequip")


def discardItem():
    print("What do you want to discard?")


def equip():

    while True:
        equipOptionsInput = str.upper(input("Equip options: Equip(E), Unequip (U), Discard(D): "))

        if equipOptionsInput == "E":

            equipItem()


        elif equipOptionsInput == "U":
            print("Player tried to unequip")
            unequipItem()
        
        elif equipOptionsInput == "D":
            print("Player tried to discard")
            discardItem()

        else:
            print("Invalid input")

    gameLoop()

def rest():
    if playerData["Stats"]["Health"] == 100:
        print("You are already max health")
        gameLoop()

    elif playerData["Stats"]["Health"] != 100:
        playerData["Stats"]["Health"] *= 25 + playerData["Stats"]["Agility"]

        if playerData["Stats"]["Health"] >= 101:
            playerData["Stats"]["Health"] = 100
            print("You rested, your health is now: ", playerData["Stats"]["Health"])
            moveForward()
            questStep += 1 

        else:
            print("You rested, your health is now: ", playerData["Stats"]["Health"])
            moveForward()
            questStep += 1 


def help():
    while True:
        helpMoveInput = str.upper(input("Help with: Move forward(M), Inventory(I), Equip(E), Rest(R), Exit(X): "))

        if helpMoveInput == "M":
            print("Moves you forward. % chance for enemy encounter, % chance for random event.\n Also increases the quest step, until step 20, where you fight the final boss.")
        
        elif helpMoveInput == "I":
            print("Shows all items within your inventory.")

        elif helpMoveInput == "E":
            print("Allows you to equip weapons and armor.")

        elif helpMoveInput == "R":
            print("Allows you to rest for a turn, which heals you 25 health + agility\n Has a chance of enemy ambush")
        
        elif helpMoveInput == "X":
            gameLoop()

        else:
            print("Invalid input")

def gameLoop():
    global questStep

    if questStep == 0:
        print("This is the first step of your adventure!\nBe sure to prepare for a harsh trek ahead!\n")

        while True:
            playerChoice = str.upper(input("Move forward(M), Inventory(I), Equip(E), Rest(R), Help(H): "))

            if playerChoice == "M":                
                moveForward()
                break

            elif playerChoice == "I":
                questStep += 1  
                inventory()
                break

            elif playerChoice == "E":
                questStep += 1  
                equip()
                break

            elif playerChoice == "R":
                questStep += 1  
                rest()  
                break

            elif playerChoice == "H":
                questStep += 1  
                help()
            else:
                print("Invalid input")

    elif questStep == 5:
        print("Shopkeeper goes here, or a selection of random events specific to each 5 quest steps.")
        moveForward()
    elif questStep == 20:
        print("player reached quest step 20, final boss goes here")

    else:
        while True:
            playerChoice = str.upper(input("Move forward(M), Inventory(I), Equip(E), Rest(R): "))
            
            if playerChoice == "M": 
                questStep += 1  
                moveForward()
                break
                
            elif playerChoice == "I":
                inventory()
                break

            elif playerChoice == "E":
                equip()
                break

            elif playerChoice == "R": 
                rest()  
                break

            elif playerChoice == "H":
                help()

            else:
                print("Invalid input")
        
def moveForward():
    global questStep, defaultHealth
    enemyOrEvent = random.randint(0, 100)
    questStep += 1
    
    if enemyOrEvent >= 90: #Encountered Random Event:

        eventSelected = random.choice(list(randomEvents.keys()))
        eventProperties = randomEvents[eventSelected]

        print(eventProperties["EventDescription"])
        playerData["Stats"]["Exp"] += eventProperties["Exp"]
        playerData["Stats"]["Gold"] += eventProperties["Gold"]
        playerData["Stats"]["Attack"] += eventProperties["Attack"]

        if eventProperties["HealthRestore"]:
            playerData["Stats"]["Health"] = defaultHealth
            print("restored health")
            gameLoop()

        else:
            gameLoop()
        

    else: #Encountered Enemy
        enemySelected = random.choice(list(enemies.keys()))
        print("")
        print("You encountered a", enemySelected)
        combat(enemySelected)

def combat(enemySelected):
    global enemyStunned
    enemyProperties = enemies[enemySelected]
    stunChance = playerData["Stats"]["Defence"] * 3

    while playerData["Stats"]["Health"] > 0:
        playerAtkChoice = str.upper(input("Attack(A), Defend(D), Run(R), Stats(S), Enemy Stats(E), Help(H): "))

        if playerAtkChoice == "A":
            playerDamage = playerData["Stats"]["Attack"] + playerData["EquippedItems"]["Weapon"][2]
            enemyProperties["Stats"]["Health"] -= playerDamage # hit enemy 

            if enemyStunned:
                print("The enemy was stunned, they couldn't attack!")
                print("You did", playerDamage ,"damage to the enemy, the enemies health is:", enemyProperties["Stats"]["Health"])
                enemyStunned = False

            elif enemyProperties["Stats"]["Attack"] <= playerData["Stats"]["Defence"]:
                playerData["Stats"]["Health"] -= 1

                print("You did:", playerDamage, "damage to the enemy, but the enemy did 1 damage to you!")
                print("Your new health is:", playerData["Stats"]["Health"], "the enemies health is:", enemyProperties["Stats"]["Health"])

            else:
                enemyDamage = enemyProperties["Stats"]["Attack"] - playerData["Stats"]["Defence"] 
                playerData["Stats"]["Health"] -= enemyDamage
                
                print("You did:", playerDamage, "damage to the enemy, but the enemy did", enemyDamage, "damage to you!") # enemy hit player
                print("Your new health is:", playerData["Stats"]["Health"], ", the enemies health is:", enemyProperties["Stats"]["Health"])
                
        elif playerAtkChoice == "D":
            print("Player Defended!")
            stun = random.randint(0, 100)
            
            if stun >= stunChance:
                enemyStunned = True
                print("You dodged the enemy!")

            else:
                print("Enemy hit you")
        
        elif playerAtkChoice == "R":
            print("Player tried to run!")

        elif playerAtkChoice == "S":
            print("")
            print(playerData["Stats"])

        elif playerAtkChoice == "E":
            print("")
            print(enemySelected, "Health:", enemyProperties["Stats"]["Health"], "|", "Attack:", enemyProperties["Stats"]["Attack"], "|", "Agility:", enemyProperties["Stats"]["Agility"] )

        elif playerAtkChoice == "H":
            while True:
                helpAttackInput = str.upper(input("Help with: Attack(A), Defend(D), Run(R), Stats(S), Exit(X): "))
                if helpAttackInput == "A":
                    print("")
                    print("Attacks the enemy, the enemy also attacks you.")

                elif helpAttackInput == "D":
                    print("")
                    print("Defends against the enemy. Has a chance to stun enemy for a turn")

                elif helpAttackInput == "R":
                    print("")
                    print("Has a chance to run from an enemy, and exit the encounter")
                
                elif helpAttackInput == "S":
                    print("")
                    print("Shows you your current stats.")

                elif helpAttackInput == "X":
                    print("")
                    print("You exited help")
                    combat(enemySelected)

                else:
                    print("Invalid input")

        else:
            print("Invalid input")

        if enemyProperties["Stats"]["Health"] <= 0:
            print("You defeated the", enemySelected)

            dropRandNum = random.randint(0, 100)

            enemyProperties["Stats"]["Health"] = enemyProperties["DefaultHealth"]

            if dropRandNum <= enemyProperties["DropChance"]: 
                dropSelected = random.choice(list(enemyProperties["Drops"].keys()))
                dropProperties = enemyProperties["Drops"][dropSelected]

                print("You aquired: ", dropSelected)

                #     "Inventory":{
                #     "Slot0": None,
                #     "Slot1": None,
                #     "Slot2": None,
                #     "Slot3": None,
                #     "Slot4": None,
                #     "Slot5": None,
                #     "Slot6": None,
                # },
                
                for slot, item in playerData["Inventory"].items():
                    if item is None:  # Check if the slot is empty
                        playerData["Inventory"][slot] = dropProperties  # Place the item in the slot
                        print("This is dropselected",dropSelected[1])
                        print(playerData["Inventory"])
                        gameLoop()
                        break

            else:
                print("no drops :(")
                gameLoop()
                break
        
    ## Relates to the while loop, when the player dies, call this function.
    cleanupFunction()

def questBegin():
    print("Welcome to TERRA, the home of the gods.\nThis is a simple text based rpg.\n")
    playerName = str(input("Please enter your name: "))
    playerData["PlayerName"] = playerName
    print("Welcome", playerData["PlayerName"])
    print("")
    gameLoop()

# Initialize the game 
questBegin()

