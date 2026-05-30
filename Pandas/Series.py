import pandas as pd
import numpy as np

# Creating a Series
s = pd.Series([10, 20, 30, 40])

print("Original Series:")
print(s)

# Accessing values
single_value = s[0]
slice_values = s[1:3]

print("\nSingle Value:")
print(single_value)

print("\nSlice Values:")
print(slice_values)

# Custom index
marks = pd.Series(
    [90, 80, 70],
    index=["Math", "Science", "English"]
)

print("\nSeries with Custom Index:")
print(marks)

# Accessing with custom labels
math_score = marks["Math"]

print("\nMath Score:")
print(math_score)

# Properties
series_values = marks.values
series_index = marks.index
series_dtype = marks.dtype

print("\nSeries Values:")
print(series_values)

print("\nSeries Index:")
print(series_index)

print("\nSeries Data Type:")
print(series_dtype)

# Operations
added = s + 10
multiplied = s * 2

print("\nSeries After Adding 10:")
print(added)

print("\nSeries After Multiplying by 2:")
print(multiplied)

# Handling missing values
s2 = pd.Series([1, np.nan, 3])

print("\nSeries with Missing Value:")
print(s2)

is_null = s2.isnull()

print("\nCheck Null Values:")
print(is_null)

filled = s2.fillna(0)

print("\nAfter Filling Null Values:")
print(filled)

dropped_na = s2.dropna()

print("\nAfter Dropping Null Values:")
print(dropped_na)

# Applying a function
def result(x):
    return "Pass" if x >= 50 else "Fail"

marks_series = pd.Series([90, 40, 75])

print("\nMarks Series:")
print(marks_series)

results = marks_series.apply(result)

print("\nResult After Applying Function:")
print(results)