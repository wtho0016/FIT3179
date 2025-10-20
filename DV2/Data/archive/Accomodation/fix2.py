import pandas as pd

# 1. Load your long-format CSV
input_file = "DV2\Data\ccommodation_long.csv"  # change to your file name
df = pd.read_csv(input_file)

# 2. Pivot indicators into separate columns
df_pivot = df.pivot(index=['Country','Year'], columns='Indicator', values='Value').reset_index()

# 3. Flatten column names
df_pivot.columns.name = None

# 4. Save to a new CSV
output_file = "accommodation.csv"
df_pivot.to_csv(output_file, index=False)

print(f"Pivoted CSV saved as {output_file}")
