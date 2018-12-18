import pandas as pd
import matplotlib.pyplot as plot


df_apple = pd.read_csv('data/apple.csv', index_col='Date', parse_dates=True)

df_apple = df_apple.sort_index()

print df_apple.resample('W')['Close'].mean()


visual_df=  df_apple.loc['2012-Feb':'2017-Feb', ['Close']]
visual_df.plot()
plot.show()