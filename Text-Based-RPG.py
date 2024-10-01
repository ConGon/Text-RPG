import math, random, copy

#NEED TO FIX SELLING, NEED TO CHECK IF SLOT IS EMPTY


#After killing a miniboss, new enemies appear

#How much players can allocate to skills when they level up
levelUpStats = 5

defaultHealth = 100
questStep = 25

plrAttributePoints = 0
deathCounter = 0
enemiesKilled = 0
itemsCollected = 0

maxStunChance = 65
maxRunChance = 85
randomEventChance = 40

enemyStunned = False
firstStep = True
traderMenu = False

trader1 = 5
trader2 = 10
goblinLordEncounter = 15
trader3 = 25
darkSorcererEncounter = 30
trader4 = 35
stoneGolemEncounter = 40
trader5 = 45
dragonEncounter = 50
trader6 = 55
demonLordEncounter = 60
trader7 = 85
ApollyonEncounter = 100

# MARK: PLAYER DATA
playerData = {
    "Stats":{
        "Health": 1000000,
        "Attack": 50000,
        "Defence": 1, 
        "Agility": 5,
        "Level": 0,
        "Exp": 0,
        "Gold": 100000000000
    },

# full inventory for testing
    # "Inventory":{
    #     "Slot0": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot1": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot2": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot3": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot4": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot5": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot6": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot7": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot8": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot9": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot10": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot10": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot11": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot12": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot13": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot14": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot15": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot16": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot17": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot18": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot19": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot20": ("Bruised Iron Leggings", "Legs", 5),
    # },

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
        "Slot10": None,
        "Slot11": None,
        "Slot12": None,
        "Slot13": None,
        "Slot14": None,
        "Slot15": None,
        "Slot16": None,
        "Slot17": None,
        "Slot18": None,
        "Slot19": None,
        "Slot20": None,
    },

    "EquippedItems":{
        "Weapon": None,
        "Shield": None,
        "Head": None,
        "Chest": None,
        "Arms": None,
        "Hands": None,
        "Legs": None,
        "Feet": None
    }
}

#HIGHSCORE: YOU MANAGED TO GET 20 QUEST STEPS

#IDEA FOR SHOP
#Create a table for all the items, and their price
#When you want to sell an item, loop through the items
#in the player's table and check which items they have.
#Then, display the prices of the items they posess.

#IDEA FOR ARMOR
#Divide the player's armor value into half
#Take one half of it, and generate a random number between 0 and half of players armor.
#And thats how much armor the player has that turn.

levelData = {
    "0": 100,
    "1": 200,
    "2": 350,
    "3": 550,
    "4": 800,
    "5": 1150,
    "6": 1550, 
    "7": 2100,
    "8": 2750,
    "9": 3500,
    "10": 4400,
    "11": 5400,
    "12": 6550,
    "13": 7850,
    "14": 9300,
    "15": 11000,
    "16": 12800,
    "17": 14750,
    "18": 16850,
    "19": 19100,
    "20": 21500,
    "21": 24050,
    "22": 26750,
    "23": 29600,
    "24": 32600,
    "25": 35750,
    "26": 39050,
    "27": 42500,
    "28": 46100,
    "29": 49850,
    "30": 53750,
    "31": 57800,
    "32": 62000,
    "33": 66350,
    "34": 70850,
    "35": 75500,
    "36": 80300,
    "37": 85250,
    "38": 90350,
    "39": 95600,
    "40": 101000,
    "41": 106550,
    "42": 112250,
    "43": 118100,
    "44": 124100,
    "45": 130250,
    "46": 136550,
    "47": 143000,
    "48": 149600,
    "49": 156350,
    "50": 163250,
    "51": 170300,
    "52": 177500,
    "53": 184850,
    "54": 192350,
    "55": 200000,
    "56": 207800,
    "57": 215750,
    "58": 223850,
    "59": 232100,
    "60": 240500,
    "61": 249050,
    "62": 257750,
    "63": 266600,
    "64": 275600,
    "65": 284750,
    "66": 294050,
    "67": 303500,
    "68": 313100,
    "69": 322850,
    "70": 332750,
    "71": 342800,
    "72": 353000,
    "73": 363350,
    "74": 373850,
    "75": 384500,
    "76": 395300,
    "77": 406250,
    "78": 417350,
    "79": 428600,
    "80": 440000,
    "81": 451550,
    "82": 463250,
    "83": 475100,
    "84": 487100,
    "85": 499250,
    "86": 511550,
    "87": 524000,
    "88": 536600,
    "89": 549350,
    "90": 562250,
    "91": 575300,
    "92": 588500,
    "93": 601850,
    "94": 615350,
    "95": 629000,
    "96": 642800,
    "97": 656750,
    "98": 670850,
    "99": 685100
}

#Trader appears 7 times

# Template "": ("", "", )


#  "Armor": {
            
#         },

#         "Weapons": {
            
#         },

#         "Shields": {
            
#         }
# MARK: TRADER GOODS

traderGoods = {
    "traderGoods1": {
        "Armors": {
            "Clothen Cap": ("Clothen Cap", "Head", 7),
            "Clothen Gambeson": ("Clothen Gambeson", "Chest", 15),
            "Clothen Bracers": ("Clothen Bracers", "Arms", 5),
            "Clothen Gloves": ("Clothen Gloves", "Hands", 4),
            "Clothen Leggings": ("Clothen Leggings", "Legs", 10),
            "Clothen Boots": ("Clothen Boots", "Feet", 3),
            "Ruined Steel Helm": ("Ruined Steel Helm", "Head", 10),
            "Ruined Hauberk": ("Ruined Hauberk", "Chest", 25)
        },

        "Weapons": {
            "Straight Sword": ("Straight Sword", "Weapon", 12),
        },

        "Shields": {
            "Reinforced Wooden Shield": ("Reinforced Wooden Shield", "Shield", 6),
            "Ancient Iron Shield": ("Ancient Iron Shield", "Shield", 10)
        }
    },
    
    "traderGoods2": {
        "Armors": {
            "Cheap Chainmail Cap": ("Cheap Chainmail Cap", "Head", 10),
            "Cheap Chainmail Shirt": ("Cheap Chainmail Shirt", "Chest", 20),
            "Cheap Chainmail Vambraces": ("Cheap Chainmail Vambraces", "Arms", 7),
            "Cheap Chainmail Mittens": ("Cheap Chainmail Mittens", "Hands", 6),
            "Cheap Chainmail Leggings": ("Cheap Chainmail Leggings", "Legs", 13),
            "Cheap Chainmail Socks": ("Cheap Chainmail Socks", "Feet", 5),
        },

        "Weapons": {
            "Zweihander": ("Zweihander", "Weapon", 20),
            "Highland Sword": ("Highland Sword", "Weapon", 15),
            "Soldiers Spear": ("Soldiers Spear", "Weapon", 16),
        },

        "Shields": {
            "Steel Buckler": ("Steel Buckler", "Shield", 12),
            "Viking Shield": ("Viking Shield", "Shield", 15),
        }
    },
    
    "traderGoods3": {
        "Armors": {
            "Iron Plate Helm": ("Iron Plate Helm", "Head", 25),
            "Iron Plate Breastplate": ("Iron Plate Breastplate", "Chest", 40),
            "Iron Plate Pauldrons": ("Iron Plate Pauldrons", "Arms", 15),
            "Iron Plate Gauntlets": ("Iron Plate Gauntlets", "Hands", 10),
            "Iron Plate Chausses": ("Iron Plate Chausses", "Legs", 20),
            "Iron Plate Boots": ("Iron Plate Boots", "Feet", 10),
            "Lordly Plated Helm": ("Lordly Plated Helm", "Head", 35)
        },

        "Weapons": {
            "Scimitar": ("Scimitar", "Weapon", 25),
            "Knights Sword": ("Knights Sword", "Weapon", 30),
            "Steel Pernach": ("Steel Pernach", "Weapon", 28),
            "Blessed Sword": ("Blessed Sword", "Weapon", 40)
        },

        "Shields": {
            "Knights Shield": ("Knights Shield", "Shield", 20),
            "Tower Shield": ("Tower Shield", "Shield", 25),
            "Decorated Shield": ("Decorated Shield", "Shield", 30)
        }
    },
    
    "traderGoods4": {
        "Armors": {
            "Darksteel Plate Helm": ("Darksteel Plate Helm", "Head", 30),
            "Darksteel Plate Breastplate": ("Darksteel Plate Breastplate", "Chest", 50),
            "Darksteel Plate Pauldrons": ("Darksteel Plate Pauldrons", "Arms", 20),
            "Darksteel Plate Gauntlets": ("Darksteel Plate Gauntlets", "Hands", 15),
            "Darksteel Plate Chausses": ("Darksteel Plate Chausses", "Legs", 25),
            "Darksteel Plate Boots": ("Darksteel Plate Boots", "Feet", 12),
            "Helm Of The Fallen Hero": ("Helm Of The Fallen Hero", "Head", 40),
            "Dragonskin Boots": ("Dragonskin Boots", "Feet", 35)
        },

        "Weapons": {
            "Knings Blade": ("Knings Blade", "Weapon", 50),
            "Sword Of Slashing": ("Sword Of Slashing", "Weapon", 40),
            "Damascus Odachi": ("Damascus Odachi", "Weapon", 60),
            "Bane": ("Bane", "Weapon", 45)
        },

        "Shields": {
            "Darksteel Shield": ("Darksteel Shield", "Shield", 30),
            "Shield Of Deflecting": ("Shield Of Deflecting", "Shield", 35)
        }
    },
    
    "traderGoods5": {
        "Armors": {
            "Lordly Enchanted Helm": ("Lordly Enchanted Helm", "Head", 50),
            "Lordly Enchanted Breastplate": ("Lordly Enchanted Breastplate", "Chest", 75),
            "Lordly Enchanted Pauldrons": ("Lordly Enchanted Pauldrons", "Arms", 30),
            "Lordly Enchanted Gauntlets": ("Lordly Enchanted Gauntlets", "Hands", 25),
            "Lordly Enchanted Chausses": ("Lordly Enchanted Chausses", "Legs", 40),
            "Lordly Enchanted Boots": ("Lordly Enchanted Boots", "Feet", 20),
            "Breastplate Of The Hero": ("Breastplate Of The Hero", "Chest", 80)
        },

        "Weapons": {
            "Ginormous Sword": ("Ginormous Sword", "Weapon", 90),
            "Blade Of The Emperor": ("Blade Of The Emperor", "Weapon", 100),
            "Slayer": ("Slayer", "Weapon", 85),
        },

        "Shields": {
            "Ginormous Shield": ("Ginormous Shield", "Shield", 70),
            "Shield Of The Hero": ("Shield Of The Hero", "Shield", 90),
            "Drakon Aspida": ("Drakon Aspida", "Shield", 100)
        }
    },
    
    "traderGoods6": {
        "Armors": {
            "Daimoniki Kefali": ("Daimoniki Kefali", "Head", 70),
            "Daimoniki Thorakisi": ("Daimoniki Thorakisi", "Chest", 100),
            "Daimonika Cheria": ("Daimonika Cheria", "Arms", 40),
            "Daimonika Cheirofilla": ("Daimonika Cheirofilla", "Hands", 30),
            "Daimonika Podia": ("Daimonika Podia", "Legs", 50),
            "Daimonika Pelmata": ("Daimonika Pelmata", "Feet", 25)
        },

        "Weapons": {
            "Sfageio tou Daimona": ("Sfageio tou Daimona", "Weapon", 120),
        },

        "Shields": {
            "Aspida tou Daimonoktonou": ("Aspida tou Daimonoktonou", "Shield", 80)
        }
    },
    
    "traderGoods7": {
        "Armors": {
            "Helm Of The Demigod": ("Helm Of The Demigod", "Head", 120),
            "Chestplate Of The Demigod": ("Chestplate Of The Demigod", "Chest", 150),
            "Pauldrons Of The Demigod": ("Pauldrons Of The Demigod", "Arms", 60),
            "Gauntlets Of The Demigod": ("Gauntlets Of The Demigod", "Hands", 40),
            "Chausses Of The Demigod": ("Chausses Of The Demigod", "Legs", 75),
            "Boots Of The Demigod": ("Boots Of The Demigod", "Feet", 35)
        },

        "Weapons": {
            "Blade Of The Demigod": ("Blade Of The Demigod", "Weapon", 160),
            "Fey Blade": ("Fey Blade", "Weapon", 140),
        },

        "Shields": {
            "Shield Of The Demigod": ("Shield Of The Demigod", "Shield", 100)
        }
    }
}

 #Trader 2
    #Armors
    #Weapons
    #Shields
#MARK: TRADER BUY PRICES
# Template "": ("", "", )
traderBuyPrices = {
    #Trader 1
    #Armors
    "Clothen Cap": 15,
    "Clothen Gambeson": 25,
    "Clothen Bracers": 10,
    "Clothen Gloves": 5,
    "Clothen Leggings": 20,
    "Clothen Boots": 8,
    "Ruined Steel Helm": 50,
    "Ruined Hauberk": 40,

    #Weapons
    "Short Sword": 170,

    #Shields
    "Reinforced Wooden Shield": 25,
    "Ancient Iron Shield": 100,

    # Trader 2
    # Armors
    "Cheap Chainmail Cap": 30,
    "Cheap Chainmail Shirt": 50,
    "Cheap Chainmail Vambraces": 20,
    "Cheap Chainmail Mittens": 15,
    "Cheap Chainmail Leggings": 35,
    "Cheap Chainmail Socks": 10,

    # Weapons
    "Zweihander": 200,
    "Highland Sword": 150,
    "Soldier's Spear": 160,

    # Shields
    "Steel Buckler": 75,
    "Viking Shield": 90,

    # Trader 3
    # Armors
    "Iron Plate Helm": 60,
    "Iron Plate Breastplate": 80,
    "Iron Plate Pauldrons": 45,
    "Iron Plate Gauntlets": 35,
    "Iron Plate Chausses": 55,
    "Iron Plate Boots": 30,
    "Lordly Plated Helm": 90,

    # Weapons
    "Scimitar": 180,
    "Knights Sword": 240,
    "Steel Pernach": 250,
    "Blessed Sword": 350,

    # Shields
    "Knights Shield": 110,
    "Tower Shield": 150,
    "Decorated Shield": 200,

    # Trader 4
    # Armors
    "Darksteel Plate Helm": 80,
    "Darksteel Plate Breastplate": 120,
    "Darksteel Plate Pauldrons": 50,
    "Darksteel Plate Gauntlets": 40,
    "Darksteel Plate Chausses": 60,
    "Darksteel Plate Boots": 35,
    "Helm Of The Fallen Hero": 150,
    "Dragonskin Boots": 170,

    # Weapons
    "Knings Blade": 400,
    "Sword Of Slashing": 350,
    "Damascus Odachi": 450,
    "Bane": 375,

    # Shields
    "Darksteel Shield": 200,
    "Shield Of Deflecting": 250,

    # Trader 5
    # Armors
    "Lordly Enchanted Helm": 200,
    "Lordly Enchanted Breastplate": 300,
    "Lordly Enchanted Pauldrons": 100,
    "Lordly Enchanted Gauntlets": 80,
    "Lordly Enchanted Chausses": 150,
    "Lordly Enchanted Boots": 75,
    "Breastplate Of The Hero": 350,

    # Weapons
    "Ginormous Sword": 500,
    "Blade Of The Emperor": 600,
    "Slayer": 550,

    # Shields
    "Ginormous Shield": 450,
    "Shield Of The Hero": 550,
    "Drakon Aspida": 600,

    # Trader 6
    # Armors
    "Daimoniki Kefali": 350,
    "Daimoniki Thorakisi": 500,
    "Daimonika Cheria": 200,
    "Daimonika Cheirofilla": 150,
    "Daimonika Podia": 250,
    "Daimonika Pelmata": 125,

    # Weapons
    "Sfageio tou Daimona": 700,

    # Shields
    "Aspida tou Daimonoktonou": 500,

    # Trader 7
    # Armors
    "Helm Of The Demigod": 600,
    "Chestplate Of The Demigod": 800,
    "Pauldrons Of The Demigod": 300,
    "Gauntlets Of The Demigod": 200,
    "Chausses Of The Demigod": 400,
    "Boots Of The Demigod": 150,

    # Weapons
    "Blade Of The Demigod": 900,
    "Fey Blade": 850,

    # Shields
    "Shield Of The Demigod": 750,
}



# MARK: SELL PRICES
sellPrices = {
    # Weapons (sorted by damage)
    "Phoenix": 1000000000,
    "Weeping Edge": 13400,
    "Leviathan, Greatsword Of Brimstone": 15450,
    "Mammon, Spear Of The Underworld": 12300,
    "Relic Sword": 5340,
    "Gemstone Greatsword": 6500,
    "Giant Blade": 1000,
    "Blade OF Fire": 550,
    "Ruby Blade": 1500,
    "Poisoned Dagger": 530,
    "Duelist Rapier": 240,
    "Large Iron Rod": 10,
    "Straight Sword": 170,
    "Wind Spear": 250,
    "Thieves Dagger": 75,
    "Bear Claw": 200,
    "Hefty Cleaver": 75,
    "Goblin Sword": 45,
    "Cultist Dagger": 100,
    "Forgotten Sword": 450,
    "Rusty Dagger": 15,
    "Old Stick": 1,
    "Expensive Trinket": 4500,
    "Red Gemstone": 2000,
    "Green Gemstone": 3000,

    # Shields (sorted by defense)
    "Knight's Shield": 650,
    "Golden Shield": 2540,
    "Platinum Buckler": 1900,
    "Steel Buckler": 150,
    "Old Iron Shield": 100,
    "Old Shield": 25,
    "Wooden Buckler": 5,

    # Head (sorted by defense)
    "Doomseer": 7500,
    "Gold Mask": 25000,
    "Horned Helm": 650,
    "Bear Pelt": 500,
    "Platinum Crown": 5000,
    "Ceremonial Hood": 300,
    "Cloth Bandana": 50,
    "Musty Skullcap": 5,

    # Chest (sorted by defense)
    "Seal of Murmur": 13000,
    "Hell Plate": 2500,
    "Ancient Plate Cuirass": 750,
    "Cultist Robe": 500,
    "Assassin Garb": 250,
    "Crude Breastplate": 150,
    "Trader's Garb": 350,
    "Wolf Pelt": 150,
    "Rat Armor": 500,

    # Feet (sorted by defense)
    "Plate Boots": 500,
    "Wisp Walkers": 750,
    "Old Adventurer's Boots": 300,
    "Heavy Iron Boots": 245,
    "Enchanted Boots": 1000,
    "Assassin Slippers": 150,
    "Slimy Boots": 15,
    "Leather Boots": 50,

    # Arms (sorted by defense)
    "Blackened Pauldrons": 545,
    "Leather Pauldrons": 250,
    "Clothen Armguards": 55,
    "White Bracers": 500,
    "Slimy Vambraces": 25,
    "Rusted Iron Vambraces": 35,

    # Legs (sorted by defense)
    "Ancient Plate Leggings": 450,
    "Broken Mail Leggings": 245,
    "Foxenfur Pants": 500,
    "Thieves Leggings": 45,
    "Mail Chausses": 75,
    "Crude Mail Leggings": 25,
    "Boar Pelt": 350,
    "Bruised Iron Leggings": 15,

    # Hands (sorted by defense)
    "Hell Gauntlets": 550,
    "Leather Gloves": 35,
    "Mail Mittens": 85,
    "Strange Gloves": 50,
    "Thieves Gloves": 30,
    "Cloth Gloves": 25,
    "Stinking Gloves": 5,
    # Trader 1
    # Armors
    "Clothen Cap": 8,
    "Clothen Gambeson": 13,
    "Clothen Bracers": 5,
    "Clothen Gloves": 3,
    "Clothen Leggings": 10,
    "Clothen Boots": 4,
    "Ruined Steel Helm": 25,
    "Ruined Hauberk": 20,

    # Weapons
    "Short Sword": 85,

    # Shields
    "Reinforced Wooden Shield": 13,
    "Ancient Iron Shield": 50,

    # Trader 2
    # Armors
    "Cheap Chainmail Cap": 15,
    "Cheap Chainmail Shirt": 25,
    "Cheap Chainmail Vambraces": 10,
    "Cheap Chainmail Mittens": 8,
    "Cheap Chainmail Leggings": 18,
    "Cheap Chainmail Socks": 5,

    # Weapons
    "Zweihander": 100,
    "Highland Sword": 75,
    "Soldier's Spear": 80,

    # Shields
    "Steel Buckler": 38,
    "Viking Shield": 45,

    # Trader 3
    # Armors
    "Iron Plate Helm": 30,
    "Iron Plate Breastplate": 40,
    "Iron Plate Pauldrons": 23,
    "Iron Plate Gauntlets": 18,
    "Iron Plate Chausses": 28,
    "Iron Plate Boots": 15,
    "Lordly Plated Helm": 45,

    # Weapons
    "Scimitar": 90,
    "Knights Sword": 120,
    "Steel Pernach": 125,
    "Blessed Sword": 175,

    # Shields
    "Knights Shield": 55,
    "Tower Shield": 75,
    "Decorated Shield": 100,

    # Trader 4
    # Armors
    "Darksteel Plate Helm": 40,
    "Darksteel Plate Breastplate": 60,
    "Darksteel Plate Pauldrons": 25,
    "Darksteel Plate Gauntlets": 20,
    "Darksteel Plate Chausses": 30,
    "Darksteel Plate Boots": 18,
    "Helm Of The Fallen Hero": 75,
    "Dragonskin Boots": 85,

    # Weapons
    "Knings Blade": 200,
    "Sword Of Slashing": 175,
    "Damascus Odachi": 225,
    "Bane": 188,

    # Shields
    "Darksteel Shield": 100,
    "Shield Of Deflecting": 125,

    # Trader 5
    # Armors
    "Lordly Enchanted Helm": 100,
    "Lordly Enchanted Breastplate": 150,
    "Lordly Enchanted Pauldrons": 50,
    "Lordly Enchanted Gauntlets": 40,
    "Lordly Enchanted Chausses": 75,
    "Lordly Enchanted Boots": 38,
    "Breastplate Of The Hero": 175,

    # Weapons
    "Ginormous Sword": 250,
    "Blade Of The Emperor": 300,
    "Slayer": 275,

    # Shields
    "Ginormous Shield": 225,
    "Shield Of The Hero": 275,
    "Drakon Aspida": 300,

    # Trader 6
    # Armors
    "Daimoniki Kefali": 175,
    "Daimoniki Thorakisi": 250,
    "Daimonika Cheria": 100,
    "Daimonika Cheirofilla": 75,
    "Daimonika Podia": 125,
    "Daimonika Pelmata": 63,

    # Weapons
    "Sfageio tou Daimona": 350,

    # Shields
    "Aspida tou Daimonoktonou": 250,

    # Trader 7
    # Armors
    "Helm Of The Demigod": 300,
    "Chestplate Of The Demigod": 400,
    "Pauldrons Of The Demigod": 150,
    "Gauntlets Of The Demigod": 100,
    "Chausses Of The Demigod": 200,
    "Boots Of The Demigod": 75,

    # Weapons
    "Blade Of The Demigod": 450,
    "Fey Blade": 425,

    # Shields
    "Shield Of The Demigod": 375,
}
#Merchant can sell armor and weapons, potions and even information.
#You can also sell your gear to the merchant

#MARK: FINAL BOSSES
finalBosses = {
    "Demon Lord": {
        "Stats":{
            "Health": 5000,
            "Attack": 45,
            "Agility": 95,
            "ExpValue": 75000

        },
        "Drops":{
            "Mammon, Spear Of The Underworld": ("Mammon, Spear Of The Underworld", "Weapon", 120),
            "Leviathan, Greatsword Of Brimstone": ("Leviathan, Greatsword Of Brimstone", "Weapon", 150),
            "Weeping Edge": ("Weeping Edge", "Weapon", 135),
            "Doomseer": ("Doomseer", "Head", 130),
            "Seal of Murmur": ("Seal of Murmur", "Chest", 150)
        
        },

        "DefaultHealth": 5000,

        "DropChance": 90
    },

      "Apollyon, Avatar Of Pride": {
        "Stats":{
            "Health": 20000,
            "Attack": 1000,
            "Agility": 95,
            "ExpValue": 75000

        },
        "Drops":{
           "Phoenix": ("Phoenix", "Weapon", 1000)
        },

        "DefaultHealth": 5000,

        "DropChance": 90
    },

}

#MARK: MINIBOSSES
miniBosses = {
    "Goblin Lord": {
        "Stats":{
            "Health": 200,
            "Attack": 30,
            "Agility": 75,
            "ExpValue": 3500

        },

        "Drops":{
            "Sword Of The Goblin": ("Sword Of The Goblin", "Weapon", 25),
            "Darksteel Warhammer": ("Darksteel Warhammer", "Weapon", 30)
        },

        "DefaultHealth": 200,

        "DropChance": 90

    },

    "Dark Sorcerer": {
        "Stats":{
            "Health": 350,
            "Attack": 45,
            "Agility": 60,
            "ExpValue": 7500

        },

        "Drops":{
            "Staff Of Onyx": ("Staff Of Onyx", "Weapon", 45),
            "Blade Of Night": ("Blade Of Night", "Weapon", 50)
        },

        "DefaultHealth": 350,

        "DropChance": 85

    },

    "Stone Golem": {
        "Stats":{
            "Health": 1000,
            "Attack": 25,
            "Agility": 30,
            "ExpValue": 17500

        },

        "Drops":{
            "Windcrest Scimitar": ("Windcrest Scimitar", "Weapon", 55),
            "Hero's Sword": ("Hero's Sword", "Weapon", 50),
            "Dragonslayer": ("Dragonslayer", "Weapon", 70)
        },

        "DefaultHealth": 1000,

        "DropChance": 70

    },

    "Dragon": {
        "Stats":{
            "Health": 750,
            "Attack": 75,
            "Agility": 75,
            "ExpValue": 45000

        },
        "Drops":{
            "Azi-Dahakha": ("Azi-Dahakha", "Weapon", 75),
            "Drained Blade": ("Drained Blade", "Weapon", 0),
            "Great Aegis": ("Great Aegis", "Shield", 50),
            "Blessed Helm": ("Blessed Helm", "Head", 65)
        },

        "DefaultHealth": 750,

        "DropChance": 85

    },
   
}

# MARK: ENEMIES
enemies = {
    
    "Slime": {
            "Stats":{
                "Health": 20,
                "Attack": 2,
                "Agility": 3,
                "ExpValue": 10
            },

            "Drops":{
                "Forgotten Sword": ("Forgotten Sword", "Weapon", 23),
                "Slimy Boots": ("Slimy Boots", "Feet", 8),
                "Slimy Vambraces": ("limy Vambraces", "Arms", 10)
                
            },

            "DefaultHealth": 20,

            "DropChance": 35
        },

    "Wild Boar": {
            "Stats":{
                "Health": 40,
                "Attack": 7,
                "Agility": 6,
                "ExpValue": 30
            },

            "Drops":{
                "Boar Pelt": ("Boar Pelt", "Legs", 7)
            },

            "DefaultHealth": 40,

            "DropChance": 45
        },

    "Wolf": {
            "Stats":{
                "Health": 50,
                "Attack": 10,
                "Agility": 10,
                "ExpValue": 65
            },

            "Drops":{
                "Wolf Pelt": ("Wolf Pelt", "Chest", 6)
            },

            "DefaultHealth": 50,

            "DropChance": 40
        },

    "Giant Rat": {
        "Stats":{
            "Health": 65,
            "Attack": 12,
            "Agility": 7,
            "ExpValue": 100
        },

        "Drops":{
            "Rat Armor": ("Rat Armor", "Chest", 1),
            "Stinking Gloves": ("Stinking Gloves", "Hands", 2),
            "Forgotten Blade": ("Forgotten Blade", "Weapon", 35)
        },

        "DefaultHealth": 65,

        "DropChance": 25
    },

    "Bandit": {
        "Stats":{
            "Health": 75,
            "Attack": 17,
            "Agility": 15,
            "ExpValue": 135
        },

        "Drops":{
            "Steel Dagger": ("Steel Dagger", "Weapon", 15),
            "Cloth Bandana": ("Cloth Bandana", "Head", 3),
            "Leather Boots": ("Leather Boots", "Feet", 3)

        },

        "DefaultHealth": 75,

        "DropChance": 65
    },

    "Skeleton warrior": {
        "Stats":{
            "Health": 100,
            "Attack": 15,
            "Agility": 5,
            "ExpValue": 175
        },

        "Drops":{
            "Bruised Iron Leggings": ("Bruised Iron Leggings", "Legs", 5),
            "Battered Iron Helm": ("Battered Iron Helm", "Head", 5),
            "Rusted Iron Vambraces": ("Rusted Iron Vambraces", "Arms", 5)
        },

        "DefaultHealth": 100,

        "DropChance": 65
    },


    "Imp": {
        "Stats":{
            "Health": 50,
            "Attack": 20,
            "Agility": 10,
            "ExpValue": 300
        },

        "Drops":{
            "Blade OF Fire": ("Blade OF Fire", "Weapon", 25)
        },

        "DefaultHealth": 50,

        "DropChance": 45
    },

    "Bear": {
        "Stats":{
            "Health": 135,
            "Attack": 13,
            "Agility": 4,
            "ExpValue": 345
        },

        "Drops":{
            "Bear Pelt": ("Bear Pelt", "Head", 15),
            "Bear Claw": ("Bear Claw", "Weapon", 15)
        },

        "DefaultHealth": 135,

        "DropChance": 75
    },

    "Orc": {
        "Stats":{
            "Health": 120,
            "Attack": 20,
            "Agility": 3,
            "ExpValue": 450
        },

        "Drops":{
            "Hefty Cleaver": ("Hefty Cleaver", "Weapon", 15),
            "Crude Breastplate": ("Crude Breastplate", "Chest", 10),
            "Crude Mail Vambraces": ("Crude Mail Vambraces", "Arms", 10),
            "Crude Mail Gauntlets": ("Crude Mail Gauntlets", "Hands", 10),
            "Crude Mail Leggings": ("Crude Mail Leggings", "Legs", 10),
            "Crude Mail Boots": ("Crude Mail Boots", "Feet", 10)        
        },

        "DefaultHealth": 100,

        "DropChance": 65
    },

    "Devil Cultist": {
        "Stats":{
            "Health": 95,
            "Attack": 28,
            "Agility": 15,
            "ExpValue": 510
        },

        "Drops":{
            "Cultist Dagger": ("Cultist Dagger", "Weapon", 10),
            "Cultist Robe": ("Cultist Robe", "Chest", 16),
            "Ceremonial Hood": ("Ceremonial Hood", "Head", 10),
            "Strange Gloves": ("Strange Gloves", "Hands", 7),
            "Enchanted Boots": ("Enchanted Boots", "Feet", 25)
        },

        "DefaultHealth": 95,

        "DropChance": 65
    },

    "Wandering Duelist": {
        "Stats":{
            "Health": 110,
            "Attack": 20,
            "Agility": 20,
            "ExpValue": 550
        },

        "Drops":{
            "Duelist Rapier": ("Duelist Rapier", "Weapon", 18),
            "Cloth Gambeson": ("Cloth Gambeson", "Chest", 5),
            "Posh Hat": ("Posh Hat", "Head", 3)
        },

        "DefaultHealth": 110,

        "DropChance": 75
    },

    "Strange Mercenary": {
        "Stats":{
            "Health": 150,
            "Attack": 15,
            "Agility": 10,
            "ExpValue": 625
        },

        "Drops":{
            "Straight Sword": ("Straight Sword", "Weapon", 17),
            "Steel Buckler": ("Steel Buckler", "Shield", 10),
            "Mail Helm": ("Mail Helm", "Head", 8),
            "Mail Shirt": ("Mail Shirt", "Chest", 15),
            "Mail Vambraces": ("Mail Vambraces", "Arms", 8),
            "Mail Mittens": ("Mail Mittens", "Hands", 17),
            "Mail Chausses": ("Mail Chausses", "Legs", 13)
        },

        "DefaultHealth": 150,

        "DropChance": 85
    }, 

    "Troll": {
        "Stats":{
            "Health": 300,
            "Attack": 10,
            "Agility": 1,
            "ExpValue": 1300
        },

        "Drops":{
            "Giant Blade": ("Giant Blade", "Weapon", 25),
            "Horned Helm": ("Horned Helm", "Head", 20)
        },

        "DefaultHealth": 300,

        "DropChance": 65
    },

    "Mimic": {
        "Stats":{
            "Health": 65,
            "Attack": 40,
            "Agility": 4,
            "ExpValue": 2321
        },

        "Drops":{
            "Ruby Blade": ("Ruby Blade", "Weapon", 20),
            "Gemstone Greatsword": ("Gemstone Greatsword", "Weapon", 30),
            "Relic Sword": ("Relic Sword", "Weapon", 60),
            "Golden Shield": ("Golden Shield", "Shield", 25),
            "Platinum Crown": ("Platinum Crown", "Head", 15)
        },

        "DefaultHealth": 65,

        "DropChance": 45
    },

    "Demon": {
        "Stats":{
            "Health": 250,
            "Attack": 23,
            "Agility": 7,
            "ExpValue": 2540
        },

        "Drops":{
            "Runed Longsword": ("Runed Longsword", "Weapon", 30),
            "Runed Shield":  ("Runed Shield", "Shield", 30),
            "Hell Helm,": ("Hell Helm", "Head", 30),
            "Hell Gauntlets": ("Hell Gauntlets", "Hands", 30),
            "Hell Plate": ("Hell Plate", "Chest", 35)
        },

        "DefaultHealth": 250,

        "DropChance": 75
},
    
}

#MARK: RANDOM EVENTS
randomEvents = {
 
"AncientStatue":{
    "Stats":{
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        "Gold": 0,
        "Exp": 55
        },

    "Drops": None,
    "HealthRestore": True,

    "EventDescription": 

"""You stumble upon an ancient statue, and 
you notice various ancient symbols. The statue begins to glow, and
you feel as though you were healed of all injury. You continue your quest."""
},
 
"TreasureChest":{
    "Stats":{
        "Exp": 60,
        "Gold": 545,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": {"Platinum Buckler": ("Platinum Buckler", "Shield", 20)},
    "HealthRestore": False,

    "EventDescription": 
    
"""You find A chest full of gold and plunder! It was laying in plain sight,
pretty strange that someone would leave it unattended. You loot it's treasure regardless."""
},

"RottenCorpse":{
    "Stats":{
        "Exp": 20,
        "Gold": 150,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""You spot a filthy, rotting corpse along the path,
you take what you can find from it, as they won't
be needing it anymore..."""
},

"GoldenMask":{
    "Stats":{
        "Exp": 500,
        "Gold": 250,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": {"Gold Mask": ("Gold Mask", "Head", 65)},
    "HealthRestore": False,

    "EventDescription": 
    
"""A glint of light blinds you for a moment,
you glance in the direction the light came from.
You walk towards it and it leads you to a innocuous tree,
but upon closer inspection, on it's trunk you see what looks
like an opening, big enough for a hand to fit. You reach inside
and feel a metal object, soon you realise what you reached inside of
is an ancient compartment built into the tree. You rip the front
off of the compartment and within is a Golden Mask! You take it and 
continue on your journey."""
},

"RuinedCaravan":{
    "Stats":{
        "Exp": 100,
        "Gold": 250,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": {"Trader's Garb": ("Trader's Garb", "Chest", 6)},
    "HealthRestore": False,

    "EventDescription": 
    
"""You are travelling along the road, and notice a paticularly dense
patch of forest. You cautiously move forward, not long before
noticing the remains of what was once a caravan. You scan 
the area for bandits or other malevolant creatures, and determine
that there is nothing lingering or waiting in ambush. You find various
things that unwise brigands left behind."""
},
     
"BattlefieldRemains":{
    "Stats":{
        "Exp": 100,
        "Gold": 50,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": {"Knight's Shield": ("Knight's Shield", "Shield", 30)},
    "HealthRestore": False,

    "EventDescription": 
    
"""A disgusting smell enters your nostrils, death.
you cautiously walk forward, and trough a clearing in
the forest, you spot what looks like the remains of a small
skirmish. You look for movement, but all that remain are dead men.
You scour the battlefeild, and you find a decent knight's Shield!"""
},
    
"CharredRemains":{
    "Stats":{
        "Exp": 10,
        "Gold": 5,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""You spot a small plume of smoke close by, so you take some time to investigate.
Eventually you spot it, the charred remains of what was once human. You pilfer
whatever was left of the remains, and return to the road ahead"""
},
    
"FriendlyTraveller":{
    "Stats":{
        "Exp": 100,
        "Gold": 0,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""You come across an old man walking along the same path as you.
You greet him and he shares his various stories from his youth.
He gives you advise of the road ahead."""
},
     
"CultistSigil":{
    "Stats":{
        "Exp": 750,
        "Gold": 0,
        "Attack": 5,
        "Defence": 1,
        "Agility": 1,
        },

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""In the distance you spot a red glow. You wearily approach it,
and notice it's coming from inside of a shallow cave. You cautiously
move inside and see a red glowing symbol on the ground. The mark of
silence, an evil and malevolant symbol. The symbol flashes red, then
dissapears, but you feel as though you have become stronger."""
},
       
"StrangeGlowing":{
    "Stats":{
        "Exp": 250,
        "Gold": 1000,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": {"Red Gemstone": ("Red Gemstone", "Weapon", 1)},
    "HealthRestore": False,

    "EventDescription": 
    
"""After a long day of travelling, you set up camp along a secluded cove.
A beautiful river runs through the middle of a clearing, it is the perfect
place for rest. You soon fall asleep in your makeshift shelter. Suddenly, you
awake, A bad dream. It is still pitch black, and you try to go back to sleep but
not too far in the distance, a strange glow catches your eye. You quickly arm yourself
and investigate. You slowly and silently inch closer to the glowing, now meters away from it.
You can see it, a bright red gemstone, a thing sure to be valuable. You let out a sigh of relief
and go back to your camp, where you sleep the night away."""
},
        
"CrazedMan":{
    "Stats":{
        "Exp": 0,
        "Gold": 0,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""You notice a man sitting in the road, talking to himself.
As you approach, his ramblings become more clear, it is a man
who lost his mind. He speaks of a sybol, or seal as he called it,
and a calamity that would soon take place. He told you to beware 
of the Phoenix. You distance yourself from the man and continue your travels."""
},
    
"EvilPresence":{
    "Stats":{
        "Exp": 0,
        "Gold": 0,
        "Attack": 0,
        "Defence": 0,
        "Agility": 1,
        },

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""All your hairs stand on end, and your heart stops for a moment. 
Fear is all you feel, and you cannot move. You sense a great evil
nearby, one that terrifies you. But soon enough, the feeling vanishes,
and you wearily contiune walking along the road."""
},

"SwordInStone":{
    "Stats":{
        "Exp": 1000,
        "Gold": 0,
        "Attack": 2,
        "Defence": 2,
        "Agility": 2,
        },

    "Drops": {"Legendary Sword": ("Legendary Sword", "Weapon", 50)},
    "HealthRestore": False,

    "EventDescription": 
    
"""A ray of light shines upon a large boulder. You make your way towards
it. You walk closer then you notice it, a beautiful sword, lodged into the rock.
You take both hands and grab the handle of the sword, and pull as hard as you can.
The sword doesn't budge, but eventually, it gets looser, and soon, with one final
pull, out it popped! You inspect it, and it is a fine blade indeed. Engraved in
symbols you have never seen, this could've been the sword of a hero!"""
},

"RuinedCastle":{
    "Stats":{
        "Exp": 125,
        "Gold": 25,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": {"Wind Spear": ("Wind Spear", "Weapon", 15)},
    "HealthRestore": False,

    "EventDescription": 
    
"""As you are travelling along the road, you come across ruined castle.
You search it's halls and dungeons, and take what you can find. Eventually,
you happen upon the armory, and find various old weapons and armor, but
only one weapon looked like it was worth taking."""
},
 
"GodlyRays":{
    "Stats":{
        "Exp": 3500,
        "Gold": 0,
        "Attack": 20,
        "Defence": 20,
        "Agility": 20,
        },

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""From the sky shine beautiful rays of gold. You look up and see it,
a rare phenomenon of the land: 'Godly Rays'. A thing spoke of in famous
tales, that rays of gold will shine upon who that will vanquish all evil
and save the world. Power surges through your veins, you feel like you can
do anything. Are the stories true?"""
},

"RejuvinatingPool":{
    "Stats":{
        "Exp": 300,
        "Gold": 0,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": None,
    "HealthRestore": True,

    "EventDescription": 
    
"""Along the road, you see a clearing. You make your way towards it.
As you walk closer you can see a lake, but moving closer to it,
you notice a small pond of water, water that almost looks like it
is glowing. You set aside your equipment and bathe in the waters.
You feel as though your wounds have completely healed."""
},

"BeautifulWaterfall":{
    "Stats":{
        "Exp": 300,
        "Gold": 0,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""The things you have seen and the creatures and men you have killed
begin to weigh on your mind, but you keep walking along the road.
Eventually you spot a river, and follow it upstream. Soon, you come 
across a beautiful waterfall, and try to meditate to relieve your soul.
Eventually you pick up and begin heading forward, to continue your journey."""
},
    
"AdventurersBackpack":{
    "Stats":{
        "Exp": 0,
        "Gold": 55,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""Along the path, you notice a backpack. You open itis look at whats inside.
From it's contents you surmise that this is the backpack of an adventurer, 
likely close by. Nonetheless, you take what you wanted and contiune your trek..."""
},

"PotionTester":{
    "Stats":{
        "Exp": 650,
        "Gold": 0,
        "Attack": 10,
        "Defence": 5,
        "Agility": 15,
        },

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""You can see strange looking man walking towards you.
He has many potions strapped to his belt and pack,
and alchemical tools line the inside of his coat.
He asks if you can try one of his potions, as he claims
he is a famous alchemist from the empire. You indulge him,
and feel as though the potion not only healed you, but made you
stronger and faster! You tell him and he is suprised to hear it.
Nonetheless, you and him part ways, but the warnings he gave you
of the road ahead make you a little more cautious."""
},

"SuspiciousBoulder":{
    "Stats":{
        "Exp": 200,
        "Gold": 500,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""Ahead of you, you notice a oddly shaped bouler, Almost unnatural. 
You move to investigate it, and Upon further inspection, the boudler 
doesn't look like a boulder at all! You tap it with the tip of your blade,
and low and behold, a small creature crawls out from under it. He repremands
you for disturbing his sleep, and throws a bag of gold on the ground and crawls
back into what now you believe to be his home. You take the gold and continue on your journey."""
},

"PathSplit":{
    "Stats":{
        "Exp": 0,
        "Gold": 0,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""The path splits into 2, so you decide to take the left path.
You hope you made the right desicion..."""
},
  
"OldHelmet":{
    "Stats":{
        "Exp": 50,
        "Gold": 0,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": {"Horned Helm": ("Horned Helm", "Head", 20)},
    "HealthRestore": False,

    "EventDescription": 
    
"""You are about to cross a bridge when you notice a slight glint
from under it. You walk under the bridge and examine the source of the glint.
A horned helm! It's not the greatest helmet but at least it's not a troll..."""

},

"AncientArtifact":{
    "Stats":{
        "Exp": 15000,
        "Gold": 0,
        "Attack": 100,
        "Defence": 50,
        "Agility": 50,
        },

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""You happen upon what appears to be a library of some sort,
disguised as a small hill. But it has long since decayed and
crumbled under its own weight, making the disguise ineffective.
You search for any surviving tomes or scrolls, but fail to find anything
of note. Just as you're about to leave the ruins, you notice on a decayed
shelf: An ancient artifact, a thing of pure beauty. It is a levitating onyx jewel
inside of a crystal ball. It is small enough to fit in your pocket, but the
more you ponder it, the larger it seems to become. In a flash of light, 
you feel it: Power surging throughout your entire body! You have become 
the vessel of something ancient, something powerful."""
},

"Skeleton":{
    "Stats":{
        "Exp": 30,
        "Gold": 0,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": {"Old shield": ("Old shield", "Shield", 8)},
    "HealthRestore": False,

    "EventDescription": 
    
"""You notice bones scattered across the ground. Upon farthur
inspection, you realise these are human remains, ancient and
decayed. But, on the ground you see an old shield!
Finders keepers!"""
},

"LoudScreech":{
    "Stats":{
        "Exp": 0,
        "Gold": 0,
        "Attack": 0,
        "Defence": 0,
        "Agility": 1,
        },

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""A loud screech fills your ears, a foul sound that puts you on edge.
You hide and anticipate an attack, but only silence rings throughout
the vast forest. You make haste to continue along the path."""
},

"Village":{
    "Stats":{
        "Exp": 550,
        "Gold": 1,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": {"Old Stick": ("Old Stick", "Weapon", 2)},
    "HealthRestore": False,

    "EventDescription": 
    
"""Along your travels, you spot a village in the distance. 
Mules and horses pulling wagons of hay, cabbages and produce from their farms,
men and women walking about, and the fresh smell of bread and soup, things that are
a very welcome sight. You say hello to the locals, and they offer you various gifts.
Soon, you continue on your journey."""
},

"StormyWeather":{
    "Stats":{
        "Exp": 100,
        "Gold": 0,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""As you walk, it begins to rain, and from rain, thunder. You seek shelter
under a nearby cliff, the overhang giving you decent coverage from the rain.
After many hours, you continue your journey."""
},
  
"AncientArmor":{
    "Stats":{
        "Exp": 200,
        "Gold": 0,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": {"Ancient Plate Cuirass": ("Ancient Plate Cuirass", "Chest", 20)},
    "HealthRestore": False,

    "EventDescription": 
    
"""You tire from many days travel, and so you seek out shelter to rest.
You spot a shaded meadow, with trees surrounding it. You lay against a tree and
look through your baggage. Many hours pass and you pick yourself up and continue,
but as you get up, you notice an ancient Plate Cuirass, lying in the grass
beside you. Suprised that you didn't see it before, you inspect it. Though it is old,
it is full plate, and will provide great protection from the dangers to come."""
},

"BandOfAdventurers":{
    "Stats":{
        "Exp": 550,
        "Gold": 0,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""A man taps you on your shoulder, a dwarf assasin from the far reaches of the world.
With a relieved look on his face, he asks you to join his group around their bonfire and lodgings.
They share with you their stories of adventure and pass around rum, forest forage and nuts.
After a long Friendly conversation with the five adventurers, you return to your journey."""
},

"SmallCave":{
    "Stats":{
        "Exp": 250,
        "Gold": 5000,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": {"Expensive Trinket": ("Expensive Trinket", "Weapon", 1)},
    "HealthRestore": False,

    "EventDescription": 
    
"""You stumble upon a small cave, within it: A golden chest!
ancient trinkets and baubles fill your vision, You're rich!
You fill your pack with as much gold and trinkets that your pack
can carry."""
},

"GoblinHorde":{
    "Stats":{
        "Exp": 250,
        "Gold": 500,
        "Attack": 0,
        "Defence": 0,
        "Agility": 0,
        },

    "Drops": {"Green Gemstone": ("Green Gemstone", "Weapon", 1)},
    "HealthRestore": False,

    "EventDescription": 
    
"""You notice a goblin horde walking along a path, you hide, 
and when they are long out of your sight, you notice a gemstone one of them dropped.
You quickly snatch it and continue on your way."""
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

#MARK: QUEST BEGIN
def questBegin():
    print("")
    print("Welcome to TERRA, the home of the gods.\nThis is a simple text based rpg.\n")
    playerName = str(input("Please enter your name: "))
    playerData["PlayerName"] = playerName
    print("")
    print("Welcome", playerData["PlayerName"])
    print("")
    gameLoop()

#MARK: MAIN GAME LOOP!!!
def gameLoop():
    global questStep, firstStep
    print("Quest Step:", questStep)
    while True:

        if questStep == 0 and firstStep:
            print("It is the first step of your journey, so prepare for it. Take good note of your")
            print("current items, and good luck on your trecherous quest...")
            print("")
            firstStep = False
            
        elif questStep == trader1:
            print("")
            print("Hello adventurer! Would you like to take a look at my wares?")
            print("")
            tradeMenu()
            #shopkeeper function here

        elif questStep == trader2:
            print("Shopkeeper goes here, or a selection of random events specific to each 5 quest steps.")
            tradeMenu()
            #shopkeeper function here

        elif questStep == goblinLordEncounter:
            print("You hear cackling and malicious laughter from behind you")
            combat("Goblin Lord")

        elif questStep == trader3:
            print("Shopkeeper goes here, or a selection of random events specific to each 5 quest steps.")
            tradeMenu()

        elif questStep == darkSorcererEncounter:
            print("Second miniboss here")
            combat("Dark Sorcerer")

        elif questStep == trader4:
            print("Shopkeeper goes here, or a selection of random events specific to each 5 quest steps.")
            tradeMenu()

        elif questStep == stoneGolemEncounter: 
            print("Third miniboss here")
            combat("Stone Golem")

        elif questStep == trader5:
            print("Shopkeeper goes here, or a selection of random events specific to each 5 quest steps.")
            tradeMenu()

        elif questStep == dragonEncounter:
            print("Final miniboss goes here")
            combat("Dragon")

        elif questStep == trader6:
            print("Greetings hero! You should take a look at my wares, as")
            print("I found a suit of divine armor that would be well suited for your task...")
            print("It is Armátoma tou Asymvívastou, or Armor of the Unyielding as it is called in legend.") 
            print("It shall fit a man like you perfectly, as long as you have the coin...")
            tradeMenu()

        elif questStep == demonLordEncounter:
            print("player reached quest step 65, final boss goes here")
            combat("Demon Lord")

        elif questStep == trader7:
            print("Shopkeeper goes here, or a selection of random events specific to each 5 quest steps.")
            tradeMenu()

        elif questStep == ApollyonEncounter:
            print("From the highest reaches of the heavens, a being of unparalleled power descended.")
            print("He pierced the firmament, shattered the skies, and crashed to the earth with a force that shook the world.")
            print("Before you lies a vast crater, the ground torn asunder by the impact.")
            print("The skies above churn with dark energy as a storm of unfathomable fury sweeps across the land.")
            print("You stand firm, knowing this will be your final battle.")
            print("Through the swirling dust and roaring flames, the malevolent figure marched forward.")
            print("As the storm clears, all you know is this: an evil god now stands before you...")

            combat("Apollyon, Avatar Of Pride")

        playerChoice = str.upper(input("Move forward(M) | Equip Menu(E) | Rest(R) | Inventory(I) | Equipped Weapons & Armor(W) | Stats(S) | Help(H): "))
    
        if playerChoice == "M": 
            questStep += 1  
            moveForward()
            break
            
        elif playerChoice == "I":
            print("")
            print("Your Inventory:", playerData["Inventory"])
            print("")

        elif playerChoice == "E":
            print("")
            equipMenu()
            break

        elif playerChoice == "R": 
            rest()  
            break
        
        elif playerChoice == "W":
            print("")
            print("Equipped Items:", playerData["EquippedItems"])
            print("")

        elif playerChoice == "S":
            print("")
            print(playerData["Stats"])
            print("")
            gameLoop()

        elif playerChoice == "H":
            mainHelp()
            break

        else:
            print("")
            print("Invalid input")
            print("")

#MARK: MOVE FORWARD
def moveForward():
    global questStep, defaultHealth, randomEventChance
    enemyOrEvent = random.randint(0, 100)
    
    if enemyOrEvent <= randomEventChance: #Encountered Random Event:

        eventSelected = random.choice(list(randomEvents.keys()))
        eventProperties = randomEvents[eventSelected]
        print("")
        print(eventProperties["EventDescription"])
        print("")
        for stat, statAmount in eventProperties["Stats"].items():

            if statAmount:
                playerData["Stats"][stat] += statAmount
                print("Your", stat, "went up by:", statAmount)

        if eventProperties["HealthRestore"]:
            playerData["Stats"]["Health"] = defaultHealth
            print("restored health")
            
        
        if eventProperties["Drops"] == None:
            print("event has no drops")
            print("")
            levelUp()

        else:
            dropItem = list(eventProperties["Drops"].values())[0]

            for slot, item in playerData["Inventory"].items():
                    
                    if slot == "Slot20" and item != None:
                        print("Inventory Full")
                        print(dropItem)
                        dropItemReplaceInput(dropItem)

                    if item is None:  # Check if the slot is empty
                        print("You aquired:", dropItem)
                        print("")
                        playerData["Inventory"][slot] = dropItem  # Place the item in the slot
                        gameLoop()

    else: #Encountered Enemy
        enemySelected = random.choice(list(enemies.keys()))
        print("")
        print("You encountered a", enemySelected)
        print("")
        combat(enemySelected)

#MARK: COMBAT
def combat(enemySelected):
    global enemyStunned, enemyDamage, maxStunChance, maxRunChance, questStep
    
    if enemySelected in ["Goblin Lord", "Dark Sorcerer", "Stone Golem", "Dragon"]:
        enemyProperties = miniBosses[enemySelected]
        questStep += 1
        print("")
        print("You encountered a", enemySelected)
        print("")

    elif enemySelected in ["Apollyon, Avatar Of Pride", "Demon Lord"]:
        enemyProperties = finalBosses[enemySelected]
        questStep += 1
        print("")
        print("You encountered a", enemySelected)
        print("")


    else:
        enemyProperties = enemies[enemySelected]

    shield = playerData["EquippedItems"].get("Shield")
    stunChance = shield[2] * 2.5 if shield else 1
    runChance = playerData["Stats"]["Agility"] * 3
    runChance -= enemyProperties["Stats"]["Agility"] 

    #Max stun chance is CURRENTLY 65
    if stunChance >= maxStunChance:
        stunChance = maxStunChance

    while playerData["Stats"]["Health"] >= 0:


        playerAtkChoice = str.upper(input("Attack(A) | Defend(D) | Run(R) | Stats(S) | Enemy Stats(E) | Help(H): "))

        if playerAtkChoice == "A":

            if playerData["EquippedItems"]["Weapon"] == None:
                playerDamage = playerData["Stats"]["Attack"]
                enemyProperties["Stats"]["Health"] -= playerDamage # hit enemy 

            else:
                playerDamage = playerData["Stats"]["Attack"] + playerData["EquippedItems"]["Weapon"][2]
                enemyProperties["Stats"]["Health"] -= playerDamage # hit enemy 

            if enemyStunned:
                print("The enemy was stunned, they couldn't attack!")
                print("")
                print("You did", playerDamage ,"damage to the enemy, the enemies health is:", enemyProperties["Stats"]["Health"])
                print("")
                enemyStunned = False

            elif enemyProperties["Stats"]["Attack"] <= playerData["Stats"]["Defence"]:
                playerData["Stats"]["Health"] -= 1
                
                print("")
                print("You did:", playerDamage, "damage to the enemy, but the enemy did 1 damage to you!")
                print("Your new health is:", playerData["Stats"]["Health"], "the enemies health is:", enemyProperties["Stats"]["Health"])
                print("")
            else:
                enemyDamage = enemyProperties["Stats"]["Attack"] - playerData["Stats"]["Defence"] 
                playerData["Stats"]["Health"] -= enemyDamage
                
                print("")
                print("You did:", playerDamage, "damage to the enemy, but the enemy did", enemyDamage, "damage to you!") # enemy hit player
                print("Your new health is:", playerData["Stats"]["Health"], ", the enemies health is:", enemyProperties["Stats"]["Health"])
                print("")
        elif playerAtkChoice == "D": 
            stun = random.randint(0, 100)
            
            if stun <= stunChance:
                enemyStunned = True
                print("")
                print("You dodged the enemy!")
                print("")

            else:
                print("")
                print("You failed to block!")
                if enemyProperties["Stats"]["Attack"] <= playerData["Stats"]["Defence"]:
                    playerData["Stats"]["Health"] -= 1
                    print("")
                    print("the enemy did 1 damage to you!")
                    print("Your new health is:", playerData["Stats"]["Health"], "the enemies health is:", enemyProperties["Stats"]["Health"])
                    print("")

                else:
                    enemyDamage = enemyProperties["Stats"]["Attack"] - playerData["Stats"]["Defence"] 
                    playerData["Stats"]["Health"] -= enemyDamage
                    print("")
                    print("the enemy did", enemyDamage, "damage to you!")
                    print("Your new health is:", playerData["Stats"]["Health"], "the enemies health is:", enemyProperties["Stats"]["Health"])
                    print("")
        
        elif playerAtkChoice == "R":
            run = random.randint(0, 100)

            if runChance <= 0:
                runChance = 1
            
            if run > maxRunChance:
                run = maxRunChance

            if run <= runChance:
                print("You ran from the enemy!")
                gameLoop()

            else:
                print("")
                print("You failed to run from the enemy!")
                enemyDamage = enemyProperties["Stats"]["Attack"] - playerData["Stats"]["Defence"] 
                playerData["Stats"]["Health"] -= enemyDamage
                
                print("")
                print("The enemy did", enemyDamage, "damage to you!") # enemy hit player
                print("Your new health is:", playerData["Stats"]["Health"], ", the enemies health is:", enemyProperties["Stats"]["Health"])
                print("")

        elif playerAtkChoice == "S":
            print("")
            print(playerData["Stats"])
            print("")

        elif playerAtkChoice == "E":
            print("")
            print(enemySelected, "Health:", enemyProperties["Stats"]["Health"], "|", "Attack:", enemyProperties["Stats"]["Attack"], "|", "Agility:", enemyProperties["Stats"]["Agility"] )
            print("")

        elif playerAtkChoice == "H":
            while True:
                helpAttackInput = str.upper(input("Help with: Attack(A) | Defend(D) | Run(R) | Stats(S) | Back(B): "))
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

                elif helpAttackInput == "B":
                    print("")
                    print("You exited help")
                    combat(enemySelected)

                else:
                    print("")
                    print("Invalid input")
                    print("")

        else:
            print("")
            print("Invalid input")
            print("")

        #Death conditions, what happens when a regular enemy vs miniboss vs main boss dies
        if enemyProperties["Stats"]["Health"] <= 0:

            if enemySelected == "Goblin Lord":
                print("You cut the goblin lord down like a dog... VICTORY!!!")

            elif enemySelected == "Dark Sorcerer":
                print("The dark sorcerer's pride went to his head, now he lies dead")

            elif enemySelected == "Stone Golem":
                print("The golem, in an avalanche of rock and boulders, crashes to the ground below")

            elif enemySelected == "Dragon":
                print("With a final strike, you peirce the dragon's scales, straight through it's heart.")

            elif enemySelected == "Demon Lord":
                print("The demon lord wretches on it's own foul blood, \"You will see the grave mistake you've made, just kill me and let this world rot.\" \n You plunge your sword into his heart, and to black mist he faded.")


            elif enemySelected == "Apollyon, Avatar Of Pride": 
                print("'You killed the final boss'")

            # Dragon (Miniboss)

            # Demon Lord (Final Boss)

            # Apollyon, Avatar Of Pride (True Final Boss)

            else:
                print("You defeated the", enemySelected)
                print("")
                playerData["Stats"]["Exp"] += enemyProperties["Stats"]["ExpValue"]
                print("You got:", enemyProperties["Stats"]["ExpValue"], "Exp")
                print("")

            dropRandNum = random.randint(0, 100)

            enemyProperties["Stats"]["Health"] = enemyProperties["DefaultHealth"]

            if dropRandNum <= enemyProperties["DropChance"]: 
                dropSelected = random.choice(list(enemyProperties["Drops"].keys()))
                dropProperties = enemyProperties["Drops"][dropSelected]

                for slot, item in playerData["Inventory"].items():
                    if slot == "Slot20" and item != None:
                        print(enemySelected, "Dropped:", dropProperties)
                        print("")
                        print("But your inventory is full, Replace an item")
                        print("in your inventory With the one you aquired.")
                        print("")
                        dropItemReplaceInput(dropProperties)

                    if item is None:  # Check if the slot is empty
                        print("You aquired:", dropSelected)
                        print("")
                        playerData["Inventory"][slot] = dropProperties  # Place the item in the slot
                        levelUp()

            else:
                levelUp()
                break
        
        if playerData["Stats"]["Health"] <= 0:
            cleanupFunction()
            break

#MARK: LEVEL UP
def levelUp():
    global plrAttributePoints

    while playerData["Stats"]["Exp"] >= levelData[str(playerData["Stats"]["Level"])]:
        playerData["Stats"]["Exp"] -= levelData[str(playerData["Stats"]["Level"])]
        plrAttributePoints += levelUpStats
        playerData["Stats"]["Level"] += 1
        print("You levelled up")

    if plrAttributePoints >= levelUpStats:
        statAllocation()
        
    if playerData["Stats"]["Exp"] <= levelData[str(playerData["Stats"]["Level"])]:
        
        print("Player did not level up")
        gameLoop()

#MARK: STAT ALLOCATION
def statAllocation():
    global plrAttributePoints
    
    while True:
        if plrAttributePoints == 0:
            gameLoop()
            break
        
        print("You have:", plrAttributePoints, "Attribute points to spend")
        print("")
        statAllocationInput = str.upper(input(f"Allocate {levelUpStats} stats to: Attack(ATK) | Defence(DEF) | Agility(AGI): "))

        if statAllocationInput == "ATK":
            playerData["Stats"]["Attack"] += levelUpStats
            print("")
            print("You increased your Attack by", levelUpStats)
            print("")
            plrAttributePoints -= levelUpStats
            
            
        elif statAllocationInput == "DEF":
            playerData["Stats"]["Defence"] += levelUpStats
            print("")
            print("You increased your Defence by", levelUpStats)
            print("")
            plrAttributePoints -= levelUpStats
            
        elif statAllocationInput == "AGI":
            playerData["Stats"]["Agility"] += levelUpStats
            print("")
            print("You increased your Agility by", levelUpStats)
            print("")
            plrAttributePoints -= levelUpStats
            
        else:
            print("")
            print("Invalid Input")
            print("")

# MARK: REST
def rest():
    global questStep
    ambushRandomNum = random.randint(0, 100)
    ambushChance =  30 - (playerData["Stats"]["Agility"] * 0.20) 
    print("Ambush chance: ", ambushChance)

    if playerData["Stats"]["Health"] == 100:
            print("You are already max health")
            gameLoop()

    if ambushChance < 5:
        ambushChance = 5


    if ambushRandomNum <= ambushChance:
        questStep += 1
        print("")
        print("You were ambushed!")
        enemySelected = random.choice(list(enemies.keys()))
        print("")
        print("You encountered a", enemySelected)
        print("")
        combat(enemySelected)

    elif playerData["Stats"]["Health"] != 100:
        playerData["Stats"]["Health"] = playerData["Stats"]["Health"] + 10 + playerData["Stats"]["Agility"]

        if playerData["Stats"]["Health"] >= 101:
            playerData["Stats"]["Health"] = 100
            print("You rested, your health is now: ", playerData["Stats"]["Health"])
            moveForward()
            questStep += 1 

        else:
            print("You rested, your health is now: ", playerData["Stats"]["Health"])
            moveForward()
            questStep += 1 

# MARK: EQUIPMENT MENU
def equipMenu():
    while True:
        equipOptionsInput = str.upper(input("Equip options: Equip(E) | Unequip(U) | Discard(D) | Help(H) | Back(B): "))

        if equipOptionsInput == "E":
            print("")
            equipItemInput(None, None, None)

        elif equipOptionsInput == "U":
            unequipItemInput()
        
        elif equipOptionsInput == "D":
            discardItemInput()

        elif equipOptionsInput == "B":
            print("")
            gameLoop()

        elif equipOptionsInput == "H":
            print("")
            equipMenuHelp()

        else:
            print("")
            print("Invalid input")
            print("")

# MARK: EQUIP INPUT
def equipItemInput(inventoryItemName, inventoryItemStat, inventoryItemType):
    print("INVENTORY ITEM TYPE:", inventoryItemType)
    print("Your Inventory:", playerData["Inventory"])
    print("")
    print("Your Equipped Items:", playerData["EquippedItems"])
    print("")
    
    if inventoryItemName and inventoryItemStat != None:

        if inventoryItemType == "Shield":
            print("You equiped:", inventoryItemName)
            print("Your defence went up by:", inventoryItemStat)
            print("")

        else: 
            print("You equiped:", inventoryItemName)
            print("Your Attack went up by:", inventoryItemStat)
            print("")

    else:

        while True:
            equipItemInput = str.upper(input("Help(H) | Back(B) | Equip item(Slot#): "))
            # Player can input 0-10, the number they input equals
            # the item that they want to equip. So prompt the user
            # with the items that are in their inventory, and 
            # what ever item them they select, it automatically gets
            # equipped to it's respective slot.

            if equipItemInput in [f"SLOT{i}" for i in range(21)]:
                equipItemMain(equipItemInput)
                

            elif equipItemInput == "H":
                print("")
                print("Input the inventory slot of the item you want to equip,")
                print("For example; If you say 'Slot1', the item in Slot1 will")                        
                print("be equipped, unless there is an item already equipped in that slot.") 
                print("")

            elif equipItemInput == "B":
                print("")
                equipMenu()          

            else:
                print("")
                print("Invalid input")
                print("")

# MARK: EQUIP MAIN
def equipItemMain(equipItemInput):
    capitalEquipItemInput = equipItemInput.capitalize()

    if playerData["Inventory"][capitalEquipItemInput] == None:
        
        print("")
        print("No item in slot", capitalEquipItemInput)
        print("") 

    else:

        inventoryItemSelected = playerData["Inventory"][capitalEquipItemInput] 
        inventoryItemName = inventoryItemSelected[0]
        inventoryItemType = inventoryItemSelected[1]
        inventoryItemStat = inventoryItemSelected[2]

        for equipSlotName, equipSlot, in playerData["EquippedItems"].items():
            if inventoryItemType == equipSlotName:

                if equipSlot is not None:
                    print("")
                    print("That slot isn't empty, unequip the item in it's slot")
                    equipMenu()

                else:
                    playerData["EquippedItems"][equipSlotName] = inventoryItemSelected
                    playerData["Inventory"][capitalEquipItemInput] = None
                    print("")
                    print("You equipped:", inventoryItemSelected)

                    if inventoryItemType == "Weapon":
                        playerData["Stats"]["Attack"] += inventoryItemStat
                        equipItemInput(inventoryItemName, inventoryItemStat, inventoryItemType)

                    else:
                        playerData["Stats"]["Defence"] += inventoryItemStat
                        equipItemInput(inventoryItemName, inventoryItemStat, inventoryItemType)    

# MARK: UNEQUIP INPUT
def unequipItemInput():
    print("")
    print("Your equipped items are:", playerData["EquippedItems"])
    print("")
    while True:
        unequipItemInput = str.upper(input("Help(H) | Back(B) | Unequip item(ItemType): "))

        if unequipItemInput == "WEAPON":
            unequipItemMain(unequipItemInput)
            break

        elif unequipItemInput == "SHIELD":
            unequipItemMain(unequipItemInput)
            break

        elif unequipItemInput == "HEAD":
            unequipItemMain(unequipItemInput)
            break

        elif unequipItemInput == "CHEST":
            unequipItemMain(unequipItemInput)
            break

        elif unequipItemInput == "ARMS":
            unequipItemMain(unequipItemInput)
            break

        elif unequipItemInput == "HANDS":
            unequipItemMain(unequipItemInput)
            break

        elif unequipItemInput == "LEGS":
            unequipItemMain(unequipItemInput)
            break

        elif unequipItemInput == "FEET":
            unequipItemMain(unequipItemInput)
            break

        elif unequipItemInput == "H":
            print("")
            print("Allows you to unequip weapons and armor. To unequip,")
            print("you must input the name of the equip slot of the item")
            print("that you wish to unequip, for example: input (Head)")
            print("To unequip any head armor.")

        elif unequipItemInput == "B":

            if not traderMenu:
                equipMenu()
                break
            
            else:
                print("")
                tradeMenu()


        else:
            print("")
            print("Invalid input")
            print("")

#MARK: UNEQUIP MAIN
def unequipItemMain(unequipItemInput):
    capitalUnequipItemInput = unequipItemInput.capitalize()
    fullInventorySlots = 0
    unequipItemMain = playerData["EquippedItems"][capitalUnequipItemInput]

    if unequipItemMain == None:
        print("")
        print("No item in that slot to unequip")
        unequipItemInput()

    unequipItemName = unequipItemMain[0]
    unequipItemType = unequipItemMain[1]
    unequipItemStat = unequipItemMain[2]

    for slot, inventoryItem in playerData["Inventory"].items():
        if inventoryItem == None:
            playerData["Inventory"][slot] = playerData["EquippedItems"][capitalUnequipItemInput]
            playerData["EquippedItems"][capitalUnequipItemInput] = None
            print("")
            print("Your equipped items are:", playerData["EquippedItems"])
            print("")
            print("You unequipped:", unequipItemName)

            if unequipItemType == "Weapon":
                playerData["Stats"]["Attack"] -= unequipItemStat
                print(playerData["EquippedItems"])
                print("")
                print("Your attack went down by:", unequipItemStat)
                print("")
                break 

            else:
                playerData["Stats"]["Defence"] -= unequipItemStat
                print("Your defence went down by:", unequipItemStat)
                print("")
                break

        elif inventoryItem:
            fullInventorySlots += 1

            if fullInventorySlots == 20:
                print("")
                print("Inventory is full, cant unequip")
                unequipItemInput()

#MARK: DISCARD INPUT
def discardItemInput():
    while True:
        print("")
        print("Your Inventory:", playerData["Inventory"])
        print("")
        discardItemInput = str.upper(input("Back(B) | Help(H) | Discard item Slot#: "))

        if discardItemInput in [f"SLOT{i}" for i in range(21)]:
            discardItemMain(discardItemInput)

        elif discardItemInput == "B":
            print("")
            equipMenu()

#MARK: DISCARD MAIN      
def discardItemMain(discardItemInputParam):
    discardItemInputCapitalized = discardItemInputParam.capitalize()
    
    if playerData["Inventory"][discardItemInputCapitalized] == None:
        print("")
        print("No item in that slot")
        discardItemInput()

    else:

        while True:
            print("")
            discardItemConfirmationInput = str.upper(input("Confirm, do you really want to discard the item? Yes(Y) | Back(B): "))

            if discardItemConfirmationInput == "Y":
                print("")
                print("You discarded:", playerData["Inventory"][discardItemInputCapitalized])
                playerData["Inventory"][discardItemInputCapitalized] = None
                discardItemInput()
            
            elif discardItemConfirmationInput == "B":
                discardItemInput()
            
            else:
                print("")
                print("Invalid input")
                print("")

#MARK: TRADE HELP
def tradeHelp():
    while True:
        tradeHelpInput = str.upper(input("Help with: Trade(T) | Sell(S) | Unequip(U) | Back(B): "))

        if tradeHelpInput == "T":
            print("")
            print("Trading allows you to buy items. The trader's goods will get better")
            print("the farther you make it into your journey.")
            print("")

        elif tradeHelpInput == "S":
            print("")
            print("Selling allows you to sell your items to the trader to get gold.")
            print("")

        elif tradeHelpInput == "U":
            print("")
            print("Allows you to unequip items so you can sell them.")
            print("")

        elif tradeHelpInput == "B":
            tradeMenu()
            break

        else:
            print("Invalid Input")

#MARK: TRADE INPUT 
def tradeMenu():
    global traderMenu, questStep
    traderMenu = True

    while True:
        tradeMenuInput = str.upper(input("Trade(T) | Sell(S) | Unequip(U) | Help(H) | Back(B): "))
    
        if tradeMenuInput == "T":
            print("")
            tradeMain()
            break

        elif tradeMenuInput == "S":
            sellInput()
            break

        elif tradeMenuInput == "U":
            unequipItemInput()
            break

        elif tradeMenuInput == "H":
            print("")
            tradeHelp()
            print("")

        elif tradeMenuInput == "B":
            traderMenu = False
            questStep+= 1
            gameLoop()
            break
            
        else:
            print("")
            print("Invalid Input")
            print("")

#MARK: TRADE MAIN
def tradeMain():
    if questStep == trader1:
        traderWave = "traderGoods1"

    elif questStep == trader2:
        traderWave = "traderGoods2"

    elif questStep == trader3:
        traderWave = "traderGoods3"

    elif questStep == trader4:
        traderWave = "traderGoods4"

    elif questStep == trader5:
        traderWave = "traderGoods5"

    elif questStep == trader6:
        traderWave = "traderGoods6"

    elif questStep == trader7:
        traderWave = "traderGoods7"

    while True:
        tradeItemTypeInput = str.upper(input("Trade for Armor(A) | Weapons(W) | Shields(S) | Back(B): "))
        if tradeItemTypeInput == "A":
            tradeItemTypeInput = "Armors"
            
        elif tradeItemTypeInput == "W":
            tradeItemTypeInput = "Weapons"
            
        elif tradeItemTypeInput == "S":
            tradeItemTypeInput = "Shields"

        elif tradeItemTypeInput == "B":
            print("")
            tradeMenu()
            
        else:
            print("")
            print("Invalid Input")
            print("")
            tradeMain()
        
        print("")
        for itemName, itemType in traderGoods[traderWave][tradeItemTypeInput].items():
            print(itemType, "Price:", traderBuyPrices[itemName])
        
        print("")
        print("Your Gold:", playerData["Stats"]["Gold"])

        while True:
            print("")
            itemBuyInput = str.title(input("Back(B) | What do you want to buy(ItemName): "))

            if itemBuyInput == "B":
                print("")
                tradeMain()
                print("")
                break  

            if itemBuyInput in traderGoods[traderWave][tradeItemTypeInput]:

                if playerData["Stats"]["Gold"] < traderBuyPrices[itemBuyInput]:
                    print("")
                    print("Not enough gold for: ", traderGoods[traderWave][tradeItemTypeInput][itemBuyInput])
                    print("")
                    tradeMenu()    
                    break  

                itemChoice = traderGoods[traderWave][tradeItemTypeInput][itemBuyInput]

                for slot, item in playerData["Inventory"].items():
                    if slot == "Slot20" and item != None:
                        print("Inventory Full! Sell an item.")

                    if item is None:  # Check if the slot is empty
                        playerData["Inventory"][slot] = itemChoice
                        playerData["Stats"]["Gold"] -= traderBuyPrices[itemBuyInput]
                        print("")
                        
                        for itemName, itemType in traderGoods[traderWave][tradeItemTypeInput].items():
                            print(itemType, "Price:", traderBuyPrices[itemName])

                        print("")
                        print("Your inventory: ", playerData["Inventory"])
                        print("")
                        print("Your Gold:", playerData["Stats"]["Gold"])
                        print("")
                        print("You bought:", itemChoice, "for", traderBuyPrices[itemBuyInput], "Gold.")
                        break

            else:
                print("")
                print("Invalid Input")

#MARK: SELL INPUT
def sellInput():
    print(playerData["Inventory"])

    while True:
        print("")
        sellInput = str.upper(input("Back(B) | Slot#: "))
        if sellInput in [f"SLOT{i}" for i in range(21)]:
            sellMain(sellInput)
            
        elif sellInput == "B":
            print("")
            tradeMenu()
            break

        else:
            print("")
            print("Invalid Input")    
            print("")

#MARK: SELL
def sellMain(sellInput):
    print("sell input",sellInput)
    sellInputCapitalized = sellInput.title()

    soldItemMain = playerData["Inventory"][sellInputCapitalized]
    soldItemName = soldItemMain[0]

    playerData["Stats"]["Gold"] += sellPrices[soldItemName]
    playerData["Inventory"][sellInputCapitalized] = None

    print(playerData["Inventory"])
    print("")
    print("You sold:", soldItemName, "for:", sellPrices[soldItemName], "Gold")
    print("")
    print("Your Gold:", playerData["Stats"]["Gold"])
    
#MARK: DROP REPLACE INPUT
def dropItemReplaceInput (dropProperties):
    print("Your Inventory:", playerData["Inventory"])
    while True:
        print("")
        dropItemInput = str.upper(input("Back(B) | Help(H) | Replace item Slot#: "))
        print("")

        if dropItemInput in [f"SLOT{i}" for i in range(21)]:
            dropItemReplaceMain(dropItemInput, dropProperties)
        
        elif dropItemInput == "B":
            gameLoop()

        elif dropItemInput == "H":
            print("Your inventory is full, so you must replace an item in your inventory")
            print("with the item you aquired. You can also go back to not replace any item.")
        
        else:
            print("")
            print("Invalid input")
            print("")

# MARK: DROP REPLACE MAIN
def dropItemReplaceMain(dropItemInput, dropProperties):
        dropItemInputCapitalized = dropItemInput.capitalize()
        print("You replaced:", playerData["Inventory"][dropItemInputCapitalized], "With:", dropProperties)
        print("")
        playerData["Inventory"][dropItemInputCapitalized] = dropProperties
        levelUp()

## Resets everything when player dies
# MARK: CLEANUP FUNCTION
def cleanupFunction():
    global playerData, enemies, firstStep, enemyStunned, deathCounter, questStep
    deathCounter += 1
    questStep = 0
    print("You died, your quest is over.")
    
    # Resets player's and enemies data
    playerData = copy.deepcopy(defaultPlayerData)
    enemies = copy.deepcopy(defaultEnemysData)

    firstStep = True
    enemyStunned = False

    while True:
        print("")
        restartQuest = str.upper(input("Restart? Yes(Y): "))  

        if restartQuest == "Y":
            questBegin()
            break
        
        else:
            print("")
            print("Invalid input")
            print("")

# MARK: MAIN HELP
def mainHelp():
    while True:
        print("")
        helpMoveInput = str.upper(input("Help with: Move forward(M) | Inventory(I) | Equip Menu(E) | Rest(R) | Back(B): "))

        if helpMoveInput == "M":
            print("")
            print("Moves you forward. % chance for enemy encounter, % chance for random event.\nAlso increases the quest step, until step 20, where you fight the final boss.")

        elif helpMoveInput == "I":
            print("")
            print("Shows all items within your inventory. Each item has a name, item type, and stat, in that order.\nExample: Rusty Dagger, Weapon, 5. The stat for weapons is attack, the stat for shield and armor is defence.  ")
           
        elif helpMoveInput == "E":
            print("")
            print("Allows you to equip weapons and armor.")
            
            
        elif helpMoveInput == "R":
            print("")
            print("Allows you to rest for a turn, which heals you 25 health + agility\nHas a chance of enemy ambush")
            
        elif helpMoveInput == "B":
            print("")
            gameLoop()

        else:
            print("")
            print("Invalid input")
            print("")

# MARK: EQUIP MENU HELP
def equipMenuHelp():
    while True:
        equipHelpInput = str.upper(input("Help with: Equip(E) | Unequip(U) | Discard(D) | Back(B): "))
        
        if equipHelpInput == "E":
            print("")
            print("Allows you to equip weapons and armor.")
            print("")

        elif equipHelpInput == "U":
            print("")
            print("Allows you to unequip weapons and armor.")
            print("")

        elif equipHelpInput == "D":
            print("")
            print("Allows you to discard or drop an item.")  
            print("")

        elif equipHelpInput == "B":
            print("")
            equipMenu()

        else:
            print("")
            print("Invalid input")
            print("")

#MARK: INITIALIZE GAME 
questBegin()
