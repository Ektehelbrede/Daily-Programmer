# Interest calculator which calculates simple interest and compound interest depending on command line arguments.
# USAGE: python CommandLineInterestCalculator.py choice principal interestRate numberOfPeriods

# argv passes command line arguments to the program; argv[0] is the path of the program? and argv[1...] are the user
# inputs.
from sys import argv


def simpleinterest(principal, interestRate, numberOfPeriods):
    return principal * (1 + (interestRate * numberOfPeriods))


def compoundinterest(principal, interestRate, numberOfPeriods):
    return principal * pow((1 + interestRate), numberOfPeriods)


if len(argv) != 5:
    print('Please pass all arguments using the command line. The type of interest can be compound or simple.')
    print('For example: python CommandLineInterestCalculator.py compound 1000 .10 5')

if argv[1] == 'simple':
    print('The value of this investment would be (including the principal): ' +
          str(simpleinterest(float(argv[2]), float(argv[3]), float(argv[4]))))
elif argv[1] == 'compound':
    print('The value of this investment would be (including the principal): ' +
          str(compoundinterest(float(argv[2]), float(argv[3]), float(argv[4]))))
else:
    print('Please check your formatting and try again.')