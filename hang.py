import random
import string

def load_words():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    WORDLIST_FILE = "palavras.txt"
    print '\nLoading word list from file...\n'
    # in_file: file
    in_file = open(WORDLIST_FILE, 'r', 0)
    # line: string
    line = in_file.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    #checks if file is empty of words
    is_wordlist_empty(wordlist)
    print '    ', len(wordlist), 'words loaded.\n'

    return random.choice(wordlist)

def is_wordlist_empty(wordlist):
    if len(wordlist) == 0:
        print 'File empty!\nBe sure that your word file is not empty!\n'
        exit(0)

def is_word_guessed(secret_word, letters_guessed):

    for letter in secret_word:
        if letter in letters_guessed:
            pass
        else:
            return False
    return True

def guessed_word(letters_guessed):

     guessed = ''
     for letter in secret_word:
         if letter in letters_guessed:
             guessed += letter
         else:
             guessed += '_ '

     return guessed

def available_letters(letters_guessed):
    # 'abcdefghijklmnopqrstuvwxyz'
    is_available = string.ascii_lowercase
    #checks if is_available has the correct letter format
    #otherwise it throws an AssertionError
    if not is_available == 'abcdefghijklmnopqrstuvwxyz':
        raise AssertionError()

    for letter in is_available:
        if letter in letters_guessed:
            is_available = is_available.replace(letter, '')

    return is_available

def hangman(secret_word):

    guesses = 8
    letters_guessed = []

    print 'Welcome to the game, Hangman!\n'
    print 'I am thinking of a word that is', len(secret_word), 'letters long.'
    print '-------------\n'

    while  is_word_guessed(secret_word, letters_guessed) == False and guesses >0:
        print 'You have', guesses, 'guesses left.'

        available = available_letters(letters_guessed)
        print 'Available letters', available, '\n'

        letter = raw_input('Please guess a letter: ')

        if letter in letters_guessed:
            guessed = guessed_word(letters_guessed)

            print 'Oops! You have already guessed that letter: ', guessed

        elif letter in secret_word:
            letters_guessed.append(letter)
            guessed = guessed_word(letters_guessed)

            print 'Good Guess: ', guessed

        else:
            guesses -= 1
            letters_guessed.append(letter)
            guessed = guessed_word(letters_guessed)

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------\n'

    else:
        if is_word_guessed(secret_word, letters_guessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was', secret_word, '.'

secret_word = load_words().lower()
hangman(secret_word)
