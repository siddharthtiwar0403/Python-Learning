import pandas as pd
import matplotlib.pyplot as plt

S = pd.read_csv("dummy_data.csv")
print(S)

# to replace default pandas sequnce no
S = pd.read_csv("dummy_data.csv", index_col='IQ')
print(S)

# header start the rows from any particular point
S = pd.read_csv("dummy_data.csv", header=3)
print(S)

# when we need specific column
S = pd.read_csv("dummy_data.csv", usecols=['CGPA','Semester','Gender'])
print(S)

# when we want to skpi any particluar rows
S = pd.read_csv("dummy_data.csv", skiprows=[1,5])
print(S)

# when we want to restric no of rows
S = pd.read_csv("dummy_data.csv", nrows=100)
print(S)

# if any ro has an extra value then it will get skipped
# S = pd.read_csv("dummy_data.csv", encoding="latin-1", error_bad_lines=False)
# print(S)

# when you want convert the data type of any column
S = pd.read_csv("dummy_data.csv", dtype={'IQ':float})
print(S)

# when you to convert in date data type
# S = pd.read_csv("dummy_data.csv", parse_dates=['date'])
# print(S)

# when you want to mark any value as NaN
S = pd.read_csv("dummy_data.csv", na_values=['Male'])
print(S)

# when to divide data into chunks
S = pd.read_csv("dummy_data.csv", chunksize=10)
print(S)



# S = S.iloc[0:5, [0, 2, 4, 5]]
# print(S)



# plt.pie(
#     S.iloc[:, 2],
#     labels=S.iloc[:, 1],
#     autopct='%1.1f%%'
# )
# plt.title("Pie Chart")
# plt.show()


# plt.pie(
#     S.iloc[:, 3],
#     labels=S.iloc[:, 1],
#     autopct='%1.1f%%'
# )
# plt.title("Pie Chart")
# plt.show()