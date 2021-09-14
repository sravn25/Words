import os
import re


def clear():

    if os.name == 'nt':
        os.system("cls")
    elif os.name == 'posix':
        os.system("clear")


def entry():
    s = input("Input a sentence or paragraph:\n")
    return s


def count(s):
    clear()
    print(s)
    # character count
    chars = len(s)
    print(chars, end=" ")
    if chars > 1:
        print("characters")
    else:
        print("character")

    # word count
    word = len(s.split())
    print(word, end=" ")
    if word > 1:
        print("words")
    else:
        print("word")


def search(s):
    word = input("Which word to find: ")
    occur = len(re.findall(word, s))
    print(f"The word \"{word}\" occured {occur}", end=" ")
    if occur > 1:
        print("times")
    else:
        print("time")


def freq(s):
    x = {char: s.count(char) for char in s}
    x = dict(sorted(x.items(), key=lambda item: item[1], reverse=True))
    for letter in x:
        if letter != " ": 
            print(letter, ":", x[letter])


def menu(s):
    while True:
        clear()
        print("Your sentence is: ")
        print(s, end="\n\n")
        print("1. Word and Character count")
        print("2. Occurence of word")
        print("3. Frequency of Words")
        print("4. Change sentence or paragraph")
        print("5. Quit")

        opt = input("\nWhat would you like to do?\n")

        if opt == "1":
            count(s)

        elif opt == "2":
            search(s)

        elif opt == "3":
            freq(s)

        elif opt == "4":
            s = entry()

        elif opt == "5":
            input("Goodbye")
            clear()
            raise SystemExit(0)

        else:
            print("Invalid option!")
            continue

        input("press ENTER to continue")


if __name__ == "__main__":
    s = entry()
    menu(s)
