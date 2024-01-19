from itertools import combinations

# target_sum = 11000
target_sum = 15000

# Change this to 1 or 2 to choose the sorting method
# 1 === sorted by key1
# 2 === sorted by key2
sorting_method = 1

# Value B Alt1
# Define variable names for key 1 and 2 used at output
key1 = "Biaya"
key2 = "Tenaga Kerja"
values = {
    'D': 1869,
    'A': 2546,
    'E': 3784,
    'C': 4357,
    'B': 6582,
}

values2 = {
    'D': 1123,
    'A': 1455,
    'E': 2324,
    'C': 2450,
    'B': 3122,
}

# Value LN2
# key1 = "Biaya"
# key2 = "Netto"
# values = {
    # 'D': 500,
    # 'B': 1000,
    # 'E': 1800,
    # 'A': 2500,
    # 'C': 4200,
    # 'F': 6500,
    # 'G': 7000,
# }

# values2 = {
    # 'D': 700,
    # 'B': 800,
    # 'E': 300,
    # 'A': 600,
    # 'C': 600,
    # 'F': 0,
    # 'G': 1400,
# }


# Fun
def calculate_combination(combination, values):
    return sum(values[key] for key in combination)

def calculate_total(combination, values, values2):
    total_value1 = sum(values.get(key, 0) for key in combination)
    total_value2 = sum(values2.get(key, 0) for key in combination)
    return total_value1, total_value2

def is_valid(combination, values, values2, target_sum):
    total_value1, total_value2 = calculate_total(combination, values, values2)
    return total_value1 <= target_sum and total_value2 > 1

def find_combinations(values, values2, target_sum):
    valid_combinations = []
    for r in range(1, len(values) + 1):
        for combination in combinations(values.keys(), r):
            if is_valid(combination, values, values2, target_sum):
                valid_combinations.append(combination)
    return valid_combinations

# Sort
# Change reverse=False to True to invert the output
valid_combinations = find_combinations(values, values2, target_sum)

if sorting_method == 1:
    sorted_combinations = sorted(valid_combinations, key=lambda combo: (
    calculate_total(combo, values, values2)[0], 
    calculate_total(combo, values, values2)[1]), 
    reverse=False)
elif sorting_method == 2:
    sorted_combinations = sorted(valid_combinations, key=lambda combo: (
    calculate_total(combo, values, values2)[1], 
    calculate_total(combo, values, values2)[0]), 
    reverse=False)
else:
    raise ValueError(f"Err, Invalid Value")


# Out
print(f"Found Combinations (Sorted by {key2}):")
for combination in sorted_combinations:
    total_value1, total_value2 = calculate_total(combination, values, values2)
    print(f"Combination:\t{combination}")
    print(f"{key1} Total:\t{round(total_value1, 2)}")
    print(f"{key2} Total:\t{round(total_value2, 2)}")
    print(f"")
