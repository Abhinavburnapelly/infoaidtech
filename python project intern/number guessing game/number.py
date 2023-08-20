import random

attempts=0
max_attempts=10
print("----------Welcome to the Number Guessing Game!!----------")
name=input('Enter your name:')

print('press \n1 to play the game\n2 to stop the game')
n=int(input())
print('---------------The Game is Starting---------------')
while(n==1):
    secret_number=random.randint(1,100)
    for i in range(max_attempts):
        a=int(input("Enter your guess number between 1-100:"))
        attempts+=1
        
        if(a==secret_number):
            print(f'Congratulations! You have guessed the number {secret_number} in {attempts} attempts!!!\n')
            break;
        elif(a>secret_number):
            print(f'Too high!! Try again.\n')
        else:
            print(f'Too low!! Try again.\n')
    else:
        print(f"\nSorry you are out of your chances...\n The number was {secret_number} \n Better luck next time!!!")
    print('\nDo you want to play the game again??')
    print('press \n1 to play the game\n2 to stop the game')
    n=int(input())
    attempts=0
print("----------Ending the Game....Hope you have enjoyed it!!!----------")