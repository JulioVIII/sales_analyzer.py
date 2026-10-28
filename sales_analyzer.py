
import pandas as pd


# Load the CSV file
df = pd.read_csv("sales_data.csv")


# Display all sales data
print("===== SALES DATA =====")
print(df.to_string(index=False))


# Calculate total revenue
print("\n===== TOTAL REVENUE =====")
total_revenue = df["Revenue"].sum()
print(f"Total revenue: €{total_revenue:.2f}")


# Calculate average order value
print("\n===== AVERAGE ORDER VALUE =====")
average_order = df["Revenue"].mean()
print(f"Average order value: €{average_order:.2f}")


# Revenue by product
print("\n===== REVENUE BY PRODUCT =====")
revenue_by_product = df.groupby("Product")["Revenue"].sum()
print(revenue_by_product)


# Revenue by city
print("\n===== REVENUE BY CITY =====")
revenue_by_city = df.groupby("City")["Revenue"].sum()
print(revenue_by_city)


# Best-selling product by revenue
print("\n===== TOP PRODUCT =====")
top_product = revenue_by_product.idxmax()
top_revenue = revenue_by_product.max()

print(f"Top product: {top_product}")
print(f"Revenue: €{top_revenue:.2f}")


# Filter orders above €500
print("\n===== HIGH-VALUE ORDERS =====")
high_value_orders = df[df["Revenue"] > 500]
print(high_value_orders.to_string(index=False))


# Sort orders by revenue
print("\n===== ORDERS SORTED BY REVENUE =====")
sorted_orders = df.sort_values("Revenue", ascending=False)
print(sorted_orders.to_string(index=False))


# Count orders by city
print("\n===== ORDERS BY CITY =====")
orders_by_city = df["City"].value_counts()
print(orders_by_city)
