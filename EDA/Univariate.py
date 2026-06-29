import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../archive/dummy_data.csv')
print(df.head())

print(df["CGPA"].describe())

print(df["CGPA"].mean())

print(df["CGPA"].mode())

print(df['CGPA'].median())

print(df["Gender"].unique())

print(df["Placed"].nunique())


numerical_cols = ["IQ", "CGPA", "Semester"]

for col in numerical_cols:
    print(f"\n----- {col} -----")
    print(df[col].describe())


print("Siddharth Tiwari")
categorical_cols = ["Gender", "Day_Boarder", "Placed"]

for col in categorical_cols:
    print(f"\n----- {col} -----")
    print(df[col].value_counts())

df["Gender"].value_counts()

sns.kdeplot(df["CGPA"], fill=True)
plt.show()