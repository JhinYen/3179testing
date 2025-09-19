# Add ISO to csv file
# import pandas as pd
# import pycountry

# # Read the CSV in the same folder
# df = pd.read_csv("Life-Expectancy-Data-Updated.csv")

# def to_iso3(name):
#     try:
#         return pycountry.countries.lookup(name).alpha_3
#     except LookupError:
#         return None

# df["ISO3"] = df["Country"].apply(to_iso3)

# # Save a new file in the same folder (keeps original intact)
# df.to_csv("Life-Expectancy-Data-Updated-with-ISO.csv", index=False)
# print("Done: Life-Expectancy-Data-Updated-with-ISO.csv created.")



# Check which ones ISO are empty
import pandas as pd
df = pd.read_csv("Life-Expectancy-Data-Updated-with-ISO.csv")

# Show all rows where ISO3 is missing
missing = df[df["ISO3"].isna()]
print(missing[["Country"]].drop_duplicates())



# Script to add the ISOs for empty country
import pandas as pd

fixes = {
    "Turkiye": "TUR",
    "Bahamas, The": "BHS",
    "Congo, Rep.": "COG",
    "Gambia, The": "GMB",
    "Yemen, Rep.": "YEM",
    "St. Vincent and the Grenadines": "VCT",
    "Micronesia, Fed. Sts.": "FSM",
    "Congo, Dem. Rep.": "COD",
    "Egypt, Arab Rep.": "EGY",
    "Cote d'Ivoire": "CIV",
    "St. Lucia": "LCA",
    "Venezuela, RB": "VEN",
    "Iran, Islamic Rep.": "IRN",
    "Lao PDR": "LAO"
}

df = pd.read_csv("Life-Expectancy-Data-Updated-with-ISO.csv")
df["ISO3"] = df.apply(
    lambda r: fixes.get(r["Country"], r["ISO3"]),
    axis=1
)
df.to_csv("Life-Expectancy-Data-Updated-with-ISO.csv", index=False)
