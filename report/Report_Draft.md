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

3. Weather Data

We also wanted to determine if weather affected home-field advantage. For the data source, we used www.nflweather.com, which keeps detailed records of weather in each NFL game over the past several seasons. Since the weather data does not go back to 2000, we decided to take the most recent complete season (2020) as our data set. As an example of our data cleaning, we split the “Temperature” column to extract the number before the letter “F” (Fahrenheit). We then used the home team in each game to merge this data with our main data set. This gave us three additional pieces of information for each game: temperature, wind speed, and weather conditions (14 possible descriptions).

## Beyond the original specifications: 

The best way to obtain game log data was by creating a scraper to the website pro-football-reference and extract the game log data from every game starting from the 2000 season to the end of the 2020 season. The website had a different url with the data for each season. For example, the data for the 2019 NFL season was in https://www.pro-football-reference.com/years/2019/games.htm. Therefore, we looped from 2000 to 2020 in our scraper to access each of the season urls and extract the data needed. We identified the html tags needed and used BeautifulSoup to extract the text and stored it as a list of rows. We then looped through this list and stored the data as a csv file.

We also took the time to create a simple function for calculating any given team's homefield advantage over any given range of years. This function takes user input for which team you would like to see, and what years you would like to calcaulate homefield advantage over. This could be useful for a quick check into a teams given advantage for any specific year, or even a range of years when dealing with more in depth sports analysis or simply looking for patterns.


## Experimental Design: Describe briefly your process

Once we had our cleaned data in a pandas dataframe, we calculated homefield advantage as the spread between points scored by the home team minus the points scored by the away team. We found that the average homefield advantage for all regular season games between the 2000 and 2020 season was 2.37 points with a standard deviation of 14.70. We then conducted a one-sample t-test with the null hypothesis that the average home field advantage is 0 versus the alternative hypothesis that the average is greater than 0. The resulting p-value was 1.71e-33, leading us to reject the null hypothesis and concluding that home-field advantage does exist in the NFL.

Conventional wisdom amongst football fans and betting enthusiasts is that home field advantage is around three points in the NFL. We conducted a hypothesis test to test this theory. We ran a one-sample t-test with the null hypothesis that the average home field advantage is equal to three points and an alternative hypothesis that the average advantage did not equal three points. The resulting p-value was 0.0015, leading us to reject the null hypothesis and the conventional wisdom that home field advantage is worth three points. 

## Results:

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

<p float="left">
  <img width="480" height="400" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/2000_2004_bar_point_diff.png">
  <img width="480" height="400" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/2005_2010_bar_point_diff.png">
</p>
<p align="center">
    <img width="480" height="400" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/2011_2015_bar_point_diff.png">
    <img width="480" height="400" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/2016_2020_bar_point_diff.png">
</p>

<p align="left">
After drilling down to the team level data, our previous findings of a reduced home-field advantage were confirmed yet again. As can be demonstrated by the y-axis in the last bar chart of the 2016-2020 seasons, the range of point differential is considerably lower than the previous groupings of seasons. Another finding that was quite interesting was that the teams with the highest difference in point differential at home vs. away weren't always the best teams in the league. For example, in the first bar chart, the Minnesota Vikings held the highest difference which makes sense considering the early 2000s Vikings teams were contenders and had potent offenses. However, in the last bar chart, the New York Jets had the highest margin betwen point differential even though they have been one of the most putrid teams in the league. Although this causes some raised eyebrows, it is an outcome of our analysis since we have not adjusted the home-field advantage for team strength (ex. applying weights to the teams based off of winning % so that point differentials account for beating bad teams and beating good teams). These graphs do not say which teams are the best but rather which teams perform better from a point differential standpoint at home vs. away.
</p>


<p float="left">
  <img width="460" height="300" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/hfa_dist.png">
  <img width="460" height="300" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/yards_dist.png">  
</p>
<p align="center">
  <img width="460" height="300" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/tod_dist.png">
</p>

One commonly held belief amongst fans is that the longer the distance that an away team must travel for their game, the worse they perform. To see if this is true, we first looked at the average home field advantage by distance travelled in miles by the away team. As seen in the top left chart, the average home-field advantage was the greatest when the away team traveled 1,500 to 2,000 miles, followed by 2,000 or more miles. A similar pattern can be seen when looking at yards differential (top right chart), which is measured as the yards gained by the home team minus the yards gained by the away team. Fianlly, when looking at turnover differential, teams that had to travel 1,000 miles or more averaged 0.1 turnovers than the home team. On the other hand, that differential shrunk to less than 0.03 for teams that travelled less than 1,000 miles. We can see from these charts that team that travel a longer distance for thier game do tend to perform worse.

When looking at building multiple linear regression models for homefield advantage there are a few variables that we found to be more indicative than others. As far as significance, we saw distance as the most accurate identifier of the overall trend we would expect to see impact the point differentials between teams at home and away. The following scatterplot shows the linear regression model including just the distance variable against the actual distribution of individual variables.

<p align="center">
  <img width="460" height="300" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/pointDiffDistanceScatter.png">
</p>

Though there does appear to be a gradually increasing advantage based on the distance between the teams, there is also extremely high variance and ultimately our ability to predict the value of a given teams homefield advantage using distance is innacurate. This lead us to consider other potential variables such as differences in altitude, latitude and longitude individually, and the type of stadium the teams play in. Ultimately these variables run into the same issue as distance, where the variance is so high that they are not particularly valuable for predicting individual games and are more useful as indicators for an overall trend.

Finally, we turned to analyzing the effects of weather on home-field advantage. Using the lm function in R, we attempted to explain point differential as a function of two quantitative variables (temperature, wind speed) and 14 categorical variables (weather conditions). As seen below, neither of the quantitative variables was statistically significant at any level. Of the various categorical variables, only one was significant at the 95% confidence level: fog. Specifically, fog seemed to significantly help the away team, a somewhat unexpected result. We have serious misgivings about this result. First, there were only 7 games with fog, which is a small sub-sample. Second, a 95% confidence level implies that 1 in 20 tested variables will be significant by accident, and we had a total of 16 tested variables. It seems entirely possible that fog was simply the “lucky” variable.

<p align="center">
  <img width="550" height="600" src="https://github.com/anath703/DS_5100_PROJECT/blob/main/visualizations/weatherModel.png">
</p>

In an attempt to find the best model, we used backwards elimination on a full model including all of these variables and it eliminated everything but distance, leading us to believe that this is the most accurate model, though we have already determined that it is not. Likely what is occuring is that because for calculating the homefield advantage using distance and other similar variables, there are many confounding variables for determining the point difference between the teams which are not considered. The high variance may be attributed to general skill levels of the teams playing, players involved, and other significantly more impactful variables that are not necessarily tied to homefield advantage, though for thew scope of this project we did not include those.

## Testing: 

Most of our testing was employed for assuring that the user fed function for calculating any given team's homefield advantage across the years. Basically just assuring that the function would take the correct variables and perform the calculations correctly given the proper inputs. The unit testing did confirm that there was an issue with calculating the team's advantage when fed the same year for both the lower and upper bound, which was then able to be corrected.

## Conclusions: 

Our research has established three findings: home field advantage exists in the NFL, it has declined noticeably in the past two seasons, and the reasons for its existence (and decline) remain obscure. While the last finding is not very satisfactory, it points the way to future research on this subject. We chose several explanatory variables that we though could be related to home-field advantage, but there are many other possible choices, including: fan attendance, noise level inside a stadium, more granular weather data, etc. These variables will likely be more difficult to obtain, but they may shed light on the subject. In particular, they may help explain one of our most puzzling findings: that home-field advantage dropped precipitously in 2019, the year before the COVID-impacted 2020 season. Recently legalized sports betting markets may also add useful information, as markets aggregate the views of their participants and are often more accurate than most individual predictions. Finally, the 2021 season will add the most current data possible once it concludes in February of 2022. With so many possible avenues of investigation, home-field advantage in the NFL will likely remain an area of study for the foreseeable future.
