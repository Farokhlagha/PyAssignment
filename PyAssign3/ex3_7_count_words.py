# Receive a sentence from the user 
# and count the number of words.

statement = input("enter your statement:")

wordlist = statement.split()
count=0

for word in wordlist:
    count+= 1

print(len(wordlist))