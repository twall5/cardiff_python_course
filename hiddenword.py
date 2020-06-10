word = 'pythonp'
wordlen = len(word)
hiddenword = '*' * wordlen
print(word)
print(hiddenword)
guess = input('Enter guess: ')
showletters = list(hiddenword)
wordletters = list(word)
print(showletters)
print(wordletters)
guessindex = word.find(guess)
print(guessindex)
showletters[guessindex] = guess
hiddenword = ''.join(showletters)
print(hiddenword)
numoccurrences = wordletters.count(guess)
print(wordletters.count(guess))
i = 0
for i in range(wordlen):
    if wordletters[i] == guess:
        showletters[i] = guess
print(showletters)
        