import pandas as pd

df = pd.read_csv("DV2\Data\Accomodation_till_2022.csv")
df_long = df.melt(id_vars=["Country","Indicator"], var_name="Year", value_name="Value")
df_long.to_csv("accommodation_long.csv", index=False)
