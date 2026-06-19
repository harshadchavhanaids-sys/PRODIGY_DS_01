import pandas as pd
import matplotlib.pyplot as plt

population_df = pd.read_csv(
    "API_SP.POP.TOTL_DS2_en_csv_v2_406129.csv",
    skiprows=4
)

metadata_df = pd.read_csv(
    "Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_406129.csv"
)


metadata_df = metadata_df[metadata_df["Region"].notna()]


merged_df = population_df.merge(
    metadata_df[["Country Code"]],
    on="Country Code",
    how="inner"
)


year = "2024"

data = merged_df[["Country Name", year]]


data = data.dropna()


top10 = data.sort_values(
    by=year,
    ascending=False
).head(10)

print(top10)


plt.figure(figsize=(12,6))

bars = plt.bar(
    top10["Country Name"],
    top10[year]
)

plt.title("Top 10 Most Populated Countries (2024)")
plt.xlabel("Countries")
plt.ylabel("Population (Billions)")

plt.xticks(rotation=45)


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