# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isLetterGuessed(chosenLetter, secretWord, lettersGuessed):
    '''
    chosenLetter: string, the letter the the user chose
    returns: boolean, True if chosenLetter is in lettersGuessed;
        False otherwise

    '''
    if chosenLetter in lettersGuessed:
        return True
    else:
        return False


def isLetterCorrect(chosenLetter, secretWord, lettersGuessed):
    '''
    chosenLetter: string, the letter the user chose
    returns: boolean, True if chosenLetter is in secretWord
        False otherwise
    '''
    if chosenLetter in secretWord and isLetterGuessed(chosenLetter, secretWord, lettersGuessed) == False:
        return True


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in secretWord:
        if i not in lettersGuessed:
            return False

    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    sofar = []

    for i in secretWord:
        if i not in lettersGuessed:
            sofar.append('_')
        else:
            sofar.append(str(i))
    string = ' '

    return string.join(sofar)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alpha = string.ascii_lowercase
    string = []
    string2 = ' '
    for i in alpha:
        if i not in lettersGuessed:
            string.append(i)
    return string2.join(string)


def addLetter(chosenLetter, lettersGuessed):
    return lettersGuessed.append(chosenLetter)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersLong = len(secretWord)

    guesses = 8
    lettersGuessed = []
    # wordIsGuessed = isWordGuessed(secretWord, lettersGuessed)
    # guessedWordsAre = getGuessedWord(secretWord, lettersGuessed)
    # availableLettersAre = getGuessedWord(lettersGuessed)
    # letterIsCorrect = isLetterCorrect(
    # chosenLetter, secretWord, lettersGuessed)
    # add = lettersGuessed.append(chosenLetter)
    loadWords()
    chooseWord(wordlist)
    print(' Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' +
          str(lettersLong) + ' letters long.')
    print('-------------')

    while guesses > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            return True
        else:
            print('You have ' + str(guesses) + ' guesses left.')
            print('Available letters: ' +
                  str(getAvailableLetters(lettersGuessed)))
            chosenLetter = input('Please guess a letter: ')
            letterIsCorrect = isLetterCorrect(
                chosenLetter, secretWord, lettersGuessed)

            if isLetterGuessed(chosenLetter, secretWord, lettersGuessed) == True:
                print("Oops! You've already guessed that letter: " +
                      getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
            elif isLetterCorrect(chosenLetter, secretWord, lettersGuessed) == True:
                addLetter(chosenLetter, lettersGuessed)
                print(
                    'Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
                guesses -= 1
            else:
                letterAdded = addLetter(chosenLetter, lettersGuessed)
                print(
                    "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
                guesses -= 1
    return False


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord=(wordlist).lower()
# hangman(secretWord)
secretWord = chooseWord(wordlist).lower()
won = hangman(secretWord)

if won == True:
    print('Congratulations, you won the game!')
else:
    print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
