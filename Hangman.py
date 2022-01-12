import random

name=input("Enter your Name: ")
print("All the best", name)

words=["Reactjs","Angular","javascript","computer","science","programming","python","java","html"]

word=random.choice(words)
print("\nGuess the Characters")
guesses=" "
turns=10
while turns>0:
    failed=0

    for char in word:
        if char in guesses:
            print(char,end=" ")

        else:
             print("_",end=" ")
             failed+=1
    if failed==0:
        print("\n\nYou Win")
        print("\nThe word is:",word)
        break

    guess=input("\n\nguess the character:")
    guesses +=guess
    if guess not in word:
        turns -=1

        print("\nWrong")

        print("\nYou have",+turns,"more guesses")
        if turns==0:
            print("\n\nYou lose")

