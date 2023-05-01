#! /usr/bin/env python3
import hashlib, time

# CONFIG GOES HERE
# (you REALLY want to REMEMBER if you changed something here)
# FORGETTING will result in you having to brute force the chars and may end up with 5 FUCKING DIGIT POTENTIAL PASSWORDS, so DON'T
special_chars = set('aeiouAEIOU6 ,?')
unused_chars = ['\n', '\t', '.']
defaultFileName = 'theSignOfFour.txt'




'''
Attempting to modularize


'''
def hasher(bin):                        # get bytes, give bytes
    return hashlib.sha256(bin).digest()

def reverseBytes(bin):                  # get bytes, give bytes
    # convert binary to hex
    hex = bin.hex()
    # reversing the hex string
    hex = hex[::-1]
    # convert the hex back to binary
    return bytes.fromhex(hex)
 
# start double hashing + reversing the binary series
def encode(phrase, novel):
    hash = hasher(phrase.encode())
    for character in novel:
        if character in special_chars:
            hash = reverseBytes(hash)
        hash = hasher(hash)
    return hash.hex()

# Example of a security failure, Don't go this way
# You don't want your password to be seen just by someone typing up 'history' from the command line
# try:
    # text = sys.argv[1]
    # fileName = sys.argv[2]
    # with open(fileName, 'r') as f:
        # novel = f.read()
# except:
    # print('Usage: python3 main.py [PRIMARY KEY] [SECRET NOVEL (.txt extension)] \nExample: python3 main.py "A REAL C#ANGE" "a_tale_of_two_cities.txt"')
    # exit()

with open(defaultFileName, 'r') as f:
    novel = f.read()
for u in unused_chars:          # removing some characters, makes the program run faster
    novel = novel.replace(u, '')
phrases = []
while True:
    phrase = input("Enter the phrase: ")
    if phrase == '':
        break
    phrases.append(phrase)

for phrase in phrases:
    secret = encode(phrase, novel)
    print(phrase)
    print(secret)
    print()
