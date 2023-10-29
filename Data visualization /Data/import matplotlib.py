import matplotlib.pyplot as plt
import pandas as pd

# Assuming you have your data loaded into a DataFrame named 'housing_data'

# Set the style sheet
plt.style.use('style_sheet_name')  # Replace 'style_sheet_name' with the actual style sheet you want to use

# Change the figure size
plt.figure(figsize=(12, 8))

# Plot ZN with a solid green line
plt.plot(housing_data['ZN'], color='green', label='ZN')

# Plot INDUS with a blue dashed line
plt.plot(housing_data['INDUS'], color='blue', linestyle='--', label='INDUS')

# Add labels and legend
plt.xlabel('X-Axis Label')
plt.ylabel('Y-Axis Label')
plt.legend()

# Show the plot
plt.show()