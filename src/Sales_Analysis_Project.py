# ===============================
# SALES ANALYSIS & FORECASTING
# ===============================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# -------------------------------
# Load data
# -------------------------------
df = pd.read_csv('sales_data.csv')
print("DF after loading:", df.shape)
print(df.head())

# -------------------------------
# Clean data
# -------------------------------
df.drop_duplicates(inplace=True)

# Fix date parsing
df['Date'] = df['Date'].astype(str).str.strip()
df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d", errors='coerce')
df.dropna(subset=['Date'], inplace=True)

print("\nDF after cleaning:", df.shape)
print(df.head())

# -------------------------------
# Monthly sales and summaries
# -------------------------------
monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Sales'].sum()
monthly_sales.index = monthly_sales.index.to_timestamp()
monthly_sales = monthly_sales.asfreq('M')

top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(10)
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
top_customers = df.groupby('Customer ID')['Sales'].sum().sort_values(ascending=False).head(10)

# -------------------------------
# PLOTS with custom window titles
# -------------------------------

# Monthly Sales Trend
plt.figure(num="Monthly Sales Trend", figsize=(10,5))
monthly_sales.plot(kind='line', marker='o', title='Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# Top 10 Products by Sales
plt.figure(num="Top Products by Sales", figsize=(10,5))
sns.barplot(x=top_products.values, y=top_products.index, palette='viridis')
plt.title('Top 10 Products by Sales')
plt.xlabel('Sales')
plt.ylabel('Product')
plt.show()

# Sales by Region
plt.figure(num="Sales by Region", figsize=(8,6))
region_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title('Sales by Region')
plt.ylabel('')
plt.show()

# Top 10 Customers by Purchase Amount
plt.figure(num="Top Customers by Sales", figsize=(10,5))
sns.barplot(x=top_customers.values, y=top_customers.index, palette='magma')
plt.title('Top 10 Customers by Purchase Amount')
plt.xlabel('Sales')
plt.ylabel('Customer ID')
plt.show()

# -------------------------------
# FORECASTING
# -------------------------------
model = ExponentialSmoothing(
    monthly_sales,
    seasonal='add',
    seasonal_periods=12
).fit()

forecast = model.forecast(6)

plt.figure(num="Sales Forecast", figsize=(10,5))
monthly_sales.plot(label='Historical Sales', marker='o')
forecast.plot(label='Forecast', marker='o', linestyle='--')
plt.title('Sales Forecast for Next 6 Months')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()

# -------------------------------
# PRINT INSIGHTS
# -------------------------------
print("\n--- Key Insights ---")
print("\nTop Products:\n", top_products)
print("\nSales by Region:\n", region_sales)
print("\nTop Customers:\n", top_customers)
print("\nForecast for Next 6 Months:\n", forecast)