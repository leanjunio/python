import random

# functions
def add(a, b):
    return a + b

# calling add function
print(add(1, 2))

# Define any function

print("Get Random Number")

def getRandomNumber():
    return random.random()

print(getRandomNumber())

print("Generate random number between 0 and 100")

def getRandomNumberWithRange(a, b):
    return random.randint(a, b)

print(getRandomNumberWithRange(0, 100))
