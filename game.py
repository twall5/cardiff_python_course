
import sys
import random
#if three cmd line arguments are not supplied
#   exit application
if len(sys.argv) != 3:
    exit(1)
gamefile = sys.argv[1]
guessesallowed = sys.argv[2]
#if number of guesses is not an integer,
#   exit application
if guessesallowed.isalpha() == 'True':
    print('Number of guesses includes alphabetic character')
    exit(2)
else:
    guessesallowed = int(guessesallowed)
#if file containing words cannot be opened,
#   exit application
try:
    file = open(str(gamefile), 'r')
except IOError:
    print("File '%s' cannot be opened." % gamefile)    
    exit(3)
#read the lines from the file
#add each word in the line to a list of words
fruitlist = []
file = open('fruit','r')
for line in file:
    line = line[:-1]
    fruitlist.append(line)
file.close()
fruits = ' '.join(fruitlist)
fruitlist = fruits.split(' ')
#select a word at random from the list of words
word = fruitlist[random.randint(0,8)]
#get length of chosen word
wordlen = len(word)
#checks that the number of allowed guesses is enough for the word
if guessesallowed < wordlen:
    print('Number of allowed guesses not enough for the word picked. Please try again.')
    exit(4)
#create a list of this length containing asterisks
hiddenword = '*' * wordlen
#output list of asterisks to screen
print(hiddenword)
#sets variable to be updated by while loop
guessnumber = 1
#converts strings to lists
showletters = list(hiddenword)
wordletters = list(word)
#while guesses not used and word not guessed
while guessnumber <= guessesallowed and hiddenword != word: 
# ask user to guess a letter
    guess = input('Please guess a letter contained in the word: ')
    guess = guess.lower()
    if len(guess) > 1:
        print('Only 1 letter may be guessed at a time!')
    else:
#   for all occurrences of the letter in chosen word,
#       replace asterisk by letter in list containing asterisks
        for i in range(wordlen):
            if wordletters[i] == guess:
                showletters[i] = guess
                hiddenword = ''.join(showletters)
# output list containing letters and asterisks    
        print(hiddenword)
        guessnumber += 1
if hiddenword == word:
    print("Well Done")
elif hiddenword != word:
    print("Hard Luck")
exit(0)
