from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read electricity consumption data from csv file
data = pd.read_csv("2022.csv", dayfirst=True, sep=";",
                   header=0, decimal=b",", usecols=[0, 1, 2, 3])

# Getting the columns
period = data.iloc[:, 0].values
night_time = data.iloc[:, 1].values
day_time = data.iloc[:, 2].values
outdoor_temperature = data.iloc[:, 3].values

Jan = {}
Feb = {}
Mar = {}
Apr = {}
May = {}
Jun = {}
Jul = {}
Aug = {}
Sep = {}
Oct = {}
Nov = {}

for i, value in enumerate(period):
    value = datetime.strptime(value, '%A %d.%m.%Y %H:%M')
    night_time[i] = night_time[i].replace(',', '.')
    day_time[i] = day_time[i].replace(',', '.')
    if night_time[i] != 'No metering data available for this period':
        curr_time = float(night_time[i])
    else:
        curr_time = float(day_time[i])
    if value.month == 1:
        Jan.update({value: curr_time})
    elif value.month == 2:
        Feb.update({value: curr_time})
    elif value.month == 3:
        Mar.update({value: curr_time})
    elif value.month == 4:
        Apr.update({value: curr_time})
    elif value.month == 5:
        May.update({value: curr_time})
    elif value.month == 6:
        Jun.update({value: curr_time})
    elif value.month == 7:
        Jul.update({value: curr_time})
    elif value.month == 8:
        Aug.update({value: curr_time})
    elif value.month == 9:
        Sep.update({value: curr_time})
    elif value.month == 10:
        Oct.update({value: curr_time})
    elif value.month == 11:
        Nov.update({value: curr_time})

# Getting the price for every month multiplying by cents per kWh unique to each month
combined = [sum(Jan.values())*0.1998, sum(Feb.values())*0.186, sum(Mar.values())*0.1425, sum(Apr.values())*0.2098, sum(May.values())*0.1392, sum(Jun.values())
            * 0.1128, sum(Jul.values())*0.1595, sum(Aug.values())*0.3298, sum(Sep.values())*0.3797, sum(Oct.values())*0.409, sum(Nov.values())*0.4749]

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
          'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']

plt.figure(figsize=(20, 5))
plt.bar(months, combined, color='#31651F')
plt.title("Price of Electricity (2022)", font="monospace",
          fontsize=22, color="#2b4b20")
# plt.grid(color='black', linestyle='--', linewidth=0.5)
plt.xlabel("Month", font="monospace", fontsize=13, color="#2b4b20")
plt.ylabel("Cost (€)", font="monospace", fontsize=13, color="#2b4b20")
plt.show()
