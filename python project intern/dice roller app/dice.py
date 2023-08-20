import random

DICE_ART={
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])

def print_dice(n):
    for i in DICE_ART[n]:
        print(i)
    
def get_number(n):
    l=[]
    for i in range(n):
        l.append(random.randint(1,6))
    return l

print('Welcome to rolling dice')
n=int(input('enter no of dices used:'))

dices={1:[]}

while(True):
    print('if you want to continue please enter 1 if not enter 2')
    if(int(input())!=1):
        break;
    l=get_number(n)
    print("The dice looks like:")
    for i in l:
        print_dice(i)
