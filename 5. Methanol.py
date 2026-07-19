import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CN Energy.csv")

years = ["2020", "2021", "2022", "2023", "2024", "2025"]

MP_capacity = df.loc[df["Indicator"] == "Methanol Production Capacity", years].iloc[0]
M_production = df.loc[df["Indicator"] == "Methanol Production", years].iloc[0]

capacity = pd.to_numeric(MP_capacity)
production = pd.to_numeric(M_production)

plt.title("China's Methanol Production Capacity and Production (2020-2025)")
plt.plot(years, capacity, marker="o", label="Capacity")
plt.plot(years, production, marker="o", label="Production")
plt.xlabel("Year")
plt.ylabel("10,000 tonnes")
plt.legend()
plt.show()

capacity_growth_rate = capacity.pct_change()*100
production_growth_rate = production.pct_change()*100

print("Methanol Production Capacity Growth Rate (%):")
print(capacity_growth_rate)

print("Methanol Production Growth Rate (%):")
print(production_growth_rate)

#----------------

utilization_rate = production / capacity * 100

plt.title("China's Methanol Production Capacity Utilization Rate (2020-2025)")
plt.plot(years, utilization_rate, marker="o", label="Capacity Utilization Rate")
plt.xlabel("Year")
plt.ylabel("%")
plt.legend()
plt.show()

print("Methanol Production Capacity Utilization Rate (%):")
print(utilization_rate.round(2))