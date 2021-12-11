## Introduction

An age-old sentiment amongst fans of the NFL (and other major sports) is that the home-team possesses a benefit from playing at home vs. the visiting team. Amongst the sports gambling world, sportsbooks set the advantage at 3 points for evenly matched teams. This benefit can possibly be traced back to many factors such as the fact that the visiting team has to travel or the home team having more support of their fans in a friendly environment. It could even be as simple as being on the field that the team is most familiar with. 

With the plethora of possibilities explaining the home-field advantage that teams possess, it needed to be investigated if an advantage even actually exists and to what extent it may exist. A historical analysis of the outcomes of games (win/loss) along with associated factors in the outcomes (points scored, yards gained, turnovers committed, etc.) will sufficiently help to determine if a home-field advantage exists. Further, the definition used for home-field advantage will be the **points scored by the home team - the points scored by the away team.**  

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


![](/Users/anoopnath/Desktop/MSDS/DS_5100/Project/pfr.png?raw=true "Title")

## Experimental Design: Describe briefly your process

* Process of choosing our data and setting goals?

## Beyond the original specifications: Highlight clearly what things you did that went beyond the original specifications. 

The best way to obtain the data we needed was by creating a scraper to extract the game log data from every game starting from the 2000 season to the end of the 2020 season. The website had a different url with the data for each season. For example, the data for the 2019 NFL season was in https://www.pro-football-reference.com/years/2019/games.htm. Therefore, we looped from 2000 to 2020 in our scraper to access each of the season urls and extract the data needed. We identified the html tags needed and used BeautifulSoup to extract the text and stored it as a list of rows. We then looped through this list and stored the data as a csv file.


## Results: Display and discuss the results.

* Include visualizations/breakdowns of home field advantage across the years. 

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

<p align="center">
  <img width="460" height="300" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/hfa_dist.png">
</p>

<p align="center">
  <img width="460" height="300" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/tod_dist.png">
</p>

<p align="center">
  <img width="460" height="300" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/yards_dist.png">
</p>

## Testing: Describe what testing you did. Describe the unit tests that you wrote.

* Describe unit tests for functions to pull a given teams home field advantage (whether that be the last 20 years or one year) which we can actually create later.

## Conclusions: 

* Conclusions
