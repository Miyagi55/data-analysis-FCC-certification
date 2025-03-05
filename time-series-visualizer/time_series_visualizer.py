import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df = pd.DataFrame({'date':pd.date_range(start='2016-05-09',end='2019-12-03', freq='D'),'value':df['value']})
#df.set_index('date', inplace=True)

# Clean data

top_percentile = df['value'].quantile(0.975)
bottom_percentile = df['value'].quantile(0.025)

df = df[(df['value'] < top_percentile) & (df['value'] > bottom_percentile)] 


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(12,6))
    sns.lineplot(data=df, x=df.index, y='value', color='red')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
   
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig



def draw_bar_plot():

    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    
    # Group by year and month, calculate mean page views
    grouped_df = df.groupby([df['year'], df['month']])['value'].mean().reset_index()
    
    # Pivot the data to create a matrix suitable for bar plotting
    pivot_df = grouped_df.pivot(index='year', columns='month', values='value')
    
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    pivot_df.plot(kind='bar', ax=ax, width=0.6)
    
    
    plt.title('Average Daily Page Views by Year and Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    
   
    month_labels = ['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']
    plt.legend(title='Months', labels=[month_labels[m-1] for m in pivot_df.columns])
    
    
    plt.tight_layout()
    
    
    

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig



def draw_box_plot():
    
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    
   
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Year-wise Box Plot (Trend)
    sns.boxplot(x='year', y='value', data=df, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    
    
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Convert numeric months to month abbreviations
    df['month_name'] = df['date'].dt.strftime('%b')
    
    sns.boxplot(x='month_name', y='value', data=df, ax=ax2, order=month_order)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    
    
    plt.tight_layout()
    

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

