# Check the range first

score = int(input("Rating (1-5): "))

if score < 1 or score > 5:
    print("Error: rating must be 1 to 5.")
else:
    print(f"Thanks for the rating of: {score}!")