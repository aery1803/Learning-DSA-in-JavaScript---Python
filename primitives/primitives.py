"""
PRIMITIVE DATA TYPES IN PYTHON
==============================

In Python, everything is an object, but some types work like primitives in other languages.
There are 4 main primitive (built-in) data types:
1. Integer (int)
2. Float (float)
3. String (str)
4. Boolean (bool)

There is also NoneType (complex/list/dict/set/tuple are compound/container types).

All keys properties:
- Immutable (int, float, bool, str, tuple)
- Dynamic Typing (no need to declare type)
"""

# ==========================================
# 1. Integer (int)
# ==========================================
print("--- 1. Integer ---")
# Basics:
age = 25
count = 100

# Advanced: Arbitrary Precision
# Python integers have arbitrary precision (limited only by memory)
big_num = 123456789012345678901234567890 * 1234567890
print(f"Big Number: {big_num}")

# Division behavior
# print(10 / 0)  # ZeroDivisionError: division by zero
print(10 / 3)  # 3.3333... (float division)
print(10 // 3) # 3 (floor division)

# Binary, Octal, Hex representations
print(0b1010) # Binary (10)
print(0o12)   # Octal (10)
print(0xA)    # Hex (10)

# ==========================================
# 2. Float (float)
# ==========================================
print("\n--- 2. Float ---")
# Basics:
price = 19.99
scientific = 1.2e3 # 1200.0

# Advanced: Precision Issues
# Floating point arithmetic based on IEEE 754
print(0.1 + 0.2) # 0.30000000000000004
# Use math.isclose() or decimal module for high precision
import math
print(math.isclose(0.1 + 0.2, 0.3)) # True

# Infinity and NaN
inf = float('inf')
nan = float('nan')
print(inf > 1000000000) # True

# ==========================================
# 3. String (str)
# ==========================================
print("\n--- 3. String ---")
# Basics:
name = "John"
single_quote = 'Hello' # Single quotes are same as double quotes in Python

# Multiline Strings (using triple quotes)
multi = """This is a
multiline string"""
print(multi)

# Advanced: Immutability
s = "hello"
# s[0] = 'H' # TypeError: 'str' object does not support item assignment
s = "Hello" # Reassignment is fine
print(s)

# Formatting (f-strings - Python 3.6+)
print(f"Name: {name}, Age: {age}") # Moved to template example above

# Raw Strings (useful for regex/paths)
path = r"C:\Users\Name" 
print(path)

# Slicing [start:stop:step]
text = "Python Programming"
print(text[0:6])   # 'Python'
print(text[::-1])  # 'gnimmargorP nohtyP' (Reverse)
print(text[::2])  # 'Pto rgamn' (Every 2nd character)

# ==========================================
# 4. Boolean (bool)
# ==========================================
print("\n--- 4. Boolean ---")
# Basics:
is_active = True # Capital T
is_deleted = False # Capital F

# Advanced: Boolean is a subclass of int
print(int(True))  # 1
print(int(False)) # 0
print(True + True) # 2 (valid code, but bad practice)

# Falsy values in Python:
# False, 0, 0.0, "", [], (), {}, None
if []:
    print("Won't print")
else:
    print("Empty list is Falsy")

# ==========================================
# 5. None (NoneType)
# ==========================================
print("\n--- 5. None ---")
# Represents the absence of a value (similar to null in other languages)
x = None
print(x) # None

# Identity check
# Always use 'is' to check for None, not '=='
print(x is None) # True
y = [] # Empty list is falsy but not None
print(y is None) # False

# ==========================================
# 6. Complex Numbers
# ==========================================
print("\n--- 6. Complex ---")
# Python has built-in support for complex numbers
z = 2 + 3j
print(z.real) # 2.0
print(z.imag) # 3.0

# ==========================================
# 7. Decimal Module
# ==========================================
print("\n--- 7. Decimal Module ---")
from decimal import Decimal, getcontext

# Why use Decimal?
# Standard floats have precision issues:
print(f"Float: {0.1 + 0.2}") # 0.30000000000000004

# Decimal fixes this (IMPORTANT: pass values as strings to avoid float conversion errors first)
d1 = Decimal('0.1')
d2 = Decimal('0.2')
print(f"Decimal: {d1 + d2}") # 0.3

# Controlling Precision
getcontext().prec = 6
print(Decimal('1') / Decimal('7')) # 0.142857
