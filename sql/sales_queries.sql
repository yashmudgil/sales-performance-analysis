
-- Total sales by product
SELECT Product_Name, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 10;

-- Average profit per region
SELECT Region, AVG(Profit) AS Avg_Profit
FROM sales_data
GROUP BY Region;

-- Monthly revenue trend
SELECT DATE_FORMAT(Order_Date, '%Y-%m') AS Month, SUM(Sales) AS Monthly_Sales
FROM sales_data
GROUP BY Month
ORDER BY Month;
