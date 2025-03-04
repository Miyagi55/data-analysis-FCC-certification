import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
BMI = ((df['weight']) / ((df['height']/100))**2) 

df['overweight'] = (BMI > 25).astype(int)

# 3


df[['smoke', 'alco', 'active','cardio']] = 1 - df[['smoke', 'alco', 'active','cardio']]

df[['cholesterol','gluc']] = np.where(df[['cholesterol','gluc']] == 1, 0, 1)



# 4
def draw_cat_plot(df):
    
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol','gluc','smoke', 'alco', 'active','overweight'], var_name='variables', value_name='value')

    df_cat = df_cat.rename(columns={'cardio':'CardioStatus'})
    

    df_cat = df_cat.sort_values('variables')
    fig = sns.catplot(x='variables', hue='value', col='CardioStatus', kind='count', data=df_cat)

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map(df):
    
    # 11
    df_heat = df.copy()

    print('Before conditions: ', df_heat[['ap_lo','ap_hi','height','weight']].head(30))

    df_heat = df_heat[(df_heat['ap_lo'] <= df_heat['ap_hi']) & 
                      (df_heat['height'] >= df_heat['height'].quantile(0.025)) & 
                      (df_heat['height'] <= df_heat['height'].quantile(0.975)) & 
                      (df_heat['weight'] >= df_heat['weight'].quantile(0.025)) & 
                      (df_heat['weight'] <= df_heat['weight'].quantile(0.975)) ]

    print('After conditions: ', df_heat[['ap_lo','ap_hi','height','weight']].head(30))

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(13,13))

    # 15
    sns.heatmap(corr, mask=mask, annot=True,ax=ax, vmax=0.6, vmin=-0.6, square=True)
    fig.savefig('heatmap.png')
    plt.show()

    return 


draw_heat_map(df)