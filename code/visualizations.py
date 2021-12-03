import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats


url = 'https://github.com/anath703/DS_5100_PROJECT/raw/main/cleanedNflFullGameLog_withstadiuminfo.csv' #location of raw data file
df = pd.read_csv(url)

mean_by_year = df.groupby(['Season']).mean().reset_index()

print(df.dtypes)


#plotting line plot of homefield advantage by season
plt.plot(mean_by_year.Season, mean_by_year.Points_Diff, linewidth=1)
plt.title('Average Homefield Advantage by Season')
plt.xlabel('Season')
plt.ylabel('Homefield Advantage')
plt.xticks(range(2000,2021), rotation =60),
plt.show() #output graph
plt.clf #clear plt


plt.plot(mean_by_year.Season, mean_by_year.Points_Diff, linewidth=1)
plt.title('Average Homefield Advantage by Season')
plt.xlabel('Season')
plt.ylabel('Homefield Advantage')
plt.xticks(range(2000,2021), rotation =60),
plt.show() #output graph
plt.clf #clear plt



sns.boxplot(x=df['distance']) #boxplot of distance
plt.show()
plt.clf #clear plt

##Distance Buckets
bins = [0,500, 1000, 1500, 2000,30000]
labels = ['Less than 500','500 to 1000','1000 to 1500', '1500 to 2000', '2000+']
df['Distance_Binned'] = pd.cut(df['distance'], bins=bins, labels= labels)

mean_by_distance = df.groupby(['Distance_Binned']).mean().reset_index()

#bar plot of points diff by distance
barplot= sns.barplot(x = "Distance_Binned", y = "Points_Diff", data = df, ci = None)
barplot.set(xlabel='Distance Travelled by Away Team', ylabel='Average Home Field Advantage', title= 'Home Field Advantage by Distance Travelled')
barplot.set_xticklabels(barplot.get_xticklabels(),rotation =5)
plt.show()
plt.clf()

#bar plot of yards diff by distance
barplot2= sns.barplot(x = "Distance_Binned", y = "Yards_Diff", data = df, ci = None)
barplot2.set(xlabel='Distance Travelled by Away Team', ylabel='Average Yards Differential', title= 'Yards Differential by Distance Travelled')
barplot2.set_xticklabels(barplot2.get_xticklabels(),rotation =5)
plt.show()
plt.clf()

#bar plot of turnover diff by distance
barplot3= sns.barplot(x = "Distance_Binned", y = "Turnover_Diff", data = df, ci = None)
barplot3.set(xlabel='Distance Travelled by Away Team', ylabel='Average Turnover Differenital', title= 'Turnover Differenital by Distance Travelled')
barplot3.set_xticklabels(barplot3.get_xticklabels(),rotation =5)
plt.show()
plt.clf()


#hypothesis test. Ho = Home Field = 0. Ha: Home Field >0
print( stats.ttest_1samp(a= df['Points_Diff'], popmean=0, alternative = 'greater') )




