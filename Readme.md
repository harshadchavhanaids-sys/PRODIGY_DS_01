# PRODIGY_DS_01

## Task 01: Population Distribution Visualization

### Objective
Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable.

### Dataset
World Bank Population Dataset (SP.POP.TOTL)

### Technologies Used
- Python
- Pandas
- Matplotlib

### Process
1. Loaded the population dataset.
2. Loaded the country metadata dataset.
3. Filtered only valid countries using region information.
4. Selected population data for 2024.
5. Sorted countries by population.
6. Visualized the top 10 most populated countries using a bar chart.
7. Saved the visualization as a PNG image.

### Output
Top 10 Most Populated Countries (2024):
- India
- China
- United States
- Indonesia
- Pakistan
- Nigeria
- Brazil
- Bangladesh
- Russian Federation
- Ethiopia

### Files
- `task1_population_distribution.py`
- `API_SP.POP.TOTL_DS2_en_csv_v2_406129.csv`
- `Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_406129.csv`
- `top10_population_bar_chart.png`

### How to Run

```bash
pip install -r requirements.txt
python task1_population_distribution.py
```

### Author
Harshad Chavhan