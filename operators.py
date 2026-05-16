# ==============================
# PYTHON OPERATORS COMPLETE CODE
# ==============================

# Variables
a = 10
b = 3

# =========================================
# 1. ARITHMETIC OPERATORS
# =========================================

print("ARITHMETIC OPERATORS")

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Power:", a ** b)

print("\n")


# =========================================
# 2. COMPARISON OPERATORS
# =========================================

print("COMPARISON OPERATORS")

print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than Equal:", a >= b)
print("Less Than Equal:", a <= b)

print("\n")


# =========================================
# 3. LOGICAL OPERATORS
# =========================================

print("LOGICAL OPERATORS")

x = True
y = False

print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)

print("\n")


# =========================================
# 4. ASSIGNMENT OPERATORS
# =========================================

print("ASSIGNMENT OPERATORS")

c = 5
print("Initial Value:", c)

c += 2
print("After += :", c)

c -= 2
print("After -= :", c)

c *= 2
print("After *= :", c)

c /= 2
print("After /= :", c)

c %= 2
print("After %= :", c)

print("\n")


# =========================================
# 5. BITWISE OPERATORS
# =========================================

print("BITWISE OPERATORS")

m = 5   # Binary: 101
n = 3   # Binary: 011

print("Bitwise AND:", m & n)
print("Bitwise OR:", m | n)
print("Bitwise XOR:", m ^ n)
print("Bitwise NOT:", ~m)
print("Left Shift:", m << 1)
print("Right Shift:", m >> 1)

print("\n")


# =========================================
# 6. MEMBERSHIP OPERATORS
# =========================================

print("MEMBERSHIP OPERATORS")

name = "siddharth"

print("'s' in name:", 's' in name)
print("'z' not in name:", 'z' not in name)

print("\n")


# =========================================
# 7. IDENTITY OPERATORS
# =========================================

print("IDENTITY OPERATORS")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is not list3:", list1 is not list3)

print("\n")


# =========================================
# END OF PROGRAM
# =========================================