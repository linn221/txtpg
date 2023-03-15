import hashlib, time

# CONFIG GOES HERE
# (you REALLY want to REMEMBER if you changed something here)
# FORGETTING will result in you having to brute force the chars and may end up with 5 FUCKING DIGIT POTENTIAL PASSWORDS, so DON'T
special_chars = set('aeiouAEIOU6 ,?')
unused_chars = ['\n', '\t', '.']
defaultFileName = 'theSignOfFour.txt'

def hasher(bin):                        # get bytes, give bytes
    return hashlib.sha256(bin).digest()

def reverseBytes(bin):                  # get bytes, give bytes
    # convert binary to hex
    hex = bin.hex()
    # reversing the hex string
    hex = hex[::-1]
    # convert the hex back to binary
    return bytes.fromhex(hex)

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

phrase = input("Enter the phrase: ")
txtFileName = input("Enter the text file name with txt entension (default is " + defaultFileName + "): ")
try:
    if txtFileName == '':
        txtFileName = defaultFileName
    with open(txtFileName, encoding='utf-8') as f:
        novel = f.read()
    for u in unused_chars:          # removing some characters, makes the program run faster
        novel = novel.replace(u, '')
except:
    print("I cannot read " + txtFileName + " file in this directory.")
    exit()

print(f"I will smash the cracker's head {len(novel):,} times!")
start = time.time()

# start double hashing + reversing the binary series
hash = hasher(phrase.encode())
for character in novel:
    if character in special_chars:
        hash = reverseBytes(hash)
    hash = hasher(hash)

timeTaken = time.time() - start
min, sec = timeTaken // 60, round(timeTaken % 60, 3)
print(f'Generating the password took {min} minutes, {sec} seconds.')
print(hash.hex())
