# %% [markdown]
# # Task 1
# ### Create a new notebook in Jupyter and write some Python code to print "Hello World".
# 

# %%
print("Hello world")

# %% [markdown]
# # Task 2
# ### Calculate the Sum of two numeric variables, a and b. Print their summation result out
# 

# %%
a = 3
b = 10
a+b

# %% [markdown]
# # Task 3
# ### Ask the user for his name and age 
# ### Check whether he is over 18 or not
# ### Print all info in a sentence. using a String Literal
# Note that we need to convert the input to int and then back to a String to print it.
# 

# %%
name = input("what is your name?")
age = int(input("what is your age?"))
if age > 18:
    print(f"{name} who is {age} years old over 18")
elif age <= 18:
    print(f"{name} who is {age} years younger than 18")

# %% [markdown]
# # Task 4
# ### Create a list containing numbers from 1-10 and display it.
# ### Display the 5th element in that List 
# ### Then add the number 11 to the end of the list using the `append()` and display the final result
# 

# %%
my_list = list(range(1,11))
for i in my_list:
    print(i, end="")
print(f"The 5th element of my_list is {my_list[4]}")
my_list.append(11)
print(my_list)

# %% [markdown]
# # Task 5
# ### Create a Tuple containing the letters ‘a’, ‘b’ and ‘c’.
# ### Display the Tuple created.
# 

# %%
letters = ("a", "b", "c")
print(letters)

# %% [markdown]
# # Task 6
# ### Create a dictionary associating the days of the week with their numbers (where Monday is 1 and Sunday is 7), then change Sunday's number to 0.
# 
# 

# %%
weekday = {}
days = ["monday", "tuesday", "wedensday", "thursday", "friday", "saturday", "sunday"]
count = 1
for day in days:
    weekday[day]=count
    count += 1
print(weekday)

weekday["sunday"] = 0
print(weekday)

# %% [markdown]
# # Task 7
# ### Create a set containing the names of three cities and display it. Add the name of another city to the set created and display the set. Remove a city name from the set and display it.
# 

# %%
city = set(["Zhengzhou", "Hainan", "Luxembourg"])
print(city)
city.remove("Zhengzhou")
print(city)

# %% [markdown]
# # Task 8
# ### Create a frozen set containing numbers from 1 to 5 and display it. Check whether the number 3 belongs to the frozen set created earlier.
# 

# %%
my_fro= frozenset(range(1,6))
print(my_fro)
check = 3 in my_fro
print(check)

# %% [markdown]
# # Task 9
# ### Create a set containing numbers from 1 to 10, then create another set containing numbers from 5 to 15. Display the intersection of these two sets.
# 

# %%
set1 = set(range(1,11))

set2 = set(range(5,16))
set3 = set1.intersection(set2)
print(set3)


# %% [markdown]
# # Task 10
# ### Get the length of the string "Python is the best" and display it. Convert the string to uppercase and display the new string.
# ### Replace all occurrences of the letter "t" with the letter "s" in the string and display the new string.
# 

# %%
str = "Python is the best"
print(len(str))
str = list(str)
for i in range(len(str)):
    if str[i] == "t":
        str[i] = "s"
print("".join(str))

# %% [markdown]
# # Task 11
# ### Convert the list ['a', 'b', 'c', 'd'] into a set and display it.
# ### Convert the list of numbers [1, 2, 3, 4, 5] into a string and display it.
# 

# %%
print(set(['a','b','c','d']))
num = range(1,6)
str_list = []
for i in num:
    str_list.append(str(i))
print(str_list)

# %% [markdown]
# # Task 12
# ### Use the `if`, `elif` and `else` statements to detect the greatest Number between 3 numbers

# %%
num_list = [123,53,135]

if num_list[0] > num_list[1]:
    max_12 = num_list[0]
    if max_12 > num_list[2]:
        pass
    elif max_12 <= num_list[2]:
        max_12 = num_list[2]
    print(f"The max num is {max_12}")
elif num_list[0] <= num_list[1]:
    max_12 = num_list[1]
    if max_12 > num_list[2]:
        pass
    elif max_12 <= num_list[2]:
        max_12 = num_list[2]
    print(f"The max num is {max_12}")




# %% [markdown]
# # Task 13
# ### Use the ternary operator to write a program that prints "even" if a number is even and "odd" if it is odd.
# 

# %%
number = 23
def check_even(num):
    if num % 2 == 0:
        print(f"The {num} is even")
    elif num % 2 == 1:
        print(f"The {num} is odd")
    else:
        print(f"The {num} is neither even nor odds")
print(check_even(number))
       


# %% [markdown]
# # Task 14
# ### Write a program that determines the nature of a triangle (equilateral, isosceles, scalene) according to the length of its sides.
# 

# %%
def check_triangle(side):
    max_side = max(side)
    side.remove(max_side)
    if side[0] == side[1]:
        if side[0] ** 2 * 2 == max_side ** 2:
            print("It's a equilateral triangle")
        elif side[0]**2 + side[1]**2 > max_side ** 2:
            print("It's a isosceles triangle")
        else:
            print("It's not a triangle")
    elif side[0] != side[1]:
        if side[0] ** 2 + side[1] ** 2 >= max_side ** 2:
            print("It's a scalene")
        elif side[0] ** 2 + side[1] ** 2 < max_side ** 2:
            print("It's not an triangle.")          

side=[3,4,5]
check_triangle(side)


# %% [markdown]
# # Task 15
# ### Use a `while` loop to calculate the product of the first 5 numbers in a list that contains 20 element.
# ### Hint: Use a break

# %%
cal = list(range(21))
figure = 1
count = 0
while count < 5:
    for i in cal:
        figure += i
        count += 1
        
print(figure)






# %% [markdown]
# # Task 16
# ### Use a `for` loop and the `continue` statement to print out all the odd numbers in a list.
# ### At the end of the program print the sum of all the numbers the list.

# %%
original_lit = [1,24,65,3,2,35,74,38,45,23]
odds_lit = []
for i in original_lit:
    if i % 2 == 1:
        odds_lit.append(i)
        print(i)
    else:
        continue
print(sum(odds_lit))

# %% [markdown]
# # Task 17 
# ### Use a `for` loop to count the number of times a specific character appears in a string.
# 

# %%
word = "asdtlgja atlkjsdfl"
count = 0
for i in word:
    if i == "t":
        count += 1
print(count)

# %% [markdown]
# # Task 18
# ### Write a program that uses a loop to find the largest number in a list. Use `break` to stop the loop if a number is greater than a certain value.
# 

# %%
num_list = [123,12,53,135,123,51234,12,2,3,32,4,513,113]
largest= num_list[0]
thres = 100
for i in num_list:
    if i > largest:
        largest = i
        if largest > thres:
            break
    else:
        pass
print(largest)
    

# %% [markdown]
# # Task 19
# ### Using a while loop write a program that uses a `while` loop to print numbers from 1 to 10, but skips the number 5.
# 

# %%
num_th = 1
while num_th < 11:
    if num_th == 5:
        num_th += 1
        continue
    else:
        print(num_th)
        num_th += 1

# %% [markdown]
# # Task 20
# ### Create a list of number cubes from 1 to 10 using list comprehension.
# 

# %%
origin = [1,5,234,23,7,123]
list_cube = [i ** 3 for i in origin]
print(list_cube)

# %% [markdown]
# # Task 21
# ### Use list comprehension to create a list of odd numbers from 1 to 20.
# 

# %%
list_odds = []
list_odds = [i for i in list(range(21)) if i%2 == 1]  ## The criteria to keep a value puts at end, for calculation varation put at front.
print(list_odds)



# %% [markdown]
# # Task 22
# ### Create a list of squares of even numbers from 1 to 10 and cubes of odd numbers from 1 to 10.
# 

# %%
mix_list = [i ** 2 if i % 2 == 0 else i ** 3 for i in list(range(11))]
print(mix_list)

# %% [markdown]
# # Task 23
# ### Write a block of code that catches a `TypeError` when you try to divide a string by a number.
# 
# ### Catch a `ValueError` when trying to convert a non-numeric string to an integer.
# 

# %%
any_string = "asdji"
any_num = 0
try:
    any_string / any_num

except TypeError as e:
    print(f"you got a type error: {e}")

except ValueError as ev:
    print(f"you got a value error: {ev}")

# %% [markdown]
# # Task 24
# ### Write a block of code that catches any exception raised when adding a number to a string.
# 
# 

# %%
try:
    a + b
except Exception as e:
    print(f"you got an error {e}")

# %% [markdown]
# 


# %% [markdown]
# # Task 25
# ### Create a function that accepts a string and returns the inverted string.
# 

# %%
def invert_str():
    str_ = input("Please input something")
    str_list = list(str_)
    str_list.reverse()
    for i in str_list:
        print(i, sep='', end='')
invert_str()

# %% [markdown]
# # Task 26
# ### Create a function that accepts two strings and returns the longer one. If they have the same length, return the first one.
# 

# %%
def return_longer():
    string1 = input("Please input the first string")
    string2 = input("Please input the second string")
    len1 = len(string1)
    len2 = len(string2)
    if len1 >= len2:
        print(string1)
    else:
        print(string2)

return_longer()  
    

# %% [markdown]
# # Task 27
# ### Create a function that accepts an unlimited number of keyword arguments and displays them as key-value pairs.
# 

# %%
def create_dict():
    while True:
        my_dict={}
        if int(input("Continue : 1, Break : 0")) == 1:
            Key_=input("please input a key")
            Value= input("Please input a value")
            my_dict[Key_]= Value
            print(my_dict)
        else:
            break

create_dict()

        

# %% [markdown]
# # Task 28
# ### Create a lambda function that takes two numbers and returns their product.
# 

# %%
product = lambda a,b: a*b

print(f"The product of a and b is {product(3,5)}")

# %% [markdown]
# # Task 29
# ### Create a lambda function that takes a string and returns its length.
# 

# %%
string_len = lambda str_: len(str_)
print(f"The word length is {string_len("Sunshine")}")

# %% [markdown]
# # Task 30
# ### Import the datetime module and use the now()  function to obtain the current time; use the date() function to create a date and use the time() function to create a specific time.
# 

# %%
from datetime import datetime, date, time

current_time = datetime.now()
our_date = date(2025,2,10)
our_time = time(4,35,30)
print(current_time)
print(our_date)
print(our_time)


# %% [markdown]
# # Task 31
# ### Obtain the current year using the year attribute on the datetime object returned by now().
# 

# %%
current_date = datetime.now()
print(current_date.year)

# %% [markdown]
# # Task 32
# ### Calculate the difference between these two dates:
# ###    January 1 2023 and December 31 2023.
# ### Print out the result obtained with its data type.
# 

# %%
date1 = date(2023,1,1)
date2 = date(2023, 12, 31)
print(date1 - date2)

# %% [markdown]
# # Task 33
# ### Get the current date and time and display them.
# 

# %%
current = datetime.now()
date_ = str(current.date())
time_ = str(current.time())

print("The current date is" + date_ + "and the current time is" + time_)


# %% [markdown]
# # Task 34
# ### Create a date representing “December 21 1999” and a time representing 03:45:00.
# 

# %%
date_1 = date(1999,12,21)
time_1 = time(3,45,0)
print(f"")

# %% [markdown]
# # Task 35
# ### Use the weekday() function to get the current day of the week. 
# ### Note: This method returns a number between 0-for Monday and 6-for Sunday
# 

# %%
current_weekday = datetime.now().weekday()


# %% [markdown]
# # Task 36
# ### Calculate the number of seconds between noon and 1:30pm on the same day.
# 

# %%
time_noon = time(12,0,0)
time_2 = time(13,30,0)
print(time_2 - time_noon)

# %% [markdown]
# # Task 37
# ### Use the 'datetime' module to obtain the date 7 days ago.
# 

# %% [markdown]
# # Task 38
# ### Use the 'random' module to select a random element from a list.
# ### Hint: use the choice function

# %% [markdown]
# # Task 39
# ### import the "random" module and use the "randint" function to generate a random integer between 1 and 10.

# %% [markdown]
# # Task 40
# 
# ### Create a base class named Animal with attributes: name and sound. Create a subclass named Cat that inherits from Animal. Override the sound attribute in the Cat class. Create a Cat object and print its name and sound.
# 

# %% [markdown]
# # Task 41
# ### Create a class named Person with attributes: name and age. Define a method named introduce that prints a greeting message using the person's name and age. Create a Person object and call the introduce method
# 


