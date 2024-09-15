import math, random, copy

defaultHealth = 100
questStep = 0
enemyStunned = False

#IDEA FOR SHOP
#Create a table for all the items, and their price
#When you want to sell an item, loop through the items
#in the player's table and check which items they have.
#Then, display the prices of the items they posess.

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
        "Defence": 0, 
        "Agility": 25,
        "Level": 0,
        "Exp": 0,
        "Gold": 0
    },

    "Inventory":{
        "SLOT0": ("Old Shortsword", "Weapon", 10),
        "SLOT1": ("Bruised Iron Leggings", "Legs", 5),
        "SLOT2": None,
        "Slot3": None,
        "SLOT4": None,
        "SLOT5": None,
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

    # full inventory for testing
    #     "Inventory":{
    #     "Slot0": ("Old Shortsword", "Weapon", 10),
    #     "Slot1": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot2": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot3": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot4": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot5": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot6": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot7": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot8": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot9": ("Bruised Iron Leggings", "Legs", 5),
    #     "Slot10": ("Bruised Iron Leggings", "Legs", 5)e
    # },

    "EquippedItems":{
        "Weapon": None,
        "Shield": ("Ragged Leather Sheild", "Shield", 1),
        "Head": ("Musty Skullcap", "Head",  2),
        "Chest": None,
        "Arms": None,
        "Hands": None,
        "Legs": None,
        "Feet": None
    }
}

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
            "Old Shortsword": ("Old Shortsword", "Weapon", 10),
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
            "Mail Mittens": ("Mail Mittens", "Hands", 6),
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

    "Drops": None,
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

    "Drops": None,
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

    "Drops": None,
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

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""A disgusting smell enters your nostrils, death.
you cautiously walk forward, and trough a clearing in
the forest, you spot what looks like the remains of a small
skirmish. You look for movement, but all that remain are dead men.
You scour the battlefeild, and you find a decent set of Soldiers Armor!"""
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

    "Drops": None, # could have a red gemstone item that does 1 damage but sells for 1000.
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

    "Drops": None,
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

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""As you are travelling along the road, you come across ruined castle.
You search it's halls and dungeons, and take what you can find. Eventually,
you happen upon the armory, and find various old weapons and armor."""
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

    "Drops": None,
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
You search for any surviving tomes and scrolls, but fail to find anything
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

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""You notice bones scattered across the ground. Upon farthur
inspection, you realise these are human remains, ancient and
decayed. But, on the ground you see an old sword and shield!
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

    "Drops": None,
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

    "Drops": None,
    "HealthRestore": False,

    "EventDescription": 
    
"""You tire from many days travel, and so you seek out shelter to rest.
You spot a shaded meadow, with trees surrounding it. You lay against a tree and
look through your baggage. Many hours pass and you pick yourself up and continue,
but as you get up, you notice ancient an ancient set of armor, lying in the grass
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

    "Drops": None,
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

    "Drops": None,
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

# MARK: INVENTORY
def inventory():
    print(playerData["Inventory"])
    gameLoop()


def itemEquipFunction(equipItemInput):
    capitalEquipItemInput = equipItemInput.capitalize()

    if playerData["Inventory"][capitalEquipItemInput] == None:
    
        print("No item in slot", capitalEquipItemInput)

    else:

        inventoryItemSelected = playerData["Inventory"][capitalEquipItemInput] # == ('Old Shortsword', 'Weapon', 10)
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
                        print("Your attack went up by:", inventoryItemStat)
                        print("")
                        equipItem()

                    else:
                        playerData["Stats"]["Defence"] += inventoryItemStat
                        print("Your defence went up by:", inventoryItemStat)
                        print("")
                        equipItem()    

# MARK: EQUIP ITEM
def equipItem():
    while True:
        equipItemInput = str.upper(input("Show Equipped Items and Inventory(I), Help(H), Back(B), Equip item(Slot#): "))
        # Player can input 0-10, the number they input equals
        # the item that they want to equip. So prompt the user
        # with the items that are in their inventory, and 
        # what ever item them they select, it automatically gets
        # equipped to it's respective slot.

        if equipItemInput in [f"SLOT{i}" for i in range(21)]:
            itemEquipFunction(equipItemInput)
            print("")


        elif equipItemInput == "I":
            print("")
            print("Your equipped items:", playerData["EquippedItems"])
            print("")    
            print("Your Inventory: ", playerData["Inventory"]) 
            print("")

        elif equipItemInput == "H":
            print("")
            print("Input the inventory slot of the item you want to equip,")
            print("For example; If you say 'Slot1', the item in Slot1 will")                        
            print("be equipped, unless there is an item already equipped in that slot.") 

        elif equipItemInput == "B":
            print("")
            equip()          

        else:
            print("Invalid input")

def unequipItemFunction(unequipItemInput):
    capitalUnequipItemInput = unequipItemInput.capitalize()
    fullInventorySlots = 0

    unequipItemMain = playerData["EquippedItems"][capitalUnequipItemInput]
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

            if fullInventorySlots == 10:
                print("")
                print("Inventory is full")
                equip()

# MARK: UNEQUIP ITEM
def unequipItem():
    print("")
    print("Your equipped items are:", playerData["EquippedItems"])
    print("")
    while True:
        unequipItemInput = str.upper(input("Help(H), Back(B), Unequip item(ItemType): "))

        if unequipItemInput == "WEAPON":
            unequipItemFunction(unequipItemInput)

        elif unequipItemInput == "SHIELD":
            unequipItemFunction(unequipItemInput)

        elif unequipItemInput == "HEAD":
            unequipItemFunction(unequipItemInput)

        elif unequipItemInput == "CHEST":
            unequipItemFunction(unequipItemInput)

        elif unequipItemInput == "ARMS":
            unequipItemFunction(unequipItemInput)

        elif unequipItemInput == "HANDS":
            unequipItemFunction(unequipItemInput)

        elif unequipItemInput == "LEGS":
            unequipItemFunction(unequipItemInput)

        elif unequipItemInput == "FEET":
            unequipItemFunction(unequipItemInput)

        elif unequipItemInput == "H":
            print("")
            print("Allows you to unequip weapons and armor. To unequip,")
            print("you must input the name of the equip slot of the item")
            print("that you wish to unequip, for example: input (Head)")
            print("To unequip any head armor.")

        elif unequipItemInput == "B":
            print("player tried to go back")
            equip()

        else:
            print("Invalid input")
            break

       
                
           
# MARK: DISCARD ITEM & HELP
def discardItem():
    print("What do you want to discard?")

def equipHelp():
    while True:
        equipHelpInput = str.upper(input("Help with: Equip(E), Unequip(U), Discard(D), Exit Help(X): "))
        
        if equipHelpInput == "E":
            print("")
            print("Allows you to equip weapons and armor.")

        elif equipHelpInput == "U":
            print("")
            print("Allows you to unequip weapons and armor.")

        elif equipHelpInput == "D":
            print("")
            print("Allows you to discard or drop an item.")  

        elif equipHelpInput == "X":
            print("")
            equip()

        else:
            print("")
            print("Invalid input")

# MARK: EQUIP MAIN
def equip():
    while True:
        equipOptionsInput = str.upper(input("Equip options: Equip(E), Unequip(U), Discard(D), Help(H), Back(B): "))

        if equipOptionsInput == "E":
            print("")
            equipItem()

        elif equipOptionsInput == "U":
            unequipItem()
        
        elif equipOptionsInput == "D":
            discardItem()

        elif equipOptionsInput == "B":
            gameLoop()

        elif equipOptionsInput == "H":
            print("")
            equipHelp()

        else:
            print("")
            print("Invalid input")

            
# MARK: REST
def rest():
    global questStep
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

# MARK: MAIN HELP
def mainHelp():
    while True:
        helpMoveInput = str.upper(input("Help with: Move forward(M), Inventory(I), Equip Menu(E), Rest(R), Exit Help(X): "))

        if helpMoveInput == "M":
            print("")
            print("Moves you forward. % chance for enemy encounter, % chance for random event.\nAlso increases the quest step, until step 20, where you fight the final boss.")
            print("")

        elif helpMoveInput == "I":
            print("")
            print("Shows all items within your inventory. Each item has a name, item type, and stat, in that order.\nExample: Rusty Dagger, Weapon, 5. The stat for weapons is attack, the stat for sheild and armor is defence.  ")
            print("")

        elif helpMoveInput == "E":
            print("")
            print("Allows you to equip weapons and armor.")
            print("") 
            
        elif helpMoveInput == "R":
            print("")
            print("Allows you to rest for a turn, which heals you 25 health + agility\nHas a chance of enemy ambush")
            print("")
        elif helpMoveInput == "X":
            gameLoop()

        else:
            print("")
            print("Invalid input")
            print("")


def stats():
    print(playerData["Stats"])
    gameLoop()

#MARK: MAIN GAME LOOP!!!
def gameLoop():
    global questStep

    if questStep == 0:
        print("This is the first step of your adventure!\nBe sure to prepare for a harsh trek ahead!\n")

        while True:
            playerChoice = str.upper(input("Move forward(M), Inventory(I), Equip Menu(E), Rest(R), Stats(S) Help(H): "))

            if questStep == 5:
                print("Shopkeeper goes here, or a selection of random events specific to each 5 quest steps.")
                moveForward()

            elif questStep == 20:
                print("player reached quest step 20, final boss goes here")
            
            elif playerChoice == "M":                
                moveForward()
                break

            elif playerChoice == "I":
                questStep += 1  
                inventory()
                break

            elif playerChoice == "E":
                questStep += 1  
                print("")
                equip()
                break

            elif playerChoice == "R":
                questStep += 1  
                print("")
                rest()  
                break

            elif playerChoice == "S":
                questStep += 1
                stats()

            elif playerChoice == "H":
                questStep += 1  
                print("")
                mainHelp()
            else:
                print("Invalid input")

    else:
        while True:
            playerChoice = str.upper(input("Move forward(M), Inventory(I), Equip(E), Rest(R), Stats(S) Help(H): "))
            
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

            elif playerChoice == "S":
                stats()
                break

            elif playerChoice == "H":
                mainHelp()

            else:
                print("Invalid input")

#MARK: MOVE FORWARD
def moveForward():
    global questStep, defaultHealth, emptyInventorySlots
    enemyOrEvent = random.randint(0, 100)
    questStep += 1
    
    if enemyOrEvent <= 90: #Encountered Random Event:

        eventSelected = random.choice(list(randomEvents.keys()))
        eventProperties = randomEvents[eventSelected]
        print("")
        print(eventProperties["EventDescription"])
        print("")
        for stat, statAmount in eventProperties["Stats"].items():

            if statAmount:
                playerData["Stats"][stat] += statAmount
                print("Your", stat, "went up by", statAmount)

                

        if eventProperties["HealthRestore"]:
            playerData["Stats"]["Health"] = defaultHealth
            print("")
            print("restored health")
            print("")
        
        

        else:
            gameLoop()
        

    else: #Encountered Enemy
        enemySelected = random.choice(list(enemies.keys()))
        print("")
        print("You encountered a", enemySelected)
        combat(enemySelected)

#MARK: COMBAT
def combat(enemySelected):
    global enemyStunned
    global enemyDamage
    enemyProperties = enemies[enemySelected]
    shield = playerData["EquippedItems"].get("Sheild")
    stunChance = shield[2] * 3 if shield else 1
    runChance = playerData["Stats"]["Agility"] * 3
    runChance -= enemyProperties["Stats"]["Agility"] 

    while playerData["Stats"]["Health"] > 1:
        playerAtkChoice = str.upper(input("Attack(A), Defend(D), Run(R), Stats(S), Enemy Stats(E), Help(H): "))

        if playerAtkChoice == "A":
            
            if playerData["EquippedItems"]["Weapon"] == None:
                playerDamage = playerData["Stats"]["Attack"]
                enemyProperties["Stats"]["Health"] -= playerDamage # hit enemy 

            else:
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
                
        elif playerAtkChoice == "D": #############################################
            stun = random.randint(0, 100)
            
            if stun >= stunChance:
                enemyStunned = True
                print("You dodged the enemy!")

            else:
                print("Enemy hit you")
        
        elif playerAtkChoice == "R":
            run = random.randint(0, 100)

            if run >= runChance:
                gameLoop()

            else:
                print("")
                print("You failed to run from the enemy!")
                enemyDamage = enemyProperties["Stats"]["Attack"] - playerData["Stats"]["Defence"] 
                playerData["Stats"]["Health"] -= enemyDamage
                
                print("The enemy did", enemyDamage, "damage to you!") # enemy hit player
                print("Your new health is:", playerData["Stats"]["Health"], ", the enemies health is:", enemyProperties["Stats"]["Health"])


        elif playerAtkChoice == "S":
            print("")
            print(playerData["Stats"])

        elif playerAtkChoice == "E":
            print("")
            print(enemySelected, "Health:", enemyProperties["Stats"]["Health"], "|", "Attack:", enemyProperties["Stats"]["Attack"], "|", "Agility:", enemyProperties["Stats"]["Agility"] )

        elif playerAtkChoice == "H":
            while True:
                helpAttackInput = str.upper(input("Help with: Attack(A), Defend(D), Run(R), Stats(S), Exit Help(X): "))
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
                
                for slot, item in playerData["Inventory"].items():
                    if item is None:  # Check if the slot is empty
                        playerData["Inventory"][slot] = dropProperties  # Place the item in the slot
                        print(playerData["Inventory"])
                        gameLoop()
                        break


            else:
                print("no drops :(")
                gameLoop()
                break
        
    ## Relates to the while loop, when the player dies, call this function.
    cleanupFunction()

#MARK: QUEST BEGIN
def questBegin():
    print("")
    print("Welcome to TERRA, the home of the gods.\nThis is a simple text based rpg.\n")
    playerName = str(input("Please enter your name: "))
    playerData["PlayerName"] = playerName
    print("Welcome", playerData["PlayerName"])
    print("")
    gameLoop()

# Initialize the game 
questBegin()

