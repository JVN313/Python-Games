
main_char = input("WELCOME TO THE ADVENTURE OF MIGHT \nEnter Your Character's Name: ")
playing = True
starting_weapons = ["THE HOLY SWORD","THE SPEAR OF MIGHT","THE STAFF OF MANA"]
subweapons = ["SHIELD","DAGGER","SPELLBOOK"]
base_spells = ["EMBER","ICE SHARD"]
player_weapon = ""
player_subweapon = ""
path_choice = ""
player_health = 100

print("And Now The Journey Begins")
print("You start your journey in the village temple. You have been summoned there by the Head Priest Artico\n")
print("Artico: " +main_char+" I have summoned you here because our world is in grave danger. The evil Black Knight has come into\nthe possesion of The Dark Crystal , and is using its unholy powers to conjure monsters all throughout the land.\nIt's up to you to stop him and destroy The Dark Crystal so its powers can never be used again.\nTo help you on your journey to the Tower Of Doom where the Black Knight resides, I will give you a choice of one of three of the temples holy weapons\nWhich shll you take?")

player_weapon = input("CHOOSE YOUR WEAPON\na)The Holy Sword\nb)The Spear of Might\nc)The Staff of Mana ").upper()
if player_weapon == "A" or player_weapon == starting_weapons[0]:
    player_weapon = starting_weapons[0]
    print("You take "+player_weapon+" and start your journey to the Tower of Doom.")
    path_choice= input("You leave the temple and head down the road leading out the village and come to a crossroads.\nDo you take the Left path or the Right?: ").upper()

    if path_choice == "LEFT":
        print("You take the left path and the road leads to an ancient forest riddled with ghosts.\nAs you continue through the forest you become under siege by ghosts and ghouls.\nUsing your Holy Sword you overcome your attackers and push forward but you sustained damage from your battle.")
        print("As you continue through the forest you come across ancient ruins with a mysterious red glow inside.\nYou go into the ruins and are by two Living Suits of Armor! You enage in combat slashing away at your two foes until you are the last one standing")
        print("After you defeat your two enemies you push further into the ruins and to the source of the red glow. At the ruins center you find a Life Elixr")
    elif path_choice == "RIGHT":
        print("You meet a stranger")

    else:
        print("You Failed To Choose Now the World Is Doomed Game Over")
elif player_weapon == "B" or player_weapon == starting_weapons[1]:
    player_weapon = starting_weapons[1]
    print("You take "+player_weapon+" and start your journey to the Tower of Doom.")
elif player_weapon == "C" or player_weapon == starting_weapons[2]:
    player_weapon = starting_weapons[2]
    print("You take "+player_weapon+" and start your journey to the Tower of Doom.")
else:
    print("You Failed To Choose Now the World Is Doomed Game Over")

test = input('')