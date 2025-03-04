# 📊 Page View Time Series Visualizer

This project focuses on visualizing **time series data** using Pandas, Matplotlib, and Seaborn. The dataset contains daily page views from the **freeCodeCamp.org** forum between **2016-05-09** and **2019-12-03**. The goal is to analyze trends in website traffic over time and identify patterns in visits.

## 📂 Dataset
- **File Name:** `fcc-forum-pageviews.csv`
- **Data Description:** The dataset consists of two columns:
  - **Date**: The date of recorded page views.
  - **Page Views**: The number of page views on that particular day.

## 🛠️ Project Tasks
### 1️⃣ Data Preparation
- Import the dataset using **Pandas**.
- Convert the `date` column to a **DateTime index**.
- **Clean the data** by filtering out days in the top and bottom 2.5% to remove outliers.

### 2️⃣ Visualizations
#### 📈 Line Plot
- Create a **line chart** of daily page views.
- **X-axis**: Date, **Y-axis**: Page Views.
- Title: *Daily freeCodeCamp Forum Page Views 5/2016-12/2019*.

#### 📊 Bar Plot
- Create a **bar chart** showing **monthly averages** of daily page views grouped by year.
- **X-axis**: Years, **Y-axis**: Average Page Views.
- Legend: Month labels.

#### 📦 Box Plots
- **Year-wise Box Plot** (Trend) – Shows yearly distribution of page views.
- **Month-wise Box Plot** (Seasonality) – Compares monthly trends across all years.
- Ensures **January is the first month** in x-axis labels.

## 🔧 Development & Execution
- Write all code in `time_series_visualizer.py`.
- Use `main.py` to test the implementation.

## 🧪 Testing
- Unit tests are in `test_module.py`.
- The tests are automatically imported into `main.py`.

## 📸 Example Visualizations
*(Insert images of generated plots here)*

---

This project is part of the **freeCodeCamp Data Analysis Certification** 🏆.

