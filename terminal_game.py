import random
from player import Player

npchp = 100

print("Welcome to the terminal game.")

nam = input("What is your name? ")

x = Player(nam)

while x.hp > 0:
    no = random.randint(1, 5)

    # Predict damage without applying it
    if no == 1:
        print('You dealt 5 damage')
        dmg = 5
    elif no == 2:
        print('You dealt 7 damage')
        dmg = 7
    elif no == 3:
        print('You dealt 10 damage')
        dmg = 10
    elif no == 4:
        print('Woo, you got some moves huh?')
        dmg = 0
    else:
        dmg = 0  # Fallback in case random returns unexpected value

    if x.hp - dmg > 0:
        x.damage(no)
    else:
        print("You died !!!")
        break

    print(f"Your current HP: {x.hp}")

    at = input("What do you want to do? (0 = heal, 1 = normal attack, 2 = great attack, 3 = power attack): ")

    if at == "0":
        print("You healed!")
        x.heal(1)  # You need to pass a value; assuming 1 for 5 HP heal
    elif at == "1":
        print("You did a normal attack!")
        npchp -= 7
    elif at == "2":
        print('You did a great attack!')
        npchp -= 10
    elif at == "3":
        print('You did a power attack!')
        npchp -= 12

    if npchp <= 0:
        print('YOU WON!!!!')
        break
    
    print(f"NPC HP: {npchp}")
