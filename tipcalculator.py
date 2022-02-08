# Tip Calculator
print("Welcome to tip calculator\n")

bill = float(input("Enter bill Amount: Rs"))
tip_percentage = int(input("What percentage tip would you like to give ? "))
people = int(input("How many people to split the bill ? "))

tip = bill * (tip_percentage / 100)
total_bill = (bill + tip) / people
final_bill = "{:0.2f}".format(total_bill)

print(f"\nThe tip you are given : Rs{tip}\n")
print(f"Each person should pay : Rs{final_bill} ""\n\nThank You")