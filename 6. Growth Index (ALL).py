import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CN Energy.csv")

years = ["2020", "2021", "2022", "2023", "2024", "2025"]

def get_growth_index(Indicator):
    data = df.loc[df["Indicator"] == Indicator, years].iloc[0]
    data = pd.to_numeric(data)
    index = data / data.iloc[0] * 100
    return index

battery_index = get_growth_index("Power Battery Production")
storage_index = get_growth_index("Cumulative installed capacity of new energy storage")
H_production_index = get_growth_index("Hydrogen Production")
M_production_index = get_growth_index("Methanol Production")
A_production_index = get_growth_index("Ammonia Production")

plt.figure(figsize=(10,6))
plt.plot(years, battery_index, marker="o", label="Power Battery")
plt.plot(years, storage_index, marker="o", label="Energy Storage")
plt.plot(years, H_production_index, marker="o", label="Hydrogen Production")
plt.plot(years, M_production_index, marker="o", label="Methanol Production")
plt.plot(years, A_production_index, marker="o", label="Ammonia Production")
plt.title("Growth Index of China's Clean Energy and Hydrogen-Related Industries (2020 = 100)")
plt.xlabel("Year")
plt.ylabel("Growth Index")
plt.legend()
plt.show()