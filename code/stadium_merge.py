# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 19:42:21 2021

@author: caliz
"""

import pandas as pd
import geopy.distance
url = 'https://raw.githubusercontent.com/anath703/DS_5100_PROJECT/main/cleanedNflFullGameLog.csv' #location of raw data file
df = pd.read_csv(url)

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
