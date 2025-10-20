import pandas as pd

# Read your wide CSV
df = pd.read_csv("DV2\Data\Arrival_Purpose.csv", encoding="latin1")

# Melt into long format
df_long = df.melt(
    id_vars=["Country","Indicator"],
    var_name="Year",
    value_name="Value"
)

# Rename for clarity
df_long = df_long.rename(columns={"Indicator": "Purpose"})

# Remove invalid/missing values
df_long = df_long[df_long["Value"].notna()]              # drop NaN
df_long = df_long[df_long["Value"] != ".."]             # drop '..'

# Remove commas and convert to float
df_long["Value"] = df_long["Value"].astype(str).str.replace(",", "")
df_long["Value"] = df_long["Value"].astype(float)

# Optional: filter by Year or Purpose here

# Save to CSV
df_long.to_csv("Purpose.csv", index=False)