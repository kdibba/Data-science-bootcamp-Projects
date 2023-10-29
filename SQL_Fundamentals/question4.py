# Departments that generated less than $600 in 2022:

import sqlite3

conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

cursor.execute("SELECT DepartmentName FROM departments WHERE DepartmentID IN (SELECT DepartmentID FROM orders WHERE strftime('%Y', OrderDate) = '2022' GROUP BY DepartmentID HAVING SUM(OrderAmount) < 600)")
departments = cursor.fetchall()

cursor.close()
conn.close()

print("Departments that generated less than $600 in 2022:")
for department in departments:
    print(department[0])
