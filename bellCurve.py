import pandas as pd
import plotly.figure_factory as ff

data = pd.read_csv('data.csv')
fig = ff.create_distplot([data["Avg Rating"].tolist()],['Average Rating'],show_hist = False)
fig.show()