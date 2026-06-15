import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
tips = sns.load_dataset("tips")
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip"
)
plt.show()


tips = sns.load_dataset("tips")
print(tips.head())
print(tips.shape)
print(tips.columns)


sns.set_theme()
sns.set_style("darkgrid")
tips = sns.load_dataset("tips")
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex"   
)
plt.show()


df = pd.DataFrame({
    "Month":[1,2,3,4,5],
    "Sales":[100,150,120,200,250]
})
sns.lineplot(
    data=df,
    x="Month",
    y="Sales",
    markers="o",
    color="red"
)
plt.show()


tips = sns.load_dataset("tips")
sns.histplot(
    data=tips,
    x="total_bill",
    bins=30,
    kde=True
)
plt.show()


tips = sns.load_dataset("tips")
sns.kdeplot(
    data=tips,
    x="total_bill",
    hue="sex"
)
plt.show()


tips = sns.load_dataset("tips")
sns.barplot(
    data=tips,
    x="day",
    y="total_bill",
    color="green"
)
plt.show()


tips = sns.load_dataset("tips")
sns.countplot(
    data=tips,
      x="sex",
      color="yellow"
)
plt.show()


tips = sns.load_dataset("tips")
sns.boxplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex"
)
plt.show()


# Boxplot + KDE Plot = Violin Plot
tips = sns.load_dataset("tips")
sns.violinplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex"
)
plt.show()


tips = sns.load_dataset("tips")
sns.stripplot(
    data=tips,
    x="day",
    y="total_bill",
    jitter=True
)
plt.show()


tips = sns.load_dataset("tips")
sns.swarmplot(
    data=tips,
    x="day",
    y="total_bill",
    color="red"
)
plt.show()


tips = sns.load_dataset("tips")
sns.pointplot(
    data=tips,
    x="day",
    y="total_bill",
    # hue="sex"
)
plt.show()


tips = sns.load_dataset("tips")
sns.regplot(
    data=tips,
    x="total_bill",
    y="tip",
    # ci=None,
    scatter_kws={"color":"red"},
    line_kws={"color":"green"}
)
plt.show()


tips = sns.load_dataset("tips")
sns.lmplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex",
    col="smoker"
)
plt.show()


# What is a Heatmap?
# A heatmap uses colors to represent values.
# Big Number   → Dark Color
# Small Number → Light Color

data = pd.DataFrame(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
sns.heatmap(data)
plt.show()
# Dark Red   → Strong Positive
# White      → Weak
# Dark Blue  → Strong Negative
corr = df.corr(numeric_only=True)
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)
plt.show()


corr = df.corr(numeric_only=True)
sns.clustermap(
    corr,
    cmap="coolwarm",
    annot=True
)
plt.show()


iris = sns.load_dataset("iris")
sns.pairplot(iris)
plt.show()


tips = sns.load_dataset("tips")
sns.jointplot(
    data=tips,
    x="total_bill",
    y="tip"
)
plt.show()