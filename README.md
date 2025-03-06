# Supreme-Court-Judgment-Prediction
A mock project of data analysis by python
## dataset used:
<a href="https://www.kaggle.com/datasets/deepcontractor/supreme-court-judgment-prediction">Dataset</a>
## Introduction
The dataset contains information about 3,304 Supreme Court cases of the United States from 1955 to 2021, including details such as case names, docket numbers, voting patterns, and issue areas. The primary goal of this analysis is to explore the dataset, address missing values, analyze key variables, and uncover insights into voting patterns and case characteristics.

## Data Overview
The dataset consists of 16 columns and 3,303 rows. Key variables include:
•	Categorical variables: term, decision_type, first_party_winner, disposition, issue_area
•	Numerical variables: facts_len, majority_vote, minority_vote

## Data Quality Assessment
Missing Values
Using df.isnull().sum(), to identify missing values in several columns:
•	docket: 11 missing values
•	first_party: 1 missing value
•	second_party: 1 missing value
•	first_party_winner: 15 missing values
•	decision_type: 7 missing values
•	disposition: 72 missing values
•	issue_area: 142 missing values

## Handling Missing Values
•	Columns with few missing values (docket, first_party, second_party) were filled with "Unknown."
•	Columns with more missing values (disposition, issue_area) were filled with "Not Specified."

## Observations:
•	facts_len (length of case facts): Most cases have fact descriptions around ~1,100 characters, but some cases have unusually long descriptions (up to 6,201 characters).
•	majority_vote: The average majority vote is ~7 votes, with a maximum of 9.
•	minority_vote: Minority votes are generally low, with an average of ~1.7 votes.

## Categorical Variable Analysis
Using .value_counts(), to analyze the distribution of key categorical variables:
Term Distribution-
The most frequent terms are clustered in recent years (e.g., post-2000), indicating a focus on modern cases.
Decision Type-
The most common decision types include "Majority Opinion" and "Per Curiam," reflecting typical Supreme Court practices.
First Party Winner-
The first party won in approximately ~80% of cases where data was available.

## Numerical Variable Analysis
Distribution Analysis
Use histograms for numerical variables (facts_len, majority_vote, and minority_vote):
•	facts_len: Skewed distribution with a few extreme outliers.
•	majority_vote: Most cases have a majority vote of either 7 or 9.
•	minority_vote: Minority votes are concentrated around lower values (0–2).

Outliers
Outliers were identified in the facts_len column, where some cases had extremely long fact descriptions (>5,000 characters). These may represent highly complex or landmark cases.

## Relationship Analysis
Cross-tabulation
Using cross-tabulations (pd.crosstab()), to explore relationships between categorical variables:
•	Cases where the first party won were more likely to involve "Majority Opinion" decision types.

Scatter Plot Analysis
A scatter plot between facts_len and majority_vote revealed no strong correlation between the length of case facts and voting outcomes.

## Key Insights and Findings
1).	The dataset primarily focuses on modern Supreme Court cases.
2).	Most decisions involve high majority votes (7–9), indicating strong consensus among justices.
3).	Outliers in the length of case facts suggest that some cases are more complex or significant than others.
4).	Missing data in key columns like disposition and issue_area may limit some analyses but can be mitigated by creating categories like "Not Specified."

## Limitations:
1).	Missing data in critical columns like issue_area may obscure trends in certain analyses.
2).	Outliers in numerical columns like facts_len could skew results if not handled carefully.

## Conclusion
This analysis provided an overview of key trends and patterns in Supreme Court decisions based on the dataset. While most decisions reflect strong consensus among justices, certain cases stand out due to their complexity or unique characteristics.

