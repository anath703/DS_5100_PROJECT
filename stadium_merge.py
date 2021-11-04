# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 19:42:21 2021

@author: caliz
"""

import pandas as pd
import geopy.distance
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

#looking only at seasons 2000 and beyond
df = df[(df['Season']>1999)]

#reading in stadium data
stadium = pd.read_csv('https://raw.githubusercontent.com/anath703/DS_5100_PROJECT/main/stadium_coordinates.csv')

#creating a dictionary of the team and then stadium info
stadium_dict = stadium.set_index('team').T.to_dict('list')

#assigning a list of the stadium info to each team based off of team name
df['Home_Stadium_List']= df['Home_Team'].map(stadium_dict)
df['Away_Stadium_List']= df['Away_Team'].map(stadium_dict)

#breaking the list of each team's stadium info into its own column
df[['Home_Latitude','Home_Longitude', 'Home_Stad_Type', 'Home_Altitude']] = pd.DataFrame(df.Home_Stadium_List.tolist(), index= df.index)
df[['Away_Latitude','Away_Longitude', 'Away_Stad_Type', 'Away_Altitude']] = pd.DataFrame(df.Away_Stadium_List.tolist(), index= df.index)

#creating latitude and longitude tuples for distance calculation
df['Home_Tupe'] = list(zip(df.Home_Latitude, df.Home_Longitude))
df['Away_Tupe'] = list(zip(df.Away_Latitude, df.Away_Longitude))

#create a function to calculate the distance in miles between the stadiums
def distance_calc(row):
    coords_1 = (row['Home_Latitude'], row['Home_Longitude'])
    coords_2 = (row['Away_Latitude'], row['Away_Longitude'])
    return geopy.distance.distance(coords_1, coords_2).miles

#apply the function to our dataframe
df['distance'] = df.apply(distance_calc, axis=1)

#remove stadium info lists since they're redundant
df.drop(['Home_Stadium_List','Away_Stadium_List'], inplace=True, axis=1)

#write to csv
df.to_csv('cleanedNflFullGameLog_withstadiuminfo.csv')