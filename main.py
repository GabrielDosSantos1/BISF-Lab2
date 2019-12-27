import numpy as np
import pandas as pd

# Exercise 1

# 1) Create a numeric array v1 with all 0 values of length 10
v1 = np.repeat(0, 10)
print("value of var v1 is " + str(v1))
print()

# 2) Create random binary array v2 of length 10
v2 = np.random.choice([0, 1], 10)
print("value of var v2 is " + str(v2))
print()

# 3) Using v2 array create a boolean array v3
v3 = v2.astype('bool')
print("value of var v3 is " + str(v3))
print()

# 4) Which indices in v3 are TRUE values
tempV3 = np.where(v3 == True)
print("value of var tempV3 " + str(tempV3))
print()

# 5) select all values in array v3 that are False
tempV3 = v3[np.where(v3 == False)]
print("value of var tempV3 " + str(tempV3))
print()

# Exercise 2

# 1) Create a random categories array v6 with this list of terms : ["adult" "child" "elder“]
v6 = np.random.choice(["adult", "child", "elder"], 10)
v6 = pd.Categorical(v6)
print("value of var v6 " + str(v6))
print()

# 2) which are categories of categories array v6
catV6 = v6.categories
print("value of var catV6 " + str(catV6))
print()

# 3) Set the order of categorical array v6 from youngest to oldest and sort the categorical array v6
v6 = v6.reorder_categories(["child", "adult", "elder"], ordered=True)
v6 = v6.sort_values()
print("value of var v6 " + str(v6))
print()

# 4) Change the categories names of categorical array from [”child”, ”adult”, ”elder”] to [“Child”, “Adult”, “Elder”]
v6 = v6.rename_categories(["Child", "Adult", "Elder"])
print("value of categories " + str(v6.categories))
print()

# 5) Create a new categories array named v7 which uses v6 with added ("Infant", "Infant") and sort array v7 elements
# from youngest to oldest
v7 = pd.Categorical(np.append(np.array(v6), np.array(["Infant", "Infant"])))
v7 = v7.reorder_categories(["Infant", "Child", "Adult", "Elder"], ordered=True)
v7 = v7.sort_values()
print("value of categories " + str(v7))
print()

# 6) Print the categories frequencies of categorical array v7
tempDescribe = v7.describe()
print("value of tempDescribe " + str(tempDescribe))
print()

# Exercise 3

# 1) Create a NaN array v8 with size 10
v8 = np.repeat(np.nan, 10)
print("value of var v8 is " + str(v8))
print()

# 2) Replace values in v8 in position index [3,4,5,6] with values [1,2,3,4]
v8[[2, 3, 4, 8]] = np.array([1, 2, 3, 4])
print("value of var v8 is " + str(v8))
print()

# 3) add 5 random values among [NA; 42] to tail of array v8 and count how many NA there are in v8
randomValues = np.random.choice([np.nan, 42], 5)
v8 = np.append(v8, randomValues)
nanSum = np.isnan(v8).sum()
print("value of var nan sum is " + str(nanSum))
print()

# 4) replace NaN in v8 with value 50
v8[np.isnan(v8)] = 50
print("value of var v8 is " + str(v8))
print()

# Exercise 4

# 1) Create a list l1 like this: h e 1 1 0
l1 = list(["H", "e", 1, 1, 0])
print("value of var l1 is " + str(l1))
print()

# 2 Get Elements in the position 0,2,3 and get last element
elementsInPosition = [l1[i] for i in (0, 2, 3)]
elementsInPosition.append(l1[-1])
print("value of variable elementsInPosition is " + str(elementsInPosition))
print()

# 3) Create a list l2 with inside:
#   1) A numeric array as (1,2,3,4,5)
#   2) A categorical array as ("child", "adult", "elder")
#   3) A boolean array as (True, False, True)
#   4) A list of following elements (1, "3", True)
c1 = np.array([1, 2, 3, 4, 5])
c2 = pd.Categorical(["child", "adult", "elder"])
c3 = np.array([True, False, False])
c4 = list([1, "3", True])
l2 = [c1, c2, c3, c4]
print("value of var l2 is " + str(l2))
print()

# Exercise 5

# 1) Create an empty matrix named m1 with 7 rows and 5 columns
m1 = np.empty((7, 5))
print("value of var m1 is " + str(m1))
print()

# 2) Print the dimension of matrix m1 and the total numbers of elements inside matrix m1
shape = m1.shape
size = m1.size
print("shape is equal to " + str(shape) + " and size is equal to " + str(size))
print()

# 3) Create the following matrices in Python in different ways:
#   1) Using Matlab notation:
#       1 0 0
#       0 2 0
#       0 0 3
matrix1 = np.matrix("1,0,0;0,2,0;0,0,3")
print("value of matrix 1 is :")
print(str(matrix1))

#   2) Using traditional numpy matrix:
#       1 2 1
#       2 1 2
matrix2 = np.matrix([1, 2, 1, 2, 1, 2]).reshape((2, 3))
print("value of matrix 2 is ")
print(str(matrix2))

#   3) Using multidimensional array:
#       4 2
#       0 0
#       2 4
matrix3 = np.array([4, 2, 0, 0, 2, 4]).reshape((3, 2))
print("value of matrix 3 is  ")
print(str(matrix3))

# Exercise 6

# 1) Create a 0 matrix m2 with 5 rows and 3 columns using multidimensional array
m2 = np.zeros((5, 3))
print("value of var m2 is " + str(m2))
print()

# 2) Create the following matrix m3 with multidimensional array and get the power of matrix created
# 21 30 36 17
# 45 12 14 31
# 15 50 32 29
# 22 33 13 40
m3 = np.array([21, 30, 36, 17, 45, 12, 14, 31, 15, 50, 22, 29, 22, 33, 13, 40]).reshape((4, 4))
power2M2 = np.power(m3, 2)
print("value of var m3 is " + str(m3))
print("value of var power2M2 is " + str(power2M2))
print()

# 3) get numbers [14, 32,13] from matrix m3:
tempMatrix = m3[1:, 2]
print("value of tempMatrix is " + str(tempMatrix))
print()

# 4) Get the last row of matrix m3:
tempMatrix = m3[-1, :]
print("value of var tempMatrix is " + str(tempMatrix))

# 5) add new row to matrix m3 with value 0 and add new coluymn with values 1
num_row = len(m3[1, :])
new_row = np.zeros((num_row,))
m3 = np.vstack((m3, new_row))

num_col = len(m3[:, 1])
new_column = np.ones((1, num_col)).T  # T -> Transpose
m3 = np.hstack((m3, new_column))

print("value of var m3 is ")
print(str(m3))
print()

# Exercise 7

# 1) Create a datafreme df1 with three columns named:
#       1 - name: (Monica, Alberto, Bruno, Ilaria, Antonio)
name = np.array(["Monica", "Alberto", "Bruno", "Ilaria", "Antorio"])
#       2 - age:  (10, 20, 05, 36, 80)
age = np.array(([10, 20, 5, 36, 80]))
#       3 - category : (child, adult, child, adult, elder) (hint: categorical column set order from youngest to oldest)
category = pd.Categorical(["child", "adult", "child", "adult", "elder"])

data = {"name": name, "age": age, "category": category}
df1 = pd.DataFrame(data)
print("value of var df1 is ")
print(str(df1))
print()

# 2) Add new categorical array named gender as a column in df1
df1['gender'] = pd.Categorical(["F", "M", "M", "F", "M"])
print("value of var df1 is ")
print(str(df1))
print()

# 3) add a new person named Francesco with age 55 (adult) as a row in df1
df1 = df1.append({"name": "Francesco", "age": 55, "category": "adult", "gender": "M"}, ignore_index=True)
print("value of var df1 is ")
print(str(df1))
print()

# Exercise 8

# 1) Load data from csv as dataframe structure in df2
df2 = pd.read_csv("test_load_dataframe.csv")
print("value of var df2 ")
print(str(df2))
print()

# 2) Check structure and statistics of dataframe loaded in df2 and show the first 5 rows
print("df2 infos ")
print(str(df2.info()))
print()
print("describe ")
print(str(df2.describe()))
print()
print("first 5 rows ")
print(str(df2.head(5)))
print()

# 3) Show the dimension and the columns names of df2
print("df2 shape")
print(str(df2.shape))
print()
print("df2 columns")
print(str(df2.columns))
print()

# 4) Check how many missing value there are in df2 for each columns
missingValues = df2.isnull().sum()
print(str(missingValues))

# Exercise 9

# 1) Replace missing value (NaN) for column x1 with its mean in df2
valuesNotNaN = df2[df2['x1'].notnull()]
df2['x1'] = df2['x1'].fillna(np.average(valuesNotNaN['x1']))
print("value of df2 ")
print(str(df2))
print()

# 2) Replace missing value (NaN) for column x3 with “AA” in df2
df2['x3'] = df2['x3'].fillna("AA")
print("value of df2 ")
print(str(df2))
print()

# 3) Remove rows which contain missing values (NaN) for column x4 in df2
df2 = df2[df2['x4'].notnull()]
print("value of df2 ")
print(str(df2))
print()

# 4) Check how many NaN values there are in each column of dataframe df2
missingValues = df2.isnull().sum()
print(str(missingValues))
print()

# 5) Check how many NaN values there are in dataframe df2
missingValues = df2.isnull().sum().sum()
print(str(missingValues))
print()
