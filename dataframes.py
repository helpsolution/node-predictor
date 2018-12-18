import pandas as pd

my_series = pd.Series(["asd","a",1,2])



dataframe = pd.DataFrame({
     'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
     'population': [17.04, 143.5, 9.5, 45.5],
     'square': [2724902, 17125191, 207600, 603628]
})


print type(dataframe['country'])
print dataframe.columns

print dataframe.index

dataframe = pd.DataFrame({
     'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine2'],
     'population': [17.04, 143.5, 9.5, 45.5],
     'square': [2724902, 17125191, 207600, 603628]
}, index=[1,2,8,4])

dataframe.index.name = 'code'

dataframe.to_csv('data/node.csv')

df_from_file = pd.read_csv('data/countries.csv', sep=',')

print dataframe

