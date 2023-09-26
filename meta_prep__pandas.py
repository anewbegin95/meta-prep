"""
Problem Scenario:

You have been provided with two datasets: sales_data.csv and customer_data.csv. These datasets contain information about sales transactions and customer details, respectively.
2. Data Cleaning and Preprocessing:

Inspect the datasets for any missing values or inconsistencies.
Clean the data if necessary.
3. Data Exploration:

Perform basic exploratory data analysis (EDA) on both datasets.
Calculate summary statistics, identify trends, and visualize the data.
4. Merging Datasets:

Merge the two datasets based on a common identifier, such as CustomerID.
5. Creating New Columns:

Create a new column that calculates the total sales amount for each transaction.
6. Filtering Data:

Filter the data to show only transactions with a sales amount greater than $500.
7. Aggregations:

Calculate the total sales revenue and the average transaction value.
8. Comparing Rows:

Create a column that compares the current transaction's sales amount with the previous transaction.
9. Visualization:

Create a bar chart to visualize the total sales revenue for each customer.
10. Further Analysis:

Perform additional analyses or visualizations that you think would provide valuable insights into the sales data.
Additional Challenge (Optional):

If you're up for an extra challenge, consider performing a time series analysis or forecasting based on the sales data.
"""
# %%
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

# %% 1. Load the Datasets: Load the sales_data.csv and customer_data.csv datasets into Pandas DataFrames.
cust_csv = 'customer_data.csv'
sales_csv = 'sales_data.csv '

cust_df = pd.read_csv(cust_csv)
sales_df = pd.read_csv(sales_csv)

print(cust_df.head())
print(sales_df.head())
# %% 
"""
#2: Filtering and Aggregating
Problem: Find the total sales amount for each product.
Expected Output: A DataFrame showing the product name and the total sales amount.
"""
sales_by_prod_df = sales_df.groupby('Product')['TotalAmount'].sum().sort_values(ascending=False)
print(sales_by_prod_df)
# %%
"""
#3: Creating New Columns
Problem: Add a column to the sales data representing the profit, calculated as 20% of the total amount.
Expected Output: The sales data with an additional column for profit.
"""
sales_df['Profit'] = sales_df['TotalAmount'] * .2
print(sales_df.head())
# %%
"""
#4: Joining/Merging Datasets

Problem: Merge the customer data with the sales data using CustomerID. Show the total sales amount for each customer.
Expected Output: A DataFrame with CustomerID, CustomerName, TotalSales.
"""
sales_by_cust_df = sales_df.groupby('CustomerID')['TotalAmount'].sum().reset_index()

merged_df = pd.merge(
    cust_df
    ,sales_by_cust_df
    ,on='CustomerID'
    ,how='left'
)
merged_df = merged_df[(merged_df['TotalAmount'] >= 0) | (merged_df['State'] == 'CA')]

print(merged_df.sort_values(by='TotalAmount', ascending=False))
# %%
"""
#5: Comparing Rows

Problem: For each transaction, find the percentage change in quantity compared to the previous transaction.
Expected Output: A DataFrame with TransactionID, Product, Quantity, PercentageChange.
"""
sales_df['PctChngQuantity'] = (sales_df.Quantity - sales_df.Quantity.shift()) / sales_df.Quantity.shift()
print(sales_df.head())
# %%
"""
#5: Creating New Rows

Problem: Add a row representing a bulk purchase of 50 units of Product_A by a new customer.
Expected Output: The updated sales data with the new row.
"""
# sales_df.loc[len(sales_df.index)] = [31, 121, 'Product_A', 50, 10, 500, '2023-09-20'] 
# print(sales_df.tail())

# cust_df.loc[len(cust_df.index)] = [121, 'Frank Darkling', 'Cleveland', 'OH', 'USA']
# print(cust_df.tail())
# %%
"""
#6: Bar Chart

Problem: Create a bar chart showing the total sales amount for each product.
Expected Output: A bar chart with product names on the x-axis and total sales on the y-axis.
"""
sales_by_prod_df = sales_df.groupby('Product')['TotalAmount'].sum().sort_values(ascending=False).reset_index()
x = sales_by_prod_df['Product'].to_list()
y = sales_by_prod_df['TotalAmount'].to_list()
fig, ax = plt.subplots()
p = ax.bar(x, y, color='Green')
ax.set_title('Total sales by product')
ax.set_xlabel('Product')
ax.set_ylabel('Total sales')
ax.bar_label(p, label_type='edge')
plt.show()
# %%
"""
#7: Line Chart

Problem: Create a line chart showing the trend of total sales over time.
Expected Output: A line chart with dates on the x-axis and total sales on the y-axis.
"""
sales_df = sales_df.sort_values('TransactionDate', ascending=True)
X = sales_df['TransactionDate'].tolist()

sale_counter = 0
Y = []
for sale in sales_df['TotalAmount'].to_list():
    sale_counter += sale
    Y.append(sale_counter)

fig, ax = plt.subplots()

p = ax.plot(X, Y)
ax.xaxis.set_major_locator(ticker.AutoLocator())
plt.xticks(rotation=45)
plt.show()
# %%
"""
#8: Scatter Plot

Problem: Create a scatter plot showing the relationship between Quantity and Total Amount.
Expected Output: A scatter plot with Quantity on the x-axis and Total Amount on the y-axis.
"""
x = sales_df['Quantity'].tolist()
y = sales_df['TotalAmount'].tolist()

ax, fig = plt.subplots()
p = fig.scatter(x, y)
fig.set_xlim(0, 10)
fig.set_ylim(0, 150)
plt.show()
# %%
"""
#9: Histogram
Problem: Create a histogram showing the distribution of Total Amount.
Expected Output: A histogram representing the frequency distribution.
"""
x = sales_df['TotalAmount'].tolist()
ax, fig = plt.subplots()
p = fig.hist(x, 10)
plt.show()
# %%
"""
#10: Pie Chart
Problem: Create a pie chart showing the proportion of sales for each product.
Expected Output: A pie chart displaying the percentage distribution.
"""
sales_by_prod_df = sales_df.groupby('Product')['TotalAmount'].sum().sort_values(ascending=False).reset_index()
z = sales_by_prod_df['Product'].to_list()
x = sales_by_prod_df['TotalAmount'].to_list()
fig, ax = plt.subplots()
p = ax.pie(x, labels=z)
ax.set_title('Total sales by product')
ax.legend()
# ax.set_xlabel('Product')
# ax.set_ylabel('Total sales')
# ax.bar_label(p, label_type='edge')
plt.show()
# %%
