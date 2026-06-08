# import sales-data-analysis-pandas as pd
#
# sales = pd.read_csv("sales.csv")
# customers =pd.read_csv("customers.csv")
#
# print(sales.head())
# print(customers.head())

import pandas as pd
import matplotlib
matplotlib.use('TkAgg')   # ✅ Important for Windows
import matplotlib.pyplot as plt

sales = pd.read_csv("sales.csv")
customers = pd.read_csv("customers.csv")

# Clean column name (ERP CSVs always have issues)
sales.columns = sales.columns.str.strip().str.lower()
customers.columns = customers.columns.str.strip().str.lower()

#Verify columns
print("Sales columns:", sales.columns)
print("Customers columns:", customers.columns)

# Ensure join keys exits
sales['customer_id'] = sales['customer_id'].astype(str)
customers['customer_id'] = customers['customer_id'].astype(str)

merged_df = pd.merge(
    sales,
    customers,
    on = 'customer_id',
    how = 'inner'
)
merged_df['quantity'] = merged_df['quantity'].fillna(0)
merged_df['price'] = merged_df['price'].fillna(0)

merged_df['revenue'] = merged_df['quantity'] * merged_df['price']

merged_df['order_date'] = pd.to_datetime(merged_df['order_date'])

weekly_sales = (
    merged_df
    .resample('W',on='order_date')['revenue']
    .sum()
)

print(weekly_sales)


weekly_sales.plot(kind='bar')
plt.title("Weekly Sales Revenue")
plt.xlabel("Week")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()