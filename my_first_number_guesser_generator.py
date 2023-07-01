# This is the generator file for my_first_number_guesser.py

# Customizable min and max values for the number guesser, can support negative values
# Just don't overdo it otherwise your computer *may* [figuratively] explode
# (not responsibe if your computer actually explodes)
min = 1
max = 101

file = open("my_first_number_guesser.py", "w")

file.write("import random\n\n" +

    # for comedic purposes
    "#TODO: Add support for decimal/floating point numbers, and numbers greater than 101\n\n" +

    "computer_number = random.randint(" + str(min) + ", " + str(max) + ")\n\n" +
    
    "print(\"Welcome to my first number guesser!\")\n" +
    "print(\"I'm thinking of an integer between " + str(min) + " and " + str(max) + ".\")\n\n" +

    "while True:\n" +
    "\ttry:\n" +
    "\t\tprint(\"\\nWhat number am I thinking of between " + str(min) + " and " + str(max) + "?\")\n" +
    "\t\tuser_number = int(input(\"Enter your number here: \"))\n")

for i in range(min, max + 1):
    file.write("\t\tif user_number == " + str(i) + ":\n")
    for j in range(min, max + 1):
        file.write("\t\t\tif computer_number == " + str(j) + ":\n")
        if i == j:
            file.write("\t\t\t\tprint(\"\\nYou guessed it! My number is \" + str(computer_number) + \"!\")\n")
            file.write("\t\t\t\tbreak\n")
        else:
            # When the code is generated, it may look a bit weird since Too High! is on top,
            # however I left it like this because I think it's more funnier this way
            if j > i:
                file.write("\t\t\t\tprint(\"\\nToo low!\")\n")
            else:
                file.write("\t\t\t\tprint(\"\\nToo high!\")\n")
            file.write("\t\t\t\tprint(\"Try again!\")\n")
    file.write("\n")

file.write("\t\tif user_number < " + str(min) + " or user_number > " + str(max) + ":\n" +
    "\t\t\tprint(\"\\nYou didn't enter a number between " + str(min) + " and " + str(max) + "! :(\")\n\n" +

    "\texcept:\n" +
    "\t\tprint(\"\\nYou didn't enter an integer between " + str(min) + " and " + str(max) + "! >:(((\")\n\n")

file.write("print(\"Goodbye!\")\n")

file.close()
