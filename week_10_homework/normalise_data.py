import pandas as pd

df = pd.read_csv("Life-Expectancy-Data-Updated-with-ISO.csv")

# filter years 2000–2015
df = df[(df["Year"] >= 2000) & (df["Year"] <= 2015)]

# group by ISO3 and Country, take mean of Life_expectancy
avg = (
    df.groupby(["ISO3", "Country"], as_index=False)
      .agg(avg_life_exp=("Life_expectancy", "mean"))
)

avg.to_csv("life_expectancy_avg_with_ISO.csv", index=False)
