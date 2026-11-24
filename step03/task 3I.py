# Free shipping and gift wrap
total = float(input("Order total: "))
wrap = input("Gift wrap? (y/n): ")

if total >= 50 and wrap.lower() == "y":
    total += 3
    print(f"Final total: ${total:.2f}")
elif total >= 50 and wrap.lower() == "n":
    print(f"Final total: ${total:.2f}")
elif total < 50 and wrap.lower() == "y":
    total += 8.99
    print(f"Final total: ${total:.2f}")
else:
    total += 5
    print(f"Final total: ${total:.2f}")