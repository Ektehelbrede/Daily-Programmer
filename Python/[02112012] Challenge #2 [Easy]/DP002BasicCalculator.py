# Create a calculator application. EXTRA CREDIT: Make the calculator have multiple functions.
# Interest calculator which calculates simple interest and compound interest depending on user's choice:
    # Simple Interest: F = P(1 + rt)
        # F is Final Investment Value
        # P is Principal
        # r is Interest Rate per Period
        # t is Number of Time Periods
    # Compound Interest: F = P(1 + i/n)^nt
        # F is Final Investment Value
        # P is Principal
        # i is Nominal Interest Rate
        # n is Compounding Frequency
        # t is Overall Length of Time (generally in years)


def simpleinterest(principal, interestRate, numberOfPeriods):
    return principal * (1 + (interestRate * numberOfPeriods))


def compoundinterest(principal, interestRate, frequency, time):
    return principal * pow(1 + (interestRate / frequency), frequency * time)


print('Would you like to calculate (simple) or (compound) interest?')
selection = input()

if selection == 'simple':
    information = input('Please input principal, interest rate, and number of periods separated by spaces: ')
    principal, interestRate, numberOfPeriods = information.split(' ')
    principal = float(principal)
    interestRate = float(interestRate)
    numberOfPeriods = float(numberOfPeriods)
    print('The value of this investment would be (including the principal): '
          + str(simpleinterest(principal, interestRate, numberOfPeriods)))

elif selection == 'compound':
    information = input('Please input principal, interest rate, frequency, and time separated by spaces: ')
    principal, interestRate, frequency, time = information.split(' ')
    principal = float(principal)
    interestRate = float(interestRate)
    frequency = float(frequency)
    time = float(time)
    print('The value of this investment would be (including the principal): '
          + str(compoundinterest(principal, interestRate, frequency, time)))

else:
    print('Sorry, please try again. Type "simple" or "compound" for your selection.')
