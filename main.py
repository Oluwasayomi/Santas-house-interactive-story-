#Santa's house descriptive task.

import time

print("Welcome players... to the immensive interactive story 'Santa's house.'")

time.sleep(1)

print("*pauses for a dramatic moment*")

time.sleep(1)

print(
  "Be cautious or be adventerous. This is all a matter of what YOU choose.")

start = input("Would you like to start this story? (yes/no): ").lower()

if start == "no":
  print("Oh, what a pity. I guess this is where we part. Bye stranger.")
  quit()
elif start == "yes":
  print("Awesome! Let's start.\n")
else:
  print("Invalid option.")
  quit()

time.sleep(1)

print("Santa's house...\n")

time.sleep(1)

print(
  "A fantastically fantasy-like dreamy house. Red lights everywhere, blinking jovially, exchanging- intertwining with its neighbours; The green lights."
)
print(
  "Together,the two neighbourly friends, they danced around the exterior part of Santa's house.\n"
)

time.sleep(2)

print(
  "A pure white snowman stood guard at the front of the door-\n'Wait! Isn't that door made out of gingerbread?!' you thought, surprised.\n"
)

time.sleep(2)

print(
  '"Indeed it is, dear player. It is made out of delicious, mouthwatering, yummilicious gingerbread!"\n'
)

time.sleep(2)

print(
  'You were surpised by the sudden voice that whispered in your right ear.\n"Relax player, it is just me, the narrator."'
)

name = input(
  '"Oh! Or would you prefer to be referred to by your name?" (yes/no): '
).lower()

if name == "no":
  print(
    '"Alright then player, we shall continue as we were" the voice said, whispering into your other ear'
  )
  name = "player"
elif name == "yes":
  name = input(
    '"Alright, what will your name be, player?" (type in your name): ')
  print(f'"Noted {name}"')
else:
  print("Invalid option.")
  quit()

print(f'\n"Let us carry on with the story now. Shall we, {name}?"\n')

time.sleep(1)

print(
  '"What a delight!" you might think as you smelled the tempting smell of the ginerbread and a mysterious smell that smells just as tasty.'
)

enter = input(
  f'"Would you like to go into Santas house, {name}?" (yes/no): ').lower()

if enter == "no":
  print(
    '"Oh well, I guess that ends our tour. Hope you enjoyed the little you were able to see."'
  )
  print(f'"I hope to see you soon {name}. It was nice playing with you"\n')
  time.sleep(3)
  print("THE END.\n")
  time.sleep(6)
  print(f"You lucky lucky {name}... you managed to survive.")
  quit()
elif enter == "yes":
  print(
    "You opened the gingerbread door and entered the house.\nYour eyes grew wide with surpise when you saw what was in Santa's house.\n"
  )
  time.sleep(2)
  print(
    "The decoration inside and the delicious snacks laids on a beautiful silver platter weren't what drew your surpise.\n"
  )
  time.sleep(2)
  print(
    "No, you didn't have the oh-I-am-so-pleasantly-surprised type of surprise.\n"
  )
  print("No, definitely not that type of surprise.\n")
  time.sleep(2)
  print(
    "It was the type of surprise brought up by a shocking large amount of fear..."
  )
  time.sleep(2)
  print(
    "One that made you want to leave Santa's house immediately you saw the blood red stains on the floor."
  )
  time.sleep(3)
else:
  print("Invalid option.")
  quit()

door = input(
  "Do you want to open the door and get out of the house? (yes/no): ").lower()

if door == "no":
  print(
    "Your feet felt glued down to the ground and your heart rate increase.\n")
  time.sleep(2)
  print(
    "You hear the door open behind you but before you could look at who came in, you felt something sharp impale you and everything went dark.\n"
  )
  time.sleep(2)
  print("THE END.\n")
  time.sleep(3)
  print(
    f'"Oh my {name}, it seems you died. What a pity"\n"No worries, you can always restart the game and choose some better(?) choices"'
  )
elif door == "yes":
  print("You whip back quickly to try and open the door but-")
  time.sleep(1)
  print('"Oh my! It seems someone-" Santa?! "-locked you in"\n')
  time.sleep(2)
  print(
    "The once deliciously tempting gingerbread house now encompassed around you like a cage."
  )
  print(
    "It felt like a jail with its sickenly metallic smell wafting around. The blood all around the room upsetted your stomach.\n"
  )
  time.sleep(2)
  print(
    "You turn to the side to expel your previous dinner out of your stomach.")
  time.sleep(2)
  print('"What a pity..."')
  time.sleep(1)
  print(
    "If only you didn't learn Santa's secret, that wouldn't have been your last dinner...\n"
  )
  time.sleep(3)
  print("THE END.\n")
  time.sleep(2)
  print(
    f'"Oh my {name}, it seems you lost this time. What a pity"\n"No worries though, you can always restart the game and choose some better(?) choices"'
  )
else:
  print("Invalid option.")
  quit()

print("Thanks for playing Santa's house!")
