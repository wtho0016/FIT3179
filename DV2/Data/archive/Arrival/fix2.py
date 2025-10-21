import pandas as pd

# Load your CSV
df = pd.read_csv("DV2\Data\Arrivals.csv")  # columns: Country, Year, Value

# Ensure Value is numeric
df['Value'] = df['Value'].replace('..', pd.NA)
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

# Rank countries **per year**
df['Rank'] = df.groupby('Year')['Value'].rank(method='dense', ascending=False)

# Create a new column for Vega-Lite plotting
# Only keep top 10 ranks; others set to NaN to break the line
df['Top10Rank'] = df['Rank'].where(df['Rank'] <= 10, pd.NA)

# Save a new CSV
df.to_csv("Arrival.csv", index=False)
