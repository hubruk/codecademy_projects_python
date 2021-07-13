# Your code below:
toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
prices = [2,6,1,3,2,7,2]
print(toppings,prices)
num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)
print("We sell "+str(num_pizzas)+" different kinds of pizza!")
pizza_and_prices = []
i =0
print("\n \n")
for x in prices:
  pizza_and_prices+=[[x]]
  for x in toppings:
    pizza_and_prices[i]+=[toppings[i]]
    i += 1

    break
print(pizza_and_prices)

pizza_and_prices.sort()
print('\n',pizza_and_prices)
cheapest_pizza=pizza_and_prices[0]
print('\n',cheapest_pizza)
priciest_pizza = pizza_and_prices[-1]
print('\n',priciest_pizza)
pizza_and_prices.pop()
print('\n',pizza_and_prices)
pizza_and_prices.insert(4,[2.5, "peppers"])
print('\n',pizza_and_prices)
three_cheapest = pizza_and_prices[:3]
print('\n',three_cheapest)
