import pandas as pd

# Read the GDP data
url = "https://raw.githubusercontent.com/wtho0016/FIT3179/refs/heads/main/DV2/Data/GDP.csv"
df = pd.read_csv(url)

# Filter for 2008 data only
df_2008 = df[df['TimePeriod'] == 2020]

# Save to a new CSV file
df_2008.to_csv('GDP_2020.csv', index=False)

print(f"✅ Created GDP_2019.csv with {len(df_2008)} countries")
print("📊 Sample of the data:")
print(df_2008[['GeoAreaName', 'Value', 'GeoCodeStr']].head())