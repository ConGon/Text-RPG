ABOUT:
Trials Of The Wanderer is a text-based RPG made by: ConGon. It is a game where you move forward through random
encounters, and fight random enemies. You will aquire loot throughout your journey, and may come across a crafty
mercant. Fight 4 minibosses, a final boss and maybe even a secret boss at the end... With a total of 168 items,
every run will be different. Will you be able to trek forward for 100 days to accomplish your final quest...


HOW TO RUN: 

EXE: 
To run the game, download the zip file from the repository, and run (TrialsOfTheWanderer.exe) done!

TERMINAL: 
Open (TrialsOfTheWanderer.py), within your chosen IDE, then run it, Done!


Guide:
Trials Of The Wanderer is quite a simple game. Most of the time you will see this line: 
Move forward(M) | Equip Menu(E) | Rest(R) | Inventory(I) | Equipped Weapons & Armor(W) | Stats(S) | Help(H):

This is an input prompt, and these are how interact with the game!
The letters or characters wrapped in brackets () are the valid inputs, and their related functions to the right of them. 
In order to finalize an input, you type the character, followed by the enter key. So if I wanted to move forward, I would 
hit the W key, followed by the enter key. There is also provided help functions every time an input prompt appears.


Enemies and Random Events:
In Trials Of The Wanderer, there are two main things that can happen when you "Move Forward": 1, you encounter a random
enemy, 2, you encounter a random event. When you encounter an enemy, you then must defeat the enemy, or run away. When 
you encounter a random event, it can give you differing rewards, such as items, gold, restore your health, or even give 
you permanent stat increases.


Combat:

Attacking:
Combat is simple, it involves Attacking, Defending, and Running. Trials Of The Wanderer runs on a "Simultanious turns"
system, where when you attack the enemy, the enemy also attacks you. When you attack, the enemy takes damage for at much
Attack stat you have. So if you have 50 Attack stat, you will do 50 damage to the enemy. Below is an enemy encounter:

You encountered a Devil Cultist

Attack(A) | Defend(D) | Run(R) | Stats(S) | Enemy Stats(E) | Help(H):

Inputting A then hitting enter will attack the enemy, but the enemy will also attack you. When an enemy attacks you, 
the damage they do will be mitigated by how much armor you have, so if the enemy does 25 damage, and you have 10 armor,
the enemy will only do 15 damage. 


Defending:
When you defend, it takes the amount of armor your shield has, multiplies it by 2,
which becomes your chance to stun the enemy. So if your sheild has 20 armor, then your chance to stun an enemy when
you block is 40%, up to a maximum of 65. 


Running:
When you run, it takes your agility and multiplies it by 1.2, then subtracts
the enemies agility. So the formula looks like this: RunChance = (agility * 1.2) - enemyAgility. So if your agility
is 10, and the enemies agility is 5, then your run chance is 7%. When you run, it ends the encounter.


Levelling:
Levelling is straightforward, there are exp requirements for each level, and when you meet the requirement, you level up.
When you level up, you are granted 5 stat-points, which you can allocated to either: Attack, Defence or Agility. Each time
you allocate stat-points, you allocate them in 5-point increments. Below is an example of a character levelling up 3 times
in a row after being granted exp:

You levelled up
You levelled up
You levelled up
You have: 15 Attribute points to spend

Allocate 5 stats to: Attack(ATK) | Defence(DEF) | Agility(AGI):

If I wanted to allocate 5 points to attack, i would input: ATK and hit enter.


Stats:
There are 3 main stats in Trials Of The Wanderer: Attack, Defence, Agility. Attack increases the damage you do to enemies,
1 point of attack means 1 point of damage increase. Defence decreases the amount of damage enemies do to you, 1 point of 
defence is 1 damage reduced.


Items:
Each item has 3 properties: Name of the item, Type of the item, damage or defence of the item. 
For this item: ("Bruised Iron Leggings", "Legs", 5), Bruised Iron Leggings is the name, Legs is the type of item
and 5 is the defence of the item.


Equipment:
An important aspect of the game is inventory management, and the equipment menu is how you interact with your inventory.
Below are the valid options in the equip menu:
Equip options: Equip(E) | Unequip(U) | Discard(D) | Help(H) | Back(B):

Each option is descriptive of what it does: Equip allows you to equip items, Unequip allows you to unequip items, etc.
But where it get's interesting is the inventory display itself: 
Your Inventory: {'Slot0': None, 'Slot1': None, 'Slot2': None, 'Slot3': None, 'Slot4': None, 'Slot5': None, 'Slot6': None, 'Slot7': None, 'Slot8': None, 'Slot9': None, 'Slot10': None, 'Slot11': None, 'Slot12': None, 'Slot13': None, 'Slot14': None, 'Slot15': None, 'Slot16': None, 'Slot17': None, 'Slot18': None, 'Slot19': None, 'Slot20': None}

Your Equipped Items: {'Weapon': None, 'Shield': None, 'Head': None, 'Chest': None, 'Arms': None, 'Hands': None, 'Legs': None, 'Feet': None}

Help(H) | Back(B) | Equip item(Slot#):

The "Your Inventory" section displays all of the items in your inventory, in the "Your Equipped Items" section, it displays
all of your currently equipped items. In order to equip an item, you must specify the slot number of the item to equip. So 
if you had a ('Horned Helm', 'Head', 20), which is a piece of armor for the "Head" armor slot, that grants you 20 defence,
and it was located in Slot0, to equip it you could input: "Slot0". This would equip the helmet to your "Head" armor slot, 
granting you 20 defence. In order to unequip items, you say the name of the item, so to unequip the Horned Helm, I would 
go to the Unequip Menu, and input "Horned Helm". This would unequip the item, decreasing my defence by 20.


