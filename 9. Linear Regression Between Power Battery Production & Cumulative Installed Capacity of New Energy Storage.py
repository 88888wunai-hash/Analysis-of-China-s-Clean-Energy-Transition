import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("CN Energy.csv")

years = ["2020", "2021", "2022", "2023", "2024", "2025"]

battery = pd.to_numeric(df.loc[df["Indicator"]=="Power Battery Production", years].iloc[0])
storage = pd.to_numeric(df.loc[df["Indicator"]=="Cumulative installed capacity of new energy storage", years].iloc[0])

X = storage.values.reshape(-1,1)
y = battery.values

model = LinearRegression()
model.fit(X,y)
prediction = model.predict(X)

r2 = model.score(X, y)

for i, year in enumerate(years):
    plt.text(storage.iloc[i], battery.iloc[i], year, fontsize=9)

plt.title("Relationship between Installed Energy Storage Capacity and Power Battery Production in China (2020–2025):")
plt.text(5, 1700, f"$R^2$ = {r2:.3f}", fontsize=11)
plt.scatter(storage, battery)
plt.plot(storage, prediction)
plt.xlabel("Installed Storage Capacity (GW)")
plt.ylabel("Power Battery Production (GWh)")
plt.show()