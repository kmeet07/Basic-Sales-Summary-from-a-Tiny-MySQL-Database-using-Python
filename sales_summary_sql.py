import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='3503',
    database='sales_db'
)

# SQL query
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product;
"""

# Load results into pandas
df = pd.read_sql(query, con=conn)

# Print summary
print("Sales Summary:")
print(df)

# Plot the revenue as a bar chart
df.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')
plt.ylabel("Revenue ($)")
plt.title("Revenue by Product")
plt.tight_layout()
plt.savefig("sales_chart.png")  # Optional: Save the chart
plt.show()

# Close connection
conn.close()
