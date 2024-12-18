
# Air Passengers Time Series Analysis and Forecasting

This project performs time series analysis and forecasting on the Air Passengers dataset using various statistical and visualization techniques.

## Key Steps

1. **Data Preprocessing**:
   - Load the dataset and set the 'Month' column as the index.
   
2. **Seasonal Decomposition**:
   - Decompose the time series into trend, seasonal, and residual components.

3. **Differencing**:
   - Apply first and second-order differencing to achieve stationarity.

4. **Statistical Tests**:
   - Perform Augmented Dickey-Fuller (ADF) test to check the stationarity of the time series.

5. **Model Fitting**:
   - Fit a Seasonal ARIMA (SARIMA) model to the data.

6. **Forecasting**:
   - Generate a 2-year forecast and create a DataFrame for the forecasted values and confidence intervals.

7. **Visualization**:
   - Plot the historical data, forecasted values, and confidence intervals.

## Installation

Install the required Python libraries:
```sh
pip install pandas numpy statsmodels matplotlib seaborn
```

## Usage

1. Ensure the `AirPassengers.csv` file is in the project directory.
2. Run the script using a Python interpreter to perform the analysis and visualize the results.

