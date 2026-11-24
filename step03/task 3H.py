# Bigger number
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

if num1 > num2:
    print(f"{num1} is bigger.")
elif num2 > num1:
    print(f"{num2} is bigger.")
else:
    print("They are equal.")