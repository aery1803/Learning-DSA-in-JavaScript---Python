"""
NON-PRIMITIVE DATA TYPES IN PYTHON
==================================

Non-primitive types are collections of items.
Main types:
1. List (Mutable, Ordered)
2. Tuple (Immutable, Ordered)
3. Set (Mutable, Unordered, Unique)
4. Dictionary (Mutable, Key-Value pairs)
"""

# ==========================================
# 1. Lists (Similar to JS Arrays)
# ==========================================
print("--- 1. Lists ---")
# Creation
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", {"id": 3}]

# Accessing
print(numbers[0]) # 1
print(len(numbers)) # 5

# Modifying
numbers.append(6) # Add to end
numbers.pop()     # Remove from end
numbers[0] = 100  # Modify element

# Looping Lists
print("Looping List:")
for num in numbers:
    print(num)

# Standard Loop (with index)
print("Looping with Index:")
for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")

# ==========================================
# 2. Tuples (Immutable Lists)
# ==========================================
print("\n--- 2. Tuples ---")
# Creation
coordinates = (10, 20)
single_item = (1,) # Note the comma

# Accessing
print(coordinates[0]) # 10

# Immutable
# coordinates[0] = 5 # TypeError: 'tuple' object does not support item assignment

# Use case: Return multiple values from function, keys in dictionary.

# ==========================================
# 3. Sets (Unique Collection)
# ==========================================
print("\n--- 3. Sets ---")
# Creation
unique_nums = {1, 2, 3, 3, 2, 1}
print(unique_nums) # {1, 2, 3} (Duplicates removed)

# Adding/Removing
unique_nums.add(4)
unique_nums.remove(1)

# Set Operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b)) # {1, 2, 3, 4, 5}
print(a.intersection(b)) # {3}

# ==========================================
# 4. Dictionaries (Similar to JS Objects/Maps)
# ==========================================
print("\n--- 4. Dictionaries ---")
# Creation
user = {
    "name": "John",
    "age": 30,
    "is_admin": True
}

# Accessing
print(user["name"]) # "John"
print(user.get("city", "Unknown")) # Safe access with default

# Modifying
user["age"] = 31
user["city"] = "New York"
del user["is_admin"]

# Looping Dictionaries
print("Looping Dictionary:")
for key, value in user.items():
    print(f"{key}: {value}")

# ==========================================
# 5. List Comprehensions (Pythonic Map/Filter)
# ==========================================
print("\n--- 5. List Comprehensions (Map/Filter equivalent) ---")

items = [
    {"name": 'Bike', "price": 100},
    {"name": 'TV', "price": 200},
    {"name": 'Album', "price": 10},
    {"name": 'Book', "price": 5},
    {"name": 'Phone', "price": 500},
    {"name": 'Computer', "price": 1000},
]

# 1. FILTER equivalent
# Get items cheaper than 100
cheap_items = [item for item in items if item["price"] < 100]
print(f"Filtered (Cheap Items): {cheap_items}")

# 2. MAP equivalent
# Get just the names of items
item_names = [item["name"] for item in items]
print(f"Mapped (Names): {item_names}")

# 3. FIND equivalent (using next())
# Find the item with name 'Book'
# next(iterator, default)
found_item = next((item for item in items if item["name"] == 'Book'), None)
print(f"Found Item 'Book': {found_item}")

# 4. REDUCE equivalent
# Calculate total price of all items
# Needs import from functools
from functools import reduce
total = reduce(lambda current_total, item: item["price"] + current_total, items, 0)
print(f"Total Price (Reduce): {total}")

# Pythonic Sum (Simpler for this specific case)
total_sum = sum(item["price"] for item in items)
print(f"Total Price (Sum): {total_sum}")
