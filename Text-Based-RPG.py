import math, random, time

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
        "Health": 0,
        "Attack": 10,
        "Defence": 0, 
        "Agility": 10,
        "Level": 0,
        "Exp": 0,
        "Gold": 0
    },

    "Inventory":{
        "Slot0": None,
        "Slot1": None,
        "Slot2": None,
        "Slot3": None,
        "Slot4": None,
        "Slot5": None,
        "Slot6": None,
    },

    "EquippedItems":{
        "Weapon": ("Fist", "Melee", 1),
        "Shield": 0,
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
            "Rusty Dagger": ("Rusty Dagger", "Melee", 5),
            "Musty Skullcap": ("Musty Skullcap", "Armor", "Head", 2)
            
        },

        "DefaultHealth": 25,

        "DropChance": 50
    },

    "Skeleton": {
        "Stats":{
            "Health": 50,
            "Attack": 10,
            "Agility": 5,
            "ExpValue": 35
        },

        "Drops":{
            "Old Shortsword": ("melee", 10),
            "Bruised Iron Leggings": ("Armor", "Legs", 5)
        },

        "DefaultHealth": 50,

        "DropChance": 25
    }

}

# EXP, GOLD, ATTACK
randomEvents = {
    "Treasure Chest":{
        "Exp": 0,
        "Gold": 25,
        "Attack": 0,
        "HealthRestore": False
    },
    "Ancient Statue": {
        "Exp": 100,
        "Gold": 10,
        "Attack": 1,
        "HealthRestore": True
    }
}

# random_item = random.choice(list(plrData.keys()))
# randomChoice = plrData[random_item]

# whenever the player moves forward, 75% chance of random event
# 25% chance of enemy encounter. After a certain number of turns,
# the player must fight a final boss with the random items they
# aquired.

def inventory():
    print("Player opened inventory")
    print(playerData["Inventory"])
    print(questStep)
    gameLoop()

def equip():
    print("Player opened equip menu")
    print(playerData["EquippedItems"])

def rest():
    print("Player rested")
    playerData["Stats"]["Health"] *= 1.25
    print("Your health is now", playerData["Stats"]["Health"])
    moveForward()

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
            print("Allows you to rest for a turn, which heals you 25% of your health\n Has a chance of enemy ambush")
        
        elif helpMoveInput == "X":
            gameLoop()

        else:
            print("Invalid input")

def gameLoop():
    global questStep
    if questStep == 0:
        print("This is the first step of your adventure!\nBe sure to prepare for a harsh trek ahead!")
        print("")

        while True:
            playerChoice = str.upper(input("Move forward(M), Inventory(I), Equip(E), Rest(R), Help(H): "))

            if playerChoice == "M": 
                questStep += 1                
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
                questStep += 1  
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
    print("Player moved forward")
    
    if enemyOrEvent >= 90: #Encountered Random Event:

        eventSelected = random.choice(list(randomEvents.keys()))
        eventProperties = randomEvents[eventSelected]

        print("You happened upon an", eventSelected)
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
        print("You encountered a", enemySelected)
        combat(enemySelected)

def combat(enemySelected):
    global enemyStunned
    enemyProperties = enemies[enemySelected]
    stunChance = playerData["Stats"]["Defence"] * 3

    while playerData["Stats"]["Health"] > 0:
        playerAtkChoice = str.upper(input("Attack(A), Defend(D), Run(R), Stats(S), Help(H): "))

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
            print(playerData["Stats"])

        elif playerAtkChoice == "H":
            print("Player used help!")

            while True:
                helpAttackInput = str.upper(input("Help with: Attack(A), Defend(D), Run(R), Stats(S), Exit(X): "))
                if helpAttackInput == "A":
                    print("Attacks the enemy, the enemy also attacks you.")

                elif helpAttackInput == "D":
                    print("Defends against the enemy. Has a chance to stun enemy for a turn")

                elif helpAttackInput == "R":
                    print("Has a chance to run from an enemy, and exit the encounter")
                
                elif helpAttackInput == "S":
                    print("Shows you your current stats.")

                elif helpAttackInput == "X":
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

            if dropRandNum >= 50: 
                dropSelected = random.choice(list(enemyProperties["Drops"].keys()))
                

                print("You aquired: ", dropSelected)
                gameLoop()
                break
            else:
                print("no drops :(")
                gameLoop()
                break
        
    print("You died, your quest is over.")

    while True:
        restartQuest = str.upper(input("Restart? Yes(Y): "))  

        if restartQuest == "Y":
            questBegin()
        
        else:
            print("Invalid input")

def questBegin():
    print("Welcome to TERRA, the home of the gods.\nThis is a simple text based rpg.")
    playerName = str(input("Please enter your name: "))
    playerData["PlayerName"] = playerName
    print("Welcome", playerData["PlayerName"])
    gameLoop()

# Initialize the game 
questBegin()
