import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web

start = dt.datetime(2020,1,1)
end = dt.datetime(2020,10,8)

df = web.DataReader('AMD', 'yahoo', start, end)
#print (df.head())
#df.to_csv('amd.csv')

# Chart Size
fig = plt.figure(figsize=[14,6])
# Chart elements, 121 stands for 1x2 grid, third 1 as the 1st chart
ax1 = fig.add_subplot(121, ylabel = '')
df['Close'].plot(ax = ax1, color = 'b', lw=2.)

plt.show()