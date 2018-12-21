import pandas as pd
import matplotlib.pyplot as plot


dataframe = pd.read_csv('data/nodes_metrics.csv', index_col='timestamp', parse_dates=True)
dataframe = dataframe.sort_index()

dataframe = dataframe.loc['10/10/2018':'12/30/2018', ['node2_avg_resp_time']]
dataframe.plot()
plot.show()

