import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('CN Energy.csv')
battery = df.loc[df["Indicator"] == "Power Battery Production"]
battery_years = ["2020","2021","2022","2023","2024","2025"]
battery_data = battery[battery_years].iloc[0]
battery_data = pd.to_numeric(battery_data)
battery_data_growth_rate = battery_data.pct_change() * 100
print("YoY Growth of Power Battery Production")
print(battery_data_growth_rate)

plt.plot(battery_years, battery_data, marker="o", linestyle="-", color="b", label="Power Battery Production")
plt.xlabel("Year")
plt.ylabel("GWh")
plt.title("China's Power Battery Production (2020-2025)")
plt.legend()
plt.show()

#----------------

storage = df.loc[df["Indicator"] == "Cumulative installed capacity of new energy storage"]
storage_years = ["2020", "2021", "2022", "2023", "2024", "2025"]
storage_data = storage[storage_years].iloc[0]
storage_data = pd.to_numeric(storage_data)
storage_growth_rate = storage_data.pct_change() * 100
print("YoY Growth of Cumulative installed capacity of new energy storage:")
print(storage_growth_rate)

plt.plot(storage_years, storage_data, marker="o", linestyle="-", color="g", label="Power Battery Production")
plt.xlabel("Year")
plt.ylabel("GW")
plt.title("China's Cumulative installed capacity of new energy storage (2020-2025)")
plt.legend()
plt.show()