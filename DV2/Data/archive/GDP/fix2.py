import pandas as pd

df = pd.read_csv("DV2\Data\GDP.csv", encoding="latin1")
df['GeoCodeStr'] = df['GeoAreaCode'].apply(lambda x: f"{int(x):03d}")
df.to_csv("GDP_prepped.csv", index=False)
