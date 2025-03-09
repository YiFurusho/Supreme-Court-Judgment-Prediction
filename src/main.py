__doc__ = """
 ╔═══════════════════════════════════════════╗
 ║                                           ║
 ║  ◆◆ Author Information ◆◆                 ║
 ║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━              ║
 ║  Author: I Furusho                        ║
 ║  Role: Upcoming Data Analyst              ║
 ║  Date: March 9, 2025                      ║
 ║                                           ║
 ║  ◆◆ Script Description ◆◆                 ║
 ║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━              ║
 ║  This script performs an exploratory      ║
 ║  data analysis (EDA) on 'justice.csv'.    ║
 ║  • Viewing dataset structure              ║
 ║  • Handling missing values                ║
 ║  • Examining columns for insights         ║
 ║  • Visualizing distributions              ║
 ║  • Investigating relationships            ║
 ║                                           ║
 ║  ◆◆ Libraries Used ◆◆                     ║
 ║  ━━━━━━━━━━━━━━━━━━━━━                    ║
 ║  • pandas                                 ║
 ║  • matplotlib                             ║
 ║  • seaborn                                ║
 ║                                           ║
 ╚═══════════════════════════════════════════╝
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(__doc__)

# use variable df for the dataset
path = 'data\justice.csv'
df = pd.read_csv(path)

# head()
print('Viewing initial rows')
print(df.head())

print('Viewing df type')
print(type(df))

# overview of the dataset
print('Viewing df overview')
print(df.info())
print(df.describe())

# identify and count missing value
print('Identify and count missing value')
print(df.isnull().sum())

# Check for and count duplicate rows
print('Check for and count duplicate rows')
print(df.duplicated().sum())

# For categorical columns, check unique values
print('For categorical columns, check unique values')
for column in df.select_dtypes(include=['object']):
    print(f"\nUnique values in {column}:")
    print(df[column].unique())

# Ensure data types are appropriate for each column
print('Ensure data types are appropriate for each column')
print(df.dtypes)

# For numerical columns, look for potential outliers
print('For numerical columns, look for potential outliers')
for column in df.select_dtypes(include=['int64', 'float64']):
    print(f"\nOutliers in {column}:")
    print(df[column].describe())

# Examine string columns for inconsistent formatting
print('Examine string columns for inconsistent formatting')
for column in df.select_dtypes(include=['object']):
    print(f"\nSample values in {column}:")
    print(df[column].sample(5))

# For columns with fewer missing values
print('For columns with fewer missing values')
df['docket'] = df['docket'].fillna('Unknown')
df['first_party'] = df['first_party'].fillna('Unknown')
df['second_party'] = df['second_party'].fillna('Unknown')
df['first_party_winner'] = df['first_party_winner'].fillna('Unknown')
df['decision_type'] = df['decision_type'].fillna('Unknown')

# For columns with more missing values
print('For columns with more missing values')
df['disposition'] = df['disposition'].fillna('Not Specified')
df['issue_area'] = df['issue_area'].fillna('Not Specified')

print(df.isnull().sum())

df.head()

df.tail()

# obtain summary statistics for numerical columns.
df.describe()

# to examine the distribution of categories in columns 'term', 'decision_type',  'first_party_winner'
df['term'].value_counts()

df['decision_type'].value_counts()

df['first_party_winner'].value_counts()

# Create histograms for 'facts_len'
plt.figure(figsize=(10, 6))
sns.histplot(df['facts_len'], bins=20, kde=True)
plt.title('Distribution of Facts Length')
plt.xlabel('Facts Length')
plt.ylabel('Frequency')
plt.show()

# Create histograms for 'majority_vote'
plt.figure(figsize=(10, 6))
sns.histplot(df['majority_vote'], bins=20, kde=True)
plt.title('Distribution of Majority Vote')
plt.xlabel('Majority Vote')
plt.ylabel('Frequency')

# Create histograms for 'minority_vote'
plt.figure(figsize=(10, 6))
sns.histplot(df['minority_vote'], bins=20, kde=True)
plt.title('Distribution of Minority Vote')
plt.xlabel('Minority Vote')
plt.ylabel('Frequency')

# Use cross-tabulations to examine relationships between first_party_winner and decision_type
pd.crosstab(df['first_party_winner'], df['decision_type'])

# Create scatter plots to visualize relationships between numerical variables between 'facts_len' and 'majority_vote'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='facts_len', y='majority_vote', data=df)
plt.title('Relationship between Facts Length and Majority Vote')
plt.xlabel('Facts Length')
plt.ylabel('Majority Vote')
plt.show()
