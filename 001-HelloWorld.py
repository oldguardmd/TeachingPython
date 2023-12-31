#We all hate hello world. It makes us feel dumb, but if you cannot do this, everything else is a waste of time.

# You Need to know how to do output to the screen
print("Hello World")

# You need to know you can print a variable
someText = "Hello World"
print("{}".format(someText))

# Or I can print two things

aString = "How Many Apples: "
aInteger = "5"

print("{}{}".format(aString,aInteger))
# Think about why this might work differently. Can you figure out what I did there?
print("{1}{0}".format(aInteger,aString))


# Newer versions of Python let you format that data quicker and with less complexity
print(f"{someText}")

# And we can do math and print the results
Something = 1
SomethingElse = 2
print(f"The variable Something plus the variable SomethingElse Equals: {Something + SomethingElse}")

# You can run these commands directly or python, or run the whole file like this

    # python3 001-HelloWorld.py