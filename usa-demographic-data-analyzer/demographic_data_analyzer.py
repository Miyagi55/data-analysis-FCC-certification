import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()


    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)


    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df[df["education"] == 'Bachelors']) / len(df)) * 100 , 1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    high_edu_levels = ("Bachelors", "Masters", "Doctorate")
    high_edu_counts = {edu: len(df[(df["education"] == edu) & (df["salary"] == ">50K")]) 
              for edu in high_edu_levels}

    high_ed_total = len(df[df["education"].isin(high_edu_levels)])

    higher_education_rich = round((sum(high_edu_counts.values()) / high_ed_total) * 100, 1)
    
    
    # What percentage of people without advanced education make more than 50K?
    low_edu_levels = ('HS-grad', '11th', '9th', 'Some-college',
       'Assoc-acdm', 'Assoc-voc', '7th-8th', 'Prof-school','5th-6th', '10th', '1st-4th', 'Preschool', '12th')

    lower_education = {edu: len(df[(df["education"] == edu) & (df["salary"] == ">50K")]) 
                for edu in low_edu_levels}

    lower_edu_total = len(df[df["education"].isin(low_edu_levels)])

    lower_education_rich = round((sum(lower_education.values()) / lower_edu_total) * 100, 1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()


    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    rich_filtered = len(df[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')])

    total_min = len(df[df['hours-per-week'] == 1])

    rich_percentage = round((rich_filtered / total_min) * 100,1)


    # What country has the highest percentage of people that earn >50K?
    total_countries = df['native-country'].value_counts()
    over_50k = df[df['salary'] == '>50K']['native-country'].value_counts()

    percentage_df = (over_50k / total_countries) * 100

    highest_earning_country_percentage = round(percentage_df.max(),1)
    highest_earning_country = percentage_df.idxmax()


    # Identify the most popular occupation for those who earn >50K in India.
    top_occupations_series = df[df['native-country'] == 'India']['occupation'].value_counts()

    top_IN_occupation = top_occupations_series.idxmax()


    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
