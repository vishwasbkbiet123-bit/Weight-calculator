# === WEIGHT CALCULATOR ===

print("=== Welcome to Advance Weight Calculator ===")
print("Choose your INPUT unit:")
print("1. Kilograms (kg)")
print("2. Pounds (lbs)")
print("3. Grams (g)")

input_choice = input("Enter choice (1/2/3): ")

# Get weight value from user
weight = float(input("\nEnter the weight value: "))

print("\nConvert into which unit?")
print("1. Kilograms (kg)")
print("2. Pounds (lbs)")
print("3. Grams (g)")

output_choice = input("Enter choice (1/2/3): ")
print()

# CONVERSION LOGIC 

# If input in Kilograms (KG)
if input_choice == "1":
    if output_choice == "1":
        print(f"{weight} kg = {weight} kg (Same unit!)")
    elif output_choice == "2":
        result = weight * 2.20462
        print(f"{weight} kg = {round(result, 2)} lbs")
    elif output_choice == "3":
        result = weight * 1000
        print(f"{weight} kg = {round(result, 2)} grams")
    else:
        print("Invalid Output Choice!")

# If input in Pounds (LBS)
elif input_choice == "2":
    if output_choice == "1":
        result = weight / 2.20462
        print(f"{weight} lbs = {round(result, 2)} kg")
    elif output_choice == "2":
        print(f"{weight} lbs = {weight} lbs (Same unit!)")
    elif output_choice == "3":
        result = weight * 453.592
        print(f"{weight} lbs = {round(result, 2)} grams")
    else:
        print("Invalid Output Choice!")

# IF inpyt in grams 
elif input_choice == "3":
    if output_choice == "1":
        result = weight / 1000
        print(f"{weight} g = {round(result, 3)} kg")
    elif output_choice == "2":
        result = weight / 453.592
        print(f"{weight} g = {round(result, 3)} lbs")
    elif output_choice == "3":
        print(f"{weight} g = {weight} g (Same unit!)")
    else:
        print("Invalid Output Choice!")

else:
    print("Invalid Input Choice! Program stopped.")