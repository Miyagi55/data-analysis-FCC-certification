# Demographic Data Analysis

## Overview
This project involves analyzing demographic data using **Pandas**. The dataset is extracted from the 1994 U.S. Census database and provides insights into different demographic attributes such as age, education, occupation, income, and work hours. The goal is to answer specific questions using **data manipulation** and **aggregation techniques** in Pandas.

## Dataset Description
The dataset contains demographic information of individuals, including their education level, occupation, salary, and other personal attributes.

| Feature | Column Name | Description |
|---------|------------|-------------|
| Age | `age` | Age of the individual |
| Work Class | `workclass` | Type of employer |
| Final Weight | `fnlwgt` | Sampling weight of the individual |
| Education | `education` | Highest level of education |
| Education Number | `education-num` | Education level in numeric form |
| Marital Status | `marital-status` | Marital status of the individual |
| Occupation | `occupation` | Type of job |
| Relationship | `relationship` | Relationship within family |
| Race | `race` | Race of the individual |
| Sex | `sex` | Gender |
| Capital Gain | `capital-gain` | Additional income from investments |
| Capital Loss | `capital-loss` | Loss from investments |
| Work Hours Per Week | `hours-per-week` | Number of work hours per week |
| Native Country | `native-country` | Country of origin |
| Salary | `salary` | Income category (`<=50K` or `>50K`) |

## Questions to Answer
Using Pandas, answer the following questions:
1. How many people of each race are represented in this dataset?
2. What is the average age of men?
3. What percentage of people have a Bachelor's degree?
4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
5. What percentage of people without advanced education make more than 50K?
6. What is the minimum number of hours a person works per week?
7. What percentage of people working the minimum number of hours per week earn more than 50K?
8. Which country has the highest percentage of people earning >50K, and what is that percentage?
9. What is the most popular occupation for those earning >50K in India?

## Development Instructions
- Implement the logic inside `demographic_data_analyzer.py`
- Update all variables currently set to `None` with appropriate calculations
- Use **Pandas** to manipulate and analyze the data
- Round all decimals to the nearest tenth

## Testing
- Run `main.py` to test your implementation
- The unit tests are located in `test_module.py`
- The test cases are automatically imported into `main.py` for convenience

## Example Visualizations
- _Race distribution in the dataset:_
  ![Race Distribution](images/race_distribution.png)

- _Income Distribution by Education Level:_
  ![Income by Education](images/income_education.png)

## How to Run the Project
```bash
uv run python main.py
```
This will generate the required results and validate the answers.


## Dataset Source
Dua, D. and Graff, C. (2019). **UCI Machine Learning Repository**. Irvine, CA: University of California, School of Information and Computer Science.

