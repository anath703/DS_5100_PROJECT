## Introduction

An age-old sentiment amongst NFL fans (and other major sports) is that the home-team possesses a benefit from playing at home versus the visiting team. 
Potential sources for this benefit include: the fact that the visiting team has to travel, familiarity with the field/stadium for the home team, and crowd noise.

With the plethora of possibilities explaining the home-field advantage that teams possess, it needed to be investigated if an advantage even actually exists and to what extent it may exist. Convential wisdom amongst football and fans and betting enthusisats is that home-field avantange is worth three points. A historical analysis of the outcomes of games (win/loss) along with associated factors in the outcomes (points scored, yards gained, turnovers committed, etc.) will sufficiently help to determine if a home-field advantage exists and if so how much. Further, the definition used for home-field advantage will be the **points scored by the home team minus the points scored by the away team.**  

## The Data

Our data comes from three different sources:

1. NFL Game Log from Pro Football Reference

We chose to get our game log data from Pro Football Reference, which has game log data for every NFL football game played going back to the 1950s. A sample of the game logs from the 2020 season can be seen below. Since the NFL has changed drastically over the decades, we wanted to stick with more recent data and were only interested in data from the 2000 season through the 2020 season. Within the game log, we wanted to extract the following information: Team Names, Scores, Yards Gained, Turnovers, and which team was playing at home. 

We found the best way to extract the data was to create a web scraper to scrape using html tags. Details about our webscraper can be found under the “Beyond the original specifications” section. Once we had our scraped data saved as a csv, we were able to load it in as a pandas dataframe.  

The first step in cleaning the data was removing any games that were played in the playoffs and Superbowl. We were only interested in looking at data for the regular season because in a playoff matchup, the team with the better record is usually awarded the ability to play at home. This introduces bias in team strengths between the home and away team that doesn’t exist in the regular season. Next, we had to determine in each matchup which team was home and which team was away. The raw data has a column that has an @ symbol if the team in the “Winner/Tie” column was away and an empty string if the team in the “Loser/Tie” column was at home. Finally, we converted the “Date” column to a datetime format.

2. Geographical and Stadium Type Data

To analyze if distance traveled by teams played an impact on the home-field advantage obtained by teams, we obtained the longitude and latitude of all stadiums that had NFL stadiums played in them since 2000. This includes the now defunct stadiums of many of the teams that have changed locations. Further, we obtained the altitude of each stadium to see if there were impacts from the elevation of stadiums. Lastly, NFL stadiums can be open (no roof), closed (dome), or have a retractible roof and wanted to see how this variable affected our response variable. 

No data set existed that accurately displayed this geographic data needed. We had to therefore leverage mapping websites and stadium info websites from the teams to obtain the data that was needed. 

Once this data was obtained, it needed to be cleaned by assuring that teams that have moved (St. Louis Rams / Los Angeles Rams) or have their name changed (Washington Redskins / Washington Football Team) have the correct longitude and latitude associated with them. Next, we needed to actually calculate the distance between the two coordinates of the stadiums. To do this, we leveraged the haversine formula for calculating distance and created a function from two sets of coordinates passed in. 



## Beyond the original specifications: Highlight clearly what things you did that went beyond the original specifications. 

The best way to obtain game log data was by creating a scraper to the website pro-football-reference and extract the game log data from every game starting from the 2000 season to the end of the 2020 season. The website had a different url with the data for each season. For example, the data for the 2019 NFL season was in https://www.pro-football-reference.com/years/2019/games.htm. Therefore, we looped from 2000 to 2020 in our scraper to access each of the season urls and extract the data needed. We identified the html tags needed and used BeautifulSoup to extract the text and stored it as a list of rows. We then looped through this list and stored the data as a csv file.


## Experimental Design: Describe briefly your process

Once we had our cleaned data in a pandas dataframe, we calculated homefield advantage as the spread between points scored by the home team minus the points scored by the away team. We found that the average homefield advantage for all regular season games between the 2000 and 2020 season was 2.37 points with a standard deviation of 14.70. We then conducted a one-sample t-test with the null hypothesis that the average home field advantage is 0 versus the alternative hypothesis that the average is greater than 0. The resulting p-value was 1.71e-33, leading us to reject the null hypothesis and concluding that home-field advantage does exist in the NFL.

Conventional wisdom amongst football fans and betting enthusiasts is that home field advantage is around three points in the NFL. We conducted a hypothesis test to test this theory. We ran a one-sample t-test with the null hypothesis that the average home field advantage is equal to three points and an alternative hypothesis that the average advantage did not equal three points. The resulting p-value was 0.0015, leading us to reject the null hypothesis and the conventional wisdom that home field advantage is worth three points. 

## Results: Display and discuss the results.

Even though the average home-field advantage is 2.37 points for all seasons, there have been large fluctuations in the average for each season. We can see in the chart below that home-field advantage decreased from 2000 to 2018 season before plunging close to zero for the 2019 and 2020 seasons. The 2020 season could be considered an anomaly due to the fact that teams played at home with no or limited fans and the fact that many teams were without key players for some or all of the season due to COVID-19 restrictions. However, it is not clear why homefield advantage was close to zero for the 2019 season. 

<p align="center">
  <img width="460" height="300" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/avg_homefield_adv.png">
</p>

<p align="left">
  We wanted to look at the distribution of the home-field advantage for each of the NFL teams in 5 season/year periods. This would allow us to determine if the home-field advantage is growing over the last 20 seasons which we are analyzing. As can be seen in the last box plot, the home-field advantage has drastically gotten smaller compared to the earlier portions of our data. This confirms what can be seen in the line plot above where the drop off is visualized in the 2019 season and continued in 2020. Not only is the median home-field advantage lower in this last box plot but there seems to also be less teams that have large home-field advantages. 
</p>

<p align="center">
  <img width="560" height="400" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/box_dist_point_diff.png">
</p>

<p align="left">
Once we examined the home-field advantage at a league level across the groups of seasons, it was important to look at the next level of the data which is on a team to team basis. When looking at a team to team basis, we wanted to see the point differential for teams at home minus the point differential for teams away because this would truly express how much more advantageous it is to play in your home stadium from a point differential standpoint.
</p>

<p align="center">
  <img width="560" height="400" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/2000_2004_bar_point_diff.png">
</p>

<p align="center">
  <img width="560" height="400" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/2005_2010_bar_point_diff.png">
</p>

<p align="center">
  <img width="560" height="400" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/2011_2015_bar_point_diff.png">
</p>

<p align="center">
  <img width="560" height="400" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/2016_2020_bar_point_diff.png">
</p>

<p align="left">
After drilling down to the team level data, our previous findings of a reduced home-field advantage were confirmed yet again. As can be demonstrated by the y-axis in the last bar chart of the 2016-2020 seasons, the range of point differential is considerably lower than the previous groupings of seasons. Another finding that was quite interesting was that the teams with the highest difference in point differential at home vs. away weren't always the best teams in the league. For example, in the first bar chart, the Minnesota Vikings held the highest difference which makes sense considering the early 2000s Vikings teams were contenders and had potent offenses. However, in the last bar chart, the New York Jets had the highest margin betwen point differential even though they have been one of the most putrid teams in the league. Although this causes some raised eyebrows, it is an outcome of our analysis since we have not adjusted the home-field advantage for team strength (ex. applying weights to the teams based off of winning % so that point differentials account for beating bad teams and beating good teams). These graphs do not say which teams are the best but rather which teams perform better from a point differential standpoint at home vs. away.
</p>


<p float="left">
  <img width="460" height="300" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/hfa_dist.png">
  <img width="460" height="300" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/tod_dist.png">  
</p>
<p align="center">
  <img width="460" height="300" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/yards_dist.png">
</p>

One commonly held belief amongst fans is that the longer the distance that an away team must travel for their game, the worse they perform. To see if this is true, we first looked at the average home field advantage by distance travelled in miles by the away team. As seen in the top left chart, the average home-field advantage was the greatest when the away team traveled 1,500 to 2,000 miles, followed by 2,000 or more miles. A similar pattern can be seen when looking at yards differential (top right chart), which is measured as the yards gained by the home team minus the yards gained by the away team. Fianlly, when looking at turnover differential, teams that had to travel 1,000 miles or more averaged 0.1 turnovers than the home team. On the other hand, that differential shrunk to less than 0.03 for teams that travelled less than 1,000 miles. We can see from these charts that team that travel a longer distance for thier game do tend to perform worse.

## Testing: Describe what testing you did. Describe the unit tests that you wrote.

* Describe unit tests for functions to pull a given teams home field advantage (whether that be the last 20 years or one year) which we can actually create later.

## Conclusions: 

* Conclusions
