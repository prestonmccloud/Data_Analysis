# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("retail_sales_dataset.csv")

# Ensure date is in datetime format
df['Date'] = pd.to_datetime(df['Date'])
df.dropna(inplace=True)

# 1) Top selling product categories by revenue
category_sales = df.groupby('Product Category', an_index=False)['Total Amount'].sum()
category_sales.sort_values(by='Total Amount', ascending=False, inplace=True)
# Plot the data into a bar graph
plt.figure(figsize=8, 5)
sns.barplot(data=category_sales, x='Product Category', y='Total Amount', palette='viridis')
plt.title('Top-Selling Product Categories by Revenue')
plt.ylabel('Revenue')
plt.xlabel('Product Category')
plt.show()

# 2) Monthly Sales Trend
monthly_sales = df.resample('M', on='Date')['Total Amount'].sum().reset_index()
# Plot data into a line graph
plt.figure(figsize=(10,5))
sns.lineplot(data=monthly_sales, x='Date', y='Total Amount', marker='o')
plt.title('Monthly Sales Trend')
plt.ylabel('Revenue')
plt.xlabel('Month')
plt.show()

# 3) Average Order Value
aov = df['Total Amount'].mean()
print(f"\n Average Order Value (AOV): ${aov:.2f}")

# 4) Customer Segmentation by age group
bins = [0, 25, 35, 45, 55, 65, 100]
labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

age_group_sales = df.groupby('Age Group')['Total Amount'].sum().reset_index()
# Plot data into bar graph
plt.figure(size=(8, 5))
sns.barplot(data=age_group_sales, x='Age Group', y='Total Amount', palette='coolwarm')
plt.title('Revenue by Age Group')
plt.ylabel('Revenue')
plt.xlabel('Age Group')
plt.show()

# 5) Gender-based purchasing behavior
gender_sales = df.groupby('Gender')['Total Amount'].sum().reset_index()
# Plot data into bar graph
plt.figure(size=(8, 5))
sns.barplot(data=gender_sales, x='Gender', y='Total Amount', palette='Set2')
plt.title('Revenue by Gender')
plt.ylabel('Revenue')
plt.xlabel('Gender')
plt.show()
