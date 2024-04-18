

import random
word_bank = ["prettiest","close","massive","hollow","cultured","seashore","explode","dizzy","minister","competent",
"thoughtful","harbor","tidy","dance","children","zesty","clean","ball","nostalgic","plan","week","strap","board",
"slope","bat","steep","mourn","cat","girl","ancient","street","mice","dare","wasteful","tub","limping","whimsical",
"eager","eggs","detail","experience","beds","train","place","cows","admit","rare","respect","loose","group","enjoy",
"internal","macabre","imported","crooked","confused","hug","unkempt","coal","meddle","hapless","country","zealous",
"sick","pray","lake","tiny","key","empty","labored","delirious","ants","need","omniscient","onerous","damp","subtract",
"sack","connection","toad","gather","record","new","trashy","flow","river","sparkling","kneel","daughter","glue",
"allow","raspy","eminent","weak","wrong","pretend","receipt","celery","plain","fire","heal","damaging","honorable",
"foot","ignorant","substance","crime","giant","learned","itchy","smoke","station","jaded","innocent"]

def select_random_word():
    return random.choice(word_bank)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def letter_guess(word):
    guessed_letters = set()
    while True:
        print("Word:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ")
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        guessed_letters.add(guess)
        if guess in word:
            print("Good job! You guessed a letter correctly.")
        else:
            print("Sorry, that letter is not in the word.")
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word:", word)
            break

def hangman():
    selected_word = select_random_word()
    print("The word has", len(selected_word), "letters.")
    letter_guess(selected_word)

hangman()
