import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../archive/dummy_data.csv')

# Scatter Plot
sns.scatterplot(data=df, x="IQ", y="CGPA")
plt.show()

# Box Plot
sns.boxplot(data=df, x="Placed", y="CGPA")
plt.show()

# Violin Plot
sns.violinplot(data=df, x="Placed", y="CGPA")
plt.show()

# Bar Plot
sns.barplot(data=df, x="Placed", y="CGPA")
plt.show()

# Count Plot
sns.countplot(data=df, x="Gender", hue="Placed")
plt.show()

# Crosstab
print(pd.crosstab(df["Gender"], df["Placed"]))

# Percentage Crosstab
print(pd.crosstab(
    df["Gender"],
    df["Placed"],
    normalize="index"
) * 100)

# GroupBy
print(df.groupby("Placed")["IQ"].mean())

# Pivot Table
print(pd.pivot_table(
    df,
    values="CGPA",
    index="Gender",
    columns="Placed",
    aggfunc="mean"
))