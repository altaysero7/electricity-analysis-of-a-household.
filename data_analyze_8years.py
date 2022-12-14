from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("energy comsuption_household.csv", dayfirst=True, sep=",",
                   header=0, decimal=b",", usecols=[0, 1, 2, 3, 4])

# Getting the columns
date = data.iloc[:, 0].values
night_time = data.iloc[:, 1].values
day_time = data.iloc[:, 2].values
total_consumption = data.iloc[:, 3].values
outdoor_temperature = data.iloc[:, 4].values

# Combining the data
whole_data = [date, night_time, day_time,
              total_consumption, outdoor_temperature]

night_time_and_outdoor_temperature = {}

for i, value in enumerate(whole_data[1]):
    date[i] = datetime.strptime(date[i], '%d-%b-%y')
    night_time_and_outdoor_temperature.update({date[i]: float(value)})

day_time_and_outdoor_temperature = {}

for i, value in enumerate(whole_data[2]):
    day_time_and_outdoor_temperature.update({date[i]: float(value)})

sns.set_style("darkgrid")
plt.figure(figsize=(20, 5))
plt.plot(night_time_and_outdoor_temperature.keys(),
         night_time_and_outdoor_temperature.values())
plt.title("Night time 8 years", fontsize=20, fontweight="bold", font='fantasy')
plt.grid(color='black', linestyle='--', linewidth=0.5)
plt.ylabel("Cosumption kWh")
plt.show()

plt.figure(figsize=(20, 5))
plt.plot(day_time_and_outdoor_temperature.keys(),
         day_time_and_outdoor_temperature.values())
plt.title("Day time 8 years", fontsize=20, fontweight="bold", font='fantasy')
plt.grid(color='black', linestyle='--', linewidth=0.5)
plt.ylabel("Cosumption kWh")
plt.show()
