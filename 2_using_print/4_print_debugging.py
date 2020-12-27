# print usage as debugger in order to know which instructions where carried out before the error popped up
print("Adding numbers")
x = 42 + 206
print("Performing division")
y = x / 0  # NaN error
print("Math complete")