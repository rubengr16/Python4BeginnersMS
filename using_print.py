# using print


# input function
name = input("Please enter your name: ")
print(name)

# blank line
print("hello world")
print()  # every time print function is called, it jumps to a blank line
print("Did you see that blank line?")
print("Blank line \nin the middle of string")  # \n sets up blank line

# debugging with print, useful to know which instructions were carried out until the error popped up
print("Adding numbers")
x = 42 + 206
print("Performing division")
y = x / 0  # NaN error
print("Math complete")