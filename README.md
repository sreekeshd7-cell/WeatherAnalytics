# Weather Analytics Dashboard

An end-to-end weather data analytics project that collects, stores, processes, analyzes, and visualizes weather information across multiple Indian cities.

## Project Overview

Weather Analytics collects weather data using the Open-Meteo API and processes it using Python and Pandas. The data is stored in SQLite and visualized through an interactive Streamlit dashboard and Power BI report.

The project explores temperature, humidity, wind speed, historical trends, city-wise comparisons, and weather correlations.

## Cities Covered

- Chandigarh
- Delhi
- Mumbai
- Bengaluru
- Chennai

## Architecture

Open-Meteo API → Python Data Collection → Pandas Processing → SQLite Database → Power BI / Streamlit Visualization

## Technologies Used

- Python
- Pandas
- Requests
- SQLite
- Streamlit
- Plotly
- Power BI
- Matplotlib
- Seaborn

## Features

- Automated weather data collection
- Hourly historical weather data
- Multi-city comparison
- SQLite database storage
- Data cleaning and preprocessing
- Interactive Streamlit dashboard
- Power BI reports
- Temperature, humidity, and wind analysis
- Correlation analysis
- Anomaly detection
- Historical trend visualization

## Dashboard

The Power BI report contains multiple analytical views:

1. Weather Overview
2. Historical Analysis
3. Advanced Analytics

The Streamlit dashboard provides an interactive interface for exploring weather observations and city-wise insights.

## Project Structure

```text
WeatherAnalytics/
├── app.py
├── fetch_weather.py
├── fetch_history.py
├── database.py
├── view_database.py
├── advanced_analysis.py
├── correlation_analysis.py
├── export_powerbi.py
├── powerbi/
├── screenshots/
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/WeatherAnalytics.git
cd WeatherAnalytics
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Initialize the database:

```bash
python database.py
```

Fetch weather data:

```bash
python fetch_weather.py
```

Fetch historical weather data:

```bash
python fetch_history.py
```

Launch the Streamlit dashboard:

```bash
streamlit run app.py
```

## Data Source

Weather data is retrieved from the Open-Meteo API.

https://open-meteo.com/

## Learning Objectives

This project demonstrates practical concepts related to:

- Data ingestion
- REST APIs
- Data cleaning
- SQL databases
- Data analysis
- Data visualization
- Business intelligence
- Data pipelines
- Historical time-series analysis

## Future Improvements

- Cloud data storage using Azure
- Automated cloud data pipelines
- Weather forecasting using machine learning
- Scheduled data collection
- Deployment of the dashboard

## Author

Sreekesh Das

Computer Science Engineering — Artificial Intelligence & Machine Learning
