# This is the generator file for my_first_number_guesser.py

# Customizable min and max values for the number guesser, can support negative values
# Just don't overdo it otherwise your computer *may* [figuratively] explode
# (not responsibe if your computer actually explodes)
min = 1
max = 101

file = open("my_first_number_guesser.py", "w")

file.write(
    "# This is my first number guessing game in Python\n" +
    "# I had some suggestions that I should be adding comments to my code\n" +
    "# So here I am adding comments to my code so it's easier to understand :D\n\n" +

    "# import random so the python program can generate a random integer\n" +
    "import random\n\n" +

    # for comedic purposes
    "# TODO: Add support for decimal/floating point numbers, and numbers greater than 101\n\n" +

    "# generate a random integer between " + str(min) + " and " + str(max) + "\n" +
    "computer_number = random.randint(" + str(min) + ", " + str(max) + ")\n\n" +
    
    "# print a welcome message\n" +
    "print(\"Welcome to my first number guesser!\")\n" +
    "print(\"I'm thinking of an integer between " + str(min) + " and " + str(max) + ".\")\n\n" +

    "# start the loop until user guesses the number\n" +
    "while True:\n" +
    "\t# try to get the user's input as an integer\n"
    "\ttry:\n" +
    "\t\tprint(\"\\nWhat number am I thinking of between " + str(min) + " and " + str(max) + "?\")\n" +
    "\t\tuser_number = int(input(\"Enter your number here: \"))\n")

for i in range(min, max + 1):
    for j in range(min, max + 1):
        file.write("\t\t# If the computer's number is " + str(i) + " and the user's number is " + str(j) + ":\n")
        file.write("\t\tif computer_number == " + str(i) + " and user_number == " + str(j) + ":\n")
        if i == j:
            file.write("\t\t\t# If the user guesses the number correctly\n")
            file.write("\t\t\tprint(\"\\nYou guessed it! My number is " + str(i) + "!\")\n")
            file.write("\t\t\t# break the loop\n")
            file.write("\t\t\tbreak\n")
        else:
            if i > j:
                file.write("\t\t\t# If the user's guess is too low\n")
                file.write("\t\t\tprint(\"\\nToo low!\")\n")
            else:
                file.write("\t\t\t# If the user's guess is too high\n")
                file.write("\t\t\tprint(\"\\nToo high!\")\n")
            file.write("\t\t\tprint(\"Try again!\")\n")
            file.write("\t\t\t# continue the loop\n")
            file.write("\t\t\tcontinue\n")

file.write("\n\t\t# If the number is outside the range\n")
file.write("\t\telse:\n" +
    "\t\t\tprint(\"\\nYou didn't enter a number between " + str(min) + " and " + str(max) + "! :(\")\n\n" +

    "\t# If the user enters something that isn't an integer (stupid user! >:((( )\n" +
    "\texcept:\n" +
    "\t\tprint(\"\\nYou didn't enter an integer between " + str(min) + " and " + str(max) + "! >:(((\")\n\n")

file.write("# print a goodbye message\n")
file.write("print(\"Goodbye!\")\n")

file.close()
