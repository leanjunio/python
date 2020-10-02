from random import randint

limit = randint(1, 10)

print("Limit: " +  str(limit))
# loops always start from 0
for i in range(limit):
    print("i: ", i)


steps = randint(1, 10)

print("Take: " +  str(steps) + " steps")
for i in range(steps):
    print("..Taking step #:", i + 1)
