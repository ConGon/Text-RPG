import math, random, copy

defaultHealth = 100
questStep = 15

deathCounter = 0
enemiesKilled = 0
itemsCollected = 0

maxStunChance = 65
maxRunChance = 85

#HIGHSCORE: YOU MANAGED TO GET 20 QUEST STEPS


enemyStunned = False
firstStep = True
traderMenu = False

#IDEA FOR SHOP
#Create a table for all the items, and their price
#When you want to sell an item, loop through the items
#in the player's table and check which items they have.
#Then, display the prices of the items they posess.


#IDEA FOR ARMOR
#Divide the player's armor value into half
#Take one half of it, and generate a random number between 0 and half of players armor.
#And thats how much armor the player has that turn.
levelData = [
    100,
    200,
    300,
    400,
    500
]


# MARK: PLAYER DATA
playerData = {
    "Stats":{
        "Health": 100,
        "Attack": 10,
        "Defence": 1, 
        "Agility": 5,
        "Level": 0,
        "Exp": 0,
        "Gold": 0
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
    #     "Slot11":("Bruised Iron Leggings", "Legs", 5),
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


# MARK: MERCHANT HERE
itemPrices = {
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
    "Platinum Crown": 2500,
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
    "Thieves Gloves": 10,
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
    "Stinking Gloves": 5
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
            "Attack": 100,
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

# MARK: INVENTORY
def inventory():
    print("")
    print("Your Inventory:", playerData["Inventory"])
    print("")
    gameLoop()

# MARK: EQUIP FUNCITON
def itemEquipFunction(equipItemInput):
    capitalEquipItemInput = equipItemInput.capitalize()

    if playerData["Inventory"][capitalEquipItemInput] == None:
    
        print("No item in slot", capitalEquipItemInput)

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
                    equip()

                else:
                    playerData["EquippedItems"][equipSlotName] = inventoryItemSelected
                    playerData["Inventory"][capitalEquipItemInput] = None
                    print("")
                    print("You equipped:", inventoryItemSelected)

                    if inventoryItemType == "Weapon":
                        playerData["Stats"]["Attack"] += inventoryItemStat
                        equipItem(inventoryItemName, inventoryItemStat)

                    else:
                        playerData["Stats"]["Defence"] += inventoryItemStat
                        equipItem(inventoryItemName, inventoryItemStat)    

# MARK: EQUIP ITEM
def equipItem(inventoryItemName, inventoryItemStat):
    print("Your Inventory:", playerData["Inventory"])
    print("")
    print("Your Equipped Items:", playerData["EquippedItems"])
    print("")
    
    if inventoryItemName and inventoryItemStat != None:
        print("You equiped:", inventoryItemName)
        print("Your defence went up by:", inventoryItemStat)
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
                itemEquipFunction(equipItemInput)
                

            elif equipItemInput == "H":
                print("")
                print("Input the inventory slot of the item you want to equip,")
                print("For example; If you say 'Slot1', the item in Slot1 will")                        
                print("be equipped, unless there is an item already equipped in that slot.") 
                print("")

            elif equipItemInput == "B":
                print("")
                equip()          

            else:
                print("")
                print("Invalid input")
                print("")

def unequipItemFunction(unequipItemInput):
    capitalUnequipItemInput = unequipItemInput.capitalize()
    fullInventorySlots = 0
    unequipItemMain = playerData["EquippedItems"][capitalUnequipItemInput]

    if unequipItemMain == None:
        print("")
        print("No item in that slot to unequip")
        unequipItem()

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
                unequipItem()

# MARK: UNEQUIP ITEM
def unequipItem():
    print("")
    print("Your equipped items are:", playerData["EquippedItems"])
    print("")
    while True:
        unequipItemInput = str.upper(input("Help(H) | Back(B) | Unequip item(ItemType): "))

        if unequipItemInput == "WEAPON":
            unequipItemFunction(unequipItemInput)
            break

        elif unequipItemInput == "SHIELD":
            unequipItemFunction(unequipItemInput)
            break

        elif unequipItemInput == "HEAD":
            unequipItemFunction(unequipItemInput)
            break

        elif unequipItemInput == "CHEST":
            unequipItemFunction(unequipItemInput)
            break

        elif unequipItemInput == "ARMS":
            unequipItemFunction(unequipItemInput)
            break

        elif unequipItemInput == "HANDS":
            unequipItemFunction(unequipItemInput)
            break

        elif unequipItemInput == "LEGS":
            unequipItemFunction(unequipItemInput)
            break

        elif unequipItemInput == "FEET":
            unequipItemFunction(unequipItemInput)
            break

        elif unequipItemInput == "H":
            print("")
            print("Allows you to unequip weapons and armor. To unequip,")
            print("you must input the name of the equip slot of the item")
            print("that you wish to unequip, for example: input (Head)")
            print("To unequip any head armor.")

        elif unequipItemInput == "B":

            if not traderMenu:
                equip()
                break
            
            else:
                trader()


        else:
            print("")
            print("Invalid input")
            print("")

       
def discardItemFunction(discardItemInput):
    discardItemInputCapitalized = discardItemInput.capitalize()
    
    if playerData["Inventory"][discardItemInputCapitalized] == None:
        print("No item in that slot")
        discardItem()

    else:

        while True:
            print("")
            discardItemConfirmationInput = str.upper(input("Confirm, do you really want to discard the item? Yes(Y) | Back(B): "))

            if discardItemConfirmationInput == "Y":
                print("")
                print("You discarded:", playerData["Inventory"][discardItemInputCapitalized])
                playerData["Inventory"][discardItemInputCapitalized] = None
                discardItem()
            
            elif discardItemConfirmationInput == "B":
                discardItem()
            
            else:
                print("")
                print("Invalid input")
                print("")

# MARK: DISCARD ITEM
def discardItem():
    while True:
        print("")
        print("Your Inventory:", playerData["Inventory"])
        print("")
        discardItemInput = str.upper(input("Back(B) | Help(H) | Discard item Slot#: "))

        if discardItemInput in [f"SLOT{i}" for i in range(21)]:
            discardItemFunction(discardItemInput)

        elif discardItemInput == "B":
            print("")
            equip()
           
# MARK: HELP
def equipHelp():
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
            equip()

        else:
            print("")
            print("Invalid input")
            print("")

# MARK: EQUIP MAIN
def equip():
    while True:
        equipOptionsInput = str.upper(input("Equip options: Equip(E) | Unequip(U) | Discard(D) | Help(H) | Back(B): "))

        if equipOptionsInput == "E":
            print("")
            equipItem(None, None)

        elif equipOptionsInput == "U":
            unequipItem()
        
        elif equipOptionsInput == "D":
            discardItem()

        elif equipOptionsInput == "B":
            print("")
            gameLoop()

        elif equipOptionsInput == "H":
            print("")
            equipHelp()

        else:
            print("")
            print("Invalid input")
            print("")

# MARK: DROP ITEM REPLACE

def dropItemReplaceFunction(dropItemInput, dropProperties):
        dropItemInputCapitalized = dropItemInput.capitalize()
        print("You replaced:", playerData["Inventory"][dropItemInputCapitalized], "With:", dropProperties)
        print("")
        playerData["Inventory"][dropItemInputCapitalized] = dropProperties
        gameLoop()

def dropItemReplace (dropProperties):
    print("Your Inventory:", playerData["Inventory"])
    while True:
        print("")
        dropItemInput = str.upper(input("Back(B) | Help(H) | Replace item Slot#: "))
        print("")

        if dropItemInput in [f"SLOT{i}" for i in range(21)]:
            dropItemReplaceFunction(dropItemInput, dropProperties)
        
        elif dropItemInput == "B":
            gameLoop()

        elif dropItemInput == "H":
            print("Your inventory is full, so you must replace an item in your inventory")
            print("with the item you aquired. You can also go back to not replace any item.")
        
        else:
            print("")
            print("Invalid input")
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


def stats():
    print("")
    print(playerData["Stats"])
    print("")
    gameLoop()

def trade():
    print("reee")

#MARK: SELLXXXXXXX
def sellFunction(sellInput):
    #Loop through the prices table AND the players inventory
    #Print the item prices of the items that the player HAS
    sellInputCapitalized = sellInput.capitalize()

    soldItemMain = playerData["Inventory"][sellInputCapitalized]
    soldItemName = soldItemMain[0]
    soldItemType = soldItemMain[1]
    soldItemStat = soldItemMain[2]

    playerData["Stats"]["Gold"] += itemPrices[soldItemName]
    playerData["Inventory"][sellInputCapitalized] = None
    print(playerData["Inventory"])
    print("")
    print("You sold:", soldItemName, "for:", itemPrices[soldItemName], "Gold")
    print("")
    sell()

def sell():
    
    while True:
        sellInput = str.upper(input("Back(B) | Slot#: "))
        if sellInput in [f"SLOT{i}" for i in range(21)]:
            sellFunction(sellInput)
            

        elif sellInput == "B":
            print("")
            trader()
            break

        else:
            print("")
            print("Invalid Input")    
            print("")
      
# traderResponses = {

#      "GenericResponses":
#     "questStep5Responses": {

#     },

#     "QuestStep10Responses": {


#     }

# }

#MARK: TRADE!!!!!!!!!!
def trader():
    global traderMenu, questStep
    traderMenu = True

    while True:
        traderInput = str.upper(input("Trade(T) | Sell(S) | Unequip(U) | Help(H) | Back(B): "))
    
        if traderInput == "T":
            trade()
            break

        elif traderInput == "S":
            sell()
            break

        elif traderInput == "U":
            unequipItem()
            break

        elif traderInput == "B":
            traderMenu = False
            questStep+= 1
            gameLoop()
            break
            
        else:
            print("")
            print("Invalid Input")
            print("")


#MARK: MAIN GAME LOOP!!!
def gameLoop():
    global questStep, firstStep
    print(questStep)
    while True:

        if questStep == 0 and firstStep:
            print("It is the first step of your journey, so prepare for it. Take good note of your")
            print("current items, and good luck on your trecherous quest...")
            print("")
            firstStep = False
            
        elif questStep == 5:
            print("First time player sees trader, dialogue will be")
            trader()
            #shopkeeper function here

        elif questStep == 10:
            print("Shopkeeper goes here, or a selection of random events specific to each 5 quest steps.")
            #shopkeeper function here

        elif questStep == 15:
            print("You hear cackling and malicious laughter from behind you")
            combat("Goblin Lord")

        elif questStep == 20:
            print("Shopkeeper goes here, or a selection of random events specific to each 5 quest steps.")
            #shopkeeper function here

        elif questStep == 25:
            print("Second miniboss here")


        elif questStep == 30:
            print("Shopkeeper goes here, or a selection of random events specific to each 5 quest steps.")
            #shopkeeper function her

        elif questStep == 35: 
            print("Third miniboss here")

        elif questStep == 40:
            print("Shopkeeper goes here, or a selection of random events specific to each 5 quest steps.")
            #shopkeeper function here

        elif questStep == 45:
            print("Final miniboss goes here")

        elif questStep == 50:
            print("Shopkeeper goes here, or a selection of random events specific to each 5 quest steps.")
            #shopkeeper function here

        elif questStep == 65:
            print("player reached quest step 65, final boss goes here")

        elif questStep == 85:
            print("Shopkeeper goes here, or a selection of random events specific to each 5 quest steps.")
            #shopkeeper function here

        elif questStep == 100:
            print("From high heavens, a being of true might decended. He first peirced the firmament,")
            print("then the skies, and soon, impacted the ground before your feet. A crater of unfathomable preportions now lie in front of you.")
            print("The skies stirred with dark power, and a great storm was now among the lands. You stood your ground, knowing that this would be")
            print("Your final battle. Through the dust and fire, the malevolent being marched forward. Eventually, he came within your sight, and all you knew was this:")
            print("an evil god now stood before you")  

        playerChoice = str.upper(input("Move forward(M) | Equip Menu(E) | Rest(R) | Inventory(I) | Equipped Weapons & Armor(W) | Stats(S) | Help(H): "))
    
        if playerChoice == "M": 
            questStep += 1  
            moveForward()
            break
            
        elif playerChoice == "I":
            inventory()
            break

        elif playerChoice == "E":
            print("")
            equip()
            break

        elif playerChoice == "R": 
            rest()  
            break
        
        elif playerChoice == "W":
            print("")
            print("Equipped Items:", playerData["EquippedItems"])
            print("")

        elif playerChoice == "S":
            stats()
            break

        elif playerChoice == "H":
            mainHelp()
            break

        else:
            print("")
            print("Invalid input")
            print("")

#MARK: MOVE FORWARD
def moveForward():
    global questStep, defaultHealth
    enemyOrEvent = random.randint(0, 100)
    
    if enemyOrEvent <= 90: #Encountered Random Event:

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
            gameLoop()

        else:
            dropItem = list(eventProperties["Drops"].values())[0]

            for slot, item in playerData["Inventory"].items():
                    
                    if slot == "Slot20" and item != None:
                        print("Inventory Full")
                        print(dropItem)
                        dropItemReplace(dropItem)

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
    global enemyStunned, enemyDamage, maxStunChance, maxRunChance
    
    if enemySelected == "Goblin Lord" or "Dark Sorcerer" or "Stone Golem" or "Dragon" or "Demon Lord":
        enemyProperties = miniBosses[enemySelected]
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

        if enemyProperties["Stats"]["Health"] <= 0:
            print("You defeated the", enemySelected)
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
                        dropItemReplace(dropProperties)

                    if item is None:  # Check if the slot is empty
                        print("You aquired:", dropSelected)
                        print("")
                        playerData["Inventory"][slot] = dropProperties  # Place the item in the slot
                        gameLoop()

            else:
                gameLoop()
                break
        
        if playerData["Stats"]["Health"] <= 0:
            cleanupFunction()
            break

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

# Initialize the game 
questBegin()

