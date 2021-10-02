from re import S
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import statistics
import random
import pandas as pd

df=pd.read_csv("Marks.csv")
data=df["Math_score"].tolist()

#fig=ff.create_distplot([data],["Scores"],show_hist=False)
#fig.show()

mean=statistics.mean(data)
STDeviation=statistics.stdev(data)
print("mean is=>",mean)
print("standard deviation is =>",STDeviation)

def randomSetofMean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
meanList=[]
for i in range (0,1000):
    setofMeans=randomSetofMean(100)
    meanList.append(setofMeans)
StandardDeviation=statistics.stdev(meanList)
Mean=statistics.mean(meanList)

print(StandardDeviation)
print(Mean)
#fig=ff.create_distplot([meanList],["Marks"],show_hist=False)
#fig.show()

first_std_deviation_start, first_std_deviation_end = mean-StandardDeviation, mean+StandardDeviation
second_std_deviation_start, second_std_deviation_end = mean-(2*StandardDeviation), mean+(2*StandardDeviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*StandardDeviation), mean+(3*StandardDeviation)

print("STD1",first_std_deviation_start,first_std_deviation_end)
print("STD2",second_std_deviation_start,second_std_deviation_end)
print("STD3",third_std_deviation_start,third_std_deviation_end)

#fig=ff.create_distplot([meanList],["Marks"],show_hist=False)
#fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
#fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
#fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
#fig.show()

df=pd.read_csv("Data1.csv")
data=df["Math_score"].tolist()
meanofSample1=statistics.mean(data)
print("mean is=>",meanofSample1)

fig=ff.create_distplot([meanList],["Scores"],show_hist=False)
#fig.show()

meanofSample1=statistics.mean(data)
print("mean is=>",meanofSample1)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[meanofSample1, meanofSample1], y=[0, 0.17], mode="lines", name="meanofSample1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
#fig.show()

df=pd.read_csv("Data2.csv")
data=df["Math_score"].tolist()
meanofSample2=statistics.mean(data)
print("mean is=>",meanofSample2)

fig=ff.create_distplot([meanList],["Scores"],show_hist=False)
fig.show()

meanofSample1=statistics.mean(data)
print("mean is=>",meanofSample2)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[meanofSample2, meanofSample2], y=[0, 0.17], mode="lines", name="meanofSample2"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.show()

df=pd.read_csv("Data3.csv")
data=df["Math_score"].tolist()
meanofSample3=statistics.mean(data)
print("mean is=>",meanofSample3)

fig=ff.create_distplot([meanList],["Scores"],show_hist=False)
fig.show()

meanofSample3=statistics.mean(data)
print("mean is=>",meanofSample3)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[meanofSample3, meanofSample3], y=[0, 0.17], mode="lines", name="meanofSample3"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.show()

