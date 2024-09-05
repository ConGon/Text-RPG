import math, random, time

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
        "Defence": 1, 
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
        "Slot7": None,
        "Slot8": None,
        "Slot9": None,
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
            "RustyDagger": ("RustyDagger", "Melee", 5),
            "MustySkullcap": ("MustySkullcap", "Armor", "Head", 2)
            
        },

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
            "OldShortsword": ("melee", 10),
            "BruisedIronLeggings": ("Armor", "Legs", 5)
        },

        "DropChance": 25
    }

}

# EXP, GOLD, ATTACK
randomEvents = {
    "TreasureChest": {
        "Exp": 0,
        "Gold:": 25
    },
    "AncientStatue": {
        "Exp": 100,
        "Attack": 5
    }
}
# random_item = random.choice(list(plrData.keys()))

# randomChoice = plrData[random_item]

questStep = 0

# whenever the player moves forward, 75% chance of random event
# 25% chance of enemy encounter. After a certain number of turns,
# the player must fight a final boss with the random items they
# aquired.

def inventory():
    print("Player opened inventory")
    print(playerData["Inventory"])
    
def equip():
    print("Player opened equip menu")

def rest():
    print("Player rested")

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
                inventory()
                break

            elif playerChoice == "E":
                equip()
                break

            elif playerChoice == "R":
                rest()  
                break

            elif playerChoice == "H":
                while True:
                    helpMoveInput = str.upper(input("Help with: Move forward(M), Inventory(I), Equip(E), Rest(R)"))
                
                    if helpMoveInput == "M":
                        print("Moves you forward. __ % chance for enemy encounter, % chance for random event.\n Also increases the quest step, until step 20, where you fight the final boss.")
                    
                    elif helpMoveInput == "I":
                        print("Shows all items within your inventory.")

                    elif helpMoveInput == "E":
                        print("Allows you to equip weapons and armor.")

                    elif helpMoveInput == "R":
                        print("Allows you to rest for a turn, which heals you 25% of your health\n Has a chance of enemy ambush")
                    
                    else:
                        print("Invalid input")
                        
            else:
                print("Invalid input")

    elif questStep == 20:
        print("player reached quest step 20, final boss goes here")

    else:
        while True:
            playerChoice = str.upper(input("Move forward(M), Inventory(I), Equip(E), Rest(R): "))
            
            if playerChoice == "M": 
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
                print("help")

            else:
                print("Invalid input")
        
def moveForward():
    global questStep 
    enemyOrEvent = random.randint(0, 100)
    questStep += 1
    print("Number generated was", enemyOrEvent)

    print("Player moved forward")
    if enemyOrEvent >= 90:

        eventSelected = random.choice(list(randomEvents.keys()))
        eventProperties = randomEvents[eventSelected]
        print("Player did not encounter enemy")
    else:
        enemySelected = random.choice(list(enemies.keys()))
        print("You encountered a", enemySelected)
        combat(enemySelected)

def combat(enemySelected):
    enemyProperties = enemies[enemySelected]
    stunChance = playerData["Stats"]["Defence"] * 2

    while playerData["Stats"]["Health"] >= 0:
        playerAtkChoice = str.upper(input("Attack(A), Defend(D), Run(R), Stats(S), Help(H): "))

        if playerAtkChoice == "A":
            playerDamage = playerData["Stats"]["Attack"] + playerData["EquippedItems"]["Weapon"][2]

            enemyProperties["Stats"]["Health"] -= playerDamage # hit enemy 
    
            if enemyProperties["Stats"]["Attack"] <= playerData["Stats"]["Defence"]:
                playerData["Stats"]["Health"] -= 1

                print("You did:", playerDamage, "damage to the enemy, but the enemy did 1 damage to you!")
                print("Your new health is:", playerData["Stats"]["Health"], "the enemies health is:", enemyProperties["Stats"]["Health"])
                
            else:
                print("noob") # enemy hit player
                
        elif playerAtkChoice == "D":
            print("Player Defended!")
            stun = random.randint(0, 100)
            
            if stun >= stunChance:
                print("You dodged the enemy!")
        
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

            if dropRandNum >= 50: 
                dropSelected = random.choice(list(enemyProperties["Drops"].keys()))

                print("You aquired: ", dropSelected)
                gameLoop()
                break
            else:
                print("no drops :(")
                gameLoop()
                break
            

print("Welcome to TERRA, the home of the gods.\nThis is a simple text based rpg.")
playerName = str(input("Please enter your name: "))
playerData["PlayerName"] = playerName
print("Welcome", playerData["PlayerName"])

gameLoop()