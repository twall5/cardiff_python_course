import random
fruitlist = []
file = open('fruit','r')
for line in file:
    line = line[:-1]
    print(line)
    fruitlist.append(line)
file.close()
print(fruitlist)
fruits = ' '.join(fruitlist)
print(fruits)
fruitlist = fruits.split(' ')
print(fruitlist)
word = fruitlist[random.randint(0,8)]
print(word)