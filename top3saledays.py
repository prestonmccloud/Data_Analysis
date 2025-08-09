# This will show how to find the top 3 sales days per product category in pandas and in sql
import pandas as pd
retail_sales = pd.read_csv("retail_sales_dataset.csv")

# Preview data
retail_sales.head()

# Group by product category and Date, and sum total amount
t1 = retail_sales.groupby(['Product Category', 'Date'], as_index=False)['Total Amount'].sum()
t1.rename(columns={'Total Amount': 'Category_Total'}, inplace=True)

# Rank Category_Total within each Product_Category
t1['Total_Rank'] = t1.groupby('Product Category')['Category_Total'] \
                     .rank(method='dense', ascending=False)
# Filter top 3 per category
t2 = t1[t1['Total_Rank'] <= 3].copy()

# Sort result and reset index
t2 = t2.sort_values(by=['Product Category', 'Total_Rank']).reset_index(drop=True, inplace=True)
# Show final table depicting the top 3 sales amounts from each category and when they occurred.
print(t2)


# Here is the same result coming from a SQL Query:
# mock database connection
import pyodbc
conn = pyodbc.connect(r"Driver={ODBC Driver 17 for SQL Server}; Server=localhost; Database=Portfolio;")
query = """WITH t1 AS (
SELECT Product_Category, Date, SUM(Total_Amount) AS Category_Total
FROM retail_sales
GROUP BY Product_Category, Date 
),
t2 AS (
SELECT *, RANK() OVER(PARTITION BY Product_Category ORDER BY Category_Total DESC) AS Total_Rank 
FROM t1)
SELECT * FROM t2 WHERE Total_Rank <= 3
ORDER BY Product_Category, Total_Rank ASC;"""
top_retail_sales = pd.read_sql_query(query, conn)
