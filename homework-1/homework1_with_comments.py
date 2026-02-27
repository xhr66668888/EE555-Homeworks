# import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


# ============================================================
# Part 1: Fuel Consumption -> Horsepower Prediction
# ============================================================

# 1.1 load the dataset
df1 = pd.read_csv('/home/veronica/桌面/Homework1/FuelEconomy.csv')
print(f"Column names: {list(df1.columns)}")
print(f"Shape: {df1.shape}")
print(f"\nSummary Statistics:")
print(df1.describe())
print(f"\nMissing values:")
print(df1.isnull().sum())


# ============================================================
# Part 2: Weather -> Electricity Consumption
# ============================================================

# 2.1 load dataset
df2 = pd.read_csv('/home/veronica/桌面/Homework1/electricity_consumption_based_weather_dataset.csv')
print(f"Column names: {list(df2.columns)}")
print(f"Shape: {df2.shape}")
print(f"\nSummary Statistics:")
print(df2.describe())
print(f"\nMissing values:")
print(df2.isnull().sum())
print(f"\nTarget variable: daily_consumption")



# ============================================================
# Part 3: Power Plant -> PE Prediction
# ============================================================

# 3.1 load dataset
df3 = pd.read_csv('/home/veronica/桌面/Homework1/usina.csv')
print(f"Column names: {list(df3.columns)}")
print(f"Shape: {df3.shape}")
print(f"\nSummary Statistics:")
print(df3.describe())
print(f"\nMissing values:")
print(df3.isnull().sum())
print(f"\nTarget: PE")
print(f"Features: AT, V, AP, RH")


print(f"\nDone!")
