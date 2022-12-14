from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("electricityConsumption_2021.csv", dayfirst=True, sep=";",
                   header=0, decimal=b",", usecols=[0, 1, 2, 3])

# Getting the columns
period = data.iloc[:, 0].values
night_time = data.iloc[:, 1].values
day_time = data.iloc[:, 2].values
outdoor_temperature = data.iloc[:, 3].values

# Combining the data
whole_data = [period, night_time, day_time, outdoor_temperature]

night_time_and_outdoor_temperature = {}

for i, value in enumerate(whole_data[1]):
    if value != 'No metering data available for this period':
        period[i] = datetime.strptime(period[i], '%A %d.%m.%Y %H:%M')
        value = value.replace(',','.')
        night_time_and_outdoor_temperature.update({period[i]: float(value)})

day_time_and_outdoor_temperature = {}

for i, value in enumerate(whole_data[2]):
    if value != 'No metering data available for this period':
        period[i] = datetime.strptime(period[i], '%A %d.%m.%Y %H:%M')
        value = value.replace(',','.')
        day_time_and_outdoor_temperature.update({period[i]: float(value)})

sns.set_style("darkgrid")
plt.figure(figsize=(20, 5))
plt.plot(night_time_and_outdoor_temperature.keys(),
         night_time_and_outdoor_temperature.values())
plt.title("Night time 2021",fontsize=20, fontweight="bold", font='fantasy')
plt.grid(color='black', linestyle='--', linewidth=0.5)
plt.ylabel("Cosumption kWh")
plt.show()

plt.figure(figsize=(20, 5))
plt.plot(day_time_and_outdoor_temperature.keys(),
         day_time_and_outdoor_temperature.values())
plt.title("Day time 2021",fontsize=20, fontweight="bold", font='fantasy')
plt.grid(color='black', linestyle='--', linewidth=0.5)
plt.ylabel("Cosumption kWh")
plt.show()
