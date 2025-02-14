# Python Data Analysis Exercises

## Overview
This repository provides a series of exercises designed to help learners understand how to perform data analysis using Python. The exercises cover topics such as SQLite database operations, data cleaning, Pandas DataFrame manipulations, NumPy array operations, and data visualization using Matplotlib.

## Prerequisites
To complete these exercises, you should have the following Python libraries installed:
- `pandas`
- `numpy`
- `sqlite3`
- `matplotlib`

You can install missing libraries using:
```bash
pip install pandas numpy matplotlib
```

## Exercises (Ordered by Difficulty)

### **Beginner Level** [Python_basic.py](https://github.com/yagebin79386/PythonDataAnalysis/blob/d47b4f1e16f65fd5accf631dd7d2668ccace7528/Python_basic.py)
#### Task 1: Python Basics
- Print statements and basic syntax.
- Variables and data types.
- Basic arithmetic operations.

#### Task 2: Lists, Tuples, and Dictionaries
- Create and manipulate lists.
- Work with tuples and dictionaries.

#### Task 3: Conditional Statements and Loops
- Implement `if`, `elif`, and `else` statements.
- Use loops (`for` and `while`) for iteration.

#### Task 4: Functions and Error Handling
- Define and call functions.
- Handle exceptions using `try` and `except`.

### **Intermediate Level** [Sqlite_Exercise.py](https://github.com/yagebin79386/PythonDataAnalysis/blob/d47b4f1e16f65fd5accf631dd7d2668ccace7528/Sqlite_Exercise.py)
#### Task 5: SQLite Database Connection
- Establish a connection with an SQLite database.
- Retrieve data from a table and display it using Pandas.

#### Task 6: Data Cleaning
- Handle missing data (replace empty values, remove NaN values).
- Remove duplicates.
- Clean and standardize text.
- Save cleaned data to a CSV file.

#### Task 7: Load Cleaned Data
- Read the cleaned data from a CSV file into a Pandas DataFrame.

### **Advanced Level** [Exercise_numpy_pandas.py](https://github.com/yagebin79386/PythonDataAnalysis/blob/d47b4f1e16f65fd5accf631dd7d2668ccace7528/Exercise_numpy_pandas.py)
#### Task 8: NumPy Arrays
- Create different types of NumPy arrays.
- Perform basic mathematical operations.
- Apply slicing, indexing, and boolean filtering.

#### Task 9: Pandas Series and DataFrame Operations
- Convert lists and dictionaries into Pandas objects.
- Perform indexing, slicing, and filtering.

#### Task 10: DataFrame Operations
- Create a DataFrame with numerical values.
- Compute column sums, averages, and apply filtering.
- Sort values and apply transformations.

#### Task 11: Grouping and Merging Data
- Use `groupby()` to calculate the mean of grouped data.
- Perform inner, outer, and left merges on DataFrames.

#### Task 12: Data Selection
- Use `loc` and `iloc` to select specific rows and columns.
- Apply filtering using conditions.

#### Task 13: Data Visualization
- Create bar charts to visualize programming language popularity.
- Create scatter plots for random data distributions.
- Generate pie charts for categorical data representation.

### **Expert Level** [Covid_Exercise.py](https://github.com/yagebin79386/PythonDataAnalysis/blob/d47b4f1e16f65fd5accf631dd7d2668ccace7528/Covid_Exercise.py)
#### Task 14: COVID-19 Data Analysis
- Perform data cleaning and preprocessing.
- Conduct time series analysis.
- Perform statistical analysis and hypothesis testing.
- Generate correlation heatmaps and trend visualizations.
- Analyze healthcare system data.

## Running the Exercises
1. Clone this repository:
   ```bash
   git clone <repo_url>
   cd python-data-analysis
   ```
2. Open a Jupyter Notebook or Python script and run the exercises step by step.

## Contribution
If you have improvements or additional exercises, feel free to fork this repository and submit a pull request!

## License
This project is open-source under the MIT License.
