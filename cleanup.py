"""
Created on Tue Oct 19 13:24:48 2021

@author: anoopnath

notes: This procedure cleans up the data so that it is ready to be used for data visualizations and analysis
"""

import pandas as pd
url = 'https://github.com/anath703/DS_5100_PROJECT/raw/main/nflFullGameLog.csv' #location of raw data file
df = pd.read_csv(url)
#print(df.dtypes)


#df=pd.read_csv('nflFullGameLog.csv') #reading in csv

df=  df[df['Week'].notna()] #removing empty rows
df['Date']= pd.to_datetime(df['Date'] ).dt.date #converting to date time

#creating new columns to indicate which team is home, which team is away, yards scored and turnovers
df['Home_Team'] = df['Loser/Tie'].where(df['Location'] == '@', df['Winner/Tie'])
df['Points_Home'] = df['Points_Loser'].where(df['Location'] == '@', df['Points_Winner'])
df['Yards_Home'] = df['Yards_Loser'].where(df['Location'] == '@', df['Yards_Winner'])
df['Turnover_Home'] = df['Turnover_Loser'].where(df['Location'] == '@', df['Turnover_Winner'])


df['Away_Team'] = df['Winner/Tie'].where(df['Location'] == '@', df['Loser/Tie'])
df['Points_Away'] = df['Points_Winner'].where(df['Location'] == '@', df['Points_Loser'])
df['Yards_Away'] = df['Yards_Winner'].where(df['Location'] == '@', df['Yards_Loser'])
df['Turnover_Away'] = df['Turnover_Winner'].where(df['Location'] == '@', df['Turnover_Loser'])

df['Points_Diff']= df['Points_Home']-df['Points_Away'] 
df['Yards_Diff']= df['Yards_Home']-df['Yards_Away'] 
df['Turnover_Diff']= df['Turnover_Home']-df['Turnover_Away'] 

#removing unneeded/duplicate columns
df.drop([ 'Winner/Tie', 'Location','Loser/Tie','Points_Winner', 'Points_Loser', 'Yards_Winner','Turnover_Winner', 'Yards_Loser', 'Turnover_Loser'], inplace=True, axis=1)

#savingto csv
df.to_csv('cleanedNflFullGameLog.csv')





    
