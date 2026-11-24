# Can they drive?

age = int(input("Enter your age: "))
permit = input("Do you have a permit? (y/n): ").lower()

if age >= 15 and permit == "y":
    print("You can drive with an adult.")
else:
    print("Not yet.")