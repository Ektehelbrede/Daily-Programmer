# Write a program that can encrypt texts with an alphabetical caesar cipher. This can ignore numbers, symbols, and
# whitespace.

from sys import argv
import codecs


def encrypt(inputString):
    return codecs.encode(inputString, 'rot-13')


def decrypt(inputString):
    return codecs.decode(inputString, 'rot-13')


# The user has not input a choice and a string, or has input too many arguments:
if len(argv) != 3:
    print('USAGE: python DP003EasyVersion choice string')
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
