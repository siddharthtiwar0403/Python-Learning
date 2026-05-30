import pandas as pd
import numpy as np

# Creating a DataFrame
data = {
    "Name": ["Rahul", "Aman", "Neha"],
    "Age": [22, 25, 21],
    "City": ["Delhi", "Mumbai", "Pune"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# DataFrame Information
print("\nShape of DataFrame:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nIndex:")
print(df.index)

print("\nData Types:")
print(df.dtypes)

print("\nDataFrame Info:")
print(df.info())

# Viewing Data
print("\nFirst 2 Rows:")
print(df.head(2))

print("\nLast 2 Rows:")
print(df.tail(2))

print("\nStatistical Summary:")
print(df.describe())

# Selecting Single Column
print("\nSelecting Name Column:")
print(df["Name"])

# Selecting Multiple Columns
print("\nSelecting Name and Age Columns:")
print(df[["Name", "Age"]])

# loc[] — Label Based Selection
print("\nloc[0] — First Row:")
print(df.loc[0])

print("\nloc[:, 'Name'] — All Names:")
print(df.loc[:, "Name"])

print("\nloc[1, 'City'] — Specific Value:")
print(df.loc[1, "City"])

print("\nloc[:, ['Name', 'Age']] — Multiple Columns:")
print(df.loc[:, ["Name", "Age"]])

# iloc[] — Position Based Selection
print("\niloc[0] — First Row:")
print(df.iloc[0])

print("\niloc[1, 2] — Row 1 Column 2:")
print(df.iloc[1, 2])

print("\niloc[0:2, 0:2] — Rows & Columns Slice:")
print(df.iloc[0:2, 0:2])

# Filtering Data
print("\nPeople with Age > 21:")
print(df[df["Age"] > 21])

# Adding New Column
df["Country"] = "India"

print("\nAfter Adding Country Column:")
print(df)

# Updating Values
df.loc[0, "Age"] = 30

print("\nAfter Updating Rahul's Age:")
print(df)

# Deleting Column
df.drop("Country", axis=1, inplace=True)

print("\nAfter Deleting Country Column:")
print(df)

# Sorting Data
print("\nSorting by Age:")
print(df.sort_values("Age"))

# Handling Missing Values
df2 = pd.DataFrame({
    "Name": ["Rahul", "Aman", "Neha"],
    "Marks": [90, np.nan, 75]
})

print("\nDataFrame with Missing Values:")
print(df2)

print("\nCheck Null Values:")
print(df2.isnull())

df2.fillna(0, inplace=True)

print("\nAfter Filling Null Values:")
print(df2)

# dropna()
df3 = pd.DataFrame({
    "Name": ["Rahul", "Aman", None],
    "Marks": [90, np.nan, 75]
})

print("\nAnother DataFrame with Missing Values:")
print(df3)

print("\nAfter Dropping Null Values:")
print(df3.dropna())

# groupby()
sales = pd.DataFrame({
    "City": ["Delhi", "Delhi", "Mumbai", "Mumbai"],
    "Sales": [100, 200, 300, 400]
})

print("\nSales Data:")
print(sales)

print("\nGroup By City and Sum:")
print(sales.groupby("City")["Sales"].sum())

print("\nGroup By City and Mean:")
print(sales.groupby("City")["Sales"].mean())

# value_counts()
print("\nCity Value Counts:")
print(df["City"].value_counts())

# MERGE OPERATIONS
students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Rahul", "Aman", "Neha"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 4],
    "Marks": [90, 80, 70]
})

print("\nStudents DataFrame:")
print(students)

print("\nMarks DataFrame:")
print(marks)

# INNER MERGE
inner_merge = pd.merge(
    students,
    marks,
    on="ID",
    how="inner"
)

print("\nInner Merge:")
print(inner_merge)

# LEFT MERGE
left_merge = pd.merge(
    students,
    marks,
    on="ID",
    how="left"
)

print("\nLeft Merge:")
print(left_merge)

# RIGHT MERGE
right_merge = pd.merge(
    students,
    marks,
    on="ID",
    how="right"
)

print("\nRight Merge:")
print(right_merge)

# OUTER MERGE
outer_merge = pd.merge(
    students,
    marks,
    on="ID",
    how="outer"
)

print("\nOuter Merge:")
print(outer_merge)

# apply()
df4 = pd.DataFrame({
    "Marks": [90, 40, 75]
})

print("\nMarks DataFrame:")
print(df4)

def grade(x):
    if x >= 50:
        return "Pass"
    else:
        return "Fail"

df4["Result"] = df4["Marks"].apply(grade)

print("\nAfter Applying Grade Function:")
print(df4)

# String Operations Using apply()
names = pd.DataFrame({
    "Name": ["rahul", "aman", "neha"]
})

print("\nOriginal Names:")
print(names)

names["Upper"] = names["Name"].apply(str.upper)

print("\nAfter Converting to Uppercase:")
print(names)

# PIVOT TABLE
sales_data = pd.DataFrame({
    "City": ["Delhi", "Delhi", "Mumbai", "Mumbai"],
    "Product": ["Phone", "Laptop", "Phone", "Laptop"],
    "Sales": [100, 200, 300, 400]
})

print("\nSales Data for Pivot Table:")
print(sales_data)

pivot = pd.pivot_table(
    sales_data,
    values="Sales",
    index="City",
    columns="Product",
    aggfunc="sum"
)

print("\nPivot Table:")
print(pivot)

# Different aggfunc Example
pivot_mean = pd.pivot_table(
    sales_data,
    values="Sales",
    index="City",
    columns="Product",
    aggfunc="mean"
)

print("\nPivot Table with Mean:")
print(pivot_mean)

# Saving CSV
df.to_csv("new_data.csv", index=False)

print("\nDataFrame saved as new_data.csv")