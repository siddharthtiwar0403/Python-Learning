# Matplotlib is a Python library used for creating graphs, charts, and visualizations from data.
# It provides a wide range of tools and functions for creating various types of plots, such as line graphs, bar charts, scatter plots, histograms, and more.
# Matplotlib is highly customizable, allowing users to adjust the appearance of their plots, including colors, labels, titles, and axes.
# It is widely used in data analysis, scientific research, and machine learning for visualizing data and presenting results.

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4, 2, 8])
plt.show()


x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
plt.plot(x, y)
plt.show()


fig, ax = plt.subplots()
plt.show()


import matplotlib.pyplot as plt
fig, ax = plt.subplots()
x = [1,2,3,4]
y1 = [10,20,30,40]
y2 = [40,30,20,10]
ax.plot(x, y1, color="red", marker="s")
ax.plot(x, y2, linewidth=5, marker="o")
plt.show()


months = [1,2,3,4,5]
sales = [100,120,140,170,200]
profit = [20,30,40,60,80]
plt.plot(months,sales,color="blue",marker="o")
plt.plot(months,profit,color="green",marker="s",linestyle="--")
plt.show()


months = [1,2,3,4]
sales = [100,150,200,250]
plt.plot(months,sales)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Report")
plt.show()


x = [1,2,3,4]
sales = [100,120,140,160]
profit = [20,30,50,70]
plt.plot(x, sales, label="Sales")
plt.plot(x, profit, label="Profit")
plt.legend()
plt.show()


x = [1,2,3,4]
y = [20,40,60,80]
plt.plot(x,y)
plt.xticks(
    [1,2,3,4],
    ["Jan","Feb","Mar","Apr"]
)
plt.yticks([0,20,40,60,80,100])
plt.show()