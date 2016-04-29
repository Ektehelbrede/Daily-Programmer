# Create a random password generator
# EXTRA: User can specify the number of passwords to generate.
# EXTRA: User can specify the length of passwords generated.

# V1.0 Generates a number of passwords of a certain length as specified by the user through command line arguments.
# Outputs these generated passwords to a text file.

import random
from sys import argv


if len(argv) != 3:
    print('USAGE: python DP004PasswordGenerator numberOfPasswords lengthOfPasswords')
    print('Where number and length of the passwords are integers.')
    exit()

numberOfPasswords = int(argv[1])
lengthOfPasswords = int(argv[2])

textFile = open('GeneratedPasswords.txt', 'a')

currentNumber = 0
while currentNumber < numberOfPasswords:
    currentLength = 0
    password = ''
    while currentLength < lengthOfPasswords:
        password += chr(random.randint(33, 126))
        currentLength += 1
    textFile.write(password + '\n')
    currentNumber += 1

print('Generated ' + str(numberOfPasswords) + ' passwords each of length ' + str(lengthOfPasswords) + '.')
print('The passwords have been placed in GeneratedPasswords.txt')
