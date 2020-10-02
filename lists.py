fruitBasket = ['apple', 'orange', 'banana']

# adding more to list
fruitBasket.append('lemon')

print(fruitBasket)

# remove last item in list: 'lemon'
fruitBasket.pop()

print(fruitBasket)

fruitBasket.reverse()

print(fruitBasket)

for f in fruitBasket:
    print("Fruit name: ", f)
