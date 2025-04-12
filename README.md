# Peregrine Hackathon Project

This repository contains the data and environment setup for the Peregrine Hackathon project.

## Data Structure

The repository contains the following data:

- **Historical Data**:
  - `01_wind_rain.csv`: Historical wind and rain data
  - `02_water_river.csv`: Historical river water data
  - `03_water_gulf.csv`: Historical gulf water data
  - `04_damage.csv`: Historical damage data

- **Future Prediction Data**:
  - `01_wind_rain.csv`: Future wind and rain predictions
  - `02_water_river.csv`: Future river water predictions
  - `03_water_gulf.csv`: Future gulf water predictions
  - `budget_config.json`: Budget constraints for capital investments
  - `capital_investments.csv`: Available capital investment options

## Environment Setup

### Using Conda

1. Clone the repository:
   ```bash
   git clone https://github.com/TheSizar/hacakthon_student.git
   ```

2. Create the conda environment from the environment.yml file:
   ```bash
   conda env create -f environment.yml
   ```

3. Activate the environment:
   ```bash
   conda activate peregrine_hackathon
   ```

### Manual Setup

If you prefer to set up the environment manually:

1. Create a new conda environment:
   ```bash
   conda create -n peregrine_hackathon python=3.10
   ```

2. Activate the environment:
   ```bash
   conda activate peregrine_hackathon
   ```

3. Install required packages:
   ```bash
   conda install pandas numpy matplotlib seaborn scikit-learn jupyter geopandas folium plotly
   ```

## Getting Started

1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Create a new notebook and start exploring the data!

## Project Goal

The goal of this hackathon is to analyze historical weather and damage data to develop a strategic plan for capital investments that will minimize future damage while staying within budget constraints. 