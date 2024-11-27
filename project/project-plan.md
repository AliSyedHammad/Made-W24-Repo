# Project Plan

## Title

An Analysis of Effectiveness of Government Response Services

## Main Question

What is the distribution of types of issues faced by the residents of NYC, what is the efficiency of the government response services in handling them, and how well prepared are these services prepared for response in times of naturally adverse conditions?

## Description

The analysis of 311 calls can be of great use for a wide variety of purposes, ranging from a rich understanding of the status of a city to the effectiveness of the government services in addressing such calls.

In this analysis, I want to answer following questions:
- What are different type of Service Requests? Which is most/least frequent?
- From which area do most Service Requests come from?
- Which type of issues are more common?
- Which agencies are more efficient in solving Service Requests?
- Which Service Requests peaks at what time of year or time of day?
- From which type of location do we get the most number of complaints?
- What is the time required to resolve specific complaints in various areas?

With the above answers, we will better understand the dynamics of the city’s issues. Our next step will be to find the following merge the 311 data set with the Storms data set and compare the average response time for complaints during a storm and otherwise.

## Datasources

### Datasource1: 311 Service Requests from 2010 to Present 
* Metadata URL: https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9/about_data
* Data URL: https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9/explore
* Data Dictionary: https://data.cityofnewyork.us/api/views/erm2-nwe9/files/b372b884-f86a-453b-ba16-1fe06ce9d212?download=true&filename=311_ServiceRequest_2010-Present_DataDictionary_Updated_2023.xlsx
* Data Type: CSV
* Our main focus will be on the 311 calls in New York City (NYC). 311 Service Requests encompass all non-emergency requests from the city, including but not limited to noise complaints, air quality issues and reports of unsanitary conditions etc.


### Datasource2: Storm Events Database, NOAA 
* Metadata URL: https://www.ncdc.noaa.gov/stormevents/
* Data URL: https://www.ncdc.noaa.gov/stormevents/choosedates.jsp?statefips=-999%2CALL
* Data Type: CSV
* Storm Data is an official publication of the National Oceanic and Atmospheric Administration (NOAA) which documents the occurrence of storms and other significant weather phenomena having sufficient intensity to cause loss of life, injuries, significant property damage, and/or disruption to commerce. In addition, it is a partial record of other significant meteorological events, such as record maximum or minimum temperatures or precipitation that occurs in connection with another event.

## Work Packages

1. Data Collection and Cleaning
2. Data Merging
3. Exploratory Data Analysis
4. Insights and Visualizations
5. Future Predictions
