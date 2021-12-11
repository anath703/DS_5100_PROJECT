## Introduction

An age-old sentiment amongst fans of the NFL (and other major sports) is that the home-team possesses a benefit from playing at home vs. the visiting team. Amongst the sports gambling world, sportsbooks set the advantage at 3 points for evenly matched teams. This benefit can possibly be traced back to many factors such as the fact that the visiting team has to travel or the home team having more support of their fans in a friendly environment. It could even be as simple as being on the field that the team is most familiar with. 

With the plethora of possibilities explaining the home-field advantage that teams possess, it needed to be investigated if an advantage even actually exists and to what extent it may exist. A historical analysis of the outcomes of games (win/loss) along with associated factors in the outcomes (points scored, yards gained, turnovers committed, etc.) will sufficiently help to determine if a home-field advantage exists. Further, the definition used for home-field advantage will be the **points scored by the home team - the points scored by the away team.**  

## The Data: Describe your data set and its significance. 

* Data scraped/collected from where

* One large data frame created from different sets of data, allowing easy access to data cleaning and analysis

* How was the data structure stored (csv files read into pandas data frames)

Our data comes from three different sources:

1. NFL Game Log from Pro Football Reference

We chose to get our game log data from Pro Football Reference, which has game log data for every NFL football game played going back to the 1950s. A sample of the game logs from the 2020 season can be seen below. Since the NFL has changed drastically over the decades, we wanted to stick with more recent data and were only interested in data from the 2000 season through the 2020 season. Within the game log, we wanted to extract the following information: Team Names, Scores, Yards Gained, Turnovers, and which team was playing at home. 

![](/Users/anoopnath/Desktop/MSDS/DS_5100/Project/pfr.png?raw=true "Title")

## Experimental Design: Describe briefly your process

* Process of choosing our data and setting goals?

## Beyond the original specifications: Highlight clearly what things you did that went beyond the original specifications. 

* Describe process of scraping, manually collecting data on location/weather/stadium descriptions

* Discuss user interaction portion (not done yet) where a user can request a specific teams home field advantage for a given year or range of years. 

* Also include an advanced queries (from rubric not sure what we would put here)

## Results: Display and discuss the results.

* Include visualizations/breakdowns of home field advantage across the years. 

![](avg_homefield_adv.png)

![](visualizations/box_dist_point_diff.png)

## Testing: Describe what testing you did. Describe the unit tests that you wrote.

* Describe unit tests for functions to pull a given teams home field advantage (whether that be the last 20 years or one year) which we can actually create later.

## Conclusions: 

* Conclusions
