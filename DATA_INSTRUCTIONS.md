# Data Instructions

This repository contains the environment setup and analysis code for the Peregrine Hackathon project, but does not include the raw data.

## Obtaining the Data

To obtain the original hackathon data:

1. Clone the original data repository:
   ```bash
   git clone https://github.com/TheSizar/hacakthon_student.git
   ```

2. This will create a directory named `hacakthon_student` containing all the necessary data files.

## Data Structure

The data structure is as follows:

- **hacakthon_student/01_Data/02_For_students/01_historical/**
  - `01_wind_rain.csv`: Historical wind and rain data
  - `02_water_river.csv`: Historical river water data
  - `03_water_gulf.csv`: Historical gulf water data
  - `04_damage.csv`: Historical damage data

- **hacakthon_student/01_Data/02_For_students/02_future/**
  - `01_wind_rain.csv`: Future wind and rain predictions
  - `02_water_river.csv`: Future river water predictions
  - `03_water_gulf.csv`: Future gulf water predictions
  - `budget_config.json`: Budget constraints for capital investments
  - `capital_investments.csv`: Available capital investment options

Please make sure to download the data before running the notebooks in this repository. 