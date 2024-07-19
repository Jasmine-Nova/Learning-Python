import random

# Function to ask for player's name
def ask_name():
    for attempt in range(10):
        try:
            player_name = input("Please Enter the name you would like to play as: ").strip()
            if len(player_name) <= 30:
                return player_name
            else:
                print("Name is too long, please enter a name up to 30 characters long")
        except KeyboardInterrupt: #quit if someone wants to ctrl c 
            exit()
    print("Failed to enter a valid name. Exiting.")
    exit()

# Function to ask for integer output between 1 and max_value
def ask_int(max_value):
  while True:
    try:
      x = int(input(f"Enter integer answer betwee 1 and {max_value}: "))
    except ValueError:
      print(f"Input Error: please select an integer from 1 to {max_value}")
      continue
    except KeyboardInterrupt: #quit if someone wants to ctrl c 
        exit()
    if 1 <= x <= max_value:
      return x
    else:
      print(f"Input Error: please enter an integer from 1 to {max_value}")

# list of possible weapons and their damage
weapon_list = ( 
    ("fists", 1),
    ("wooden sword", 2),
    ("dagger", 3),
    ("axe", 4),
    ("short sword", 5),
    ("long sword", 6),
    ("bo staff", 7),
    ("spear", 8),
    ("Spongebob's spatula", 10)
    )

# list of possible armor and their defense
armor_list = (
    ("naked", 1),
    ("cloth tunic", 2),
    ("padded armor", 3),
    ("studded leather", 4),
    ("chain mail", 5),
    ("scale mail", 6),
    ("plate mail", 7),
    ("full plate", 8),
    ("Sandy's suit", 10)
)


# player start naked without a weapon
player_name = "NO-NAME"
player_damage = weapon_list[0][1]
player_defense = armor_list[0][1]
player_health = 100
player = [player_name, player_damage, player_defense, player_health]

# function to calculate damage dealt from attack
def deal_damage(attacker, defender):
    attacker_name, attacker_damage, _, _ = attacker
    defender_name, _, defender_defense, _ = defender
    # 5% dodge chance
    if random.randint(1,100) <= 5:
        print("Attack is dodged!")
        return 0
    # damage dealt
    damage_dealt = round(attacker_damage * 5 / (5 + defender_defense))
    if random.randint(1,100) <= 5: # critical strike
        damage_dealt *= 2
        print("A critical strike! The damage is doubled") 
    #text output for player
    print(f"{attacker_name} attacked {defender_name} and dealt {damage_dealt} damage!")
    return damage_dealt

# Function to list the stats of player or enemies
def list_stats(entity):
    name, damage, defense, health = entity
    print(f"""{name} stats:
  health: {health}
  damage: {damage}
  defense: {defense}\n""")

# Function to simulate combat by changing outside variables
def combat(monster):
   while True:
        monster[3] -= deal_damage(player, monster)
        monster[3] = max(0, monster[3])
        if monster[3] == 0:
            return print(f"{monster[0]} has been slain!\n")
        print(f"{monster[0]} has {monster[3]} hp remaining!")
        print("\n")
        player[3] -= deal_damage(monster, player)
        player[3] = (max(0, player[3]))
        if player[3] == 0:
            return print(f"{player[0]} has unfortunately died, good luck next time!\n")
        print(f"{player[0]} has {player[3]} hp remaining!")
        print("\n")

# Function to ask the play if they want to fight the enemy found
def ask_fight(monster):
    print("Ahead of you you have found a creature")
    list_stats(monster)
    print(f"Would you like to fight this {monster[0]}\n 1. Yes\n 2. No, take a different path\n")
    return ask_int(2)

# Function to generate random weapon/armor
# Stronger monsters are more likely to drop better loot
def reward(number):
    big_number = (2*number + 1)
    if big_number > 8:
        big_number = 8
    weapon = weapon_list[random.randint(max(1,number), big_number)]
    armor = armor_list[random.randint(max(1,number), big_number)]
    print("\nCongratulations, you have survived the battle and found a weapon and armor!")
    print(f"The {weapon[0]} has {weapon[1]} damage")
    print(f"The {armor[0]} has {armor[1]} defense")
    print(f"Your current weapon has {player[1]} damage and your current armor has {player[2]} defense")
    print(f"""
    1. Replace both weapon and armor
    2. Replace only your weapon
    3. Replace only your armor
    4. Keep your current weapon and armor
    """)
    choice = ask_int(4)
    if choice == 1:
        player[1] = weapon[1]
        player[2] = armor[1]
        print("You have replaced both weapon and armor")
    elif choice == 2:
        player[1] = weapon[1]
        print("You have replaced your weapon")
    elif choice == 3:
        player[2] = armor[1]
        print("You have replaced your armor")
    else:
        print("you kept your current weapon and armor")

        

#starting main function
player[3] = 100
player[0] = ask_name()
print(f"""\nHello {player[0]}!\n 
You have found yourself without any armor nor weapon besides your fists in this maze full of monsters!!
The only way out of this maze is to find and kill Mr. Krabs.
You will need to travel across many of the paths in this maze to find and kill him.
However, you would be wise to pick you fights carefully.
Killing enemies drops loot. You can find armor and weapons.

here are your stats: 
  health: 100 
  damage: 1 
  defence: 1

Would you like to continue? 
1. Yes
2. No, exit this game
""")
play = ask_int(2)
if play == 1:
    # First monster is always little worm
    number = 0
    # start combat
    while True:
        # generating monsters on each iteration
        monster1 = ["little worm", 1, 1, 5]
        monster2 = ["big maggot", 2, 1, 10]
        monster3 = ["rabid wolf", 2, 2, 15]
        monster4 = ["grizzly bear", 2, 4, 20]
        monster5 = ["shark monster", 4, 3, 30]
        monster6 = ["Mr. Krabs", 8, 8, 50]
        monsters = (monster1, monster2, monster3, monster4, monster5, monster6)
        monster = monsters[number]
        fight = ask_fight(monster)
        if fight == 1:
            print("\n")
            combat(monster)
            # end of combat reward
            if player[3] > 0: 
                reward(number)
                if monster == monster6:  # defeating Mr. Krabs wins the game
                    print("Congratulations, you have defeated Mr. Krabs and won this game!")
                    exit()
            # player has died
            if player[3] == 0:
                print("＊*•̩̩͙✩•̩̩͙*˚　Bye Bye　˚*•̩̩͙✩•̩̩͙*˚＊\n")
                exit()
        # selecting random monster to fight, excluding little worm
        number = random.randint(1,5)
else:
    print("＊*•̩̩͙✩•̩̩͙*˚　Bye Bye　˚*•̩̩͙✩•̩̩͙*˚＊\n")

