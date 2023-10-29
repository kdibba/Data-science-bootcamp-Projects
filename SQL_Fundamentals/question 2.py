# Total number of orders completed on 18th March 2023 with the first name 'John' and last name 'Doe':

import sqlite3

conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM orders WHERE CompletedDate = '2023-03-18' AND FirstName = 'John' AND LastName = 'Doe'")
total_orders = cursor.fetchone()[0]

cursor.close()
conn.close()

print(f"Total orders completed on 18th March 2023 by John Doe: {total_orders}")
