# Functions are defined pieces of code you can run where ever you want. 

# This is how we define functions. 


def ReturnHelloWorld (): 
    # Functions will never run until you call them. 
    # In this case, all we do is return a string. Nothing else happens here
    return "Hello World"
    # Notice the indent. Everything that is indented is in this function 

def PrintHelloWord ():
    # This time we print to screen, but return nothing from the function
    print("Hello World")

def SomeMath (startsWith):
    # Here we perform two math functions on a number
    # The startsWith variable only exists within the function and go away when a function finishes unless returned to the caller.
    startsWith = startsWith * 2
    # Then we return the result back to what ever called this.
    # Nothing goes to the screen by this function.
    return (startsWith + 1)

# Here we call the function and print the result
print(ReturnHelloWorld())

# Here the result gets printed  by the function, so all we do is call it.
PrintHelloWord()

# Here we  create a variable we will pass to a function. This variable can be seen or change anywhere
# Because it is created outside of a function, we call it a global variable.
startingNumber = 5
print(f"The result is: {SomeMath(startsWith=startingNumber)}") 

# We can call the function in different ways
# We have called the function before, but nothing about the previous instance is remembered. 
print(f"Now the result is: {SomeMath(7)}")