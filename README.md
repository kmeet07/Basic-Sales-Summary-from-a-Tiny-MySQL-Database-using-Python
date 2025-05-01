🛒 Sales Data Summary - SQL + Python Integration
🎯 Task 7: Get Basic Sales Summary from a Tiny MySQL Database Using Python

📁 Dataset Used
Dataset: Simple Sales Dataset
Source: Manually created sample in MySQL
Tool: Python (MySQL Connector, Pandas, Matplotlib)
Database: MySQL
Environment: Jupyter Notebook or .py script

📌 Objective
The goal of this task was to connect a MySQL database to Python, extract basic sales insights using SQL queries, and visualize the results.
The task helps in learning how to integrate SQL queries into Python for analysis and creating visual summaries with matplotlib.

🛠 Methods Used

MySQL for creating a basic sales database
SQL for querying total quantity and revenue by product
Pandas for executing queries and analyzing data
Matplotlib for data visualization
Steps involved:
Create a database and populate it with sample sales records
Connect Python to the MySQL database
Run GROUP BY SQL query to aggregate data
Display and visualize results
📊 Key Visualizations
Revenue by Product (Bar Chart)

Clearly shows total revenue for each product: Apple, Banana, Orange
Generated using matplotlib and saved as sales_chart.png
📉 Summary Statistics

Total quantity and revenue calculated per product
Data queried and loaded directly into a Pandas DataFrame
Table printed with product-wise breakdown
💡 Observations

Products like Banana and Orange appear multiple times with varying quantities
Revenue = Quantity × Price, which is calculated for each product group
SQL aggregation helps summarize repetitive data effectively
Bar chart provides an at-a-glance view of top-selling items
📤 Deliverables

sales_summary_sql.py – Python script that runs SQL query and plots chart
sales_chart.png – Bar chart showing revenue by product
sales_db – MySQL database with one table: sales
README.md – This documentation summary
🧠 Learning Outcome

Gained experience connecting MySQL with Python using mysql-connector-python
Learned how to run aggregation SQL queries inside Python scripts
Practiced visualizing tabular data using Pandas and Matplotlib
Understood how to summarize and communicate insights from small datasets
📌 Internship Context
This project is part of a Data Analyst Internship Program under Task 7:
“Get Basic Sales Summary from a Tiny MySQL Database using Python”, focused on data extraction, summary statistics, and visualization through real-time SQL-Python integration.
