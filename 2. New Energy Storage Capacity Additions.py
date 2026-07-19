import pandas as pd

df = pd.read_csv('CN Energy.csv')
storage = df.loc[df["Indicator"] == "Cumulative installed capacity of new energy storage"]
storage_years = ["2020", "2021", "2022", "2023", "2024", "2025"]
storage_data = storage[storage_years].iloc[0]
storage_data = pd.to_numeric(storage_data)

difference = storage_data.diff()

print("New Energy Storage Capacity Additions:")
print(difference)