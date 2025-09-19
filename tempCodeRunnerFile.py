import pandas as pd
df = pd.read_csv("Life-Expectancy-Data-Updated-with-ISO.csv")

# Show all rows where ISO3 is missing
missing = df[df["ISO3"].isna()]
print(missing[["Country"]].drop_duplicates())