import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\Users\dhara\Downloads\diabetes2.csv")
print("First 5 rows of the dataset:")
print(df.head())
print("\nSummary statistics:")
print(df.describe())
column_name = "Age" 
if column_name in df.columns:
    avg_value = df[column_name].mean()
    print(f"\nThe average value of {column_name}: {avg_value}")
plt.figure(figsize=(8, 5))
df["Glucose"].value_counts().plot(kind="bar", color="skyblue")  
plt.title("Bar Chart of Categorical Column")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()
plt.figure(figsize=(8, 5))
plt.scatter(df["BMI"], df["Glucose"], alpha=0.5, color="red")  
plt.title("Scatter Plot between Two Numeric Columns")
plt.xlabel("X-axis Column")
plt.ylabel("Y-axis Column")
plt.show()
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Heatmap of Feature Correlations")
plt.show()