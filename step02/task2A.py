# Name: Matthew Phillips
# Date: 11/12/2026
# Program Name: Pizza Party Planner
# Description: Write a program that plans the pizza for a party: how many whole pizzas, how many extra slices, and what it costs.

people = 10
spp = 3
slices = people * spp
pizzas = slices // 8
leftover = slices % 8
cost = pizzas * 12.99 + leftover * 2.25
cpp = cost / people
print("Host name: Jordan")
print("Number of people: " + str(people))
print("Slices per person: " + str(spp))
print()
print("=" * 3 + " Pizza Plan for Jordan's Party " + "=" * 3)
print("Slices needed:    " + str(slices) + "\nWhole pizzas:     " + str(pizzas))
print("Extra slices:     " + str(leftover) + "\nTotal cost:       $" + str(cost))
print("Cost per person:  $" + str(cpp))
