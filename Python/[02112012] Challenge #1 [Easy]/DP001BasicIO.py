# Create a program that will ask the user's name, age, and reddit username.
# Then the information will be repeated to the user in the following format:
    # your name is (blank), you are (blank) years old, and your username is (blank)
# EXTRA CREDIT: Log this information into a file to be accessed later.

# Get user's name:
print('What is your name?')
name = input()

# Get user's age:
print('What is your age?')
age = input()

# Get user's reddit username:
print('What is your reddit username?')
username = input()

# Print back the provided information:
information = 'your name is ' + name + ', you are ' + age + ' years old, and your username is ' + username
print(information)

# Save this information to be accessed later:
file = open('Saved Information', 'a')
file.write(information + '\n')
file.close()