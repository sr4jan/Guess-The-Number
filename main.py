import random
n1 = random.randint(1,100)
a = -1
print("*****LET'S PLAY GUESS THE NUMBER*****\nGuess a number between 1 to 100")
p1 = input("Enter Player 1 name: ")
guesses1 = 1
while(a != n1):
    a = int(input("Guess the number: "))
    if(a>n1):
        print("Lower number please")
        guesses1 += 1
    elif(a<n1):
        print("Higher number please")
        guesses1 += 1
        
print(f"{p1} has guessed the number correctly in {guesses1} attempts")

n2 = random.randint(1,100)
p2 = input("Enter Player 2 name: ")
guesses2 = 1
while(a != n2):
    a = int(input("Guess the number: "))
    if(a>n2):
        print("Lower number please")
        guesses2 += 1
    elif(a<n2):
        print("Higher number please")
        guesses2 += 1
        
print(f"{p2} has guessed the number correctly in {guesses2} attempts")

if (guesses1 > guesses2):
    print(f"{p2} wins!!")
elif (guesses1 < guesses2):
    print(f"{p1} wins!!")
else:
    print("It's a tie!")
