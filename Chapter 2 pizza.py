# Input
slices_per_person = int(input("Enter the number of slices each person eats: "))

# Constants
people = 4
slices_of_pizza = 8

# Calculations
total_slices_needed = slices_per_person * people
pizzas_needed = total_slices_needed // slices_of_pizza
leftover_slices = total_slices_needed % slices_of_pizza

# at least one pizza if there is any need for more slices
if leftover_slices > 0:
    pizzas_needed += 1
    leftover_slices = slices_of_pizza - (total_slices_needed % slices_of_pizza)


print(f"You need {pizzas_needed} pizzas.")
print(f"Leftover slices: {leftover_slices}")
