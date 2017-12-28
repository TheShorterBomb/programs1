import random
# Generate Random Number
nRandom = str(random.randint(1,101))
print(nRandom)

# Ask for a string
string = input("Your String: ")
stringlist = list(string)

# Generate Another Number
pRandom = random.randint(1,len(string))
print(stringlist)

# Join the list into one string
stringlist.insert(pRandom, nRandom)
string = ''.join(stringlist)

# Final Output
print(string)
