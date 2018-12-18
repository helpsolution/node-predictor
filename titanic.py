import pandas as pd

titanic_df = pd.read_csv('data/titanic.csv')

print titanic_df.groupby(['PClass','Survived'])['PassengerID'].count()
