import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    #remove empty rows
    df = df.dropna(subset=['Year','CSIRO Adjusted Sea Level'])


    # Create scatter plot
    fig = plt.figure(figsize=(12,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Observed data')

    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    x_full = np.array([df['Year'].min(), 2050])
    y_full = intercept + slope * x_full

    plt.plot(x_full, y_full, color='red', linestyle='--', label='Full dataset Trend')

    df_recent = df[df['Year'] >= 2000] 
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Create line of best fit for recent data
    x_recent = np.array([df_recent['Year'].min(), 2050])
    y_recent = intercept_recent + slope_recent * x_recent
    plt.plot(x_recent, y_recent, color='green', linestyle='--', label='Post-2000 Trend')

    # Calculate predictions for 2050
    prediction_full = intercept + slope * 2050
    prediction_recent = intercept_recent + slope_recent * 2050

    # Annotate predictions
    plt.annotate(f'2050 Prediction (Full Dataset): {prediction_full:.2f} inches', 
                xy=(2050, prediction_full), xytext=(10, 10), 
                textcoords='offset points', ha='left', va='bottom')
    plt.annotate(f'2050 Prediction (Post-2000): {prediction_recent:.2f} inches', 
                xy=(2050, prediction_recent), xytext=(10, -10), 
                textcoords='offset points', ha='left', va='top')

    
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

