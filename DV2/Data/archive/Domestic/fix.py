import pandas as pd
import pycountry
import pycountry_convert as pc

# --- 1. Load your existing CSV ---
input_file = "DV2\Data\Domestic_Trips_2022.csv"   # Replace with your CSV filename
df = pd.read_csv(input_file)

# --- 2. Function to convert country name to continent ---
def country_to_continent(country_name):
    try:
        country = pycountry.countries.get(name=country_name)
        if not country:
            # Try lookup by common name (some countries have different naming)
            country = pycountry.countries.search_fuzzy(country_name)[0]
        country_alpha2 = country.alpha_2
        continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        return continent_name
    except:
        return "Unknown"

# --- 3. Add Region column ---
df['Region'] = df['Country'].apply(country_to_continent)

# --- 4. Save to a new CSV ---
output_file = "travel_data_with_region.csv"
df.to_csv(output_file, index=False)

print(f"Saved updated CSV with Region column to {output_file}")
