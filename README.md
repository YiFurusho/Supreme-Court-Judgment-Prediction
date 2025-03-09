# Supreme Court Judgment Prediction: Exploratory Data Analysis

## Project Overview

This project performs an exploratory data analysis (EDA) on a dataset of United States Supreme Court cases spanning from 1955 to 2021. The analysis aims to uncover key insights into voting patterns, case characteristics, and data quality issues.  The ultimate goal of such an EDA is often to inform predictive modeling efforts, though this project focuses on the descriptive analysis.

## Author Information

*   **Author:** I Furusho
*   **Role:** Upcoming Data Analyst
*   **Date:** March 9, 2025

## Dataset

*   **Source:** [Supreme Court Judgment Prediction Dataset on Kaggle](https://www.kaggle.com/datasets/deepcontractor/supreme-court-judgment-prediction)
*   **Description:** The dataset contains information on 3,304 Supreme Court cases, including case details, voting patterns of the justices, and assigned issue areas.

## Data Description

The dataset comprises 3,303 rows and 16 columns with the following structure:

*   **Categorical Variables:**
    *   `term`:  The Supreme Court term in which the case was decided.
    *   `decision_type`: The type of decision issued (e.g., Majority Opinion, Per Curiam).
    *   `first_party_winner`: Indicates whether the first party in the case won (True/False).
    *   `disposition`:  The outcome of the case.
    *   `issue_area`: The primary legal area involved in the case (e.g., Civil Rights, First Amendment).
*   **Numerical Variables:**
    *   `facts_len`: The length (in characters) of the case's factual description.
    *   `majority_vote`: The number of justices voting with the majority.
    *   `minority_vote`: The number of justices voting with the minority.

## Methodology

The analysis follows these steps:

1.  **Data Loading and Inspection:** Load the dataset using `pandas` and examine its structure, datatypes, and initial rows.
2.  **Data Quality Assessment:** Identify and quantify missing values using `df.isnull().sum()`.  Check for duplicate rows that might skew analysis.
3.  **Missing Value Handling:** Address missing data using appropriate strategies based on the nature and extent of missingness.
4.  **Exploratory Data Analysis:**
    *   **Categorical Variable Analysis:** Examine the distribution of key categorical variables (e.g., `term`, `decision_type`, `first_party_winner`) using `value_counts()` to understand the prevalence of different categories.
    *   **Numerical Variable Analysis:**
        *   Generate descriptive statistics (`df.describe()`) for numerical variables to understand their central tendency, dispersion, and range.
        *   Visualize the distributions of numerical variables (e.g., `facts_len`, `majority_vote`, `minority_vote`) using histograms.
        *   Identify potential outliers in numerical variables based on their distributions and descriptive statistics.
5.  **Relationship Analysis:**
    *   Explore relationships between categorical variables using cross-tabulations (`pd.crosstab()`).
    *   Investigate relationships between numerical variables using scatter plots.

## Data Cleaning and Preprocessing

### Handling Missing Values:

*   **Columns with low missingness:** (`docket`, `first_party`, `second_party`, `first_party_winner`, `decision_type`)
    *   Missing values were imputed with the string "Unknown."
*   **Columns with higher missingness:** (`disposition`, `issue_area`)
    *   Missing values were imputed with the string "Not Specified."

This approach aims to preserve the information contained in the existing data while acknowledging the absence of specific values.

## Key Observations

*   **Temporal Distribution:** The dataset appears to be more heavily weighted towards more recent Supreme Court terms (post-2000).
*   **Decision Type:**  "Majority Opinion" and "Per Curiam" are the most frequent decision types, reflecting standard Supreme Court practices.
*   **Case Outcomes:** The first party wins the case in approximately 80% of the instances where the outcome is recorded.
*   **Voting Patterns:** Majority votes tend to be clustered at 7 or 9, indicating a high degree of consensus among the justices in many cases.
*   **Case Complexity:** The length of case facts (`facts_len`) varies considerably, with some cases having significantly longer fact descriptions, suggesting a higher degree of complexity or importance.

## Insights and Findings

*   The dataset provides a valuable overview of recent Supreme Court decisions and their characteristics.
*   The strong consensus observed in many cases (high majority votes) highlights the Court's role in establishing legal precedent.
*   The presence of outliers in the length of case facts suggests the existence of particularly complex or significant cases that may warrant further investigation.
*   The handling of missing data allowed for the inclusion of all cases in the analysis, albeit with an acknowledgment of the imputed values.

## Limitations

*   **Missing Data:**  Although addressed, missing data in columns such as `issue_area` may still limit the depth of analysis for specific legal areas.  Further investigation into the reasons *why* this data is missing could be valuable.
*   **Potential Biases:**  The dataset's focus on more recent cases may introduce a temporal bias, potentially overlooking important historical trends.
*   **Scope of Analysis:**  This analysis is primarily descriptive and does not delve into causal relationships or predictive modeling.

## Conclusion

This exploratory data analysis provides a foundation for further investigation into Supreme Court judgment prediction. Future work could focus on:

*   Developing predictive models to forecast case outcomes based on the available features.
*   Conducting more in-depth analysis of specific issue areas.
*   Incorporating external data sources to enrich the analysis and provide additional context.
*   Addressing the limitations related to missing data and potential biases.
