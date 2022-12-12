# Requirements
# The program must also meet the following requirements.

# The program must include a README file.
# The program must include class and method comments.
# The program must have at least four classes.
# The program must remain true to game play described in the overview.

# The puzzle is a secret word randomly chosen from a list.
# The player guesses a letter in the puzzle.
# If the guess is correct, the letter is revealed.
# If the guess is incorrect, a line is cut on the player's parachute.
# If the puzzle is solved the game is over.
# If the player has no more parachute the game is over.

import random
from turtle import begin_fill

# a class to get a random word
class Word:
    def __init__(self) -> None:
        pass

    # the generator method
    def wordGen(self):

        # this is from https://simple.wikipedia.org/wiki/List_of_fruits
        words = [
            "Abiu",
            "Acai",
            "Acerola",
            "Akebi",
            "Ackee",
            "African Cherry Orange",
            "American Mayapple",
            "Apple",
            "Apricot",
            "Araza",
            "Avocado",
            "Banana",
            "Bilberry",
            "Blackberry",
            "Blackcurrant",
            "Black sapote",
            "Blueberry",
            "Boysenberry",
            "Breadfruit",
            "Buddhas hand",
            "Cactus pear",
            "Canistel",
            "Cashew",
            "Cempedak",
            "Cherimoya",
            "Cherry",
            "Chico fruit",
            "Cloudberry",
            "Coco De Mer",
            "Coconut",
            "Crab apple",
            "Cranberry",
            "Currant",
            "Damson",
            "Date",
            "Dragonfruit",
            "Durian",
            "Egg Fruit",
            "Elderberry",
            "Feijoa",
            "Fig",
            "Finger Lime",
            "Goji berry",
            "Gooseberry",
            "Grape",
            "Raisin",
            "Grapefruit",
            "Grewia asiatica",
            "Guava",
            "Hala Fruit",
            "Honeyberry",
            "Huckleberry",
            "Jabuticaba",
            "Jackfruit",
            "Jambul",
            "Japanese plum",
            "Jostaberry",
            "Jujube",
            "Juniper berry",
            "Kaffir Lime",
            "Kiwano",
            "Kiwifruit",
            "Kumquat",
            "Lemon",
            "Lime",
            "Loganberry",
            "Longan",
            "Loquat",
            "Lulo",
            "Lychee",
            "Magellan Barberry",
            "Mamey Apple",
            "Mamey Sapote",
            "Mango",
            "Mangosteen",
            "Marionberry",
            "Melon",
            "Cantaloupe",
            "Galia melon",
            "Honeydew",
            "Mouse melon",
            "Musk melon",
            "Watermelon",
            "Miracle fruit",
            "Momordica fruit",
            "Monstera deliciosa",
            "Mulberry",
            "Nance",
            "Nectarine",
            "Orange",
            "Blood orange",
            "Clementine",
            "Mandarine",
            "Tangerine",
            "Papaya",
            "Passionfruit",
            "Pawpaw",
            "Peach",
            "Pear",
            "Persimmon",
            "Plantain",
            "Plum",
            "Prune",
            "Pineapple",
            "Pineberry",
            "Plumcot",
            "Pomegranate",
            "Pomelo",
            "Purple mangosteen",
            "Quince",
            "Raspberry",
            "Salmonberry",
            "Rambutan",
            "Redcurrant",
            "Rose apple",
            "Salal berry",
            "Salak",
            "Sapodilla",
            "Sapote",
            "Satsuma",
            "Shine Muscat",
            "Sloe",
            "Soursop",
            "Star apple",
            "Star fruit",
            "Strawberry",
            "Surinam cherry",
            "Tamarillo",
            "Tamarind",
            "Tangelo",
            "Tayberry",
            "Ugli fruit",
            "White currant",
            "White sapote",
            "Ximenia",
            "Yuzu",
        ]
        num = random.randint(0, len(words) - 1)
        word = words[num]
        return word


# a class for the board display
class Board:
    def __init__(self, guesses, game, checked, wrong, right, word, already, final):
        self.index = guesses
        self.status = game
        self.guess = checked
        self.wrong = wrong
        self.right = right
        self.word = word
        self.already = already
        self.final = final
        self.blanks = ""

    # display parachute in phases depending on number of guesses
    def chute(self):
        CHUTE_PHASES = [
            """\t \\ /""",
            """\t\\   /""",
            """\t/___\\""",
            """\t ___""",
        ]
        for i in range(self.index, -1, -1):
            print(CHUTE_PHASES[i])

    # display head, if game over then head is X
    def head(self):
        if self.status == 1:
            print("\t  O")
        else:
            print("\t  X")

    # display body
    def body(self):
        print("\t /|\\")
        print("\t  |")
        print("\t / \\")

    def blank(self):
        # finds the guess in the word

        for letter in self.word:
            if self.already.find(letter) > -1:
                self.blanks = self.blanks + letter
                self.final = self.blanks
            else:
                self.blanks = self.blanks + "_"
                self.final = self.blanks

    def display(self):
        print(self.blanks, end=" ")

        # prints the wrong guesses so the player knows what they guessed already
        print("\n\nWrong guesses:")
        for character in self.wrong:
            print(character, end=", ")
        print()

        return self.final


# a class for checking if a guess is valid
class Checker:
    def __init__(self, already):
        self.already = already

    # a method to check if the guess is:
    # 1) a single character
    # 2) not already guessed
    # 3) a valid english letter
    def check(self):
        while True:
            print(f"\nYou have {guesses + 1} guesses left.\n")
            print("Guess a letter (spaces are valid guesses).")
            guess = input(">>> ").lower()
            if len(guess) != 1:
                print("\nEnter a single character.")
            elif guess in self.already:
                print("\nYou've already guessed that, try again.")
            elif guess not in "abcdefghijklmnopqrstuvwxyz ":
                print("\nEnter a valid English letter.")
            else:
                return guess


# a class for comparing the guesses with the word
class Compare:
    def __init__(self, checked, word, final):
        self.checked = checked
        self.word = word
        self.final = final

    # a method for comparing if a letter is in the word
    def compare(self):
        if self.checked in self.word:
            return 1
        else:
            return 0

    def guessed(self):
        if "_" in self.final:
            return 3
        else:
            return 2


# player starts with 4 incorrect guesses left and that the game is going
guesses = 3
game = 1
wrong = ""
right = ""
already = ""
final = "_"
# gets random word from list
randomWord = Word()
word = randomWord.wordGen().lower()

while game:
    print("\n===========================================")
    guess = Checker(already)
    checked = guess.check()

    compare = Compare(checked, word, final)
    compared = compare.compare()

    if compared == 0:
        wrong += checked
        guesses -= 1
        if guesses < 0:
            print("\nYou lose, game over!")
            print(f'\nThe word was "{word}".\n')
            game = 0
    elif compared == 1:
        right += checked

    already = wrong + right

    # display the board as long as the game is still running

    display = Board(guesses, game, checked, wrong, right, word, already, final)

    if game == 1:
        display.chute()
    display.head()
    display.body()
    print()
    display.blank()
    final = display.display()

    display = Board(guesses, game, checked, wrong, right, word, already, final)
    compare = Compare(checked, word, final)
    guessed = compare.guessed()
    if guessed == 2:
        print("\nYou win, game over!")
        print(f'\nThe word was "{word}".\n')
        game = 0

    elif guessed == 3:
        pass
