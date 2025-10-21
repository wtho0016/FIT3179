import pandas as pd

# Load wide CSV
df = pd.read_csv("DV2\Data\Arrivals.csv", index_col=0)
import pandas as pd

# Melt to long format
df_long = df.reset_index().melt(id_vars=['index'], var_name='Year', value_name='Value')
df_long = df_long.rename(columns={'index': 'Country'})

# Remove '..' and commas, convert to float
df_long = df_long[df_long['Value'] != '..']
df_long['Value'] = df_long['Value'].str.replace(',', '')  # remove commas
df_long['Value'] = df_long['Value'].astype(float)
df_long['Year'] = df_long['Year'].astype(int)

# Save cleaned long-format CSV
df_long.to_csv("inbound_arrivals_long.csv", index=False)
