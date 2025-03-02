import pandas as pd
import numpy as np
import lxml

def warn(*args,**kwargs):
    pass
import warnings
warnings.warn=warn
warnings.filterwarnings('ignore')

#Exercise 1
URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

tables=pd.read_html(URL)
df=tables[3]

df.columns=range(df.shape[1])

df=df[[0,1,2]]

df=df.iloc[1:6,:]

df.columns=['Country','UN Regions','GDP Value']

df['GDP Value']=df['GDP Value'].astype(int)

df[['GDP Value']]=df[['GDP Value']]/1000

df[['GDP Value']]=np.round(df[['GDP Value']],2)

df.rename(columns={'GDP Value':'GDP Value(in Billion USD)'})

df.to_csv('./top5.csv')

tables=pd.read_html(URL)
df=tables[3]

df.columns=range(df.shape[1])

df=df[[0,2]]

df=df.iloc[1:16,:]

df.columns=['Country','GDP(Million USD)']

#Exercise 2
df['GDP(Million USD)']=df['GDP(Million USD)'].astype(int)

df[['GDP(Million USD)']]=df[['GDP(Million USD)']]/1000

df[['GDP(Million USD)']]=np.round(df[['GDP(Million USD)']],4)

df.rename(columns={'GDP(Million USD)':'GDP(Billion USD)'})

#Exercise 3
df.to_csv('./Largest Economies.csv')