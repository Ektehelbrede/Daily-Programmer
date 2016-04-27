# Write a program that can encrypt texts with an alphabetical caesar cipher. This can ignore numbers, symbols, and
# whitespace.

# V1.0 Take a command (encrypt / decrypt) and string from the command line and output the result ignoring (AS IN DON'T
# INPUT THEM BECAUSE THEY WILL BREAK) case, numbers, symbols, and whitespace.

from sys import argv


def encrypt(inputString):
    alphabetNormal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
                      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    outputString = ''

    for char in inputString:
        index = alphabetNormal.index(char)
        outputString += alphabetNormal[(index + 13) % 26]

    return outputString


def decrypt(inputString):
    alphabetNormal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
                      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    outputString = ''

    for char in inputString:
        index = alphabetNormal.index(char)
        outputString += alphabetNormal[(index + 13) % 26]

    return outputString


# The user has not input a choice and a string, or has input too many arguments:
if len(argv) != 3:
    print('USAGE: python DP003CaesarCipher choice string')
    print('Where choice is either encrypt OR decrypt and string is the string to be coded.')
    exit(1)

# User wants string to be encrypted:
if argv[1] == 'encrypt':
    print(encrypt(argv[2]))

# User wants string to be decrypted:
elif argv[1] == 'decrypt':
    print(decrypt(argv[2]))

# User has made an error in entering encrypt OR decrypt, but has provided the correct number of arguments.
else:
    print('choice can be either encrypt OR decrypt, please try again.')
    exit(2)
