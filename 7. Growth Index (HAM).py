import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CN Energy.csv")

years = ["2020", "2021", "2022", "2023", "2024", "2025"]

def get_growth_index(Indicator):
    data = df.loc[df["Indicator"] == Indicator, years].iloc[0]
    data = pd.to_numeric(data)
    index = data / data.iloc[0] * 100
    return index

H_production_index = get_growth_index("Hydrogen Production")
M_production_index = get_growth_index("Methanol Production")
A_production_index = get_growth_index("Ammonia Production")

plt.figure(figsize=(10,6))
plt.plot(years, H_production_index, marker="o", label="Hydrogen Production", color="r")
plt.plot(years, M_production_index, marker="o", label="Methanol Production", color="g")
plt.plot(years, A_production_index, marker="o", label="Ammonia Production", color="b")
plt.title("Growth Index of China's Hydrogen-Related Industries (2020 = 100)")
plt.xlabel("Year")
plt.ylabel("Growth Index")
plt.legend()
plt.show()