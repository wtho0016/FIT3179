import pandas as pd

df = pd.read_csv("DV2\Data\ccommodation.csv")

# Remove commas from numeric columns and convert to numbers
num_cols = [
    "Number of bed-places",
    "Number of establishments",
    "Number of rooms",
    "Occupancy rate / bed-places",
    "Occupancy rate / rooms",
    "Average length of stay",
    "Available capacity (bed-places per 1000 inhabitans)"
]

for col in num_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.replace(",", "")
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Save cleaned CSV
df.to_csv("accommodation.csv", index=False)
print("Cleaned CSV saved as accommodation.csv")
