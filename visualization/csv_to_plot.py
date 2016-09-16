import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go


# from https://plot.ly/python/plot-data-from-csv/




df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')

#priint csv
df.head()

#printing plot
In [11]:

trace = go.Scatter(
                  x = df['AAPL_x'], y = df['AAPL_y'],
                  name='Share Prices (in USD)'
                  )
layout = go.Layout(
                  title='Apple Share Prices over time (2014)',
                  plot_bgcolor='rgb(230, 230,230)',
                  showlegend=True
                  )
fig = go.Figure(data=[trace], layout=layout)

py.iplot(fig, filename='apple-stock-prices')
