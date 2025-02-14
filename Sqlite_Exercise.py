# %% [markdown]
# # Task 1
# ##  SQLite : Data Base 
# ### Create the connection with the data base provided to you

# %%
import sqlite3
import pandas as pd

conn = sqlite3.connect('myDatabase.db')

df = pd.read_sql_query('SELECT * from users', conn)
print(df)


# %% [markdown]
# # Task 2

# %%
import pandas as pd
import sqlite3

# Database file
DB_FILE = 'myDB.db'

try:
   # Connect to the database
   conn = sqlite3.connect(DB_FILE)
   
   # SQL query to retreive all data from the table
   user_query = "SELECT username, name, lastname, email FROM users"
   
   # Load data
   df_users = pd.read_sql_query(user_query, conn)
   

   # Data Cleaning
   
   # 1. Replace empty strings and whitespace with NaN using the replace() function
   # replace them by pd.NA
   df_users = df_users.replace('', pd.NA)
   df_users = df_users.replace(' ', pd.NA)
   
   # 2.a. Handle missing data for the name using a lambda function


   # for each row in the username column check if the name is null using isna() function
   df_users['username_null'] = df_users.apply(
      lambda row: pd.isna(row['username']) , axis=1
   )
   #print(df_users.username_null)
   # if the name is null fill it with the username otherwise keep the original name


   # The changes should be applied to the name column, use apply() to save the changes
   df_users['name'] = df_users.apply(
       lambda row: row['username'] if pd.isna(row['name']) else row['name'],
       axis=1
   )

   
   # 2.b Fill the empty last names with 'Unknown' text
   df_users['lastname'].replace('Unknown', pd.NA)
   print('Unknown' in df_users['lastname'])
   
   # 3. Remove rows with missing emails using the dropna()
   # use the subset=['email'] to not affect other columns
   df_users.dropna(subset=['email'], inplace=True)
   print(df_users)
   print(df_users['email'].isna())
   
   # 4. Remove duplicates using the drop_duplicates()
   df_users = df_users.drop_duplicates()
   
   # 5. Clean and standardize text
   for col in ['username', 'name', 'lastname', 'email']:
      df_users[col] = df_users[col].astype(str).str.lower().str.strip()
   
   # 6. Reset index using the reset_index(drop=True)
   df_users = df_users.reset_index(drop=True)
   print(df_users)
   # Verify cleaning results
   print("\nChecking for remaining empty values:")
   for column in df_users.columns:
       empty_count = (df_users[column] == '').sum()
       na_count = df_users[column].isna().sum()
       print(f"{column}: {empty_count} empty strings, {na_count} NA values")
   
   # Display cleaned data
   print("\nCleaned User Data:")
   print(df_users.to_string(index=False))
   
   # Save to CSV
   df_users.to_csv("./cleaned_user_data.csv", index=False)
   print("\nData saved to 'cleaned_user_data.csv'")

except sqlite3.Error as e:
   print(f"Database error: {e}")
except Exception as e:
   print(f"An error occurred: {e}")
finally:
   if conn:
       conn.close()

# %% [markdown]
# # Task 3
# ## Create a data set from the cleaned_user_data csv file

# %%
cleaned_df = pd.read_csv("cleaned_user_data.csv")
print(cleaned_df)

# %% [markdown]
# # Task 4
# ### a. Create a DataFrame with columns 'X' and 'Y' containing values 
# ### [1, 2, 3, 4, 5] and [6, 7, 8, 9, 10] respectively. Then calculate the sum of column 'X'.
# 
# ### b. From the DataFrame created in the previous exercise, calculate the average of the 'Y' column.
# ### c. Select the rows of the DataFrame from exercise 14 where 'X' is greater than 3.
# ### d. Use the sort_values() to Sort the DataFrame obtained in exercise 12 according to the 'Y' column in ascending order.
# ### e. Apply the square function to the 'X' column of the DataFrame from the previous exercise.
# 
# 
# 

# %%
key1 = ['X','Y']
value1 = [range(1,6), range(6,11)]

df_dict = {key: value for key, value in zip(key1 , value1)}
print(df_dict)

df_tr = pd.DataFrame(df_dict)
print(df_tr)
print(f"the sum of X is {df_tr.X.sum()}")
print(f"the mean of Y is {df_tr.Y.mean()}")

# c. 
print(df_tr[df_tr.X > 3])

# d.
print(df_tr.sort_values('Y', ascending=True))


# e.
df_tr.X = df_tr.X ** 2
print(df_tr)



# %% [markdown]
# # Task 5
# ### consider this as data for you data frame:
# #### {'Animal': ['Eagle', 'Eagle','Sparrow','Sparrow'],
# ####  'Max Speed': [350., 320., 26., 30.]}
# 
# ## Group them by the Animal name and see the average speed for each animal

# %%
data1 = {'Animal':['Eagle','Eagle','Sparrow','Sparrow'], 'Max Speed':[350.,320.,26.,30.]}
df3 = pd.DataFrame(data1)
ani_name = set(df3.Animal)
gk = df3.groupby('Animal')
eagle = gk.get_group('Eagle')
print(eagle)
print(gk.first())
print(gk.sum())
gk_sp = gk.mean()
print(gk_sp)


# %% [markdown]
# # Task 6
# ### Create two DataFrames df1 and df2 with a common column 'key'.
# #### df1 = { 'key': ['K0', 'K1', 'K2', 'K3'],
# ####  'A': ['A0', 'A1', 'A2', 'A3'],
# ####   'B': ['B0', 'B1', 'B2', 'B3']}
# ### a. Then merge these two DataFrames on the 'key' column.
# ### b. merge them using the 'outer' method.
# ### c. merge them using the 'left' method.

# %%
data3 = {'key':['K0','K1','K2','K3','K5'], 'A':['A0','A1','A2','A3','A4'], 'B':['B0','B1','B2','B3','B12']}
data4 = {'key':['K0','K1','K2','K3','K4'], 'D':['A3','A12','A63','A03','A99'], 'E':['B23','B14','B8','B24','B24']}
df3 = pd.DataFrame(data3)
df4 = pd.DataFrame(data4)



df_conca = pd.concat([df3 ,df4], axis=1)
print(df_conca)
df_merge = pd.merge(df3, df4, on = 'key')
print(df_merge)
df_merge_left = pd.merge(df3, df4, how='left', on = 'key')
print(df_merge_left)
df_merge_right = pd.merge(df3, df4, how='right', on = 'key')
print(df_merge_right)
df_merge_inner = pd.merge(df3, df4, how='inner', on = 'key')
print(df_merge_inner)
df_merge_outer = pd.merge(df3, df4, how='outer', on = 'key')
print(df_merge_outer)


# %% [markdown]
# # Task 7
# ### create a data frame containing these data:
# #### {
# ####     'A': range(10),
# ####     'B': range(10, 20),
# ####     'C': range(20, 30),
# ####     'D': range(30, 40)
# ####  }
# 
# ## a. se loc to select the first 5 elements of the first column
# ## b. Use `loc` to select the elements in the 3rd and 7th rows of the second column of your DataFrame.
# ## c. Use `loc` to select elements from the 2nd to the 6th row of columns 'A' and 'C'.
# ## d. Use `iloc` to select the elements in the last 4 rows of the last column.
# ## e. Use `iloc` to select elements in the 2nd, 4th and 6th rows of the 1st and 3rd columns.
# ## f. Filter your DataFrame to keep only rows where column 'B' is greater than 13.
# ## g. Filter your DataFrame to keep only rows where column 'C' equals 21 or 24 use isin().
# ## h.Filter your DataFrame to keep only rows where column 'D' is less than 32 and not equal to 30.
# 
# 

# %%
data4 = {'A':range(10), 'B':range(10,20), 'C':range(20,30), 'D':range(30,40)}
df4 = pd.DataFrame(data4)
print(df4)
# a.
print(df4.loc[range(6),'A'])

# b.
print(df4.loc[[2,6],'B'])

# c.
print(df4.loc[range(1,6),['A', 'C']])

# d.
print(df4.iloc[-4:,-1])

# e.
print(df4.iloc[[1,3,5],[0,2]])

# f.
print(df4[df4['B']>13])

 # g
mask = df4.C.isin([21, 24])
print(df4[mask]) 

# h.
print(df4[(df4.D <= 32) & (df4.D != 30)])


# %% [markdown]
# # Task 8
# ## Write a  Python programming to display a bar chart of the popularity of  programming Languages.
# 
# ### Sample data:
# ### Programming languages: Java, Python, PHP, JavaScript, C#, C++
# ### Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

# %%
import pandas as pd
data = {'Prog_lang': ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'],
        'Popularity': [22.2, 17.6, 8.8, 8, 7.7, 6.7]}

df = pd.DataFrame(data)
print(df)

# %%
pip install matplotlib

# %% [markdown]
# import matplotlib.pyplot as plt
# x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
# popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
# x_pos = [i for i, _ in enumerate(x)]
# plt.bar(x_pos, popularity, color='blue')
# plt.xlabel("Languages")
# plt.ylabel("Popularity")
# plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
# plt.xticks(x_pos, x)
# # Turn on the grid
# plt.minorticks_on()
# plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# # Customize the minor grid
# plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
# plt.show()

# %%
import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

# %% [markdown]
# # Task 9
# ## Write a Python programming to display a horizontal bar chart of the popularity of programming Languages.
# 
# ### Sample data:
# ### Programming languages: Java, Python, PHP, JavaScript, C#, C++
# ### Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

# %%
import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color='blue')
plt.ylabel("Languages")
plt.xlabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.yticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

# %% [markdown]
# # Task 10
# ## Write a  Python programming to create a pie chart of the popularity of  programming Languages.
# 
# ### Sample data:
# ### Programming languages: Java, Python, PHP, JavaScript, C#, C++
# ### Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

# %%
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
import matplotlib.pyplot as plt
plt.pie(popularity, labels=x, autopct='%1.1f%%', colors=['blue', 'green', 'orange', 'red', 'purple', 'yellow'])

# define the title
plt.title("Popularity of Programming language")
plt.show()


# %% [markdown]
# # Task 11
# ## Write a  Python program to draw a scatter graph taking a random distribution in X and Y and plotted against each other.

# %%
import numpy as np
x = np.random.rand(100)
y = np.random.rand(100)
print(x)

plt.scatter(x,y)
plt.xlabel("X Values")
plt.ylabel("Y values")
plt.title("The scatter spot chart")

plt.show()





# %% [markdown]
# # Task 12
# ## Write a  Python program to draw a scatter plot with empty circles taking a random distribution in X and Y and plotted against each other.

# %%


# %% [markdown]
# # Task 13
# ## Write a  Python program to draw a scatter plot for three different groups comparing weights and heights.







