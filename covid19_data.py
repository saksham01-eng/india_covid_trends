import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


data = pd.read_csv("covid19_india_status.csv")
print(data.head())

print(data.isnull().sum())

country_data = data.groupby('State/UTs').sum()
print(country_data.head())

fig, ax = plt.subplots(figsize=(26,12 ))
plt.plot(country_data['Deaths'], label='deaths', color='red')
plt.plot(country_data['Discharge Ratio'], label='Discharged', color='blue')
plt.plot(country_data['Total Cases'], label='Total Cases', color='green')
plt.title('India Covid-19 Trends')
plt.xlabel('India status during covid-19')
plt.ylabel('State/UTs')
ax.xaxis.set_major_locator(MultipleLocator(1))  # Show every 2nd x-tick
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend()
plt.grid(True)
plt.show()