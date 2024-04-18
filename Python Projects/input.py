num = int(input("Enter a number: "))
print(num)
num += 10
print(num)

# If an integer is not input, an error will be thrown: fix with try/except

try:
    num = int(input("Enter a number: "))
    num += 10
except:
    print("You dummy! That's not a number!")

print("continue")

'''
The print function's output appears in the terminal window

'''

print("the rain in spain", end = ' ') # does not end the line of output
print("stays mainly in the plain")

# f-strings are useful for embedding variables
print(f"hello this is a number: {num}")

with open("movies.txt") as file:
    for line in file:
        line = line.strip() # strip gets rid of the "end line" charachter, so they wont have gaps in output
        print(line)

with open("heights.txt") as file:
    for line in file:
        line = line.strip()
        lst = line.split()
        print(lst)
