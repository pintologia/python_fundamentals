import random as r

def roll_dice():
    dice_total = r.randint(1, 6) + r.randint(1, 6)
    return dice_total

player1=input('Enter players one name: \n')
player2=input('Enter players two name: \n')

roll1 = roll_dice()
roll2 = roll_dice()

print(player1, 'rolled', roll1 )
print(player2, 'rolled', roll2)

if roll1 > roll2:
    print(player1, 'WINS')
elif roll1< roll2:
    print(player2, 'WINS')
else:
    print('DRAW')