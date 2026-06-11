import matplotlib.pyplot as plt
age = [18,20,25,30,35,40]
salary = [15000,18000,25000,35000,50000,65000]
plt.scatter(
    age,
    salary,
    color="blue"
)
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary")
plt.show()


months = ["Jan","Feb","Mar","Apr"]
sales = [100,120,150,180]
plt.bar(
    months,
    sales,
    color="orange"
)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()


departments = ["HR", "IT", "Sales"]
employees = [10,30,20]
plt.barh(
    departments,
    employees
)
plt.show()


expenses = [40,30,20,10]
labels = [
    "Food",
    "Rent",
    "Travel",
    "Entertainment"
]
plt.pie(
    expenses,
    labels=labels,
    autopct="%1.1f%%"
)
plt.title("Monthly Expense Distribution")
plt.show()


fig, ax = plt.subplots(1,2)
ax[0].plot([1,2,3],[10,20,30])
ax[1].plot([1,2,3],[30,20,10])
plt.show()


fig, ax = plt.subplots(2,2)
ax[0,0].plot([1,2,3],[10,20,30])
ax[0,1].bar(["A","B"],[5,10])
ax[1,0].scatter([1,2,3],[7,8,9])
ax[1,1].hist([1,2,2,3,3,3,4])
plt.show()


months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]
sales = [100,120,150,180,220]
plt.figure(figsize=(10,5))
plt.bar(months,sales)
plt.title("Monthly Sales")
plt.show()


# print(plt.style.available)


plt.style.use("ggplot")
x = [1,2,3,4]
y = [10,20,30,40]
plt.plot(x,y)
plt.show()


months = [1,2,3,4,5]
sales = [100,120,140,250,180]
plt.plot(
    months,
    sales,
    marker="o"
)
plt.annotate(
    "Best Month",
    xy=(4,250),
    xytext=(2,280),
    arrowprops={
        "arrowstyle":"->"
    }
)
plt.show()


days = [1,2,3,4]
temperature = [30,32,35,34]
error = [1,2,1,1]
plt.errorbar(
    days,
    temperature,
    yerr=error,
    marker="o"
)
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Temperature Measurements")
plt.show()


days = [1,2,3,4,5]
sales = [100,120,90,150,130]
plt.stem(days, sales)
plt.show()


hours = [1,2,3,4,5]
price = [100,100,150,150,200]
plt.step(hours, price)
plt.show()