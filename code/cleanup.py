"""

Date: 10/31/2021
Name: Anoop Nath
Description: Module 8 Exercise: Data Cleaning
UVA Computing ID:nux9aq
Notes: The raw csv contains a log of every NFL game played since 1970. However, there are several missing row, which I want to remove. The log indicates score for the winning team and losing team but I want to convert this to score for the home team and the away team.

"""



import pandas as pd
import numpy as np

url = 'https://github.com/anath703/DS_5100_PROJECT/raw/main/nflFullGameLog.csv' #location of raw data file
df = pd.read_csv(url)
df2= pd.read_csv('https://github.com/anath703/DS_5100_PROJECT/raw/main/nflFullGameLog_neutral.csv')
df['Neutral'] = df2['Neutral'] 
df['Neutral'] =  np.where(df['Location'] == 'N', True , False) # adding a column that indicates if a game is played in a neutral stadium
df['Away_Team'] = df['Winner/Tie'].where(df['Location'] == '@', df['Loser/Tie'])


df=  df[df['Week'].notna()] #removing rows that have NAs in the "Week" column
df['Date']= pd.to_datetime(df['Date'] ).dt.date #converting to date time

#creating new columns to indicate which team is home, which team is away, and yards,points and turnovers for each.
df['Home_Team'] = df['Loser/Tie'].where(df['Location'] == '@', df['Winner/Tie'])
df['Points_Home'] = df['Points_Loser'].where(df['Location'] == '@', df['Points_Winner'])
df['Yards_Home'] = df['Yards_Loser'].where(df['Location'] == '@', df['Yards_Winner'])
df['Turnover_Home'] = df['Turnover_Loser'].where(df['Location'] == '@', df['Turnover_Winner'])


df['Away_Team'] = df['Winner/Tie'].where(df['Location'] == '@', df['Loser/Tie'])
df['Points_Away'] = df['Points_Winner'].where(df['Location'] == '@', df['Points_Loser'])
df['Yards_Away'] = df['Yards_Winner'].where(df['Location'] == '@', df['Yards_Loser'])
df['Turnover_Away'] = df['Turnover_Winner'].where(df['Location'] == '@', df['Turnover_Loser'])
###

#creating columns to indicate point, yards and turnover differential (Home minus Away)
df['Points_Diff']= df['Points_Home']-df['Points_Away'] 
df['Yards_Diff']= df['Yards_Home']-df['Yards_Away'] 
df['Turnover_Diff']= df['Turnover_Home']-df['Turnover_Away'] 
##

#removing unneeded/duplicate columns
df.drop([ 'Winner/Tie', 'Location','Loser/Tie','Points_Winner', 'Points_Loser', 'Yards_Winner','Turnover_Winner', 'Yards_Loser', 'Turnover_Loser'], inplace=True, axis=1)

#savingto csv
df.to_csv('cleanedNflFullGameLog.csv')




    
