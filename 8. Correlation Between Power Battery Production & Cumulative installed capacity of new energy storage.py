import pandas as pd

df = pd.read_csv("CN Energy.csv")

years = ["2020", "2021", "2022", "2023", "2024", "2025"]

battery = pd.to_numeric(df.loc[df["Indicator"]=="Power Battery Production", years].iloc[0])
storage = pd.to_numeric(df.loc[df["Indicator"]=="Cumulative installed capacity of new energy storage", years].iloc[0])

correlation = battery.corr(storage)

print(correlation)