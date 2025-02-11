# %% [markdown]
# # Task 1
# ### Create a one-dimensional Numpy array containing numbers from 1 to 10.
# 

# %%
import numpy as np
arr1 = np.array(range(1,11))
print(arr1)

# %%
arr2 = np.arange(11,0,-2)
print(arr2)
arr3 = np.arange(0,11,3)
print(arr3)

# %%
arr_4 = np.linspace(0,1,11, dtype= "int64")
print(arr_4)

# %% [markdown]
# # Task 2
# ### Create a two-dimensional Numpy array, with three rows and three columns, filled with the value 5.
# 

# %%
array = np.full((2,3),None)
print(array)

# %% [markdown]
# # Task 3
# ### Create a Numpy array of zeros with five rows and five columns.
# 

# %%
array_0 = np.full((5,5),0)
print(array_0)

# %% [markdown]
# # Task 4
# ### Create a Numpy array of units with 4 rows and 4 columns.
# 

# %%
arr_u = np.full((4,4), "unit")
print(arr_u)

# %% [markdown]
# # Task 5
# ### Create a Numpy array containing even numbers from 0 to 20.
# 

# %%
arr_20 = np.linspace(0,20,21)
print(arr_20)

# %%
arr_50 = np.array([1,2,3,4])
arr_60 = np.array([5,6,7,8])
arr_70 = np.array([3,6,3,7])

print(arr_50 + arr_60 + arr_70)
print(np.add(arr_50, arr_60, arr_70))

print(arr_50 - arr_60 - arr_70)
print(np.subtract(arr_50, arr_60, arr_70))

print(arr_50 * arr_60 * arr_70)
print(np.multiply(arr_50, arr_60, arr_70))

print(arr_50 / arr_60)
print(np.divide(arr_50, arr_60))

# Original array
array = np.array([[1,2,3],[4,5,6]])
reshaped_array = array.reshape((2,3))
print(reshaped_array)


# Flatten an array
print(np.ravel(array))

# Concatinte 
np.concatenate([arr_50,arr_60])

# using indexing to create a new array
index = list(range(6,1,-1))
print(index)
ori_arr = np.concatenate((arr_60, arr_50, arr_70))
print(ori_arr[index])

a = np.array([[1,2,3,4], [5,6,7,8]])
print(a)
c = a[1,2]
print(c)


# 3 dimensioanl indexing
b = np.array(
    [[[1,2,3,4], [5,6,7,8]],[[9,10,11,12], [13,14,15,16]]]
)

print(b[...,[0,1]])
print(b[:,:,[0,1]])

# Boolean indexing
print("-----------")
mask = b > 11
print(b[mask])

# %% [markdown]
# # Task 6
# ### Create a Numpy array containing a sequence of numbers from 0 to 1, with a step of 0.1.
# 

# %%
arr_s1 = np.linspace(0,1,11)
print(arr_s1)

# %% [markdown]
# # Task 7
# ##  Create a Pandas series containing integers from 1 to 5.

# %%
import pandas as pd
ser = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'])
print(ser)




# %% [markdown]
# # Task 8
# ## Create a Pandas DataFrame from a dictionary, with two columns: 'name' and 'age', containing the names 'Alice', 'Bob', 'Charlie' and 'David' respectively, and the ages 25, 30, 35 and 40

# %%
names = ['Alice', 'Bob', 'Charlie', 'David']
ages = [25,30,35,40]



df_dict = {name: age for name, age in zip(names, ages)}
print(df_dict)

df_dict = {names[i]: ages[i] for i in range(len(names))}
print(df_dict)

df = pd.DataFrame(list(df_dict.items()), columns=["names", "ages"])
print(df)
        

# %% [markdown]
# # Task 9
# ##  Display the first three lines of the DataFrame created in the previous exercise.

# %%
print(df[1:3])

lst = ["asdf","dag","asd","asdge","age","asd","ht","vr","verh","ce"]
df1 = pd.DataFrame(lst)
print(df1)


# %% [markdown]
# # Task 10
# ## Display the last two lines of the DataFrame created in task 9

# %%
df_la2 = df[-2:]
print(df_la2)

# %% [markdown]
# # Tas 11
# ## Display the information from the DataFrame created in task 9.

# %%
print(df)

# %% [markdown]
# # Task 12
# ##  Add a new 'ville' column to the DataFrame created in task 9 containing the cities 'Paris', 'Lyon', 'Marseille' and 'Toulouse'

# %%
df["ville"] = ["Paris", "Lyon", "marseille", "Toulouse"]
print(df)
df.head(3)

# %% [markdown]
# # Task 13
# ##  Create a DataFrame from the following Numpy array: `np.array([[7, 8, 9], [10, 11, 12]])`, with columns 'D','E', 'F'

# %%
array_f = np.array([[7,8,9],[10,11,12]])
df_ar = pd.DataFrame(array_f, columns= ['D','E','F'])
print(df_ar)

# %% [markdown]
# # Task 14
# ## Assuming there's a CSV file named 'data.csv' in the same directory as your Python script. Write a code to read this CSV file and convert it into a DataFrame

# %%
import pandas as pd

file = pd.read_excel("./Fruit-Prices-2022.xlsx")

print(file)



# %%
pip install openpyxl

# %% [markdown]
# # Task 15
# ## Assuming there's an Excel file named ‘Fruit-Prices-2022.xlsx' in the same directory as your Python script. Write a code to read this Excel file and convert it into a DataFrame.

# %%
import pandas as pd

file = pd.read_excel("./Fruit-Prices-2022.xlsx")

print(file)

# %% [markdown]
# # Task 16
# ## Write a code to export the DataFrame created in Task 9 to a CSV file named 'exported.csv’. Be sure not to write the DataFrame index to the CSV file.

# %%
print(df)
df.to_csv("./exported.csv", index=False)

# %% [markdown]
# # Task 17
# ## Create a DataFrame with columns 'X' and 'Y' containing values [1, 2, 3, 4, 5] and [6, 7, 8, 9, 10] respectively. Then calculate the sum of column 'X'.
# 

# %%
import numpy as np
arr_n = np.array([[1,2,3,4,5],[6,7,8,9,10]])
arr_n = arr_n.reshape(5,2)
print(arr_n)
df_ar = pd.DataFrame(arr_n, columns=['X', 'Y'])
somme = df_ar.iloc[:,0].sum()
print(somme)

# %% [markdown]
# # Task 18
# ## From the DataFrame created in the previous exercise, calculate the average of the 'Y' column

# %%
sum_y = df_ar.loc[:,'Y'].sum()
print(df_ar.shape[0])
sum_y / df_ar.shape[0]

# %% [markdown]
# # Task 19
# ## Select the rows of the DataFrame from Task 18 where 'X' is greater than 3

# %%
mask_x = df_ar.X > 3
print(mask_x)
df_ar.X[mask_x]

# %% [markdown]
# # Task 20
# ## Use the sort_values() to Sort the DataFrame obtained in Task 20 according to the 'Y' column in ascending order

# %%
df_ar_new = df_ar.sort_values(by = 'Y', ascending=True).reset_index(drop=True)



print(df_ar_new)

# %% [markdown]
# # Task 21
# ##  Apply the square function to the 'X' column of the DataFrame from the previous exercise

# %%
df_ar_new['X'] = df_ar_new['X'] ** 2

print(df_ar_new)
    

# %% [markdown]
# # Now run the folowing in a code cell : 
# ### pip install openpyxl to open and read Excel files

# %% [markdown]
# # You have been provided with an Excel file named Fruit-Prices-2022.xlsx that contains data on various fruits, their forms (e.g., fresh, dried, juice, canned), and their retail prices. Your task is to analyze this dataset and extract meaningful insights.
# 
# ## Instructions:
# ###     1. Read the Excel File: Import the dataset using the pandas library.
# 
# ###     2. Dataset Information: Display basic information about the dataset.
# 
# ###     3. Data Overview: Print the first 5 rows to understand the structure of the data.
# 
# ###     4. Retail Price Statistics:
# 
# ####        . Calculate and display the mean retail price.
# 
# ####        . Identify and display the maximum and minimum retail prices and display the cheapest and most expensive fruit accordingly
# 
# ###     5. Unique Fruits: Count and display the number of unique fruits.
# 
# ###     6. Fruit Forms: Identify and display the unique forms of fruits.
# 
# ###     7. Top 10 Most Expensive Fruits: Find and display the top 10 most expensive fruits based on retail price.
# 
# ###     8. Fresh Fruits Analysis:
# 
# ####        . Count and display the number of fresh fruits.
# 
# ####        . Calculate and display the average price of fresh fruits.

# %%
import pandas as pd

file = pd.read_excel("./Fruit-Prices-2022.xlsx")

# 3.
print(file.head(5))

#4. statistic of retail price
mean_re = file.RetailPrice.sum()/file.shape[0]
print(mean_re)

max_re = file.RetailPrice.max()

print(max_re)

min_re = file.RetailPrice.min()
print(min_re)

max_in = file[file.RetailPrice == max_re].index[0]
min_in = file[file.RetailPrice == min_re].index[0]

print(file.Fruit[max_in])
print(file.Fruit[min_in])

uni_fruit = set(file.Fruit)
print(len(uni_fruit))
print(uni_fruit)

uni_form = set(file.Form)
print(len(uni_form))
print(uni_form)

file = file.sort_values(by="RetailPrice", ascending=False).reset_index(drop=True)
file.Fruit.head(5)


fresh_file = file[file.Form == 'Fresh']
fresh_Fruit = set(fresh_file.Fruit)
print(len(fresh_Fruit))
print(fresh_Fruit)
fresh_file.RetailPrice.sum()/fresh_file.shape[0]

# %%



