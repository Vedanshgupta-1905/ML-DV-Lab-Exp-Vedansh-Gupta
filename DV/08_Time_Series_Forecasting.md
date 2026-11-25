# Experiment 8: Time Series Forecasting

## Aim
Implement Time Series Forecasting using Power BI Desktop.

## Dataset
[retail_sales.csv](retail_sales.csv) (synthetic demonstration data).

## Procedure
Create a calendar table using `Calendar = CALENDAR(MIN(retail_sales[Date]),MAX(retail_sales[Date]))` and relate Calendar[Date] to retail_sales[Date]. Use a line chart with continuous Calendar[Date] and Total Sales (define as SUM(retail_sales[Sales])). Add a 30-day moving average measure: `Moving Average = AVERAGEX(DATESINPERIOD('Calendar'[Date],MAX('Calendar'[Date]),-30,DAY),CALCULATE([Total Sales]))`. For forecasting use a separate line chart with one sales series, no legend, continuous date axis; Analytics > Forecast, if available, choose 30 days and 95% confidence. Add trend line if supported by visual/version.

## Expected result
The configured visual or transformation should demonstrate the stated aim. Save your Power BI report and add a screenshot of your actual output after completing the procedure.
