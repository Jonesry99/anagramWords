from itertools import permutations
from math import factorial


def error():
    return print("Invalid input, try again")


def repeat():
    userChoice = input("Would you like to do something else?\n(Y/N): ")
    if userChoice.upper() == "Y":
        menu()
    elif userChoice.upper() == "N":
        None
    else:
        error(), repeat()


def compareWord():
    flag = False
    text1 = input("Please enter your chosen 1st word: ").lower()
    text2 = input("Please enter your chosen 2nd word: ").lower()
    perms1 = permutations(text1)
    perms2 = permutations(text2)
    for results in list(perms1):
        for results2 in list(perms2):
            if results == results2:
                flag = True
    if flag:
        print('The two words are perfect anagrams of one another!')
    else:
        print('The two words are not perfect anagrams of one another!')
    repeat()


def factorialWord():
    text = input("Please enter your chosen word: ")
    print("There are", factorial(len(text)), "different ways of arranging the word", text.upper())
    repeat()


def permutationWord():
    text = input("Please enter your chosen word: ")
    perms = permutations(text)
    for results in list(perms):
        print(*results, sep=" ")
    repeat()


def menu():
    try:
        userChoice = int(
            input("Please choose from the following:\n1. Permutations of a Word\n2. Factorial of a Word\n3. "
                  "Compare Words for Anagrams\n?: "))
        if userChoice == 1:
            permutationWord()
        elif userChoice == 2:
            factorialWord()
        elif userChoice == 3:
            compareWord()
        else:
            error(), menu()

    except ValueError:
        error(), menu()


if __name__ == '__main__':
    menu()
