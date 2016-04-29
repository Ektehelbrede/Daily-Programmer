# Create a random password generator
# EXTRA: User can specify the number of passwords to generate.
# EXTRA: User can specify the length of passwords generated.

# V1.0 Generates a number of passwords of a certain length as specified by the user through command line arguments.
# Outputs these generated passwords to a text file.

from random import randint
from sys import argv


if len(argv) != 3:
    print('USAGE: python DP004PasswordGenerator numberOfPasswords lengthOfPasswords')
    print('Where number and length of the passwords are integers.')
    exit()

numberOfPasswords = int(argv[1])
lengthOfPasswords = int(argv[2])

textFile = open('GeneratedPasswords.txt', 'a')


for i in range(numberOfPasswords):
    password = ''
    for j in range(lengthOfPasswords):
        password += chr(randint(33, 126))
    textFile.write(password + '\n')

print('Generated ' + str(numberOfPasswords) + ' passwords each of length ' + str(lengthOfPasswords) + '.')
print('The passwords have been placed in GeneratedPasswords.txt')
