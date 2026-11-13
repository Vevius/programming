# Name: Matthew Phillips
# Date: 11/12/2026
# Program Name: Road Trip Calculator
# Description: Write a program that figures out gas, cost per person, and driving time for a road trip.

miles = 150
mpg = 30
gppg = 3.20
splitcost = 2
gallons = 5
time = 163
AVERAGE_SPEED = 55
print("Destination: Columbus")
print("Trip distance (miles): " + str(miles))
print("Car\'s miles per gallon: " + str(mpg))
print(f"Gas price per gallon: {gppg:.2f}")
print("Number of people splitting the cost: " + str(splitcost))

print("-" * 3 + " Trip to Columbus " + "-" * 3)
print(f"Gallons of gas:   {gallons}")
print(f"Gas cost:         ${(gppg * gallons):.2f}")
print(f"Cost per person:  ${(gppg * gallons / splitcost):.2f}")
print(f"Driving time:     {time // 60} hr {time % 60} min (at {AVERAGE_SPEED} mph)")
print(f"Round trip gas:   ${(gppg * gallons * 2):.2f}")
