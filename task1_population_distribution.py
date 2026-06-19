# import pandas as pd
# import matplotlib.pyplot as plt

# # Load dataset
# df = pd.read_csv(
#     "API_SP.POP.TOTL_DS2_en_csv_v2_406129.csv",
#     skiprows=4
# )

# data = df[
#     (df["Region"].isna()) &
#     (df["Country Name"] != "World")
# ]

# # Remove missing values
# data = data.dropna()

# aggregates = [
#     "World",
#     "IDA & IBRD total",
#     "IBRD only",
#     "IDA total",
#     "South Asia",
#     "East Asia & Pacific",
#     "Middle income",
#     "Low income",
#     "High income",
#     "European Union"
# ]

# data = data[~data["Country Name"].isin(aggregates)]

# # Top 10 countries by population
# top10 = data.sort_values(
#     by="2024",
#     ascending=False
# ).head(10)

# # Plot
# plt.figure(figsize=(12, 6))

# plt.bar(
#     top10["Country Name"],
#     top10["2024"]
# )

# plt.title("Top 10 Most Populated Countries (2024)")
# plt.xlabel("Country")
# plt.ylabel("Population")

# plt.xticks(rotation=45)

# plt.tight_layout()

# plt.savefig("top10_population_bar_chart.png")
# plt.show()


# import pandas as pd

# df = pd.read_csv(
#     "API_SP.POP.TOTL_DS2_en_csv_v2_406129.csv",
#     skiprows=4
# )

# print(df.columns.tolist())

# import pandas as pd

# meta = pd.read_csv(
#     "Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_406129.csv"
# )

# print(meta.columns.tolist())
# print(meta.head())

import pandas as pd
import matplotlib.pyplot as plt

# Load population dataset
population_df = pd.read_csv(
    "API_SP.POP.TOTL_DS2_en_csv_v2_406129.csv",
    skiprows=4
)

# Load metadata dataset
metadata_df = pd.read_csv(
    "Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_406129.csv"
)

# Keep only real countries
metadata_df = metadata_df[metadata_df["Region"].notna()]

# Merge datasets using Country Code
merged_df = population_df.merge(
    metadata_df[["Country Code"]],
    on="Country Code",
    how="inner"
)

# Select required columns
year = "2024"

data = merged_df[["Country Name", year]]

# Remove missing values
data = data.dropna()

# Get top 10 countries by population
top10 = data.sort_values(
    by=year,
    ascending=False
).head(10)

print(top10)

# Create bar chart
plt.figure(figsize=(12,6))

bars = plt.bar(
    top10["Country Name"],
    top10[year]
)

plt.title("Top 10 Most Populated Countries (2024)")
plt.xlabel("Countries")
plt.ylabel("Population (Billions)")

plt.xticks(rotation=45)

# Add values above bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height/1e9:.2f}B",
        ha='center',
        va='bottom'
    )

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.savefig(
    "top10_population_bar_chart.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()