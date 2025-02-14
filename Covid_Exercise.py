# %% [markdown]
# #Install all needed Modules for the project using the pip package
# #Such as:
#     # Numpy
#     # Pandas
#     # Matplotlib
#     # Seaborn
#     # datetime

# %%
import pandas as pd
import numpy as np
import datetime

# %% [markdown]
# # Phase 1:
# ## Data Preprocessing and Cleaning:
# 
# ### a. Handling missing values
# ### b. Converting date formats
# ### c. Data type validation
# ### d. Data quality assessment using data_quality_grade

# %%

# Load data
df = pd.read_csv("./covid_tracking.csv")

# Convert dates:
#Create a list containing all Labels for dates columns
date_column = ['date', 'last_update_et', 'date_checked', 'load_time']

# In a for loop iterate through these columns and use the to_datetime() to convert the data type to date
for col in date_column:
    df[col] = pd.to_datetime(df[col])
    print(df[col].dtype)
df.head(10)


# %%

# Define Numerical columns for conversion in a list
all_col = df.columns.to_list
check_nan = all(pd.isna(val) for val in df.data_quality_grade)
print(check_nan)
numeric_cols = ['positive', 'negative', 'pending','hospitalized_currently', 'hospitalized_cumulative', 'in_icu_currently',
       'in_icu_cumulative', 'on_ventilator_currently',
       'on_ventilator_cumulative', 'recovered', 
       'death', 'hospitalized',
       'total', 'total_test_results', 'pos_neg', 'fips', 'death_increase',
       'hospitalized_increase', 'negative_increase', 'positive_increase',
       'total_test_results_increase', 
       ]

# Convert numeric columns using a for loop use the to_numeric()
for col_val in numeric_cols:
    if df[col_val].dtype == "object":
        df[col_val] = df[col_val].str.strip().str.replace(',','')
        df[col_val] = pd.to_numeric(df[col_val])
    else:
        df[col_val] = pd.to_numeric(df[col_val])



## Handle missing values
# Convert to integer the columns declared in numeric_cols using a for loop. use the astype()
print(df.positive.dtype)
for col_val in numeric_cols:
    df[col_val].fillna(method = 'ffill', inplace=True)
    df[col_val].fillna(method = 'bfill', inplace=True)
    df[col_val] = df[col_val].astype('int64')


# Handle missing values of categorical columns: state, iso_country and data_quality_grade
categorical_cols = ['state', 'iso_country', 'data_quality_grade']
for col_cat in categorical_cols:
    df[col_cat].fillna('Unknown', inplace=True)


# Remove duplicates
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)


# Quality assessment
def assess_data_quality():
    return {
        'missing_values_by_column': df.isnull().sum(),
        'unique_quality_grades': df['data_quality_grade'].value_counts(),
        'date_range': f"From {df['date'].min()} to {df['date'].max()}",
        'records_per_state': df['state'].value_counts()
    }


# Print reports and save
quality_report = assess_data_quality()
print("\nData Quality Report:")
print(quality_report)
print(df.isnull().sum())
print(df.dtypes)


df.to_csv('covid_tracking_cleaned.csv', index=False)
print("Data cleaning and preparation completed!")

for fix_na in ['date_checked', 'last_update_et']:
    df[fix_na].fillna('Unknown', inplace=True)

# %% [markdown]
# # Phase 2:
# ## Time Series Analysis:
# 
# ### a. Trend analysis of cases, deaths, and hospitalizations
# ### b. Rolling averages to smooth daily fluctuations
# ### c. Seasonality patterns in COVID-19 spread
# ### d. Growth rate calculations

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, date

# Read the cleaned data
df = pd.read_csv('./covid_tracking_cleaned.csv')
# convert the date column to date data type using the datetime()
df.date = pd.to_datetime(df.date)
df.date = df.date.apply(lambda x: datetime.combine(x, datetime.min.time()))
print(df.date.dtype)



# Calculate daily national totals for the folowing columns: positive_increase, death_increase, hospitalized_currently
#Group them by date and use the agg() function and reset the index after that
gy_date = df.groupby('date')
daily_totals = gy_date.agg(
                {
                    'positive_increase': 'sum',
                    'death_increase' : 'sum',
                    'hospitalized_currently' : 'sum'
                }
).reset_index()





# Calculate 7-day rolling averages for the following colums : positive_increase, death_increase, hospitalized_currently
daily_totals['cases_7day_avg'] = daily_totals['positive_increase'].rolling(window=7).mean()
daily_totals['deaths_7day_avg'] = daily_totals['death_increase'].rolling(window=7).mean()
daily_totals['hospitalized_7day_avg'] = daily_totals['hospitalized_currently'].rolling(window=7).mean()

# Calculate growth rates for the folowing columns: positive_increase, death_increase
daily_totals['case_growth_rate'] = daily_totals['positive_increase'].pct_change() * 100
daily_totals['death_growth_rate'] = daily_totals['death_increase'].pct_change() * 100

print(daily_totals)

# Set style for better visualizations
# 1. Set Seaborn Styles:
#    sns.set_style("style_name") sets the overall style of the plots.  "whitegrid" adds a white background with gridlines.
#    sns.set_palette("palette_name") sets the color palette to be used in the plots. "husl" is a color palette name.




# Create subplots
# 2. Create Figure and Subplots (using Matplotlib):
#    fig, (ax1, ax2) = plt.subplots(rows, columns, figsize=(width, height)) creates the figure (plot window) and subplots.
#    2, 1 means 2 rows, 1 column of subplots.
#    figsize sets the figure size (width, height) in inches.
#    The returned values are:
#        fig: The Figure object (represents the entire plot).
#        (ax1, ax2): A tuple containing the Axes objects. ax1 is the first subplot, ax2 is the second, and so on.  You'll use these to plot on the individual subplots.
plt.figure(figsize=(12,12))
plt.subplot(2,1,1)
plt.plot(daily_totals['date'], daily_totals['cases_7day_avg'])
plt.xlabel('Dates')
plt.ylabel('Cases(cases_7day_avg)')

plt.plot(daily_totals['date'], daily_totals['deaths_7day_avg']*10)
plt.title("Covid-19 Trends")
plt.legend(['Positive cases', 'Deaths'])
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(daily_totals['date'], daily_totals['case_growth_rate'])
plt.xlabel('Dates')
plt.ylabel('Percentage_change')

plt.plot(daily_totals['date'], daily_totals['death_growth_rate'].rolling(7).mean())
plt.title("Covid-19 Trends")
plt.legend(['Positive growth rate', 'Deaths growth rate'])
plt.grid(True)
plt.show()



# Plot trends
# 1. Plotting with Seaborn's lineplot:
#    sns.lineplot(data=DataFrame, x='column_for_x', y='column_for_y', label='legend_label', ax=subplot_axes) plots a line.
#    data: The DataFrame.
#    x, y: Columns for the x and y axes.
#    label: Label for the legend.
#    ax: The Axes object where the plot should be drawn (e.g., ax1, ax2 from plt.subplots).


# 2. Setting Titles and Labels for the Subplot:
#    ax.set_title("title_text") sets the title of the subplot.
#    ax.set_xlabel("x_axis_label") sets the label for the x-axis.
#    ax.set_ylabel("y_axis_label") sets the label for the y-axis.

# Plot growth rates
# 1. Plotting with Seaborn's lineplot (on the second subplot):
#    Same as before, but now using ax2 (the second subplot).
# 2. Setting Titles and Labels for the Second Subplot:
# 3. Adjust Layout and Show Plot:
#    plt.tight_layout() adjusts subplot parameters for a tight layout.
#    plt.show() displays the entire figure (containing both subplots).


# Monthly analysis
#1. Group by Month:
#    df.groupby(df['date'].dt.month) groups the DataFrame 'df' by the month of the 'date' column.
#    df['date'].dt.month extracts the month number (1 for January, 2 for February, etc.) from the 'date' column.

# 2. Aggregate by Mean:
#    .agg({'column1': 'aggregation_function', 'column2': 'aggregation_function', ...}) calculates the specified aggregation function for each group (each month).
#    Here, we use 'mean' to calculate the average of 'positive_increase', 'death_increase', and 'hospitalized_currently' for each month.

# 3. Round to 2 Decimal Places:
#    .round(2) rounds the resulting averages to two decimal places.
gk_new = df.groupby(df['date'].dt.month)
monthly_avg = gk_new.agg(
    {
        'positive_increase' : 'mean',
        'death_increase': 'mean',
        'hospitalized_increase' : 'mean'
    }
).round(2)

print("\nMonthly Averages:")
print(monthly_avg)

# Save results to an csv file named : time_series_analysis.csv
daily_totals.to_csv("./daily_total_report.csv")
print("Time series analysis completed!")


# %% [markdown]
# # Phase 3:
# ## Statistical Analysis:
# 
# ### a. Descriptive statistics of key metrics
# ### b. Distribution analysis of cases and deaths
# ### c. Hypothesis testing between different states/regions
# ### d. Confidence intervals for key metrics

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read data
df = pd.read_csv('covid_tracking_cleaned.csv')

# Descriptive statistics for key metrics that includes the folowing columns : positive, death, hospitalized_currently
desc_stats={}
key_lst = ['positive','death','hospitalized_currently']
for col in key_lst:
    desc_stats[col] = df[col].describe



# Describe only the part of the df that include the key_metrics
df_key_metrics = df[key_lst]
print(df_key_metrics)

print("\nDescriptive Statistics:")
print(desc_stats)

# Distribution plots
# 1. Create Figure and Subplots:
#    plt.figure(figsize=(15, 5)) creates a figure (plot window) 15 inches wide and 5 inches tall.
#    plt.subplot(1, 2, 1) creates the first subplot (1 row, 2 columns, the 1st plot).  Same logic for the 2nd subplot.
plt.figure(figsize=(15, 5)) 
plt.subplot(1, 2, 1)
# plt.boxplot(df[key_lst[0]], df[key_lst[1]], df[key_lst[2]])

# 2. Create Histograms with Seaborn:
#    sns.histplot(data=df, x='column_name', bins=number) creates a histogram.
#    data=df specifies the DataFrame.
#    x='column_name' specifies the column to plot.
#    bins=number specifies the number of bins (bars) in the histogram

sns.histplot(data=df, x= "positive", bins=50)
plt.title('Distribution of cases')
plt.xlabel("The number of cases")
plt.tight_layout()
plt.show()

# 3. Adjust Layout and Show Plot:
#    plt.tight_layout() adjusts subplot spacing.
#    plt.show() displays the plot.

# State comparisons
# Group by the state and calculate the average(mean),the standard deviation(std) 
# and count the missing values(count) for the columns in the metrics
state_stats = df.groupby('state')[key_lst].agg(['mean', 'std', 'count'])
print(state_stats)


# Calculate confidence intervals (95%)
# This is the formula used: SEM = σ / √n
# σ is the population standard deviation.
# n is the sample size 
confidence_level = 0.95
state_stats['positive_ci'] = state_stats[('positive', 'std')] * \
   (1.96 / np.sqrt(state_stats[('positive', 'count')]))
   
state_stats['death_ci'] = state_stats['death', 'std'] * \
(1.96/ np.sqrt(state_stats[('death', 'count')]))

print("\nState Statistics with Confidence Intervals:")
print(state_stats)

# Box plots for state comparisons
plt.figure(figsize=(15, 6))
sns.boxplot(data=df, x='state', y='positive')
plt.xticks(rotation=90)
plt.title('Cases Distribution by State')
plt.show()

state_stats.to_csv("./statistical_analysis.csv")
print("Statistical analysis completed!")

'''
# Save results to csv file name it: statistical_analysis.csv
state_stats.
print("Statistical analysis completed!")
'''

# %% [markdown]
# # Phase 4:
# ## Correlation Analysis:
# 
# ### a. Relationships between different metrics
# ### b. Lag analysis between cases and hospitalizations/deaths
# ### c. Impact of testing on reported cases

# %%
#Read cleane data
df = pd.read_csv("./covid_tracking_cleaned.csv")
# convert the date column to date data type using the datetime()
df['date'] = pd.to_datetime(df.date)

# Calculate correlations between metrics stored in correlation_metrics using the corr() function
correlation_metrics = ['positive', 'negative', 'death', 'hospitalized_currently', 
                     'total_test_results', 'positive_increase', 'death_increase']
correlation_matrix = df[correlation_metrics].corr()
print(correlation_matrix)


# Plot correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Between COVID-19 Metrics')
plt.tight_layout()
plt.show()


# Lag analysis
max_lag = 14  # Days to analyze

df_ts = df.groupby('date').sum()
lag_correlations = pd.DataFrame()

for lag in range(max_lag + 1):
   lag_correlations.loc['cases_to_deaths', lag] = df_ts['positive_increase'].corr(
       df_ts['death_increase'].shift(-lag))
   lag_correlations.loc['cases_to_hospitalization', lag] = df_ts['positive_increase'].corr(
       df_ts['hospitalized_currently'].shift(-lag))

# Plot lag correlations
plt.figure(figsize=(12, 6))
for metric in lag_correlations.index:
   plt.plot(range(max_lag + 1), lag_correlations.loc[metric], label=metric, marker='o')
plt.xlabel('Lag (days)')
plt.ylabel('Correlation Coefficient')
plt.title('Lag Analysis')
plt.legend()
plt.grid(True)
plt.show()

# Testing impact analysis
df_ts['positivity_rate'] = (df_ts['positive_increase'] / df_ts['total_test_results_increase']) * 100

plt.figure(figsize=(12, 6))
sns.scatterplot(data=df_ts, x='total_test_results_increase', y='positive_increase')
plt.title('Testing Volume vs New Cases')
plt.xlabel('Daily Tests')
plt.ylabel('Daily New Cases')
plt.show()

# Save results
correlation_matrix.to_csv('correlation_analysis.csv')
lag_correlations.to_csv('lag_analysis.csv')
print("Correlation analysis completed!")

# %% [markdown]
# # Phase 5:
# ## Geographic Analysis:
# 
# ### a. State-by-state comparisons
# ### b. Regional patterns using FIPS codes
# ### c. Clustering states by COVID-19 metrics

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read cleaned data
df = pd.read_csv("./covid_tracking_cleaned.csv")

# State-by-state analysis for the folowing columns: positive,death,hospitalized_currently,positive_increase,death_increase
#Group them by state and the maximum value for each column
state_metrics = df.groupby('state').agg(
    {
        'positive': 'mean',
        'death': 'mean',
        'hospitalized_currently': 'mean',
        'positive_increase': 'max',
        'death_increase' : 'max'        
    }
)
print(state_metrics)


# Calculate state-level metrics per capita
total_cases_by_state = df.groupby('state')['positive'].sum()
total_deaths_by_state = df.groupby('state')['death'].sum()

# Regional patterns using FIPS
# Extract region from FIPS code (first 2 digits) make sure that you convert it to string before
df['region'] = df['fips'].astype(str).apply(lambda x: x[:2])

#Group by region and sum up the values of the columns: positive, death,hospitalized_currently
regional_metrics = df.groupby('region').agg(
    {'positive': 'sum',
     'death': 'sum',
     'hospitalized_currently': 'sum'
    }
)


# Basic clustering using numpy
# Normalize the metrics for clustering
# Use the folowing formula: Z = (X - μ) / σ
# Z: The standardized value
# X: The original value -- metrics_for_clustering
# μ (mu): The mean of the distribution  -- metrics_for_clustering.mean()
# σ (sigma): The standard deviation of the distribution -- metrics_for_clustering.std()
metrics_for_clustering = state_metrics[['positive', 'death', 'hospitalized_currently']]
normalized_metrics = (metrics_for_clustering - metrics_for_clustering.mean()) / metrics_for_clustering.std()
print(normalized_metrics)


# Simple grouping based on cases and deaths (creating 4 groups using median splits)
state_metrics['case_group'] = pd.qcut(state_metrics['positive'], q=4, labels=['Low', 'Medium-Low', 'Medium-High', 'High'])
state_metrics['death_group'] = pd.qcut(state_metrics['death'], q=4, labels=['Low', 'Medium-Low', 'Medium-High', 'High'])

# Visualizations
plt.figure(figsize=(15, 10))

# State comparisons
plt.subplot(2, 1, 1)
sns.barplot(x=state_metrics.index, y='positive', data=state_metrics)
plt.xticks(rotation=90)
plt.title('Total Cases by State')
plt.ylabel('Number of Cases')


# Regional patterns
plt.subplot(2, 1, 2)
sns.barplot(x=regional_metrics.index, y='positive', data=regional_metrics)
plt.title('Total Cases by Region (FIPS)')
plt.ylabel('Number of Cases')
plt.xlabel('Region Code')

plt.tight_layout()
plt.show()

# State grouping visualization
plt.figure(figsize=(12, 6))
sns.scatterplot(data=state_metrics, 
               x='positive', 
               y='death',
               hue='case_group',
               style='death_group')
plt.title('States Grouped by Cases and Deaths')
plt.xlabel('Total Cases')
plt.ylabel('Total Deaths')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# Save the analysis results to 2 csv files named : state_metrics to state_analysis.csv 
#                                                  and regional_metrics to regional_analysis.csv
state_metrics.to_csv('./state_analysis.csv')
regional_metrics.to_csv('./regional_analysis.csv')

# Print summary statistics
print("\nState Analysis Summary:")
print(state_metrics.describe())

print("\nRegional Analysis Summary:")
print(regional_metrics.describe())


# %% [markdown]
# # Phase 6:
# ## Healthcare System Analysis:
# 
# ### a. Hospital capacity analysis
# ### b. ICU and ventilator usage patterns
# ### c. Recovery rate calculations

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read data
df = pd.read_csv('covid_tracking_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])


# Calculate healthcare metrics
# ICU Usage Rate = (Number of Patients Currently in ICU / Number of Patients Currently Hospitalized) * 100
df['icu_usage_rate'] = df['in_icu_currently']/df['hospitalized_currently']
# Ventilator Usage Rate = (Number of Patients Currently on Ventilator / Number of Patients Currently in ICU) * 100
df['ventilator_usage_rate'] = df['on_ventilator_currently']/df['in_icu_currently']
# Recovery Rate = (Number of Recovered Patients / Number of Positive Cases) * 100
df['recovery_rate'] = (df['recovered'] / df['positive'] * 100).round(2)

# Daily healthcare system load
daily_load = df.groupby('date').agg({
   'hospitalized_currently': 'sum',
   'in_icu_currently': 'sum',
   'on_ventilator_currently': 'sum',
   'icu_usage_rate': 'mean',
   'ventilator_usage_rate': 'mean',
   'recovery_rate': 'mean'
}).rolling(7).mean()

# Visualizations
plt.figure(figsize=(15, 10))

# Hospital capacity trends
plt.subplot(2, 1, 1)
sns.lineplot(data=daily_load, y='hospitalized_currently', x=daily_load.index, label='Hospitalized')
sns.lineplot(data=daily_load, y='in_icu_currently', x=daily_load.index, label='ICU')
sns.lineplot(data=daily_load, y='on_ventilator_currently', x=daily_load.index, label='Ventilator')
plt.title('Healthcare System Load (7-day rolling average)')
plt.legend()

# Usage rates
plt.subplot(2, 1, 2)
sns.lineplot(data=daily_load, y='icu_usage_rate', x=daily_load.index, label='ICU Usage Rate')
sns.lineplot(data=daily_load, y='ventilator_usage_rate', x=daily_load.index, label='Ventilator Usage Rate')
sns.lineplot(data=daily_load, y='recovery_rate', x=daily_load.index, label='Recovery Rate')
plt.title('Healthcare Metrics (%)')
plt.legend()

plt.tight_layout()
plt.show()

# State-level analysis
state_healthcare = df.groupby('state').agg({
   'hospitalized_currently': 'mean',
   'icu_usage_rate': 'mean',
   'ventilator_usage_rate': 'mean',
   'recovery_rate': 'mean'
}).round(2)

print("\nHealthcare System Statistics by State:")
print(state_healthcare.sort_values('hospitalized_currently', ascending=False).head())

# Save results
daily_load.to_csv('healthcare_analysis.csv')
state_healthcare.to_csv('state_healthcare_analysis.csv')

# %% [markdown]
# # Phase 7:
# ## Data Visualization:
# 
# ### a. Time series plots
# ### b. Choropleth maps
# ### c. Heatmaps for correlations
# ### d. Dashboard creation

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read data
df = pd.read_csv('covid_tracking_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

# Time Series Plots
plt.figure(figsize=(15, 5))
daily_cases = df.groupby('date')['positive_increase'].sum()
sns.lineplot(data=daily_cases)
plt.title('Daily New Cases Over Time')
plt.xticks(rotation=45)
plt.show()

# Correlation Heatmap
correlation_metrics = ['positive', 'death', 'hospitalized_currently', 
                     'in_icu_currently', 'recovered']
correlation_matrix = df[correlation_metrics].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Between COVID-19 Metrics')
plt.show()

# Dashboard Creation (Multiple Plots)
fig, axes = plt.subplots(2, 2, figsize=(20, 15))

# Top left: Cases Timeline
sns.lineplot(data=df.groupby('date')['positive'].sum(), ax=axes[0,0])
axes[0,0].set_title('Total Cases Over Time')
axes[0,0].tick_params(axis='x', rotation=45)

# Top right: Deaths Timeline
sns.lineplot(data=df.groupby('date')['death'].sum(), ax=axes[0,1], color='red')
axes[0,1].set_title('Total Deaths Over Time')
axes[0,1].tick_params(axis='x', rotation=45)

# Bottom left: State Comparison
state_totals = df.groupby('state')['positive'].max().sort_values(ascending=False)
sns.barplot(x=state_totals.index, y=state_totals.values, ax=axes[1,0])
axes[1,0].set_title('Total Cases by State')
axes[1,0].tick_params(axis='x', rotation=90)

# Bottom right: Testing vs Cases
sns.scatterplot(data=df, x='total_test_results', y='positive', ax=axes[1,1])
axes[1,1].set_title('Testing vs Cases')

plt.tight_layout()
plt.show()

# Save visualizations
fig.savefig('covid_dashboard.png')
print("Visualizations completed!")

# %% [markdown]
# # Phase 8:
# ## Derived Metrics:
# 
# ### a. Case fatality rates
# ### b. Testing positivity rates
# ### c. Hospitalization rates
# ### d. Recovery rates

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read cleaen data and make sure to have the date column as a datetime data type
df = pd.read_csv('./covid_tracking_cleaned.csv')
df['date'] = pd.to_datetime(df.date)

# Calculate derived metrics
# Case Fatality Rate (CFR): CFR = (Number of Deaths / Number of Positive Cases) * 100
df['case_fatality_rate'] = df['death'] / df['positive'] * 100
# Positivity Rate: Positivity Rate = (Number of Positive Tests / Total Number of Tests) * 100
df['positivity_rate'] = (df.total_test_results - df.pos_neg) / df.total_test_results_increase * 100
# Hospitalization Rate = (Number of Currently Hospitalized Patients / Number of Positive Cases) * 100
df['hospitalization_rate'] = df.hospitalized_currently / df.positive * 100
#  Recovery Rate = (Number of Recovered Patients / Number of Positive Cases) * 100
df['recovery_rate'] = (df['recovered'] / df['positive'] * 100).round(2)

# Time series of rates
daily_rates = df.groupby('date').agg({
   'case_fatality_rate': 'mean',
   'positivity_rate': 'mean',
   'hospitalization_rate': 'mean',
   'recovery_rate': 'mean'
})

# Visualization
plt.figure(figsize=(15, 10))

# Plot all rates
plt.subplot(2, 1, 1)
sns.lineplot(data=daily_rates)
plt.title('COVID-19 Rates Over Time')
plt.xticks(rotation=45)
plt.legend()

# State comparison
state_rates = df.groupby('state').agg({
   'case_fatality_rate': 'mean',
   'positivity_rate': 'mean',
   'hospitalization_rate': 'mean',
   'recovery_rate': 'mean'
}).round(2)

plt.subplot(2, 1, 2)
sns.boxplot(data=df[['case_fatality_rate', 'positivity_rate', 
                    'hospitalization_rate', 'recovery_rate']])
plt.title('Distribution of Rates')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Save results
daily_rates.to_csv('derived_metrics_time.csv')
state_rates.to_csv('derived_metrics_state.csv')
print("Derived metrics analysis completed!")

# %%



