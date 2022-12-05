#### Day 3: Rucksack Reorganization

## Part 1, sum priorities of duplicate types

from itertools import chain

# Read in packing file
#input_file = open("./day3_input.txt", "r")
input_file = open("./day3_input.txt", "r")
packing_input = input_file.read()

# Turn into a list
packing_list = list(packing_input.split("\n"))

## Make dictionary of item types (keys) and priorities (values)
# Item types (keys) using ACII characters
keys = []
for i in chain(range(97,123), range(65,91)):
    #print(chr(i), end="")
    keys.append(chr(i))

# Priorities (values)
values = []
for i in range(1, 53):
    values.append(i)

# Combine key and value lists into a dictionary
priority_dict = dict(zip(keys, values))

## Find duplicate characters in each packing list
# Initialize empty lists to hold item types per compartment and duplicate types
compartment1_list = []
compartment2_list = []
duplicate_list = []

# For each packing list (per rucksack)
for i in packing_list:
    # Split items into 2 compartments
    compartment1 = i[:len(i)//2]
    compartment2 = i[len(i)//2:]
    # Split each compartment string into individual characters
    compartment1_split = [*compartment1]
    compartment2_split = [*compartment2]
    # Save as lists
    compartment1_list.append(compartment1_split)
    compartment2_list.append(compartment2_split)

# For each packing list in compartment 1 and compartment 2
for j, k in zip(compartment1_list, compartment2_list):
    # Find the item type they share
    # Use extend() instead of append() to avoid curly brackets in the resulting list
    duplicate_list.extend(set(j) & set(k))

## Extract key's value if key present in list of duplicated item types
# Initialize priority sum as zero
sum = 0

# For each item in list
for x in duplicate_list:
    # Add the priority to the total
    sum += priority_dict[x]

print("Sum of the priorities of duplicated item types:", sum)

## Part 2, sum priorities of badges

# Split packing lists into groups of 3
list_of_groups = list(zip(*(iter(packing_list),) * 3))

## Find shared badge in each group's rucksacks
# Initialize empty rucksack lists and group list
rucksack1_list = []
rucksack2_list = []
rucksack3_list = [] 
badge_list = []

# For each group
for i in list_of_groups:
    # Split 3 rucksacks per group
    rucksack1, rucksack2, rucksack3 = i
    # Split each rucksack into individual characters
    rucksack1_split = [*rucksack1]
    rucksack2_split = [*rucksack2]
    rucksack3_split = [*rucksack3]
    # Save as lists
    rucksack1_list.append(rucksack1_split)
    rucksack2_list.append(rucksack2_split)
    rucksack3_list.append(rucksack3_split)

# For each of the 3 rucksacks per group
for j, k, l in zip(rucksack1_list, rucksack2_list, rucksack3_list):
    # Find the item type they share; this is their badge
    badge_list.extend(set(j) & set(k) & set(l))

## Extract key's value if key present in list of duplicated item types
# Initialize priority sum as zero
sum = 0

# For each item in list
for x in badge_list:
    # Add the priority to the total
    sum += priority_dict[x]

print("Sum of the priorities of the badges:", sum)

# Close input file
input_file.close()