## Introduction

An age-old sentiment amongst fans of the NFL (and other major sports) is that the home-team possesses a benefit from playing at home vs. the visiting team. Amongst the sports gambling world, sportsbooks set the advantage at 3 points for evenly matched teams. This benefit can possibly be traced back to many factors such as the fact that the visiting team has to travel or the home team having more support of their fans in a friendly environment. It could even be as simple as being on the field that the team is most familiar with. 

With the plethora of possibilities explaining the home-field advantage that teams possess, it needed to be investigated if an advantage even actually exists and to what extent it may exist. A historical analysis of the outcomes of games (win/loss) along with associated factors in the outcomes (points scored, yards gained, turnovers committed, etc.) will sufficiently help to determine if a home-field advantage exists. Further, the definition used for home-field advantage will be the **points scored by the home team - the points scored by the away team.**  

## The Data: Describe your data set and its significance. 

Our data comes from three different sources:

1. NFL Game Log from Pro Football Reference

We chose to get our game log data from Pro Football Reference, which has game log data for every NFL football game played going back to the 1950s. A sample of the game logs from the 2020 season can be seen below. Since the NFL has changed drastically over the decades, we wanted to stick with more recent data and were only interested in data from the 2000 season through the 2020 season. Within the game log, we wanted to extract the following information: Team Names, Scores, Yards Gained, Turnovers, and which team was playing at home. 

We found the best way to extract the data was to create a web scraper to scrape using html tags. Details about our webscraper can be found under the “Beyond the original specifications” section. Once we had our scraped data saved as a csv, we were able to load it in as a pandas dataframe.  

The first step in cleaning the data was removing any games that were played in the playoffs and Superbowl. We were only interested in looking at data for the regular season because in a playoff matchup, the team with the better record is usually awarded the ability to play at home. This introduces bias in team strengths between the home and away team that doesn’t exist in the regular season. Next, we had to determine in each matchup which team was home and which team was away. The raw data has a column that has an @ symbol if the team in the “Winner/Tie” column was away and an empty string if the team in the “Loser/Tie” column was at home. Finally, we converted the “Date” column to a datetime format.


![](/Users/anoopnath/Desktop/MSDS/DS_5100/Project/pfr.png?raw=true "Title")

## Experimental Design: Describe briefly your process

* Process of choosing our data and setting goals?

## Beyond the original specifications: Highlight clearly what things you did that went beyond the original specifications. 

The best way to obtain the data we needed was by creating a scraper to extract the game log data from every game starting from the 2000 season to the end of the 2020 season. The website had a different url with the data for each season. For example, the data for the 2019 NFL season was in https://www.pro-football-reference.com/years/2019/games.htm. Therefore, we looped from 2000 to 2020 in our scraper to access each of the season urls and extract the data needed. We identified the html tags needed and used BeautifulSoup to extract the text and stored it as a list of rows. We then looped through this list and stored the data as a csv file.


## Results: Display and discuss the results.

* Include visualizations/breakdowns of home field advantage across the years. 

![](avg_homefield_adv.png)

![](visualizations/box_dist_point_diff.png)

## Testing: Describe what testing you did. Describe the unit tests that you wrote.

* Describe unit tests for functions to pull a given teams home field advantage (whether that be the last 20 years or one year) which we can actually create later.

## Conclusions: 

* Conclusions
