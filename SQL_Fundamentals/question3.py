# Total number of customers that purchased in January 2023 and the average amount spent per customer:

import sqlite3

conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

cursor.execute("SELECT COUNT(DISTINCT CustomerID) FROM orders WHERE OrderDate >= '2023-01-01' AND OrderDate < '2023-02-01'")
total_customers = cursor.fetchone()[0]

cursor.execute("SELECT AVG(OrderAmount) FROM orders WHERE OrderDate >= '2023-01-01' AND OrderDate < '2023-02-01'")
avg_amount_per_customer = cursor.fetchone()[0]

cursor.close()
conn.close()

print(f"Total customers in January 2023: {total_customers}")
print(f"Average amount spent per customer: {avg_amount_per_customer}")
