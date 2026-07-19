import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("CN Energy.csv")

years = ["2020", "2021", "2022", "2023", "2024", "2025"]

battery = df.loc[df["Indicator"]=="Power Battery Production", years].iloc[0]
battery = pd.to_numeric(battery)

X = [[2020], [2021], [2022], [2023], [2024], [2025]]
y = battery.values

model = LinearRegression()
model.fit(X, y)

future_years = [[2026], [2027], [2028], [2029], [2030]]
prediction = model.predict(future_years)
print(prediction)

all_years = [[2020], [2021], [2022], [2023], [2024], [2025], [2026], [2027], [2028], [2029], [2030]]
all_prediction = model.predict(all_years)

plt.plot([x[0] for x in all_years], all_prediction, label="Linear Regression")
plt.scatter([x[0] for x in X], y, label="Historical Data")
plt.scatter([x[0] for x in future_years], prediction, color="r", label="Forecast")
plt.xticks(range(2020,2031))
plt.xlabel("Year")
plt.ylabel("Power Battery Production (GWh)")
plt.title("Forecasting China's Power Battery Production Using Linear Regression")
plt.legend()
plt.grid(True)
plt.show()

r2 = model.score(X, y)
print(r2)