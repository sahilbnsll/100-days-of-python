print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
after_tip_amount = bill * (1 + tip/100)
per_person_amount = after_tip_amount / people
final_amount = round(per_person_amount, 2)
print(f"Each person should pay: ${final_amount}")