#### Day 1: Calorie Counting

## Part 1, get the highest calorie total per elf

# Read in measurements file
input_file = open("./day1_input.txt", "r")
calories_input = input_file.read()

# Turn into a list
calories_list = list(calories_input.split("\n"))

# Make sure I have a list
#print(type(calories_list))

# Initialize calories as 0
calories = 0

# Initialize an empty array to store calorie totals for each elf
total_cal_per_elf = []

for i in calories_list:
    # If there is a break between elves, symbolized as '' in the list
    if i == '':
        # Print the total number of calories totaled thus far
        total_cal_per_elf.append(calories)
        # Reset calorie counter to 0 for the next elf
        calories = 0
    # Else if there is a value in calories
    else:
        # Add that calorie value to the curent total
        more_calories = int(i) + int(calories)
        # Re-save as the calorie variable
        calories = more_calories

# Sort list in descending order so largest calorie totals come first
total_cal_per_elf.sort(reverse = True)

# Print the largest calorie total
print(total_cal_per_elf[0], "is the greatest number of calories.")

## Part 2, sum the calorie totals for the top 3 elves

# Initialize top_3 as 0
top_3 = 0

# Sum the top 3 calorie totals
for i in range(0,3):
    top_3 += int(total_cal_per_elf[i])

# Print the sum of the top 3 calorie totals
print(top_3, "is the calorie total for the top 3 elves.")

# Close input file
input_file.close()