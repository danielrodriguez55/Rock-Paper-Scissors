# Creator: Daniel E. Rodriguez Olivera
# Rock Paper Scissors
import random

print('Welcome to Rock Paper Scissors')

best = str(input("Would you like to have a best of five?? Yes or No?? "))
best = best.lower()

gamer = str(input('Make your choice (rock, paper, or scissors): '))
gamer = gamer.lower()
print('You chose ' + gamer)

computer = random.choice(['rock', 'paper', 'scissors'])
print('I chose ' + computer)

gamerscore = 0
computerscore = 0


def rock():
    if computer == 'rock':
        print("It's a tie we both suck")
    elif computer == 'paper':
        global computerscore
        computerscore += 1
        print("Jaja I covered you")
    else:
        global gamerscore
        gamerscore += 1
        print("Why did you have to smash me")


def paper():
    if computer == 'rock':
        global gamerscore
        gamerscore += 1
        print("It's so dark in here")
    elif computer == 'paper':
        print("It's a tie we both suck")
    else:
        global computerscore
        computerscore += 1
        print("Too bad you're shredded")


def scissors():
    if computer == 'rock':
        global computerscore
        computerscore += 1
        print("Jaja you just got smashed")
    elif computer == 'paper':
        global gamerscore
        gamerscore += 1
        print("Guess it's my turn to get shredded")
    else:
        print("It's a tie we both suck")


if gamer == 'paper':
    paper()

elif gamer == 'rock':
    rock()

elif gamer == 'scissors':
    scissors()

print('Score: You(' + str(gamerscore) + ') Me(' + str(computerscore) + ')')

if best == 'yes':
    while gamerscore != 3 and computerscore != 3:
        gamer = str(input('Make your choice (rock, paper, or scissors): '))
        gamer = gamer.lower()
        print('You chose ' + gamer)

        computer = random.choice(['rock', 'paper', 'scissors'])
        print('I chose ' + computer)

        if gamer == 'paper':
            paper()

        elif gamer == 'rock':
            rock()

        elif gamer == 'scissors':
            scissors()

        print('Score: You(' + str(gamerscore) + ') Me(' + str(computerscore) + ')')
    if gamerscore == 3:
        print("I guess humans are the superior race")

    elif computerscore == 3:
        print("It's about time you learn your inferiority")
