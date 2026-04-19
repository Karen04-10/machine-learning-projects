# Sales Analysis

## Project Type
Python Mini Project (Pandas, NumPy, Matplotlib)

## Description
This project analyzes e-commerce order data by combining orders and customer datasets. It performs data cleaning, feature engineering, filtering, and aggregation to uncover insights such as customer behavior, top spenders, and city-wise performance.

## Dataset
1. Orders Data (orders)
Contains:
order_id – Unique order identifier
customer_id – Customer reference
product – Product category (A, B, C)
price – Product price
quantity – Quantity ordered
date – Order date
2. Customers Data (customers)
Contains:
customer_id – Unique customer identifier
city – Customer location
signup_date – Date of registration

## Skills & Tools
- Pandas, Numpy, Matplotlib
- Data cleaning, merging, grouping
- Data preprocessing & feature engineering

# Key Steps
1. Data Cleaning
Filled missing price values using median per product
Filled missing quantity values using overall median
2. Data Processing
Merged orders and customers data
Created new features: total_amount = price × quantity, days_since_signup
3. Filtering
Selected orders where: total_amount > 350, days_since_signup >= 1
4. Analysis
- City-wise aggregation (sum, mean, count)
- Customer-wise total spending
- Identified top 5 customers
- Most frequent customer (by orders)
- Customer behavior classification: New vs Returning

## Results / Visualizations
1. Insights Generated
Top 5 customers by total spending
Average order value by city
Average sales by product
Customer purchase behavior
2. Visualizations
Bar chart of Top Customers
Bar chart of Average Total Amount by City
Bar chart of Average Total Amount by Product
