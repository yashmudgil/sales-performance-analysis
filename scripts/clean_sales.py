
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel('data/Superstore_Sales.xlsx')

# Basic cleaning
df = df.dropna(subset=['Order Date', 'Sales', 'Region'])
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Monthly aggregation
monthly_sales = df.groupby(pd.Grouper(key='Order Date', freq='M'))['Sales'].sum().reset_index()
monthly_sales.columns = ['ds', 'y']

# Forecasting
model = Prophet()
model.fit(monthly_sales)
future = model.make_future_dataframe(periods=3, freq='M')
forecast = model.predict(future)

# Save forecast to Excel
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_excel('output/sales_forecast.xlsx', index=False)

# Optional: plot forecast
fig = model.plot(forecast)
plt.title('Sales Forecast')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.savefig('output/sales_forecast.png')
