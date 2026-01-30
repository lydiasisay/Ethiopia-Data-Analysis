import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load the data
# -------------------------------
data_path = "data/ethiopia_rainfall_food_inflation.csv"
df = pd.read_csv(data_path)

# Display basic info
print("Dataset Preview:")
print(df.head())
print("\nSummary Statistics:")
print(df.describe())

# -------------------------------
# 2. Check correlation
# -------------------------------
rainfall = df["rainfall_mm"]
food_inflation = df["food_inflation_pct"]

correlation, p_value = pearsonr(rainfall, food_inflation)

print("\nPearson Correlation Results:")
print(f"Correlation coefficient: {correlation:.3f}")
print(f"P-value: {p_value:.4f}")

# -------------------------------
# 3. Interpretation
# -------------------------------
if correlation < 0:
    print("Interpretation: There is an inverse relationship between rainfall and food inflation.")
else:
    print("Interpretation: There is no inverse relationship between rainfall and food inflation.")

# -------------------------------
# 4. Visualization
# -------------------------------
plt.figure(figsize=(8, 5))
plt.scatter(rainfall, food_inflation)
plt.xlabel("Rainfall (mm)")
plt.ylabel("Food Inflation (%)")
plt.title("Rainfall vs Food Inflation in Ethiopia")
plt.grid(True)

# Add trend line
z = pd.Series(rainfall).corr(pd.Series(food_inflation))
plt.show()
