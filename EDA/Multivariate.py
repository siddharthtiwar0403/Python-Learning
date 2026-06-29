import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../archive/dummy_data.csv')

# Correlation Matrix
print(df.corr(numeric_only=True))

# Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.show()

# Pair Plot
sns.pairplot(df)
plt.show()

# Pair Plot with Target
sns.pairplot(df, hue="Placed")
plt.show()

# GroupBy
print(df.groupby("Placed")["CGPA"].mean())

# Crosstab
print(pd.crosstab(df["Gender"], df["Placed"]))

# Pivot Table
print(pd.pivot_table(
    df,
    values="CGPA",
    index="Gender",
    columns="Placed",
    aggfunc="mean"
))