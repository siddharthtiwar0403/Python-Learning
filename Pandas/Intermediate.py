import pandas as pd
import numpy as np

# ==============================
# SAMPLE DATAFRAME
# ==============================

data = {
    "Name": ["rahul", "aman", "neha", "rahul"],
    "Age": [22, 25, 21, 22],
    "City": ["Delhi", "Mumbai", "Delhi", "Delhi"],
    "Marks": [90, 80, np.nan, 90],
    "Gender": ["M", "M", "F", "M"],
    "Date": ["2025-01-10", "2025-02-15", "2025-03-20", "2025-01-10"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# ==============================
# ADVANCED FILTERING
# ==============================

print("\nStudents with Age > 21:")
print(df[df["Age"] > 21])

print("\nStudents from Delhi AND Marks > 85:")
print(
    df[
        (df["City"] == "Delhi") &
        (df["Marks"] > 85)
    ]
)

print("\nStudents from Delhi OR Mumbai:")
print(
    df[
        (df["City"] == "Delhi") |
        (df["City"] == "Mumbai")
    ]
)

print("\nUsing isin():")
print(
    df[df["City"].isin(["Delhi", "Pune"])]
)

print("\nUsing between():")
print(
    df[df["Age"].between(21, 23)]
)

print("\nUsing query():")
print(
    df.query("Age > 21")
)


# ==============================
# DATETIME HANDLING
# ==============================

df["Date"] = pd.to_datetime(df["Date"])

print("\nDate Column Converted to Datetime:")
print(df["Date"])

print("\nExtract Year:")
print(df["Date"].dt.year)

print("\nExtract Month:")
print(df["Date"].dt.month)

print("\nExtract Day:")
print(df["Date"].dt.day)

print("\nExtract Day Name:")
print(df["Date"].dt.day_name())


# ==============================
# map()
# ==============================

print("\nMap Gender Values:")

df["Gender Full"] = df["Gender"].map({
    "M": "Male",
    "F": "Female"
})

print(df)


print(replaced_df)

# ==============================
# lambda FUNCTION
# ==============================

print("\nAdd 5 to Age Using Lambda:")

print(
    df["Age"].apply(lambda x: x + 5)
)

# ==============================
# SORTING
# ==============================

print("\nSort by Age:")
print(df.sort_values("Age"))

print("\nSort by Marks Descending:")
print(
    df.sort_values(
        "Marks",
        ascending=False
    )
)

# ==============================
# RANKING
# ==============================

print("\nRank Based on Marks:")

df["Rank"] = df["Marks"].rank(
    ascending=False
)

print(df)


# ==============================
# transform()
# ==============================

print("\nTransform Example:")

print(
    df.groupby("City")["Marks"]
    .transform("mean")
)

# ==============================
# concat()
# ==============================

df1 = pd.DataFrame({
    "Name": ["Rahul", "Aman"]
})

df2 = pd.DataFrame({
    "Name": ["Neha", "Priya"]
})

print("\nConcatenated DataFrame:")

concat_df = pd.concat([df1, df2])

print(concat_df)


# ==============================
# MULTIINDEX
# ==============================

multi_data = pd.DataFrame({
    "City": ["Delhi", "Delhi", "Mumbai"],
    "Year": [2024, 2025, 2024],
    "Sales": [100, 200, 300]
})

multi_index_df = multi_data.set_index([
    "City",
    "Year"
])

print("\nMultiIndex DataFrame:")
print(multi_index_df)

# ==============================
# FILL MISSING VALUES
# ==============================

print("\nFill Missing Marks with Mean:")

df["Marks"] = df["Marks"].fillna(
    df["Marks"].mean()
)

print(df)

# ==============================
# DROP MISSING VALUES
# ==============================

df_missing = pd.DataFrame({
    "A": [1, np.nan, 3],
    "B": [4, 5, np.nan]
})

print("\nOriginal Missing DataFrame:")
print(df_missing)

print("\nAfter dropna():")
print(df_missing.dropna())

# ==============================
# VALUE COUNTS
# ==============================

print("\nCity Value Counts:")
print(df["City"].value_counts())

# ==============================
# GROUPBY + AGGREGATION
# ==============================

print("\nGroupBy Mean Marks by City:")

print(
    df.groupby("City")["Marks"]
    .mean()
)

print("\nGroupBy Multiple Aggregations:")

print(
    df.groupby("City")["Marks"]
    .agg(["sum", "mean", "max"])
)

# ==============================
# PIVOT TABLE
# ==============================

pivot = pd.pivot_table(
    df,
    values="Marks",
    index="City",
    columns="Gender",
    aggfunc="mean"
)

print("\nPivot Table:")
print(pivot)