import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv(r"D:\BI\Business-Intelligence-_-Student\Business Intelligence Group Work\data\clean\clean_dataset.csv")
print("Dataset loaded successfully!")
print(df.head())

# Ensure numeric columns are correct
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['discounted_price'] = pd.to_numeric(df['discounted_price'], errors='coerce')
df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')

# Set output folder
output_folder = r"D:\BI\Business-Intelligence-_-Student\Business Intelligence Group Work\visuals"

#Bar chart
category_counts = df['category'].value_counts().head(10)
plt.figure(figsize=(10,6))
category_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Top 10 Amazon Product Categories", fontsize=16)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Number of Products", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(f'{output_folder}/bar_categories.png')
plt.close()
print("Bar chart generated")
print("Interpretation: Shows which product categories dominate Amazon sales. Useful for inventory and marketing decisions.\n")

#Histogram
plt.figure(figsize=(10,6))
df['rating'].dropna().plot(kind='hist', bins=20, color='lightgreen', edgecolor='black')
plt.title("Distribution of Product Ratings", fontsize=16)
plt.xlabel("Rating (1-5 stars)", fontsize=12)
plt.ylabel("Number of Products", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(f'{output_folder}/hist_ratings.png')
plt.close()
print("Histogram generated")
print("Interpretation: Helps understand overall customer satisfaction and product quality trends.\n")

#Line chart
sample = df.sort_values(by='discounted_price').head(200)
plt.figure(figsize=(10,6))
plt.plot(sample['discounted_price'].values, color='orange', marker='o', linestyle='-', markersize=6, linewidth=2)
plt.title("Discounted Price Trend (Sample of 200 Products)", fontsize=16)
plt.xlabel("Product Index", fontsize=12)
plt.ylabel("Discounted Price (KSh)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(f'{output_folder}/line_discounted_price.png')
plt.close()
print("Line chart generated")
print("Interpretation: Shows how discounted prices vary across products. Useful for pricing and promotion strategies.\n")

#Bar chart
top_reviews = df.sort_values(by="rating_count", ascending=False).head(10)
plt.figure(figsize=(12,6))
plt.bar(top_reviews['product_name'], top_reviews['rating_count'], color='coral', edgecolor='black')
plt.title("Top 10 Most Reviewed Products", fontsize=16)
plt.xlabel("Product Name", fontsize=12)
plt.ylabel("Number of Reviews", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(f'{output_folder}/bar_top_reviews.png')
plt.close()
print("Bar chart generated")
print("Interpretation: Shows which products attract the most customer feedback. Useful for focus and promotions.\n")

print("All charts generated successfully in visuals/ folder!")
